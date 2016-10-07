""" Self-Driving Car: Following Distance
    Name: Jozua Kleu
    Date: 05/10/2016
    """


def optimum_distances(front_car, behind_car):

    equal_distance = (front_car + behind_car)/2
    return equal_distance

def weather(current_weather, optimum_distance):

    if current_weather == "clear":
        return optimum_distance
    elif current_weather == "rain" or current_weather == "low visibility":
        optimum_distance =  optimum_distance*2
        return optimum_distance
    else:
        print("Please input a vaild weather condition! (clear, rain or low visibilty)")
        return ("invalid") 

def main():

    front_car = int(input("what is the distance between the car in front and yourself"))
    behind_car = int(input("what is the distance between the car behind and yourself"))
    speed = int(input("what is the current speed in mph"))
    while True:
        optimum_distance = optimum_distances(front_car, behind_car)
        break
    while True:
        current_weather = input("what is the current weather type: either - clear, rain or low visibility").lower()
        final_distance = weather(current_weather, optimum_distance)
        break

    print ("the optimum distance between both cars is", final_distance,"meters away from both")

    #optimum distance fron front car at current speed
        


if __name__ == "__main__":
    main()
