class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.gender}, {self.age} y.o.'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.record_book}: {self.first_name} {self.last_name}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) == 10:
            raise ValueError('No more students can\'t be added. This group has 10 students already')
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            return self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if last_name == student.last_name:
                return student

    def __str__(self):
        if not self.group:
            return "There are no students"
        all_students = ''
        for student in self.group:
            all_students += f'{student}\n'
        return f'Number:{self.number}\n{all_students}'



st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 28, 'Chris', 'White', 'AN143')
st4 = Student('Female', 24, 'Anna', 'Smith', 'AN144')
st5 = Student('Male', 28, 'Nicholas', 'Flamel', 'AN146')
st6 = Student('Male', 26, 'Draco', 'Malfoy', 'AN148')
st7 = Student('Female', 28, 'Katie', 'James', 'AN150')
st8 = Student('Male', 26, 'Harry', 'Potter', 'AN149')
st9 = Student('Female', 31, 'Amanda', 'Jones', 'AN151')
st10 = Student('Male', 29, 'James', 'Bond', 'AN007')
st11 = Student('Female', 29, 'Anastasiia', 'Prokofieva', 'AN152')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(gr)
try:
    gr.add_student(st11)  # ValueError
except ValueError as err:
    print(err)
print(gr)
