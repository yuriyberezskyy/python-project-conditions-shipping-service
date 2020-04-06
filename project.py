premium_ground_shipping = 125.00


def ground_shipping(weight):
    if(weight <= 2):
        return 1.50 * weight + 20
    elif(weight <= 6):
        return 3.00 * weight + 20
    elif(weight <= 10):
        return 4.00 * weight + 20
    elif(weight > 10):
        return 4.75 * weight + 20
    else:
        return premium_ground_shipping


def drone_shipping(weight):
    if(weight <= 2):
        return 4.50 * weight + 0
    elif(weight <= 6):
        return 9.00 * weight + 0
    elif(weight <= 10):
        return 12.00 * weight + 0
    elif(weight > 10):
        return 14.25 * weight + 0


def calculator(weight):
    if(ground_shipping(weight) < drone_shipping(weight)):
        return "The cheapest way to ship " + str(weight) + \
            " pound package is using ground shipping and it will cost $" + \
            str(ground_shipping(weight))
    else:
        return "The cheapest way to ship " + str(weight) + \
            " pound package is using ground shipping and it will cost $" + \
            str(drone_shipping(weight))


print(calculator(3.5))
