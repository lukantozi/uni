from datetime import datetime


NOW = datetime.now().year
BASE_SALARY = 5000
EXP_MANAGER = 5


class Employee:
    emp_count = 0
    cur_team = 0
    def __init__(self, name, surname, birth_year, experience, position):
        self.birth_year = birth_year
        self.position = position
        self.id_number = f"{(Employee.emp_count + 1):04}"
        self.experience = experience
        self.name = name
        self.surname = surname
        self.salary = 5000 * (1 + experience / 10)
        Employee.emp_count += 1
        Employee.cur_team += 1

    @property
    def id_number(self):
        return self._id_number
    
    @id_number.setter
    def id_number(self, idn):
        if (int(idn) % 20 == 0) and self.position != "Manager":
            raise Exception("Current team is full. Hire new manager.")
        self._id_number = idn

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, year):
        if type(year) != int:
            raise ValueError("Please enter only integer values")
        if 18 < NOW - int(year) > 99:
            raise ValueError("Valid range: 18-99")
        self._birth_year = int(year)

    def email(self):
        return f"{self.name}_{self.surname}_{(self._birth_year % 100):02}@job.email.com"
    
    def age(self):
        return NOW - self._birth_year

    @classmethod
    def members_in_team(cls):
        return cls.emp_count
    

class Manager(Employee):

    def __init__(self, name, surname, birth_year, experience):
        super().__init__(name, surname, birth_year, experience, position="Manager")
        self.salary = self.salary + 2000

    def manages(self):
        return f"Manages {Employee.emp_count - 1} employees"

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, xp):
        if xp < EXP_MANAGER:
            raise ValueError(f"Not experienced enough... try again in {EXP_MANAGER - xp} years")
        self._experience = xp


emp = Manager("John", "Doe", 1999, 5)
print(emp.email())
print(emp.members_in_team())
#print(emp.manages())
print(emp.salary)
print(emp.id_number)

emp = Manager("John", "Doe", 1999, 5)
print(emp.email())
print(emp.members_in_team())
#print(emp.manages())
print(emp.salary)
print(emp.id_number)
