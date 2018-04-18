import random

from employee import Employee


class Velocity():
    def __init__(value):
        self.value = value

    @staticmethod
    def random_velocity():
        return random.randint(0, 100)


class Developer(Employee):
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
