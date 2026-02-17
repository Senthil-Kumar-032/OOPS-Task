#   Problem:- 2 Employee Management


class Employee:

    #   Base class for all employees

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):

        #   Return base salary

        return self.base_salary

    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.calculate_salary():.2f}"


class Regular_Employee(Employee):

    #   Employee with bonus

    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):

        #   Return salary including bonus

        return self.base_salary + self.bonus


class Contract_Employee(Employee):

    #   Employees who get paid hourly

    def __init__(self, name, hour_rate, hours_worked):
        super().__init__(name, 0)
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):

        #   Return salary based on hours worked

        return self.hour_rate * self.hours_worked


class Manager(Employee):

    #   Manager with incentive

    def __init__(self, name, base_salary, incentive):
        super().__init__(name, base_salary)
        self.incentive = incentive

    def calculate_salary(self):

        #   Return salary including incentive

        return self.base_salary + self.incentive


def main():

    #   Run employee salary calculations

    employee1 = Regular_Employee("Senthil", 40000, 10000)
    employee2 = Contract_Employee("Siva", 250, 100)
    employee3 = Manager("Kumar", 50000, 15000)

    employees = [employee1, employee2, employee3]

    print("Employee Salary Details:- \n")
    for employee in employees:
        print(employee)


if __name__ == "__main__":
    main()
