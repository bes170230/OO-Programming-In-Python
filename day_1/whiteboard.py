#Fizz Buzz #2
#Write a function to print all numbers 1 to n, but there are some constraints
#If the number is divisible by 3, print 'Fizz' instead of the number
#If the number is divisible 5, print 'Buzz' instead of the number
#If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
#Otherwise, simply print the number

def fizzbuzz(number):
    for x in range(1, number):
        if x % 3 == 0 and x % 5 != 0:
            print("Fizz")
        elif x % 5 == 0 and x % 3 != 0:
            print("Buzz")
        elif x % 3 == 0 and x % 5 == 0:
            print("Fizzbuzz")
        else:
            print(x)


fizzbuzz(16)
