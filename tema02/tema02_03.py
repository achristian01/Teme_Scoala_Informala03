
# Sa se scrie o functie care citeste de la tastatura si returneaza valoarea daca aceasta este un nr intreg,
# altfel returneaza valoarea 0.


def func_input():

    try:
        entered_value = int(input("Type in something, please: "))
        print(entered_value)

    except ValueError:
        print(0)

func_input()

