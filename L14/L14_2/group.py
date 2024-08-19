class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
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
