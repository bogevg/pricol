class Person:
    def __init__(self, name: str, age: int, profession: str):
        self.name = name
        self.age = age
        self.profession = profession
    def display_info(self) -> str:
        print(' name:', self.name, '\n','age:', self.age, '\n', 'profession:',self.profession)


list_per = [Person('', 0, '') for i in range(4)]
list_per[0].name = 'person1'
list_per[0].age = '100'
list_per[0].profession = 'giga'

list_per[1].name = 'person2'
list_per[1].age = '101'
list_per[1].profession = 'giga_good'

list_per[2].name = 'person3'
list_per[2].age = '103'
list_per[2].profession = 'giga_mb'


for i in range(4):
    list_per[i].display_info()