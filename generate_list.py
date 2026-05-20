import time
import random


def generate_list(row_count):

    number_list = []

    for i in range(row_count):
        number_list.append(random.randint(10000,19999))

    return number_list

