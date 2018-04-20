"""
Handles SAP Project Manager departement.
"""

from employee import Employee


class ProjectManager(Employee):
    """
    Represents an SAP Project Manager.
    """

    base_salary = 40000
    probability_to_hire = 0.1
