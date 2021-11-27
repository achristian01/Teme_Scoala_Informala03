# This is a sample Python script.
import copy
import csv
import uuid
cars_list = [{"id":uuid.uuid1(), "Brand":"Hyundai", "Model":"Santa_Fe", "hp":189, "price":30000},
             {"id":uuid.uuid1(), "Brand":"Kia", "Model":"Sorento", "hp":140, "price":20000},
             {"id":uuid.uuid1(), "Brand":"BMW", "Model":"X6", "hp":5233, "price":110000},
             {"id":uuid.uuid1(), "Brand":"Mercedes", "Model":"'Gelandewagen'", "hp":416, "price":120000},
             {"id":uuid.uuid1(), "Brand":"Dacia", "Model":"Logan", "hp":87, "price":10000},
             {"id":uuid.uuid1(), "Brand":"VW", "Model":"Golf-1", "hp":75, "price":800},
             {"id":uuid.uuid1(), "Brand":"Opel", "Model":"Vectra", "hp":130, "price":4800}]

#

with open('car_file01.csv','w') as file:
    fieldnames = ["id", "Brand", "Model", "hp", "price"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for i in cars_list:
        writer.writerow(i)



def check_speed(car):
    global checked_car
    checked_car = copy.deepcopy(car)
    checked_car["slow car"] = True if checked_car["hp"] < 120 else False
    checked_car["fast car"] = True if checked_car["hp"] >= 120 and  checked_car["hp"] < 180 else False
    checked_car["sport car"] = True if checked_car["hp"] >= 180 else False
    return checked_car


cars_based_on_performance = map(check_speed, cars_list)
print("Cars based on performance are:\n", list(cars_based_on_performance))
print()

def check_price(car):
    checked_car = copy.deepcopy(car)
    checked_car["cheap"] = True if checked_car["price"] < 1000 else False
    checked_car["medium"] = True if checked_car["price"] >= 1000 and  checked_car["price"] < 5000 else False
    checked_car["sport"] = True if checked_car["price"] >= 5000 else False
    return checked_car

cars_based_on_price= map(check_price, cars_list)
print("Cars based on price are:\n", list(cars_based_on_price))
print("check")
print("check")
print(cars_based_on_price)
print("Cars based on price are:\n", list(cars_based_on_price))
print("check")

# with open('car_performance.csv','w') as file:
#
#     fieldnames = ["id", "Brand", "Model", "hp", "price", "slow car", "fast car", "sport car", "cheap", "medium", "expensive"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for i in cars_based_on_performance:
#         writer.writerow(i)
#
# performance = list(cars_based_on_performance)
# price = list(cars_based_on_price)

new_car_list = list(cars_based_on_performance) + list(cars_based_on_price)  ### Not working?


print(new_car_list)


