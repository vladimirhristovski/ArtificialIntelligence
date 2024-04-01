import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"


class Subject:
    def __init__(self, subject_name, points_practice, points_theory, points_labs):
        self.subject_name = subject_name
        self.points_practice = int(points_practice)
        self.points_theory = int(points_theory)
        self.points_labs = int(points_labs)

    def get_grade(self):
        total_points = self.points_practice + self.points_theory + self.points_labs
        if 50 < total_points <= 60:
            return "6"
        elif 60 < total_points <= 70:
            return "7"
        elif 70 < total_points <= 80:
            return "8"
        elif 80 < total_points <= 90:
            return "9"
        elif 90 < total_points <= 100:
            return "10"
        else:
            return "5"

    def get_subject_name(self):
        return self.subject_name


class Student:

    def __init__(self, name, surname, index):
        self.name = name
        self.surname = surname
        self.index = index
        self.subjects = []

    def add_subject(self, subject_add: Subject):
        self.subjects.append(subject_add)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_subjects(self):
        return self.subjects


if __name__ == "__main__":
    students = {}
    input_text = input()
    while input_text != "end":
        words = input_text.split(",")
        subject = Subject(words[3], words[4], words[5], words[6])
        if words[2] in students.keys():
            student = students.get(words[2])
            student.add_subject(subject)
        else:
            student = Student(words[0], words[1], words[2])
            students[words[2]] = student
            student = students.get(words[2])
            student.add_subject(subject)
        input_text = input()

    for student in students:
        print("Student: " + students[student].get_full_name())
        """----Artificial Intelligence: 9"""
        subjects = students[student].get_subjects()
        for subject in subjects:
            print("----" + subject.get_subject_name() + ": " + subject.get_grade())
        print()
