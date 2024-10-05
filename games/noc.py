import random
import math

def secondNoc(a, b):
    return abs(a * b) // math.gcd(a, b)

def thirdNoc(a, b, c):
    return secondNoc(lcm_two(a, b), c)

def generate_question():
    numbers = [random.randint(1, 100) for _ in range(3)]
    lcm = thirdNoc(*numbers)

    question = '{} {} {}'.format(*numbers)
    return question, lcm