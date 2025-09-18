def speedometer(pos1, pos2, time):
    speed = (pos2 - pos1)/time
    return speed

def animal_average_speed(animal_type):
    if animal_type == 0:
        return 68
    elif animal_type == 1:
        return 88
    elif animal_type == 2:
        return 50
  

def animal_speed_compare(animal1_pos1, animal1_pos2, animal1_time, animal2_type):
    animal_speed_one = (animal1_pos2 - animal1_pos1)/animal1_time
    if animal2_type == 0:
        animal_speed_two = 68
    elif animal2_type == 1:
        animal_speed_two = 88
    elif animal2_type == 2:
        animal_speed_two = 88
    if animal_speed_two > animal_speed_one:
        return "The animal is slower"
    else:
        return "The animal is faster"

def myTestString(func, params):
    """
    Do not modify
    """
    return func.__name__ + "" + str(params) + " produces " + str(func(*params))


#Examples to see the difference between "print" and "return"
def function_that_prints():
    print("I printed")


def function_that_returns():
    return "I returned"


# For more information about the line below, refer to the link: https://docs.python.org/3/library/__main__.html
#   You can read more about it but it is to help when handling multiple files
#   Will be dicussed at a later point
if __name__ == "__main__":
    print("Final Test Code\n")
    print("Testing speedometer()")
    for x in [(0.0,400,5.0), (-1,5,0.5), (0,0,1.0), (6,-100,3)]:
        print(myTestString(speedometer, x))
    print("Testing animal_average_speed()")
    for x in [(0,), (1,),(2,), (3,)]:
        print(myTestString(animal_average_speed, x))
    print("Testing animal_speed_compare()")
    for x in [(0.0,400,5.0,1), (0.0,400,5.0,0), (25,150,1.0,2)]:
        print(myTestString(animal_speed_compare, x))
