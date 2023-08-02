# Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName,
# getAge, getGroupNumber, setNameAge, setGroupNumber.
# Метод getName нужен для получения данных об имени конкретного студента,
# метод getAge нужен для получения данных о возрасте конкретного студента,
# метод setGroupNumber нужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber
# позволяет изменить номер группы установленный по умолчанию.
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.


class Student:
    def __init__(self, name="Ivan", groupNumber="10A", age=18):
        self.name = name
        self.groupNumber = groupNumber
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setGroupNumber(self, newGroupNumber: str):
        self.groupNumber = newGroupNumber


me = Student("Арсений", "9В", 15)
slava = Student("Слава", "11А", 19)
dima = Student("Дима", "1Б", 19)
rofl_fish = Student("Синяя рыбка", "Аквариум", 2)
babidjon = Student("Бабиджон", "4Г", 33)
zubarev = Student("Александр", "7Д", 37)
