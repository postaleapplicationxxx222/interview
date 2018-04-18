from enum import Enum
import random

import utils


class Grade(Enum):
    JUNIOR = 0
    MID_LEVEL = 1
    ADVANCED = 2
    SENIOR = 3

    @staticmethod
    def random_grade():
        return random.choice(list(Grade))


class Employee:
    """
    A Generic SAP Employee.
    """
    base_salary = None

    def __init__(self, first_name, last_name, email, grade, salary, identifier=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.identifier = identifier
        self.grade = grade
        self.salary = salary

    @classmethod
    def random_attrs(cls):
        random_first_name = utils.get_random_first_name()
        random_last_name = utils.get_random_last_name()
        random_grade = Grade.random_grade()
        random_salary = cls.random_salary(random_grade)
        return {
            'first_name': random_first_name,
            'last_name': random_last_name,
            'email': '{}.{}@sap.com'.format(random_first_name.lower()[:6],
                                            random_last_name.lower()[:6]),
            'grade': Grade.random_grade(),
            'salary': random_salary,
            'identifier': 114422335555551,
        }

    @classmethod
    def random_salary(cls, grade):
        grade_booster = (1 + grade.value / 10)
        return str(cls.base_salary * grade_booster + random.randint(0, grade.value * 10000))
