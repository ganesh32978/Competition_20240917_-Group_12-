#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print(weight)
Under 18.5	Underweight	Minimal
18.5 - 24.9	Normal Weight	Minimal
25 - 29.9	Overweight	Increased
30 - 34.9	Obese	High
35 - 39.9	Severely Obese	Very High
40 and over	Morbidly Obese	Extremely High


# In[1]:


##Make sure to convert the datatypes into integers for weight and height to convert them add int before input function.

name  = str(input("Enter your name: "))
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))
BMI = (weight *703)/(height*height)

print(BMI)


# In[2]:


if BMI>0:
    if BMI<18.5:
        print(name +",You are Underweight")
    elif BMI<=24.5:
        print(name +",You are Normalweight")
    elif BMI<29.9:
        print(name +",You are Overweight and you need to start exercising frequently.")
    elif BMI<34.9:
        print(name +",You are Obese, You need to start exercising immediately")
    elif BMI<39.9:
        print(name +",You are Severely Obese")
    else:
        print("You are extremely obese")
else:
    print("Please, enter a valid input")


# In[ ]:
# Commit by Sai Surya Prakzsh Tamminedi



