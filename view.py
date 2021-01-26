#!/usr/bin/env python
class View:
    #сотрудники
    @staticmethod
    def show_employeesmodel(list):
        print(f'in database {len(list)} employeesmodel. they are:')
        for item in list:
            print(item.info_employeesmodel)
    @staticmethod
    def delete_employeesmodel(list):
        print('Deleted')
    @staticmethod
    def change_info_employeesmodel(list):

    # производственные участки
        print('Data is changed')
    @staticmethod
    def show_production_sites(list):
        print(f'in database {len(list)} production_sites. they are:')
        for item in list:
            print(item.info_production_sites)
    @staticmethod
    def delete_production_sites(list):
        print('Deleted')
    @staticmethod
    def change_info_production_sites(list):
        print('Data is changed')

    # оборудование
    @staticmethod
    def show_equipments(list):
        print(f'in database {len(list)} equipments. they are:')
        for item in list:
            print(item.info_equipments)
    @staticmethod
    def delete_equipments(list):
        print('Deleted')
    @staticmethod
    def change_info_equipments(list):
        print('Data is changed')

    # учёт отказа оборудования
    @staticmethod
    def show_equipment_failure_records(list):
        print(f'in database {len(list)} equipment_failure_records. they are:')
        for item in list:
            print(item.info_equipment_failure_records)
    @staticmethod
    def delete_equipment_failure_records(list):
        print('Deleted')
    @staticmethod
    def change_info_equipment_failure_records(list):
        print('Data is changed')

    # технический осмотр
    @staticmethod
    def show_inspection_records(list):
        print(f'in database {len(list)} inspection_records. they are:')
        for item in list:
            print(item.info_inspection_records)
    @staticmethod
    def delete_inspection_records(list):
        print('Deleted')
    @staticmethod
    def change_info_inspection_records(list):
        print('Data is changed')

    # пользователи
    @staticmethod
    def show_users(list):
        print(f'in database {len(list)} users. they are:')
        for item in list:
            print(item.info_users)
    @staticmethod
    def delete_users(list):
        print('Deleted')
    @staticmethod
    def change_info_users(list):
        print('Data is changed')

    # учётные записи
    @staticmethod
    def show_employee_accounts(list):
        print(f'in database {len(list)} employee_accounts. they are:')
        for item in list:
            print(item.info_employee_accounts)
    @staticmethod
    def delete_employee_accounts(list):
        print('Deleted')
    @staticmethod
    def change_info_employee_accounts(list):
        print('Data is changed')

    # пользователи-сотрудники
    @staticmethod
    def show_user_employees(list):
        print(f'in database {len(list)} user_employees. they are:')
        for item in list:
            print(item.info_user_employees)

    @staticmethod
    def delete_user_employees(list):
        print('Deleted')

    @staticmethod
    def change_info_user_employees(list):
        print('Data is changed')

    # пользователи-управляющие
    @staticmethod
    def show_user_managers(list):
        print(f'in database {len(list)} user_managers. they are:')
        for item in list:
            print(item.info_employee_accounts)

    @staticmethod
    def delete_user_managers(list):
        print('Deleted')

    @staticmethod
    def change_info_user_managers(list):
        print('Data is changed')

    # пользователи-администраторы
    @staticmethod
    def show_user_administrators(list):
        print(f'in database {len(list)} user_administrators. they are:')
        for item in list:
            print(item.info_employee_accounts)

    @staticmethod
    def delete_user_administrators(list):
        print('Deleted')

    @staticmethod
    def change_info_user_administrators(list):
        print('Data is changed')



    @staticmethod
    def get_data(text):
        return input('enter ' + text + ':')
    @staticmethod
    def show_menu():
        print('what do you want:\n'+
            '\t (1) show_employeesmodel\n'+
            '\t (2) delete_employeesmodel\n' +
            '\t (3) change_info_employeesmodel\n' +
            '\t (4) add_employeesmodel\n'+
            '\t (5) show_production_sites\n' +
            '\t (6) delete_production_sites\n' +
            '\t (7) change_info_production_sites\n' +
            '\t (8) add_production_sites\n' +
            '\t (9) show_equipments\n' +
            '\t (10) delete_equipments\n' +
            '\t (11) change_info_equipments\n' +
            '\t (12) add_equipments\n' +
            '\t (13) show_equipment_failure_records\n' +
            '\t (14) delete_equipment_failure_records\n' +
            '\t (15) change_info_equipment_failure_records\n' +
            '\t (16) add_equipment_failure_records\n' +
            '\t (17) show_inspection_records\n' +
            '\t (18) delete_inspection_records\n' +
            '\t (19) change_info_inspection_records\n' +
            '\t (20) add_inspection_records\n' +
            '\t (21) show_users\n' +
            '\t (22) delete_users\n' +
            '\t (23) change_info_users\n' +
            '\t (24) add_users\n' 
            '\t (25) show_employee_accounts\n' +
            '\t (26) delete_employee_accounts\n' +
            '\t (27) change_info_employee_accounts\n' +
            '\t (28) add_employee_accounts\n'  +
            '\t (29) show_user_employees\n' +
            '\t (30) delete_user_employees\n' +
            '\t (31) change_info_user_employees\n' +
            '\t (32) add_user_employees\n' +
            '\t (33) show_user_managers\n' +
            '\t (34) delete_user_managers\n' +
            '\t (35) change_info_user_managers\n' +
            '\t (36) add_user_managers\n' +
            '\t (37) show_user_administrators\n' +
            '\t (38) delete_user_administrators\n' +
            '\t (39) change_info_user_administrators\n' +
            '\t (40) add_user_administrators\n' +
            '\t (41) exit\n')