def calculate_distance(speed, time):
    return speed * time

speed = float(input("Enter speed: "))
time = float(input("Enter time: "))

distance = calculate_distance(speed, time)

print("Distance traveled:", distance)