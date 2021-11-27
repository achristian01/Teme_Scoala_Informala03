
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

print("My starting list is: my_list = ", my_list)

working_list = my_list[:]  # a working list to deal with
print("My clone, working list is: ", working_list)

working_list.sort()
print("My sorted list is: sorted working list =", working_list)

working_list.reverse()
print("My list having the elements in reverse order is: reverse working list =", working_list)

working_list.reverse()
print(my_list)

even_slice = working_list[1::2]
print("My even number list is: even working list =", even_slice)

odd_slice = working_list[0::2]
print("My odd number list is: odd working list =", odd_slice)

multi3_list = working_list[2::3]
print("My list containing multiples of 3 is: multi3 working list =", multi3_list)



