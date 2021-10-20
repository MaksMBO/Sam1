class GROUP:

    def __init__(self, *students):
        self.students = students

    def get_students_grades(self):
        """"Returning a list of all students with their GPA"""
        return self.students

    def sorting(self):
        """"Selects the top five, according to the average score, students"""
        return sorted(self.students, key=lambda stud: stud.average_score())[-1:-6:-1]


class STUDENT:
    student_number = 0

    def __init__(self, name, surname, **grades):
        STUDENT.student_number += 1
        if STUDENT.student_number <= 20:
            self.name = name
            self.surname = surname
            self.student_number = STUDENT.student_number
            self.grade = grades
        else:
            raise ValueError("The number of students cannot exceed 20")

    def average_score(self):
        """"Calculates the average score of all students in the group"""
        return sum(self.grade.values()) / len(self.grade)


Maksim = STUDENT('Maksim', 'Brediuk', maths=84, basics_of_programming=85, discrete_math=98)
Vlad = STUDENT('Vlad', 'Melnick', maths=88, basics_of_programming=78, discrete_math=89)
David = STUDENT('David', 'Bondar', maths=77, basics_of_programming=65, discrete_math=79)
Misha = STUDENT('Misha', 'Golub', maths=73, basics_of_programming=89, discrete_math=90)
Andrey = STUDENT('Andrey', 'Leshitsky', maths=89, basics_of_programming=94, discrete_math=86)
Nikolay = STUDENT('Nikolay', 'Voitenko', maths=67, basics_of_programming=75, discrete_math=69)
Alexander = STUDENT('Alexander', 'Pitishin', maths=86, basics_of_programming=84, discrete_math=87)
Valentine = STUDENT('Valentine', 'Bondarchuk', maths=77, basics_of_programming=88, discrete_math=91)
Evgeniy = STUDENT('Evgeniy', 'Stepura', maths=80, basics_of_programming=80, discrete_math=99)
Evgen = STUDENT('Evgeniy', 'Stepura', maths=80, basics_of_programming=80, discrete_math=99)
Evgeni = STUDENT('Evgeni', 'Stepura', maths=87, basics_of_programming=78, discrete_math=96)
Evge = STUDENT('Evge', 'Stepura', maths=96, basics_of_programming=79, discrete_math=95)
Evg = STUDENT('Evg', 'Stepura', maths=66, basics_of_programming=74, discrete_math=87)
Ev = STUDENT('Ev', 'Stepura', maths=79, basics_of_programming=57, discrete_math=89)
E = STUDENT('E', 'Stepura', maths=86, basics_of_programming=86, discrete_math=96)
Alexande = STUDENT('E', 'Stepura', maths=84, basics_of_programming=82, discrete_math=89)
Alexand = STUDENT('Ev', 'Stepura', maths=77, basics_of_programming=76, discrete_math=79)
Alexan = STUDENT('Evg', 'Stepura', maths=69, basics_of_programming=68, discrete_math=67)
Alexa = STUDENT('Evge', 'Stepura', maths=96, basics_of_programming=79, discrete_math=76)
Alex = STUDENT('Evgen', 'Stepura', maths=86, basics_of_programming=96, discrete_math=95)
# Ale = STUDENT('Evgeni', 'Stepura', maths=78, basics_of_programming=81, discrete_math=92)


group = GROUP(Maksim, Vlad, David, Misha, Andrey, Nikolay, Alexander, Valentine, Evgeniy, Evgen, Evgeni, Evge, Evg, Ev,
              E, Alexande, Alexand, Alexan, Alexa, Alex)

for student in group.get_students_grades():
    print(f"Name: {student.name}, student number: {student.student_number} ,"
          f" average score:  {round(student.average_score(), 2)}")
print("\n\n")
for student in group.sorting():
    print(f"Name: {student.name}, student number: {student.student_number} ,"
          f" average score:  {round(student.average_score(), 2)}")
