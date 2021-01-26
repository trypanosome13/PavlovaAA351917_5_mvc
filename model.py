#!/usr/bin/env python
import mysql.connector
from datetime import date

#Сотрудники

class EmployeeModel:
    def __init__(self, Employee_Num=0, Employee_Lastname=None, Employee_Firstname=None, Employee_Patronumic=None, Employee_Position=None):
        self.Employee_Num = Employee_Num
        self.Employee_Lastname = Employee_Lastname
        self.Employee_Firstname= Employee_Firstname
        self.Employee_Patronumic = Employee_Patronumic
        self.Employee_Position = Employee_Position
    @property
    def info_employeesmodel(self):
        return f'{self.Employee_Num} | {self.Employee_Lastname} | {self.Employee_Firstname} | {self.Employee_Patronumic} | {self.Employee_Position}'

    @staticmethod
    def Get_employees():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from EmployeeModel')
        rows = c.fetchall()
        for row in rows:
            employeemodel = EmployeeModel(row[0], row[1], row[2], row[3], row[4])
            result.append(employeemodel)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_employee(Employee_Num, Employee_Lastname,Employee_Firstname,Employee_Patronumic,Employee_Position):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into EmployeeModel values(%s, %s, %s, %s, %s)', \
                  (int(Employee_Num), Employee_Lastname,Employee_Firstname,Employee_Patronumic,Employee_Position,))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_employee(Employee_Num, Employee_Lastname,Employee_Firstname,Employee_Patronumic,Employee_Position):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE EmployeeModel SET Employee_Lastname = %s, Employee_Firstname = %s, Employee_Patronumic = %s, Employee_Position = %s WHERE Employee_Num = %s"""
            ch2 = (Employee_Lastname,Employee_Firstname,Employee_Patronumic,Employee_Position,Employee_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_employee(Employee_Num):
        try:
            dl = "DELETE FROM EmployeeModel WHERE Employee_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (Employee_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

#Участки

class ProductionSiteModel:
    def __init__(self, ProductionSite_Num=0, ProductionSite_Name=None):
        self.ProductionSite_Num = ProductionSite_Num
        self.ProductionSite_Name = ProductionSite_Name
    @property
    def info_production_sites(self):
        return f'{self.ProductionSite_Num} | {self.ProductionSite_Name} '

    @staticmethod
    def Get_production_sites():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from ProductionSiteModel')
        rows = c.fetchall()
        for row in rows:
            productionsitemodel = ProductionSiteModel(row[0], row[1])
            result.append(productionsitemodel)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_production_site(ProductionSite_Num, ProductionSite_Name):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into ProductionSiteModel values(%s, %s)', \
                  (int(ProductionSite_Num), ProductionSite_Name),)
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_production_site(ProductionSite_Num, ProductionSite_Name):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE ProductionSiteModel SET ProductionSite_Name = %s WHERE ProductionSite_Num = %s"""
            ch2 = (ProductionSite_Name,ProductionSite_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_production_site(ProductionSite_Num):
        try:
            dl = "DELETE FROM ProductionSiteModel WHERE ProductionSite_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (ProductionSite_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

#Оборудование

class EquipmentModel:
    def __init__(self, Equipment_Num=0, Equipment_Name=None,ProductionSite_ProductionSite_Num=0):
        self.Equipment_Num = Equipment_Num
        self.Equipment_Name = Equipment_Name
        self.ProductionSite_ProductionSite_Num = ProductionSite_ProductionSite_Num


    @property
    def info_equipments(self):
        return f'{self.Equipment_Num} | {self.Equipment_Name}| {self.ProductionSite_ProductionSite_Num} '

    @staticmethod
    def Get_equipments():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from EquipmentModel')
        rows = c.fetchall()
        for row in rows:
            equipmentmodel = EquipmentModel(row[0], row[1],row[2])
            result.append(equipmentmodel)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_equipment(Equipment_Num, Equipment_Name,ProductionSite_ProductionSite_Num):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into EquipmentModel values(%s, %s,%s)', \
                  (int(Equipment_Num), Equipment_Name,int(ProductionSite_ProductionSite_Num),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_equipment(Equipment_Num, Equipment_Name,ProductionSite_ProductionSite_Num):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE EquipmentModel SET Equipment_Name = %s,ProductionSite_ProductionSite_Num = %s WHERE Equipment_Num"""
            ch2 = (Equipment_Name,ProductionSite_ProductionSite_Num,Equipment_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_equipment(Equipment_Num):
        try:
            dl = "DELETE FROM EquipmentModel WHERE Equipment_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (Equipment_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

#Учёт отказа оборудования

class EquipmentFailureAccountingModel:
    def __init__(self, EquipmentFailureAccounting_Num=0, EquipmentFailureAccounting_Date=None,EquipmentFailureAccounting_Result=None,EquipmentFailureAccounting_Cause=None,Equipment_Equipment_Num=0,Employee_Employee_Num=0,):
        self.EquipmentFailureAccounting_Num = EquipmentFailureAccounting_Num
        self.EquipmentFailureAccounting_Date = EquipmentFailureAccounting_Date
        self.EquipmentFailureAccounting_Result = EquipmentFailureAccounting_Result
        self.EquipmentFailureAccounting_Cause = EquipmentFailureAccounting_Cause
        self.Equipment_Equipment_Num = Equipment_Equipment_Num
        self.Employee_Employee_Num = Employee_Employee_Num


    @property
    def info_equipment_failure_records(self):
        return f'{self.EquipmentFailureAccounting_Num} | {self.EquipmentFailureAccounting_Date}| {self.EquipmentFailureAccounting_Result}| {self.EquipmentFailureAccounting_Cause}| {self.Equipment_Equipment_Num}| {self.Employee_Employee_Num} '

    @staticmethod
    def Get_equipment_failure_records():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from EquipmentFailureAccountingModel')
        rows = c.fetchall()
        for row in rows:
            equipmentfailureaccountingmodel = EquipmentFailureAccountingModel(row[0], row[1],row[2],row[3],row[4],row[5])
            result.append(equipmentfailureaccountingmodel)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_equipment_failure_record(EquipmentFailureAccounting_Num, EquipmentFailureAccounting_Date,EquipmentFailureAccounting_Result,EquipmentFailureAccounting_Cause,Equipment_Equipment_Num,Employee_Employee_Num):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into EquipmentFailureAccountingModel values(%s, %s,%s,%s, %s,%s)', \
                  (int(EquipmentFailureAccounting_Num), date.fromisoformat(EquipmentFailureAccounting_Date),EquipmentFailureAccounting_Result,EquipmentFailureAccounting_Cause,int(Equipment_Equipment_Num),int(Employee_Employee_Num),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_equipment_failure_record(EquipmentFailureAccounting_Num, EquipmentFailureAccounting_Date,EquipmentFailureAccounting_Result,EquipmentFailureAccounting_Cause,Equipment_Equipment_Num,Employee_Employee_Num):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE EquipmentFailureAccountingModel SET EquipmentFailureAccounting_Date = %s,EquipmentFailureAccounting_Result = %s,EquipmentFailureAccounting_Cause = %s,Equipment_Equipment_Num = %s,Employee_Employee_Num = %s  WHERE EquipmentFailureAccounting_Num"""
            ch2 = (EquipmentFailureAccounting_Date,EquipmentFailureAccounting_Result,EquipmentFailureAccounting_Cause,Equipment_Equipment_Num,Employee_Employee_Num,EquipmentFailureAccounting_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_equipment_failure_record(EquipmentFailureAccounting_Num):
        try:
            dl = "DELETE FROM EquipmentFailureAccountingModel WHERE EquipmentFailureAccounting_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (EquipmentFailureAccounting_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

#Технический осмотр

class TechniacalInspectionModel:
    def __init__(self, TechniacalInspection_Num=0, TechniacalInspection_Date=None,TechniacalInspection_Result=None,Equipment_Equipment_Num=0,Employee_Employee_Num=0,):
        self.TechniacalInspection_Num = TechniacalInspection_Num
        self.TechniacalInspection_Date = TechniacalInspection_Date
        self.TechniacalInspection_Result = TechniacalInspection_Result
        self.Equipment_Equipment_Num = Equipment_Equipment_Num
        self.Employee_Employee_Num = Employee_Employee_Num


    @property
    def info_inspection_records(self):
        return f'{self.TechniacalInspection_Num} | {self.TechniacalInspection_Date}| {self.TechniacalInspection_Result}| {self.Equipment_Equipment_Num}| {self.Employee_Employee_Num} '

    @staticmethod
    def Get_inspection_records():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from TechniacalInspectionModel')
        rows = c.fetchall()
        for row in rows:
            techniacalinspectionmodel = TechniacalInspectionModel(row[0], row[1],row[2],row[3],row[4])
            result.append(techniacalinspectionmodel)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_inspection_record(TechniacalInspection_Num, TechniacalInspection_Date,TechniacalInspection_Result,Equipment_Equipment_Num,Employee_Employee_Num):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into TechniacalInspectionModel values(%s, %s, %s, %s, %s)', \
                  (int(TechniacalInspection_Num), date.fromisoformat(TechniacalInspection_Date),TechniacalInspection_Result,int(Equipment_Equipment_Num),int(Employee_Employee_Num),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_inspection_record(TechniacalInspection_Num, TechniacalInspection_Date,TechniacalInspection_Result,Equipment_Equipment_Num,Employee_Employee_Num):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE TechniacalInspectionModel SET TechniacalInspection_Date = %s,TechniacalInspection_Result = %s,Equipment_Equipment_Num = %s,Employee_Employee_Num = %s  WHERE TechniacalInspection_Num"""
            ch2 = (TechniacalInspection_Date,TechniacalInspection_Result,Equipment_Equipment_Num,Employee_Employee_Num,TechniacalInspection_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_inspection_record(TechniacalInspection_Num):
        try:
            dl = "DELETE FROM TechniacalInspectionModel WHERE TechniacalInspection_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (TechniacalInspection_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

#Пользователи

class User:
    def __init__(self, User_Num=0, User_Login=None, User_Password=None, User_LoginStatus=None, User_RegisterDate=None):
        self.User_Num = User_Num
        self.User_Login = User_Login
        self.User_Password= User_Password
        self.User_LoginStatus = User_LoginStatus
        self.User_RegisterDate = User_RegisterDate
    @property
    def info_users(self):
        return f'{self.User_Num} | {self.User_Login} | {self.User_Password} | {self.User_LoginStatus} | {self.User_RegisterDate}'

    @staticmethod
    def Get_users():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from User')
        rows = c.fetchall()
        for row in rows:
            user = User(row[0], row[1], row[2], row[3], row[4])
            result.append(user)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_user(User_Num, User_Login,User_Password,User_LoginStatus,User_RegisterDate):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into User values(%s, %s, %s, %s, %s)', \
                  (int(User_Num), User_Login,User_Password,User_LoginStatus, date.fromisoformat(User_RegisterDate),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_user(User_Num, User_Login,User_Password,User_LoginStatus,User_RegisterDate):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE User SET User_Login = %s, User_Password = %s, User_LoginStatus = %s, User_RegisterDate = %s WHERE User_Num = %s"""
            ch2 = (User_Login,User_Password,User_LoginStatus,User_RegisterDate, User_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_user(User_Num):
        try:
            dl = "DELETE FROM User WHERE User_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (User_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

#Учётные записи сотрудников

class EmployeeAccountModel:
    def __init__(self, EmployeeAccount_Num=0, EmployeeAccount_Login=None, EmployeeAccount_Password=None, EmployeeAccount_LoginStatus=None, EmployeeAccount_RegisterDate=None,User_User_Num=0):
        self.EmployeeAccount_Num = EmployeeAccount_Num
        self.EmployeeAccount_Login = EmployeeAccount_Login
        self.EmployeeAccount_Password= EmployeeAccount_Password
        self.EmployeeAccount_LoginStatus = EmployeeAccount_LoginStatus
        self.EmployeeAccount_RegisterDate = EmployeeAccount_RegisterDate
        self.User_User_Num = User_User_Num
    @property
    def info_employee_accounts(self):
        return f'{self.EmployeeAccount_Num} | {self.EmployeeAccount_Login} | {self.EmployeeAccount_Password} | {self.EmployeeAccount_LoginStatus} | {self.EmployeeAccount_RegisterDate},| {self.User_User_Num}'

    @staticmethod
    def Get_employee_accounts():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from EmployeeAccountModel')
        rows = c.fetchall()
        for row in rows:
            employeeaccountmodel = EmployeeAccountModel(row[0], row[1], row[2], row[3], row[4], row[5])
            result.append(employeeaccountmodel)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_employee_accounts(EmployeeAccount_Num, EmployeeAccount_Login,EmployeeAccount_Password,EmployeeAccount_LoginStatus,EmployeeAccount_RegisterDate,User_User_Num):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into EmployeeAccountModel values(%s, %s, %s, %s, %s,%s)', \
                  (int(EmployeeAccount_Num), EmployeeAccount_Login,EmployeeAccount_Password,EmployeeAccount_LoginStatus, date.fromisoformat(EmployeeAccount_RegisterDate),int(User_User_Num)))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_employee_accounts(EmployeeAccount_Num, EmployeeAccount_Login,EmployeeAccount_Password,EmployeeAccount_LoginStatus,EmployeeAccount_RegisterDate,User_User_Num):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE EmployeeAccountModel SET EmployeeAccount_Login = %s, EmployeeAccount_Password = %s, EmployeeAccount_LoginStatus = %s, EmployeeAccount_RegisterDate = %s, User_User_Num = %s WHERE EmployeeAccount_Num = %s"""
            ch2 = (EmployeeAccount_Login,EmployeeAccount_Password,EmployeeAccount_LoginStatus,EmployeeAccount_RegisterDate,User_User_Num, EmployeeAccount_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_employee_accounts(EmployeeAccount_Num):
        try:
            dl = "DELETE FROM EmployeeAccountModel WHERE EmployeeAccount_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (EmployeeAccount_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

#Пользователь-сотрудник

class Employee:
    def __init__(self, Employee_Num=0, Employee_Name=None, User_User_Num=0):
        self.Employee_Num = Employee_Num
        self.Employee_Name = Employee_Name
        self.User_User_Num= User_User_Num
    @property
    def info_user_employees(self):
        return f'{self.Employee_Num} | {self.Employee_Name} | {self.User_User_Num} '

    @staticmethod
    def Get_user_employees():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from Employee')
        rows = c.fetchall()
        for row in rows:
            employee = Employee(row[0], row[1], row[2])
            result.append(employee)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_user_employee(Employee_Num, Employee_Name,User_User_Num):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into Employee values(%s, %s, %s)', \
                  (int(Employee_Num), Employee_Name,int(User_User_Num),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_user_employee(Employee_Num, Employee_Name,User_User_Num):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE Employee SET Employee_Name = %s, User_User_Num = %s WHERE Employee_Num = %s"""
            ch2 = (Employee_Name,User_User_Num, Employee_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_user_employee(Employee_Num):
        try:
            dl = "DELETE FROM Employee WHERE Employee_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (Employee_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

#Пользователь-управляющий

class Manager:
    def __init__(self, Manager_Num=0, Manager_Name=None, User_User_Num=0):
        self.Manager_Num = Manager_Num
        self.Manager_Name = Manager_Name
        self.User_User_Num= User_User_Num
    @property
    def info_employee_accounts(self):
        return f'{self.Manager_Num} | {self.Manager_Name} | {self.User_User_Num} '

    @staticmethod
    def Get_user_managers():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from Manager')
        rows = c.fetchall()
        for row in rows:
            manager = Manager(row[0], row[1], row[2])
            result.append(manager)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_user_manager(Manager_Num, Manager_Name,User_User_Num):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into Manager values(%s, %s, %s)', \
                  (int(Manager_Num), Manager_Name,int(User_User_Num),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_user_manager(Manager_Num, Manager_Name,User_User_Num):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE Manager SET Manager_Name = %s, User_User_Num = %s WHERE Manager_Num = %s"""
            ch2 = (Manager_Name,User_User_Num, Manager_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_user_manager(Manager_Num):
        try:
            dl = "DELETE FROM Manager WHERE Manager_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (Manager_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()

#Пользователь-администратор

class Administrator:
    def __init__(self, Administrator_Num=0, Administrator_Name=None, User_User_Num=0):
        self.Administrator_Num = Administrator_Num
        self.Administrator_Name = Administrator_Name
        self.User_User_Num= User_User_Num
    @property
    def info_employee_accounts(self):
        return f'{self.Administrator_Num} | {self.Administrator_Name} | {self.User_User_Num} '

    @staticmethod
    def Get_user_administrators():
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        result = []
        c.execute('select * from Administrator')
        rows = c.fetchall()
        for row in rows:
            administrator = Administrator(row[0], row[1], row[2])
            result.append(administrator)
        c.close()
        conn.close()
        return result

    @staticmethod
    def Add_user_administrators(Administrator_Num, Administrator_Name,User_User_Num):
        conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
        c = conn.cursor()
        c.execute('insert into Administrator values(%s, %s, %s)', \
                  (int(Administrator_Num), Administrator_Name,int(User_User_Num),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def Change_user_administrators(Administrator_Num, Administrator_Name,User_User_Num):
        try:
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            ch1 = """UPDATE Administrator SET Administrator_Name = %s, User_User_Num = %s WHERE Administrator_Num = %s"""
            ch2 = (Administrator_Name,User_User_Num, Administrator_Num)
            c.execute(ch1, ch2)
            conn.commit()
            c.close()
        finally:
            conn.close()

    @staticmethod
    def Delete_user_administrators(Administrator_Num):
        try:
            dl = "DELETE FROM Administrator WHERE Administrator_Num = %s"
            conn = mysql.connector.connect(user='root', password='trypanosome!3', host='localhost', database='EquipmentFailureAccounting')
            c = conn.cursor()
            c.execute(dl, (Administrator_Num,))
            conn.commit()
            c.close()
        finally:
            conn.close()



