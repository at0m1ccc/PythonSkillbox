import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    karma_random = random.randint(1, 7)
    if random.randint(0, 9) == 9:
        raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
    return karma_random


with open("karma.log", "w") as file:
    sum_karma = 0
    while sum_karma < 500:
        try:
            karma = one_day()
            sum_karma += karma
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as exc:
            file.write(f"Exception: {exc.__class__.__name__}\n")
