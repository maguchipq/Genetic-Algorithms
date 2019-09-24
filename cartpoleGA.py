import random
import copy
import cartpole
import time

gene_length = 200
individual_length = 30
generation = 300
mutate_rate = 0.1
elite_rate = 0.2

def get_population():
    population = []
    for i in range(individual_length):
        population.append([random.randint(0,1) for j in range(gene_length)])
    return population

def evaluate(pop):
    pop.sort(reverse=True)
    return pop

def two_point_crossover(parent1, parent2):
    r1 = random.randint(0, gene_length-1)
    r2 = random.randint(r1, gene_length-1)
    child = copy.deepcopy(parent1)
    child[r1:r2] = parent2[r1:r2]
    return child

def mutate(parent):
    r = random.randint(0, gene_length-1)
    child = copy.deepcopy(parent)
    child[r] = 1 if child[r]==0 else 0
    return child

def fitness(pop):
    for i in range(individual_length):
        observation = env.reset()
        for t in range(200):
            action = pop[t]
            observation, reward, done, info = env.step(action)
            if done:
                break
    env.reset()
    return t+1

env = cartpole.CartPoleEnv()
pop = evaluate([(fitness(p), p) for p in get_population()])

for i_episode in range(generation):

    eva = evaluate(pop)
    elites = eva[:int(len(pop)*elite_rate)]

    print('Min : {}'.format(eva[-1][0]))
    print('Max : {}'.format(eva[0][0]))
    print('--------------------------')

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

env.reset()
print(pop[0])
for t in range(200):
    env.render()
    if t == 0:
        time.sleep(5.0)
    action = pop[0][1][t]
    observation, reward, done, info = env.step(action)
    if done:
        break

print(t+1)
