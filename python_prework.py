# QUESTION 1

# Write a function to print "hello_USERNAME!" USERNAME 
# is the input of the function. The first line of the code
# has been defined as below.

def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name("USERNAME")

# QUESTION 2

# Write a python function, first_odds that prints the odd numbers
# from 1-100 and returns nothing

def first_odds():
    for i in range(1,100):
        if i % 2 == 1:
            print(i)

first_odds()


# QUESTION 3

# Please write a Python function, max_num_in_list to return
# the max number of a given list. The first line of the code
# has been defined as below.

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

nums = [1, 3, 5, 7, 9]
print(max_num_in_list(nums))


# QUESTION 4

# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100,
# unless it is also divisible by 400. The return should be
# boolean Type (true/false).

def is_leap_year(a_year):
    leap = False
    if a_year % 400 == 0:
        leap = True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        leap = True
    return leap

print(is_leap_year(2020))
print(is_leap_year(2022))


# QUESTION 5

# Write a function to check to see if all numbers in list are
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive
# numbers, but [1,2,4,5] are not consecutive numbers. The return
# should be boolean Type.

def is_consecutive(a_list):
    maximum = max(a_list)
    if sum(a_list) == maximum * (maximum + 1) / 2:
        return True
    return False

list_a = [1,2,3,4,5]
list_b = [1,3,5,7,9]
print(is_consecutive(list_a))
print(is_consecutive(list_b))