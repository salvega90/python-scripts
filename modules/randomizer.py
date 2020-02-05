import random


class Randomizer:
    def __init__(self):
        self.butt = ""

    @staticmethod
    def rand_humans(humans):
        """
        Returns randomized list of humans
        :param humans: List of Human Names
        :return: Randomized list of human names
        """
        random.shuffle(humans)
        return humans

    @staticmethod
    def rand_rows():
        """
        :return: Randomized list of numbers 0-9
        """
        outside_rows = list(range(0, 10))
        random.shuffle(outside_rows)
        return outside_rows
