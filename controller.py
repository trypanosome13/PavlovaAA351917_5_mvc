from model import EmployeeModel,ProductionSiteModel,EquipmentModel,EquipmentFailureAccountingModel,TechniacalInspectionModel,User,EmployeeAccountModel,Employee,Manager,Administrator
from view import View
class Controller:
    #Сотрудники
    def show_employeesmodel(self):
        employeemodel = EmployeeModel.Get_employees()
        return View.show_employeesmodel(employeemodel)

    def delete_employeesmodel(self):
        num = View.get_data('Employee_Num')
        employeemodel = EmployeeModel.Delete_employee(num)
        return View.delete_employeesmodel(employeemodel)

    def change_info_employeesmodel(self):
        Employee_Num = View.get_data('Employee_Num')
        Employee_Lastname = View.get_data('Employee_Lastname')
        Employee_Firstname = View.get_data('Employee_Firstname')
        Employee_Patronumic = View.get_data('Employee_Patronumic')
        Employee_Position = View.get_data('Employee_Position')
        employeemodel = EmployeeModel.Change_employee(Employee_Num,Employee_Lastname,Employee_Firstname,Employee_Patronumic,Employee_Position)
        return View.change_info_employeesmodel(employeemodel)

    def add_employeesmodel(self):
        Employee_Num = View.get_data('Employee_Num')
        Employee_Lastname = View.get_data('Employee_Lastname')
        Employee_Firstname = View.get_data('Employee_Firstname')
        Employee_Patronumic = View.get_data('Employee_Patronumic')
        Employee_Position = View.get_data('Employee_Position')
        employeemodel = EmployeeModel.Add_employee(Employee_Num,Employee_Lastname,Employee_Firstname,Employee_Patronumic,Employee_Position)

    #Участки
    def show_production_sites(self):
        productionsitemodel = ProductionSiteModel.Get_production_sites()
        return View.show_production_sites(productionsitemodel)

    def delete_production_sites(self):
        num = View.get_data('Employee_Num')
        productionsitemodel = ProductionSiteModel.Delete_production_site(num)
        return View.delete_production_sites(productionsitemodel)

    def change_info_production_sites(self):
        ProductionSite_Num = View.get_data('ProductionSite_Num')
        ProductionSite_Name = View.get_data('ProductionSite_Name')
        productionsitemodel = ProductionSiteModel.Change_production_site(ProductionSite_Num,ProductionSite_Name)
        return View.change_info_production_sites(productionsitemodel)

    def add_production_sites(self):
        ProductionSite_Num = View.get_data('ProductionSite_Num')
        ProductionSite_Name = View.get_data('ProductionSite_Name')
        productionsitemodel = ProductionSiteModel.Add_production_site(ProductionSite_Num,ProductionSite_Name)

    #Оборудование
    def show_equipments(self):
        equipmentmodel = EquipmentModel.Get_equipments()
        return View.show_equipments(equipmentmodel)

    def delete_equipments(self):
        num = View.get_data('Equipment_Num')
        equipmentmodel = EquipmentModel.Delete_equipment(num)
        return View.delete_equipments(equipmentmodel)

    def change_info_equipments(self):
        Equipment_Num = View.get_data('Equipment_Num')
        Equipment_Name = View.get_data('Equipment_Name')
        equipmentmodel = EquipmentModel.Change_equipment(Equipment_Num,Equipment_Name)
        return View.change_info_equipments(equipmentmodel)

    def add_equipments(self):
        Equipment_Num = View.get_data('Equipment_Num')
        Equipment_Name = View.get_data('Equipment_Name')
        equipmentmodel = EquipmentModel.Add_equipment(Equipment_Num,Equipment_Name)

    #Учёт отказа оборудования
    def show_equipment_failure_records(self):
        equipmentfailureaccountingmodel = EquipmentFailureAccountingModel.Get_equipment_failure_records()
        return View.show_equipments(equipmentfailureaccountingmodel)

    def delete_equipment_failure_records(self):
        num = View.get_data('EquipmentFailureAccounting_Num')
        equipmentfailureaccountingmodel = EquipmentFailureAccountingModel.Delete_equipment_failure_record(num)
        return View.delete_equipment_failure_records(equipmentfailureaccountingmodel)

    def change_info_equipment_failure_records(self):
        EquipmentFailureAccounting_Num = View.get_data('EquipmentFailureAccounting_Num')
        EquipmentFailureAccounting_Date = View.get_data('EquipmentFailureAccounting_Date')
        EquipmentFailureAccounting_Result = View.get_data('EquipmentFailureAccounting_Result')
        EquipmentFailureAccounting_Cause = View.get_data('EquipmentFailureAccounting_Cause')
        Equipment_Equipment_Num = View.get_data('Equipment_Equipment_Num')
        Employee_Employee_Num = View.get_data('Employee_Employee_Num')
        equipmentfailureaccountingmodel = EquipmentFailureAccountingModel.Change_equipment_failure_record(EquipmentFailureAccounting_Num,EquipmentFailureAccounting_Date,EquipmentFailureAccounting_Result,EquipmentFailureAccounting_Cause,Equipment_Equipment_Num,Employee_Employee_Num)
        return View.change_info_equipment_failure_records(equipmentfailureaccountingmodel)

    def add_equipment_failure_records(self):
        EquipmentFailureAccounting_Num = View.get_data('EquipmentFailureAccounting_Num')
        EquipmentFailureAccounting_Date = View.get_data('EquipmentFailureAccounting_Date')
        EquipmentFailureAccounting_Result = View.get_data('EquipmentFailureAccounting_Result')
        EquipmentFailureAccounting_Cause = View.get_data('EquipmentFailureAccounting_Cause')
        Equipment_Equipment_Num = View.get_data('Equipment_Equipment_Num')
        Employee_Employee_Num = View.get_data('Employee_Employee_Num')
        equipmentfailureaccountingmodel = EquipmentFailureAccountingModel.Add_equipment_failure_record(EquipmentFailureAccounting_Num,EquipmentFailureAccounting_Date,EquipmentFailureAccounting_Result,EquipmentFailureAccounting_Cause,Equipment_Equipment_Num,Employee_Employee_Num)

    #Технический осмотр
    def show_inspection_records(self):
        techniacalinspectionmodel = TechniacalInspectionModel.Get_inspection_records()
        return View.show_inspection_records(techniacalinspectionmodel)

    def delete_inspection_records(self):
        num = View.get_data('TechniacalInspection_Num')
        techniacalinspectionmodel = TechniacalInspectionModel.Delete_inspection_record(num)
        return View.delete_inspection_records(techniacalinspectionmodel)

    def change_info_inspection_records(self):
        TechniacalInspection_Num = View.get_data('TechniacalInspection_Num')
        TechniacalInspection_Date = View.get_data('TechniacalInspection_Date')
        TechniacalInspection_Result = View.get_data('TechniacalInspection_Result')
        Equipment_Equipment_Num = View.get_data('Equipment_Equipment_Num')
        Employee_Employee_Num = View.get_data('Employee_Employee_Num')
        techniacalinspectionmodel = TechniacalInspectionModel.Change_inspection_record(TechniacalInspection_Num,TechniacalInspection_Date,TechniacalInspection_Result,Equipment_Equipment_Num,Employee_Employee_Num)
        return View.change_info_inspection_records(techniacalinspectionmodel)

    def add_inspection_records(self):
        TechniacalInspection_Num = View.get_data('TechniacalInspection_Num')
        TechniacalInspection_Date = View.get_data('TechniacalInspection_Date')
        TechniacalInspection_Result = View.get_data('TechniacalInspection_Result')
        Equipment_Equipment_Num = View.get_data('Equipment_Equipment_Num')
        Employee_Employee_Num = View.get_data('Employee_Employee_Num')
        techniacalinspectionmodel = TechniacalInspectionModel.Add_inspection_record(TechniacalInspection_Num,TechniacalInspection_Date,TechniacalInspection_Result,Equipment_Equipment_Num,Employee_Employee_Num)

    #Пользователи
    def show_users(self):
        user = User.Get_users()
        return View.show_users(user)

    def delete_users(self):
        num = View.get_data('User_Num')
        user = User.Delete_user(num)
        return View.delete_users(user)

    def change_info_users(self):
        User_Num = View.get_data('User_Num')
        User_Login = View.get_data('User_Login')
        User_Password = View.get_data('User_Password')
        User_LoginStatus = View.get_data('User_LoginStatus')
        User_RegisterDate = View.get_data('User_RegisterDate')
        user = User.Change_user(User_Num,User_Login,User_Password,User_LoginStatus,User_RegisterDate)
        return View.change_info_users(user)

    def add_users(self):
        User_Num = View.get_data('User_Num')
        User_Login = View.get_data('User_Login')
        User_Password = View.get_data('User_Password')
        User_LoginStatus = View.get_data('User_LoginStatus')
        User_RegisterDate = View.get_data('User_RegisterDate')
        user = User.Add_user(User_Num,User_Login,User_Password,User_LoginStatus,User_RegisterDate)

    #Учётные записи сотрудников
    def show_employee_accounts(self):
        employeeaccountmodel = EmployeeAccountModel.Get_employee_accounts()
        return View.show_users(employeeaccountmodel)

    def delete_employee_accounts(self):
        num = View.get_data('EmployeeAccount_Num')
        user = EmployeeAccountModel.Delete_employee_accounts(num)
        return View.delete_users(user)

    def change_info_employee_accounts(self):
        EmployeeAccount_Num = View.get_data('EmployeeAccount_Num')
        EmployeeAccount_Login = View.get_data('EmployeeAccount_Login')
        EmployeeAccount_Password = View.get_data('EmployeeAccount_Password')
        EmployeeAccount_LoginStatus = View.get_data('EmployeeAccount_LoginStatus')
        EmployeeAccount_RegisterDate = View.get_data('EmployeeAccount_RegisterDate')
        User_User_Num = View.get_data('User_User_Num')
        employeeaccountmodel = EmployeeAccountModel.Change_employee_accounts(EmployeeAccount_Num,EmployeeAccount_Login,EmployeeAccount_Password,EmployeeAccount_LoginStatus,EmployeeAccount_RegisterDate,User_User_Num)
        return View.change_info_users(employeeaccountmodel)

    def add_employee_accounts(self):
        EmployeeAccount_Num = View.get_data('EmployeeAccount_Num')
        EmployeeAccount_Login = View.get_data('EmployeeAccount_Login')
        EmployeeAccount_Password = View.get_data('EmployeeAccount_Password')
        EmployeeAccount_LoginStatus = View.get_data('EmployeeAccount_LoginStatus')
        EmployeeAccount_RegisterDate = View.get_data('EmployeeAccount_RegisterDate')
        User_User_Num = View.get_data('User_User_Num')
        employeeaccountmodel = EmployeeAccountModel.Add_employee_accounts(EmployeeAccount_Num,EmployeeAccount_Login,EmployeeAccount_Password,EmployeeAccount_LoginStatus,EmployeeAccount_RegisterDate,User_User_Num)

    #Пользователь-сотрудник
    def show_user_employees(self):
        employee = Employee.Get_user_employees()
        return View.show_user_employees(employee)

    def delete_user_employees(self):
        num = View.get_data('Employee_Num')
        employee = Employee.Delete_user_employee(num)
        return View.delete_user_employees(employee)

    def change_info_user_employees(self):
        Employee_Num = View.get_data('Employee_Num')
        Employee_Name = View.get_data('Employee_Name')
        User_User_Num = View.get_data('User_User_Num')
        employee = Employee.Change_user_employee(Employee_Num,Employee_Name,User_User_Num)
        return View.change_info_users(employee)

    def add_user_employees(self):
        Employee_Num = View.get_data('Employee_Num')
        Employee_Name = View.get_data('Employee_Name')
        User_User_Num = View.get_data('User_User_Num')
        employee = Employee.Add_user_employee(Employee_Num,Employee_Name,User_User_Num)

    #Пользователь-управляющий
    def show_user_managers(self):
        manager = Manager.Get_user_managers()
        return View.show_user_managers(manager)

    def delete_user_managers(self):
        num = View.get_data('Employee_Num')
        manager = Manager.Delete_user_manager(num)
        return View.delete_user_managers(manager)

    def change_info_user_managers(self):
        Manager_Num = View.get_data('Manager_Num')
        Manager_Name = View.get_data('Manager_Name')
        User_User_Num = View.get_data('User_User_Num')
        manager = Manager.Change_user_manager(Manager_Num,Manager_Name,User_User_Num)
        return View.change_info_user_managers(manager)

    def add_user_managers(self):
        Manager_Num = View.get_data('Manager_Num')
        Manager_Name = View.get_data('Manager_Name')
        User_User_Num = View.get_data('User_User_Num')
        manager = Manager.Add_user_manager(Manager_Num,Manager_Name,User_User_Num)

    #Пользователь-администратор
    def show_user_administrators(self):
        administrator = Administrator.Get_user_administrators()
        return View.show_user_administrators(administrator)

    def delete_user_administrators(self):
        num = View.get_data('Administrator_Num')
        administrator = Administrator.Delete_user_administrators(num)
        return View.delete_user_administrators(administrator)

    def change_info_user_administrators(self):
        Administrator_Num = View.get_data('Administrator_Num')
        Administrator_Name = View.get_data('Administrator_Name')
        User_User_Num = View.get_data('User_User_Num')
        administrator = Administrator.Change_user_administrators(Administrator_Num,Administrator_Name,User_User_Num)
        return View.change_info_user_administrators(administrator)

    def add_user_administrators(self):
        Administrator_Num = View.get_data('Administrator_Num')
        Administrator_Name = View.get_data('Administrator_Name')
        User_User_Num = View.get_data('User_User_Num')
        administrator = Administrator.Add_user_administrators(Administrator_Num,Administrator_Name,User_User_Num)

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.show_employeesmodel(),
            2: lambda: self.delete_employeesmodel(),
            3: lambda: self.change_info_employeesmodel(),
            4: lambda: self.add_employeesmodel(),
            5: lambda: self.show_production_sites(),
            6: lambda: self.delete_production_sites(),
            7: lambda: self.change_info_production_sites(),
            8: lambda: self.add_production_sites(),
            9: lambda: self.show_equipments(),
            10: lambda: self.delete_equipments(),
            11: lambda: self.change_info_equipments(),
            12: lambda: self.add_equipments(),
            13: lambda: self.show_equipment_failure_records(),
            14: lambda: self.delete_equipment_failure_records(),
            15: lambda: self.change_info_equipment_failure_records(),
            16: lambda: self.add_equipment_failure_records(),
            17: lambda: self.show_inspection_records(),
            18: lambda: self.delete_inspection_records(),
            19: lambda: self.change_info_inspection_records(),
            20: lambda: self.add_inspection_records(),
            21: lambda: self.show_users(),
            22: lambda: self.delete_users(),
            23: lambda: self.change_info_users(),
            24: lambda: self.add_users(),
            25: lambda: self.show_employee_accounts(),
            26: lambda: self.delete_employee_accounts(),
            27: lambda: self.change_info_employee_accounts(),
            28: lambda: self.add_employee_accounts(),
            29: lambda: self.show_user_employees(),
            30: lambda: self.delete_user_employees(),
            31: lambda: self.change_info_user_employees(),
            32: lambda: self.add_user_employees(),
            33: lambda: self.show_user_managers(),
            34: lambda: self.delete_user_managers(),
            35: lambda: self.change_info_user_managers(),
            36: lambda: self.add_user_managers(),
            37: lambda: self.show_user_administrators(),
            38: lambda: self.delete_user_administrators(),
            39: lambda: self.change_info_user_administrators(),
            40: lambda: self.add_user_administrators(),
        }
        while (choice != 41):
            View.show_menu()
            choice = int(View.get_data('choice option'))
            if choice in choices:
                choices[choice]()


if __name__ == '__main__':
    Controller().run()