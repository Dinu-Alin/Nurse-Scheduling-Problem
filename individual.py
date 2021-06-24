from week import Week
from utility_functions import fifty_fifty
from random import uniform, randint

from input import MUTATION_RATE, SHIFTS, PERSONNEL_NEEDS


class Individual:
    def __init__(self, weekly_schedule: str):
        self.chromosome = weekly_schedule

    def __str__(self):
        return self.chromosome.__str__()

    def __repr__(self):
        return self.chromosome.__str__()


def is_valid(schedule):
    daily_nurses = [0] * len(Week)

    for nurse_schedule in schedule:
        for index in range(len(daily_nurses)):
            if index != SHIFTS[nurse_schedule][0].value and index != SHIFTS[nurse_schedule][1].value:
                daily_nurses[index] += 1

    for day in Week:
        if daily_nurses[day.value] < PERSONNEL_NEEDS[day]:
            return False
    return True


def crossover(father: Individual, mother: Individual):
    nurses = len(father.chromosome)

    first_child = ['0'] * nurses
    second_child = ['0'] * nurses

    while True:
        for gene in range(nurses):
            if fifty_fifty():
                first_child[gene] = father.chromosome[gene]
                second_child[gene] = mother.chromosome[gene]
            else:
                first_child[gene] = mother.chromosome[gene]
                second_child[gene] = father.chromosome[gene]
        if is_valid(first_child) and is_valid(second_child):
            break

    first_child = mutate(first_child)
    second_child = mutate(second_child)

    return Individual("".join(first_child)), Individual("".join(second_child))


def mutate(chromosome):
    for index in range(len(chromosome)):
        chance = uniform(0., 1.)
        if chance <= MUTATION_RATE:

            while True:
                shift_mutated = str(randint(1, len(Week) - 1))

                if shift_mutated != chromosome[index]:
                    chromosome[index] = shift_mutated
                    break

    return chromosome
