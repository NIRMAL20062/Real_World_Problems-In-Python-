#Q1. A teacher has 30 students in a class. Each student has a list of 5 exam scores. Write a program to calculate and display the average score of each student.

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



# Q2 . A store has 10 different items. The store manager wants to apply a 10% discount on every item that costs more than INR 50. Write a program to display the updated prices for each item.

dicts={'Notebook':60,"Iphone":100,"Mobile":30}
dict1={}
for i in dicts:
    x=(dicts[i])
    if x>50: 
        discounted_price=((dicts[i] )-(((dicts[i])*(10/100))))
        dict1[i]=discounted_price
print(dict1)


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




# Q5. A bank records the daily transactions of 20 customers. Some transactions are deposits, and some are withdrawals. Write a program that calculates the total deposit and withdrawal amounts for each customer.


dict1={'Alice': [-1873, -1039, -1106, -317, 1461], 'Bob': [-2153, 648, 1415, -2460, 576], 'Charlie': [80, 550, 1283, -2421, -2119], 'David': [470, 2417, -1108, -1835, -980], 'Eve': [1472, -1897, 202, -1299, -1016], 'Frank': [-2908, 893, -1069, 2058, 2879], 'Grace': [-2980, 1757, 1101, 2828, -2281], 'Hannah': [1813, 932, 1119, 2267, 609], 'Isaac': [-2354, -2618, 175, 111, -195], 'Jack': [-1964, 2700, -658, 386, 1017], 'Kara': [1707, 2126, 2187, 2550, 2571], 'Liam': [656, 617, 1484, 1270, -70], 'Mia': [-732, 377, -1000, 585, 2812], 'Noah': [-1048, 2942, -2242, -394, 581], 'Olivia': [-1180, -2142, -1436, -2188, 2857], 'Paul': [-2561, -1214, 2524, 835, 2532], 'Quinn': [-1195, 1388, -1510, 2044, -2154], 'Ruby': [-2849, 1068, -1864, 2967, -550], 'Sam': [-2422, -607, 1773, 610, -90], 'Tina': [-1070, 2911, -238, 1538, 2513]}

# Method-1
for key,value in dict1.items():
    deposite=0
    withdrawal=0
    for ele in value:
        if ele>0 :
           deposite+=ele
        elif ele<0:
           withdrawal+=ele
    print(f'For costomer {key} deposite is: ',deposite)
    print(f'For costomer {key} withdrawal is:',withdrawal)

# Method-2
for key, value in dict1.items():
        deposit = sum(x for x in value if x > 0)
        withdrawal = sum(x for x in value if x < 0)
        print(f'For customer {key} deposit is: {deposit}')
        print(f'For customer {key} withdrawal is: {withdrawal}')


#Q6. A cafeteria has a menu of 15 items. Every day, the cafeteria gives a random discount of 5%, 10%, or 15% on all items. Write a program to calculate the new prices for each item after the discount is applied.

# Make  dictionaries








