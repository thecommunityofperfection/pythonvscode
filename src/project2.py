from sys import exit

SPEEDS = [
    (30, "Warning", "That is too fast!"),
    (20, "Caution", "Drive carefully!"),
    (0, "Safe", "You are driving safely.")
]

message: str = "{}, {}! Your speed is {:.2f} m/s. {}"

def assess_speed(speed: float, car_name: str) -> None:
    for threshold, status, critique in SPEEDS:
        if speed > threshold:
            print(message.format(status, car_name, speed, critique))
            break

def main() -> None:
    car_name: str = input("What is the car's name?\n")

    try:
        distance: float = float(
            input("How far did the car travel? (meters)\n")
        )
        time: float = float(
            input("How long did it take to travel that distance? (seconds)")
        )
    except ValueError:
        print("Error: Please enter a valid number.")
        exit(1)

    if time <= 0:
        print("Error: Time must be greater zero.")
        exit(1)
    
    speed: float = distance / time

    assess_speed(speed, car_name)

if __name__ == "__main__":
    main()