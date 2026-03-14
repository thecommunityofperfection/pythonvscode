car_name = input("What is the car's name?\n")
distance = float(input("How far did the car travel?(meters)\n"))
time = float(input("How long did it take to travel that distance?(seconds)"))
speed = distance/time
if speed > 30:
    print(f"Warning, {car_name}! Your speed is {speed} m/s, which is too fast!")
elif speed <= 30 and speed >= 20:
    print(f"Caution, {car_name}! Your speed is {speed} m/s. Drive carefully!")
elif speed < 20:
    print(f"Safe, {car_name}! Your speed is {speed} m/s. You are driving safely.")
else:
    print(f"Error: Time cannot be zero. Please check the input values for {car_name}.")