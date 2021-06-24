from plotting import plot_result, plot_answer
from utility_functions import get_fitness
from random import choice, uniform

from timeit import default_timer as timer

from individual import Individual, crossover
from input import INDIVIDUALS_PER_GENERATION, SHIFTS, NUMBER_OF_NURSES, GENERATIONS


def rank_the_population(sorted_individuals, fitness):
    gauss_sum = float(len(sorted_individuals) * (1 + len(sorted_individuals))) / 2.0

    for index in range(len(sorted_individuals)):
        fitness[index] = (index + 1) / gauss_sum


def rank_selection(population, fitness):

    copy = fitness[:]

    group_to_sort = zip(population, copy)
    group_to_sort = sorted(group_to_sort, key=lambda value: value[1])

    population = [x[0] for x in group_to_sort]
    fitness = [x[1] for x in group_to_sort]

    rank_the_population(population, copy)

    pivot = uniform(0., 1)
    current = copy[0]
    index = 0

    while current < pivot and index < len(copy) - 1:
        index += 1
        current += copy[index]

    return population[index]


def next_generation(population):
    children = []
    fitness = []
    for individual in population:
        individual_fitness, _ = get_fitness(individual)
        fitness.append(individual_fitness)

    while len(children) < len(population):
        father = rank_selection(population, fitness)
        mother = rank_selection(population, fitness)

        first_child, second_child = crossover(father, mother)
        children.append(first_child)
        children.append(second_child)

    return children, fitness


def starting_population(number_of_nurses: int):

    population = []
    for index1 in range(INDIVIDUALS_PER_GENERATION):

        individual = []
        for index2 in range(number_of_nurses):
            individual.append(choice(list(SHIFTS.keys())))

        population.append(Individual("".join(individual)))
    return population


def evolve(number_of_nurses: int):
    population = starting_population(number_of_nurses)
    ancestors = list(dict())
    for _ in range(GENERATIONS):
        population, fitness = next_generation(population)
        history_stamp = {}
        for individual, fitness_score in zip(population, fitness):
            history_stamp[individual.chromosome] = fitness_score
        ancestors.append(history_stamp)
    return population, ancestors


def main():

    start = timer()
    last_population, ancestors = evolve(NUMBER_OF_NURSES)
    end = timer()
    elapsed_time = (end - start)

    plot_result(ancestors)
    plot_answer(last_population, ancestors)

    last_population.sort(key=lambda x: get_fitness(x)[1])
    print(f"Number of generations: {GENERATIONS}")
    print(str(round(elapsed_time, 4)), 'seconds')


if __name__ == '__main__':
    main()
