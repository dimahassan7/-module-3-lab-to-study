class Vehicle:
    """
    A super class for vehicles, containing a generic vehicle type.
    """
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    """
    A class representing an automobile, inheriting from Vehicle and
    containing specific attributes for cars.
    """
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")  # Automatically sets vehicle_type to "car"
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def run_car_app():
    """
    Runs the car information application, collecting user input
    and displaying the automobile's details.
    """
    print("Welcome to the Automobile Information App!")
    print("Please provide the following details for your car:")

    while True:
        try:
            year = int(input("Enter the year (e.g., 2022): "))
            if year <= 1900 or year > 2025: # Basic validation
                raise ValueError
            break
        except ValueError:
            print("Invalid year. Please enter a valid four-digit year.")

    make = input("Enter the make (e.g., Toyota): ")
    model = input("Enter the model (e.g., Corolla): ")

    while True:
        try:
            doors = int(input("Enter the number of doors (2 or 4): "))
            if doors not in [2, 4]:
                raise ValueError
            break
        except ValueError:
            print("Invalid number of doors. Please enter 2 or 4.")

    while True:
        roof = input("Enter the type of roof (solid or sun roof): ").lower()
        if roof not in ["solid", "sun roof"]:
            print("Invalid roof type. Please enter 'solid' or 'sun roof'.")
        else:
            break

    # Create an Automobile object with the collected data
    my_car = Automobile(year, make, model, doors, roof)

    print("\n--- Your Car Details ---")
    print(f"Vehicle type: {my_car.vehicle_type.capitalize()}")
    print(f"Year: {my_car.year}")
    print(f"Make: {my_car.make.capitalize()}")
    print(f"Model: {my_car.model.capitalize()}")
    print(f"Number of doors: {my_car.doors}")
    print(f"Type of roof: {my_car.roof.capitalize()}")
    print("------------------------")

if __name__ == "__main__":
    run_car_app()