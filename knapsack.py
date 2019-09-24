import random
import copy
from collections import Counter

def get_population():
    population = []
    for i in range(individual_length):
        population.append([random.randint(0,1) for j in range(gene_length)])
    return population

def evaluate(pop):
    pop.sort(reverse=True)
    return pop

def two_point_crossover(parent1, parent2):
    r = [random.randint(0,1) for _ in range(gene_length)]
    child = [parent1[i] if r[i] else parent2[i] for i in range(gene_length)]
    return child

def mutate(parent):
    r = random.randint(0, gene_length-1)
    child = copy.deepcopy(parent)
    child[r] = 1 if child[r] == 0 else 0
    return child

def fitness(pop):
    value = 0
    weight = 0
    for i in range(N):
        if pop[i]:
            value += L[i][1]
            weight += L[i][0]
    if weight <= W:
        return value
    else:
        return 0

N,W = [int(zz) for zz in input().split()]
L = [[0,0] for _ in range(N)]

ans = []
for _ in range(3):
    for i in range(N):
        p,q = [int(zz) for zz in input().split()]
        L[i][0] = p
        L[i][1] = q

    gene_length = N
    individual_length = 20
    generation = 150
    mutate_rate = 0.1
    elite_rate = 0.2

    pop = evaluate([(fitness(p), p) for p in get_population()])

    for i_episode in range(generation):

        eva = evaluate(pop)
        elites = eva[:int(len(pop)*elite_rate)]

        pop = elites
        while len(pop) < individual_length:
            if random.random() < mutate_rate:
                m = random.randint(0, len(elites)-1)
                child = mutate(elites[m][1])
            else:
                m1 = random.randint(0, len(elites)-1)
                m2 = random.randint(0, len(elites)-1)
                child = two_point_crossover(elites[m1][1], elites[m2][1])
            pop.append((fitness(child), child))

    eva = evaluate(pop)
    ans.append(pop[0][0])

counter = Counter(ans)

print(counter.most_common()[0][0])
