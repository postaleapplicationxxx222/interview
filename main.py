from factory import EmployeeFactory
from developer import Developer


if __name__ == '__main__':
    n_sap_employees = 100

    # Ratios of employees by type
    sap_ratios = {
        'sales': 0.25,
        'developer': 0.35,
        'project_manager': 0.25,
        'support': 0.15,
    }

    print('Generating workforce...')
    sap_workforce = EmployeeFactory.generate_workforce(n_sap_employees, sap_ratios)
    print('Workforce generated.\n')

    print('Employee of the month is:', sap_workforce[0])
