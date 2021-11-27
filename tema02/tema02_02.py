# Calculati sumele de la 0 la n, respectiv ale numerelor pare si impare

my_number = int(input("Enter here your number, please: "))

def my_summ(my_number):
    # First, calculate the sum of numbers from zero to mine:

    summ = 0
    for i in range(my_number+1):
        summ += i
    print("The sum of the numbers from zero to mine is: ", summ)


    # Second, calculate the sum of even numbers in our series from zero to my_number:

    def even_sum(my_number):
        even_sum = 0
        for i in range(my_number+1):
            if i % 2 == 0:
                even_sum += i
        print("The sum of even numbers from zero to my_number is: ", even_sum)

    even_sum(my_number)

    # Third, calculate the sum of odd numbers in our series from zero to my_number:

    def odd_sum(my_number):
        odd_sum = 0
        for i in range(my_number + 1):
            if i % 2 != 0:
                odd_sum += i

        print("The sum of odd numbers from zero to my_number is: ", odd_sum)

    odd_sum(my_number)


my_summ(my_number)

