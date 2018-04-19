"""
Main entry point.
Generates SAP workforce.
"""

from factory import EmployeeFactory


if __name__ == '__main__':
    N_SAP_EMPLOYEES = 1000

    # Ratios of employees by type
    SAP_RATIOS = {
        'sales': 0.25,
        'developer': 0.35,
        'project_manager': 0.25,
        'support': 0.15,
    }

    print('Generating workforce...')
    sap_workforce = EmployeeFactory.generate_workforce(N_SAP_EMPLOYEES, SAP_RATIOS)
    print('Workforce generated.\n')

    print('Employee of the month is:', sap_workforce[0])
