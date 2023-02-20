"""
Write a Python program that outputs all prime numbers < 100. (2 Points)

A number is called a prime number if it is greater than 1 and has exactly
two divisors, 1 and the number itself.

For instance, the first ten prine numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.


"""

for current_number in range(2,100):
    division_counter = 0
    for i in range(1,current_number):
        if current_number % i == 0:
            division_counter+=1
            if division_counter>1:
                break
    if division_counter<=1:
        print(current_number,end=" , ")