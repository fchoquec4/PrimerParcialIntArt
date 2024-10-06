import random

population_size = 10
gene_length = 5  
generations = 3
mutation_rate = 0.01
crossover_point = 4  

def fitness(individual):
    decimal_value = int("".join(map(str, individual)), 2)
    return decimal_value ** 2 + 1  

def create_individual():
    return [random.randint(0, 1) for _ in range(gene_length)]

def create_population():
    return [create_individual() for _ in range(population_size)]

def selection(population):
    return random.choices(population, k=2, weights=[fitness(ind) for ind in population])

def crossover(parent1, parent2):
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    if random.random() < mutation_rate:
        mutate_point = random.randint(0, gene_length - 1)
        individual[mutate_point] = 1 - individual[mutate_point]  
    return individual

def genetic_algorithm():
    population = create_population()

    for generation in range(generations):
        new_population = []
        print(f"\nGeneración {generation + 1}")
        for i in range(population_size // 2):
            parent1, parent2 = selection(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

            print(f"Padre 1: {parent1} ({int(''.join(map(str, parent1)), 2)})")
            print(f"Padre 2: {parent2} ({int(''.join(map(str, parent2)), 2)})")
            print(f"Hijo 1: {child1} ({int(''.join(map(str, child1)), 2)})")
            print(f"Hijo 2: {child2} ({int(''.join(map(str, child2)), 2)})")

        population = new_population

        best_individual = max(population, key=fitness)
        best_value = int("".join(map(str, best_individual)), 2)
        print(f"Mejor individuo: {best_value}, Fitness = {fitness(best_individual)}")

genetic_algorithm()
