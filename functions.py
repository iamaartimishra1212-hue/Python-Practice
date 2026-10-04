# def greeting_someone(name):  # name is parameter
#     print( f"Hello {name} , goodmorning !")
#     print("Its a beautyful day.. ! ")

# # calling function 
# greeting_someone("bittu")  #bittu is argument 
# greeting_someone("ankur")
# greeting_someone("tanya")
# # greeting_someone()
# greeting_someone()
    

# def even_odd(number):
#     if number % 2 ==0 :
#         print("even")

#     else : 
#       print("odd") 

# even_odd(2)   # positional argument 
# even_odd(9)
# even_odd(8)
# even_odd(15)

# Create a function to print your name.

# def user(name):
#     print( f" hello {name },  ")

# user("Aarti, Mishra ") 


# def arithmetic(num1 , num2):
#     add = num1 + num2
#     sub = num1 - num2
#     mul = num1 * num2
#     return add , sub, mul

# val_1 = int(input("Enter a Number :"))
# val_2 = int(input("Enter a Number :"))

# res1, res2, res3 = arithmetic(val_1, val_2)
# print(f"Addition of {val_1} and {val_2} is {res1}")
# print(f"Difference between {val_1} and {val_2} is {res2}")
# print(f"product of  {val_1} and {val_2} is {res3}")




# a=int("20", 4)
# print(a)



# Create a function to print numbers from 1 to 10.

# def add(num1 , num2):
#     result = num1 + num2
#     print(f"Result : {result}")

# add(10 ,3) 
# add(9, -4)


# return value function 

# def even_odd(num):
#     if num % 2==0 :
#         return "Even"

#     else:
#         return "Odd"

# result = even_odd(8)
# result = even_odd(5)
# result = even_odd(4)
# result = even_odd(1)

# print(result)
# print(result)
# print(result)

#   RETURNING VALUES FROM THE FUNCTION 
# def add(num1 , num2) :
#     result = num1 + num2
#     return result

# val =add(5, 10)
# print(val)








# Create a function that prints "Hello Python".

# def hello():
#     print("Hello Python")

# hello()

# Create a function that prints your name.

# def name():
#     print("Hello , Aarti"  )

# name()


# Create a function that prints numbers from 1 to 10.
# def number():
#     for i in range(1,11):
#         print(i)

# number()

# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)

# print_numbers(15)


# Create a function that prints the multiplication table of 5.
# def print_number(n):
#     for i in range(5, n +5):
#         print(i)

# print_number(50)

# def table():
#     for i in range(5, 55,5):
#         print(i)

# table()

# def table():
#     for i in range(1, 11):
#         print(f"5 x {i} = {5 * i}")

# table()


# Create a function that prints all even numbers from 1 to 20.
# def even():
#     for i in range(1,21):
#         if i % 2==0:
#             print(i)

# even() 


#  Create a function that prints numbers from 1 to 20

# def numbers():
#     for i in range(1, 21):
#         print(i)

# numbers() 


# Create a function that prints all odd numbers from 1 to 25.
# def odd():
#     for i in range(1,26):
#         if  i % 2 !=0:
#             print(i)

# odd()

# Create a function that prints the multiplication table of 8.
# def table(num):   # second method
#     for i in range(1, 11):
#        print(f"{num} x {i} = {num * i} ") 
 

# table(8)
# table(12)
# table(16) 

# Write a function that prints the squares of numbers from 1 to 10.

# def square():
#     for num in range(1,11):
#         print(f" {num * num}")

# square()



# Write a function that prints cubes of numbers from 1 to 10.
# def cubes():
#     for i in range(1,11):
#         print( i * i * i )

# cubes()

# Write a function that prints numbers from 20 to 1.
# def reverse():
#     for i in range(20 ,0, -1):
#         print(i)

# reverse()

# Create a function that prints all numbers divisible by 3 from 1 to 50.

# def division():
#     for i in range(1,51):
#         if i % 3 ==0:
#             print(i)

# division()

# Write a function that prints the sum of numbers from 1 to 100. 


# Create a function that prints the sum of numbers from 1 to 100. 

# def sum_of_numbers():
#     total =0
#     for i in range(1,101):
#        total +=i
#     print(total)

# sum_of_numbers()
        
# Create a function that calculates the sum of all even numbers from 1 to 100. 

# def even_sum():
#     total =0
#     for i in range(1,101):
#       if i %2 ==0:
#         total +=i

#     print(total)
# even_sum()


# Return Value Function  Exercise
# Create a function that takes a number and returns its square.

# def add(num1 , num2) :
#     result = num1 + num2
#     return result

# val =add(5, 10)
# print(val)

# def square(num):
#     result =result = square(5)
#     return  result

# square(5)

# def square(num):
#     result = num * num
#     return result

