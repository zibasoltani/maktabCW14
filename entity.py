class Entity:
    def __init__(self, id):
        self.id = id


class Student(Entity):
    def __init__(self, name, date_of_birth):
        super().__init__(id)
        self.name = name
        self.date_of_birth = date_of_birth


class Course(Entity):
    def __init__(self,title, number_of_credits):
        super().__init__(id)
        self.title = title
        self.number_of_credits = number_of_credits


class Instructor(Entity):
    def __init__(self, name, specialization, department):
        super().__init__(id)
        self.name = name
        self.specialization = specialization
        self.department = department


class Department(Entity):
    def __init__(self, name):
        super().__init__(id)
        self.name = name


class StudentRegistration(Entity):
    def __init__(self, student_id, course_id, registration_date):
        super().__init__(id)
        self.student = student_id
        self.course = course_id
        self.registration_date = registration_date
