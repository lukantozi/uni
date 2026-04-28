from datetime import datetime


NOW = datetime.now().year
BASE_SALARY = 5000
EXP_MANAGER = 5


class Employee:
    emp_count = 0
    def __init__(self, name, surname, birth_year, experience, position):
        self.birth_year = birth_year
        self.position = position
        self.id_number = f"{(Employee.emp_count):04}"
        self.experience = experience
        self.name = name
        self.surname = surname
        self.__salary = 5000 * (1 + experience / 10)
        Employee.emp_count += 1

    def get_salary(self):
        return self.__salary

    @property
    def id_number(self):
        return self._id_number
    
    @id_number.setter
    def id_number(self, idn):
        if not str(idn).isdigit():
            raise ValueError("ID number must contain digits only")
        self._id_number = f"{int(idn):04}"

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, year):
        if not isinstance(year, int):
            raise ValueError("Please enter only integer values")
        age = NOW - year
        if not (18 < age < 100):
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
        self.__salary = super().get_salary() + 2000

    def get_salary(self):
        return self.__salary

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, xp):
        if xp < EXP_MANAGER:
            raise ValueError(f"Not experienced enough... try again in {EXP_MANAGER - xp} years")
        self._experience = xp


emp = Employee("John", "Doe", 1988, 3, "acc")
print(emp.experience)
print(emp.get_salary())
print(emp._Employee__salary)
# man = Manager("John", "Harvard", 1970, 1) # -> will raise an error due to insufficient exp years
man = Manager("John", "Harvard", 1970, 10)
print(man.get_salary())
# emp_1 = Employee("baby", "boss", 2025, 0, "ceo") # -> will raise an error because baby boss too young
print(man.email())