# result = square(6)
# print(result)

# Create a function that takes two numbers and returns their sum.

# def add(num1 , num2):
#     result = num1 + num2 
#     return result

# result = add(10,20)
# print(result)


# Create a function that takes two numbers and returns their multiplication.
# def mul(num1 , num2):
#     result = num1 *num2
#     return result

# result = mul(5,10)
# print(result)

# Create a function that takes a number and returns whether it is even or odd.

# def check_even(num) :
#     if num % 2==0:
#         return "Even"

#     else :
#         return "Odd"

# result = check_even(7)
# print(result)

    
# 1. Create a function that takes a number and returns its cube
# def check(num):
#     result = num * num  * num
#     return result

# result = check(4)
# print(result)

#2. Create a function that takes two numbers and returns their subtraction.
# def sub(num1 , num2):
#     result = num1 - num2
#     return result
# result = sub(20 ,8)

# print(result)

# 3. Create a function that takes two numbers and returns their division.
# def divide(num1 , num2):
#     result = num1 / num2
#     return result

# result = divide(20,5)
# print(result)

# 4. Create a function that takes a number and returns "Positive", "Negative", or "Zero".
# def check_number(num):
#     if num >0:
#         return("positive")

#     elif num <0:
#         return ("Negative")

#     else :
#         return ("zero")

# result = check_number(-5)
# print(result)

# 5. Create a function that takes a person's age and returns:  "Eligible" or Not
# def age(Age):
#     if Age >=18:
#         return("Eligible")

#     else :
#         return("Not Eligible")

# result = age(18)
# print(result)

# 6. Create a function that takes two numbers and returns the larger number.
# def largest_number(num1 , num2):
#     if num1 >  num2 :
#         return ( num1)

#     else : 
#         return (num2)


# result = largest_number(25, 15)
# print(result)

# 7. Create a function that takes n and returns the sum from 1 to n.
# def sum_number(n):
#     total = 0
#     for i in range(1, n+1):
#      total +=i


#     return   total
       
# result = sum_number(10)
# print(result)   

# 8. Create a function that takes n and returns the sum of even numbers from 1 to n. 

# def sum_even(n):
#     total =0
    
#     for i in range(1,n+1):
#      if i%2==0:
#         total +=i


#     return total
# result =sum_even(10)   
# print(result)

# factorial(n) that returns the factorial of a number.  

# def factorial(n):
#     total = 1
#     for i in range(1, n + 1 ):
    
#         total *= i

#     return total

# result = factorial(5)
# print(result)


# Create a function that takes a number and returns the number of digits.

# def count_digit(n):
#     count = 0
#     while n >0 :
#         count +=1
#         n = n //10


#     return count
# result = count_digit(12345)
# print(result) 


# 12. Create a function that takes a number and returns "Prime" if it is a prime number, otherwise "Not Prime".

# def check_prime(num):
#     if num < 2:
#         return "Not Prime"

#     for i in range(2, num):
#         if num % i == 0:
#             return "Not Prime"

#     return "Prime"


# result = check_prime(7)
# print(result)

# ----------------------TYPES OF ARGUMENT------------------------------

'''
1.Positional Arguments
2.Default Arguments 
3.Keyword Arguments
4. Variable-Length Positional Arguments (*args)
5. Variable-Length Keyword Arguments (**kwargs)

'''

# Default Arguments 
# def add(a, b =10):
#     print(f"a:{a}, b: {b} ")
#     return a +b

# result = add(10, 5 )
# print(result)

# result1 = add(15)
# print(result1)


# positional argument 
# def add(a, b):
#     return a+b
# result = add (10,5)
# print(result) 

# default argument
# def add(a, b=10):
#     return a +b

# result = add(10, 15) # Default arguments are like if  2 nd parameter dosnt get any value then it will take default value whatever you ve been passed through argument 
# print(result)

# def even_odd(num):
#     if num % 2 ==0  :
#         print("Even")

#     else :
#         print("Odd")

# even_odd(8)
# even_odd(9) 


# default argument 
# def add(a, b=10):
#     return a + b 

# result = add(15)
# print(result) 


#  with 3 variable 

def add (a, b, c=10):
    print(f" a: {a}, b: {b}, c: {c}")
    return a + b+ c

# result = add (30, 20)
# print(result) 

# keyword argument 
# result = add(c=50, b=9, a=5)
# print(result)



# def add(num1):
#     if num1  >=18:
#         print("Adult")

#     else:
#         print("Minor")

# add(19) 


# def check_even(num):
    

# def multiply(num1 , num2):
#     return num1 * num2

# result = multiply(5,4)
# print(result)

def add1(a, b):
    print(a + b)

def add2(a, b):
    return a + b

x = add1(10, 20)
y = add2(10, 20)

print(x)
print(y)