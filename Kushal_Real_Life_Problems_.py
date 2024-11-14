# A teacher has 30 students in a class. Each student has a list of 5 exam scores. Write a program to calculate and display the average score of each student.

students_scores = [
    [85, 90, 78, 92, 88],  # Scores for student 1
    [75, 80, 72, 85, 90],  # Scores for student 2
    [88, 94, 90, 86, 85],  # Scores for student 3
    # Add more lists for each of the 30 students
    # ...
]
lists=[]
for i in range(len(students_scores)):
            for j in range(len(students_scores[i])): 
                total=sum(students_scores[i])   
                avg=total/len(students_scores[i])
            lists.append(avg)
            
print(lists)


""" x=[85, 90, 78, 92, 88]
print(sum(x)) """