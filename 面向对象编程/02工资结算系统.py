"""要求：某公司有三种类型的员工，分别是部门经理、程序员和销售员。
需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪。
其中，部门经理的月薪是固定 15000 元；
程序员按工作时间（以小时为单位）支付月薪，每小时 200 元；
销售员的月薪由 1800 元底薪加上销售额 5% 的提成两部分构成。"""
from abc import ABC, abstractmethod

class Employee:
    """员工类，包含员工的名字和计算月薪的方法
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod # 定义抽象方法，要求子类必须实现这个方法
    def get_salary(self):
        """计算月薪的方法，子类需要重写这个方法来实现不同类型员工的月薪计算
        """
        pass
class Manager(Employee):
    """部门经理类，继承自员工类，月薪固定为15000元
    """
    def get_salary(self):
        return 15000
class Programmer(Employee):
    """程序员类，继承自员工类，按工作时间支付月薪，每小时200元
    """
    def __init__(self, name, work_hours=0):
        super().__init__(name) # 调用父类的构造方法来初始化名字
        self.work_hours = work_hours # 工作时间（小时）

    def get_salary(self):
        return self.work_hours * 200 # 月薪等于工作时间乘以每小时的工资
class Salesman(Employee):
    """销售员类，继承自员工类，月薪由底薪加提成两部分构成
    """
    def __init__(self, name, sales_amount=0):
        super().__init__(name) # 调用父类的构造方法来初始化名字
        self.sales_amount = sales_amount # 销售额

    def get_salary(self):
        return 1800 + self.sales_amount * 0.05 # 月薪等于底薪加上销售额的5%提成
# 创建一些员工对象并计算他们的月薪
employees = [
    Manager("张经理"),
    Programmer("李程序员"),
    Salesman("王销售")
]

for employee in employees:
    if isinstance(employee, Programmer):
        employee.work_hours = int(input(f"请输入{employee.name}的工作时间（小时）：")) # 输入程序员的工作时间
    elif isinstance(employee, Salesman):
        employee.sales_amount = float(input(f"请输入{employee.name}的销售额：")) # 输入销售员的销售额
    print(f"{employee.name}的月薪是: {employee.get_salary()}元")    