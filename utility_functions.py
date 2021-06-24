import statistics
from random import uniform

from input import BASE_SALARY, WEEKEND_BONUS, SHIFTS
from week import Week

import numpy as np
import random


def fifty_fifty():
    """
    Return 0 or 1 with 50% chance for each
    """
    return random.randrange(2)


def weekend_day(day: Week):
    return day == Week.SATURDAY or day == Week.SUNDAY


def get_salary(free_days: (Week, Week)):
    if weekend_day(free_days[0]) and weekend_day(free_days[1]):
        return BASE_SALARY
    if weekend_day(free_days[0]) or weekend_day(free_days[1]):
        return BASE_SALARY + WEEKEND_BONUS

    return BASE_SALARY + 2 * WEEKEND_BONUS


def get_all_salaries():
    salaries = []

    for free_days in SHIFTS.values():
        salaries.append(get_salary(free_days))

    return salaries


MAX_SALARY = np.max(get_all_salaries())
MIN_SALARY = np.min(get_all_salaries())
AVG_SALARY = np.mean(get_all_salaries())


def mean_normalization(x):
    x_prime = (x - AVG_SALARY) / (MAX_SALARY - MIN_SALARY)

    return x_prime


def get_fitness(individual):
    fitness_score = 0
    full_salary = 0

    for nurse_schedule in individual.chromosome:
        weekly_salary = get_salary(SHIFTS[nurse_schedule])
        fitness_score -= mean_normalization(weekly_salary)
        full_salary += weekly_salary

    return fitness_score, full_salary


def get_schedule(schedule):
    daily_nurses = [0] * len(Week)

    for nurse_schedule in schedule:
        for index in range(len(daily_nurses)):
            if index != SHIFTS[nurse_schedule][0].value and index != SHIFTS[nurse_schedule][1].value:
                daily_nurses[index] += 1
    return daily_nurses
