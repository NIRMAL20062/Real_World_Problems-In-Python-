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
import random
dicts={"Pesty":90,"Magii":80,"Smoothy":50}
new_dicts={}
list1=[5,10,15]

for key,value in dicts.items():
    new_price=value-value*(random.choice(list1)/100)
    print(f'New price of {key} is: {new_price}')
    new_dicts[key]=new_price
print(new_dicts)

# Q7. A school election has 4 candidates, and 30 students cast their votes. Write a program to count how many votes each candidate received and display the winner.
import random
list1=['Ram',"Shayam","Mohit","Bardx"]
list2=[]
for candidate in list1:
    x=random.randint(1,30)
    list2.append(x)
    print(candidate)
    candidate=x
    print("Got Vote from" ,candidate," Candidates")
print(f'Winner of the Election is {candidate} ,Won By Maximum Vote Of ,{max(list2)}')


#Q8. A library has a collection of 25 books, and each book is either available or checked out. Write a program to count the number of available books and the number of books that are checked out.

dict={"Conch Bearer":'T',"The Alchemist":'F',"Atomic habits":'T'}
count_a=0
count_c=0
for key,value in dict.items():
    if value=="T":
        count_a+=1
    elif value=="F":
        count_c+=1
print(count_a,"Books are Available")
print(count_c,"Books are Checked-Out")


#Q9. A university records the attendance of 100 students for 10 classes. Write a program to calculate the percentage of attendance for each student and display the list of students who attended less than 90% of the classes.

dict={'A':4,"B":6,"C":8,"D":9}
list=[]
for key , value in dict.items():
    percentage=(value/10)*100
    if percentage<90:
        x=f"{key}:Percentage of Attendance is {percentage}%"
        list.append(x)
print(list)



#Q10. A sports coach needs to select 5 players from a pool of 12 for a basketball team. Write a program to calculate the number of different ways the coach can select 5 players.
# Combination npr=n!/((n-r)!*r!)

n=12 #number of players
r= 5 #number of players to be selected
c=n-r
def fact1(x):
    fact=1
    while x>0:
        fact=fact*x
        x=x-1
    return fact
combination=fact1(n)/(fact1(c)*(fact1(r)))
print(combination)


# Q11. A fitness tracker records the number of steps a person takes for 30 days. Write a program to find the average steps per day, and identify the days when the user exceeded 10,000 steps.

dict1={'a':20000,"b":50000,"c":90000,"d":3000}
total=0
list=[]
for key, value in dict1.items():
    total+=value
    avg=total/30
    if value>10000:
        list.append(value)
print(total)
print(avg)
print(list)


# Q12. A fitness app is tracking the steps of users daily. A user logs 3,500 steps on Monday, 6,200 on Tuesday, and 4,800 on Wednesday. On Thursday, they plan to do a workout for 45 minutes instead of walking. The app recommends users take at least 5,000 steps a day on average. Write a program to check if the user has met their step goal by Wednesday.

dict1={'Monday':3500,"Tuesday":6200,"Wednesday":4800}
total=0
for key,value in dict1.items():
    total+=value
    avg=total/len(dict1)
if avg==5000:
    print("User has met their step goal by Wednesday")
else:
    print("User has not-met their step goal by Wednesday")

#Q13. A parking garage charges INR 30 for the first hour and INR 20 for each additional hour. A car entered the garage at 9 AM and left at 2 PM. The car owner also bought a coffee from the café inside the garage for INR 63. Write a program to calculate the total parking fee.

def fee(entry,exit):
    # entry=int(input('Enter the entry time in 24 hour format: '))
    extra_fee=63
    if entry==exit:
        total_fee=0
    elif entry>0 and exit>0:
        total_times_stayed=exit-entry
        if total_times_stayed==1:
            total_fee=30+extra_fee  #30+4*20+63=110+63=173
            return total_fee
        else:
            total_fee=30+(total_times_stayed-1)*20+extra_fee
            return total_fee

print(fee(9,14))

# Q14. A household is monitoring its water usage. The total water consumption for the month is 25,000 liters. The water company charges INR 50 per 1,000 liters. The family uses 5,000 liters for gardening. Write a program to calculate the total water bill for the household, excluding gardening usage.


def water_bill(total_water, gardening_usage):
    bill_for_month=(((total_water)-(gardening_usage))/1000)*50
    return bill_for_month
print(water_bill(25000,5000))


# Q15. Given a dictionary with student names and a list of booleans representing their attendance over 5 days, return a dictionary with student names and their attendance percentage.


""" """ attendance = {
    "Alice": [True, False, True, True, False],
    "Bob": [True, True, False, True, True],
    "Charlie": [False, True, True, False, True],
    "David": [True, True, True, True, True],
    "Eve": [False, False, True, False, True]
}
def attendence_percentage():
    attend_dict = {}
    for key,value in attendance.items():
        for booleans in value:
            if booleans==True:
                attend_dict[key]=((value.count(True))/len(value))*100
            else:
                attend_dict[key]=((value.count(False))/len(value))*100
    return attend_dict
print(attendence_percentage())

# Q16. Given a username string, return True if the username is valid (must be between 6 and 12 characters and contain only alphanumeric characters).

def username():
    str="Nirmal2608"
    import re
    x = re.match('^[a-zA-Z0-9]{6,12}', str)
    # return x
    if x:
        print('True')
    else:
        print('False')
# print(username())
(username())


# Q17. Given the current room conditions, find out if the air conditioner should be turned on.

# Used AI for Help


def should_turn_on_ac(current_temperature, current_humidity, desired_temperature=24):
    # Check if the current temperature exceeds the desired temperature
    if current_temperature > desired_temperature:
        return True
    # Check if the humidity is above a comfortable level (e.g., 60%)
    elif current_humidity > 60:
        return True
    else:
        return False

# Example usage
current_temp = 28  # Current temperature in °C
current_humidity = 65  # Current humidity in %

if should_turn_on_ac(current_temp, current_humidity):
    print("The air conditioner should be turned on.")
else:
    print("The air conditioner can remain off.")


















