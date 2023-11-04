from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)

    class Meta:
        db_table = "Student_Table"
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "Course_Table"
    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)


    class Meta:
        db_table = "Grade_Table"
    def __str__(self):
        return f'{self.student.name} - {self.course.name}: {self.grade}'





