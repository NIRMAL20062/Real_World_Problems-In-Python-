#Q1. A teacher has 30 students in a class. Each student has a list of 5 exam scores. Write a program to calculate and display the average score of each student.

""" students_scores = [
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
            
print(lists) """


""" x=[85, 90, 78, 92, 88]
print(sum(x)) """



# Q2 . A store has 10 different items. The store manager wants to apply a 10% discount on every item that costs more than INR 50. Write a program to display the updated prices for each item.

""" dicts={'Notebook':60,"Iphone":100,"Mobile":30}
dict1={}
for i in dicts:
    x=(dicts[i])
    if x>50: 
        discounted_price=((dicts[i] )-(((dicts[i])*(10/100))))
        dict1[i]=discounted_price
print(dict1) """


# Q3. There is a running competition with 20 participants. You need to find the top 3 participants who ran the fastest.

dict1={'Alice': 16, 'Bob': 19, 'Charlie': 2, 'David': 1, 'Eve': 28, 'Frank': 26, 'Grace': 13, 'Hannah': 23, 'Isaac': 21, 'Jack': 13, 'Kara': 17, 'Liam': 28, 'Mia': 12, 'Noah': 23, 'Olivia': 4, 'Paul': 14, 'Quinn': 30, 'Ruby': 32, 'Sam': 14, 'Tina': 7}
list1=[]
for key,value in dict1.items():
    #  print(key,end=' ')
    #  print(value,end=',')
        maxo1=max(dict1.values())
print(key,maxo1)
      


#Q4. A movie website has ratings from 5 users for 3 different movies. Each user gives a rating between 1 to 5. Write a program to find the highest-rated movie.

dict1={"A":[1,2,3],"B":[4,5,6],"C":[2,4,1],"D":[1,2,1],"E":[1,1,1]}
list=[]
for value in dict1.values(): #iterating over values
        sum=0
        for ele in value:    #iterating over ele in values
                sum=sum+ele
        list.append(sum)     #apending in the list
print(max(list))





