# #List
# a_string = "like this"
# a_number = 3
# a_float = 3.12
# a_boolean = False
# a_none = None
# print(type(a_boolean))

# #Tuple
# days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
# days.append("Added Content")
# print(days)

# #Dictionary
# jiwon = {
#   "name": "Jiwon",
#   "age": "27",
#   "korean": True,
#   "fav_food": ["Ramen","Samgyupsal"]
# }
# print(jiwon)

# #Built in Functions
# age = "18"
# print(age)
# print(type(age))
# n_age = int(age)
# print(n_age)
# print(type(n_age))

# #Function
# def say_hello():
#   print("Hello")
#   print("Bye")
# say_hello()

# #Function Arguments
# person = ["Jiwon", "Nico", "Raha"]
# def say_hello(person):
#   print("hello" + person)
# say_hello(person[2])

# #Return
# def p_plus(a, b):
#   print(a + b)
# def r_plus(a, b):
#   return a + b
# p_result = p_plus(2, 3)
# r_result = r_plus(2, 3)
# print(p_result,r_result)
# def exam(a, b):
#   return a+b
#   print("This is never gonna be printed")
# print(exam(3,4))

# # Keworded Arguments
# def plus(a, b):
#   return a - b

# result = plus(b=30, a=1)
# print(result)

# def say_hello(name, age):
#   return f"Hello {name} you are {age} years old"

# hello = say_hello(age=27, name="Jiwon")

# print(hello)

# # Simple Calculator

# def plus(a,b):
#   return int(a)+int(b)

# def minus(a,b):
#   return int(a)-int(b)

# def multiply(a,b):
#   return int(a)*int(b)

# def division(a,b):
#   return int(a)/int(b)

# def negation(number):
#   return -int(number)

# def remainder(a,b):
#   return int(a) % int(b)

# def power(a,b):
#   return int(a) ** int(b)

# print(plus(2,3))

# print(minus(2,3))

# print(multiply(2,3))

# print(division(2,3))

# print(negation(2))

# print(power(2,3))

# print(remainder(2,3))

# # Condition 1
# def plus(a,b):
#   if type(a) is int or type(b) is float:
#     return a + b
#   else:
#     return None

# print(plus(12,1.2))

# # if else and or
# def age_check(age):
#   print(f"you are {age}")
#   if age < 18:
#     print("you cant drink")
#   elif age == 18:
#     print("you are new to this! be carful especially!")
#   else:
#     print("You hove the right to drink! but be careful")

# age_check(18)

# # For in

# days = ("Mon", "Tue", "Wed", "Thu", "Fri")

# for potato in days:
#   print(potato)

# for day in days:
#   if day == "Wed":
#     break
#   else:
#     print(day)

# for letter in "Jiwon":
#   print(letter)

# # Modules
# from math import ceil, fabs
# from math import fsum as sexy_sum

# print(ceil(1.2))
# print(fabs(-1.2))
# print(sexy_sum([1,2,3,4,5]))

# from calculator import plus, minus

# print(plus(1,2))
# print(minus(1,2))
