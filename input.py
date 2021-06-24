from week import Week

PERSONNEL_NEEDS = {
    Week.MONDAY: 27,
    Week.TUESDAY: 22,
    Week.WEDNESDAY: 26,
    Week.THURSDAY: 25,
    Week.FRIDAY: 21,
    Week.SATURDAY: 19,
    Week.SUNDAY: 18,
}

GENERATIONS = 60
INDIVIDUALS_PER_GENERATION = 30
NUMBER_OF_NURSES = 100
MUTATION_RATE = 0.01

SHIFTS = {
    '1': (Week.SATURDAY, Week.SUNDAY),
    '2': (Week.MONDAY, Week.SUNDAY),
    '3': (Week.MONDAY, Week.TUESDAY),
    '4': (Week.TUESDAY, Week.WEDNESDAY),
    '5': (Week.WEDNESDAY, Week.THURSDAY),
    '6': (Week.THURSDAY, Week.FRIDAY),
    '7': (Week.FRIDAY, Week.SATURDAY),
}

BASE_SALARY = 755
WEEKEND_BONUS = 50
