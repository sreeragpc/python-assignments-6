"""Grades are computed using a weighted average. Suppose that the written test counts 70%,  lab exams 20% and assignments 10%.
If Arun has a score of
Written test = 81
Lab exams = 68
Assignments = 92
Arun’s overall grade = (81x70)/100 + (68x20)/100 + (92x10)/100 = 79.5
 Write a program to find the grade of a student during his academic year.
Program should accept the scores for written test, lab exams and assignments
Output the grade of a student (using weighted average)
"""
wt=int(input("enter the mark got in written test :"))
le=int(input("enter the mark got in lab exams :"))
ag=int(input("enter the mark got in assignments :"))
og=wt*70/100 + le*20/100 + ag*10/100
print("overall grade ="+str(og))