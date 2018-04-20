"""
Handles SAP Developers departement.
"""

import random

from employee import Employee


class Velocity():
    """
    Holds the Agile Velocity of a Developer.
    The velocity is an integer value between 0 and 100.
    """

    def __init__(self, value):
        self.value = value

    @staticmethod
    def random_velocity():
        """
        Returns a random velocity.
        """
        return random.randint(0, 100)


class Developer(Employee):
    """
    Represents an SAP Developer Employee.
    """

    base_salary = 40000
    probability_to_hire = 0.05

    def __init__(self, velocity, **kwargs):
        super().__init__(**kwargs)
        self.velocity = velocity

    @classmethod
    def random_attrs(cls):
        random_attrs = super().random_attrs()
        random_attrs.update({'velocity': Velocity.random_velocity()})
        return random_attrs
