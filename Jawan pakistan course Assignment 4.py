#!/usr/bin/env python
# coding: utf-8

# In[1]:


#write a python code in the follwing string in a specific format.
print('Twinkle,twinkle,little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle,twinkle,little star,\n\tHow I wonder what you are')


# In[2]:


#write a python code to find the version of python.
import sys
print ('Python version is:')
print(sys.version)
print('\nthe version is')
print(sys.version_info)


# In[6]:


#write a python code to display current Date and Time.
from datetime import datetime
now = datetime.now()
print('date and time : ',now)


# In[21]:


# Write a python code to find the area of a circle.
r=int(input("Enter a radius:"))
p=3.142
a=p*r**2
print("The area of a circle is",a)


# In[12]:


#write a python code to revese your first and last name.
a =str(input('Enter first name :'))
b = str(input('Enter second name:'))
c = a[-1::-1]
d = b[-1::-1]
print (c,d)


# In[13]:


#write a python code to add two inputs.
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c = a+b
print(c)


# In[14]:


#write a python code to find your grade.
subject1 = int(input('Enter First Subject Mark :'))
subject2 = int(input('Enter Second Subject Mark :'))
subject3 = int(input('Enter Third Subject Mark :'))
subject4 = int(input('Enter Fourth Subject Mark :'))
subject5 = int(input('Enter Fifth Subject Mark :'))
TotalMarksofSubjects = subject1+subject2+subject3+subject4+subject5
TotalMarks = 500
percentage = (TotalMarksofSubjects/TotalMarks)*100
if percentage > 80 and percentage <= 100 :
    print("Congragulations Your Grade is A+")
elif percentage > 70 and percentage <= 80:
    print("Your Grade is A")
elif percentage > 60 and percentage <= 70:
    print("Your Grade is B")
elif percentage > 50 and percentage <= 60:  
    print("Your Grade is C")
elif percentage > 40 and percentage <= 50:
    print("Your Grade is D")
elif percentage > 33 and percentage <= 40:
    print("Your Grade is E")
elif percentage < 33:
    print("You Are Fail")
elif percentage > 100 or t <= 0:
    print("Invalid result")


# In[15]:


#write a python code to check a number is Even or Odd.
Number = int(input('Enter no :'))
Reminder = Number%2
if (Reminder == 0):
    print (Number,"is Even number")
else:
    print(Number,'is Odd number')


# In[16]:


#write a python code to search lenght of user list.
list = ['1','2','3','4','5','6','7','8']
a = len(list)
print(a)


# In[18]:


#write a python code to find sum of all elements in user list.
list = [ 1,1,1,1,1,1]
Sum = 0
for i in range(len(list)) :
    Sum = Sum + list[i]  
print('Sum of list is :',Sum)


# In[19]:


#write a python code to find max number of element in user list.
list = [ 1, 2,4 ,5, 6 ,7]
print(max(list))


# In[20]:


#write a python code to find all less than 5 numbers of elements in list.
mylist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in mylist:
    if i < 5:
        print(i)


# In[ ]:




