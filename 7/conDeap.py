import random
from deap import base, creator, tools, algorithms

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

population_size = 10
gene_length = 5
generations = 3
mutation_rate = 0.01
crossover_point = 4

def eval_fitness(individual):
    decimal_value = int("".join(map(str, individual)), 2)
    return decimal_value ** 2 + 1,

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, gene_length)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", eval_fitness)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=mutation_rate)
toolbox.register("select", tools.selTournament, tournsize=3)

def genetic_algorithm_deap():
    population = toolbox.population(n=population_size)
    
    algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=mutation_rate, ngen=generations, 
                        stats=None, halloffame=None, verbose=True)

    best_ind = tools.selBest(population, 1)[0]
    best_value = int("".join(map(str, best_ind)), 2)
    print(f"Mejor individuo: {best_value}, Fitness: {eval_fitness(best_ind)[0]}")

genetic_algorithm_deap()
