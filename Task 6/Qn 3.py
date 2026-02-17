#   Problem:- 3 Vehicle Rental


class Vehicle:

    #   Base class for all vehicles

    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):

        #   Calculate rental cost

        return self.rental_rate * days


class Car(Vehicle):

    #   Car class

    def __init__(self, model, rental_rate, seats):
        super().__init__(model, rental_rate)
        self.seats = seats

    def calculate_rental(self, days):

        #   Car rental with small insurance fee

        insurance_fee = 100
        return (self.rental_rate * days) + insurance_fee


class Bike(Vehicle):

    #   Bike class

    def __init__(self, model, rental_rate, engine_cc):
        super().__init__(model, rental_rate)
        self.engine_cc = engine_cc

    def calculate_rental(self, days):

        #   Bike rental with discount for longer usage

        total = self.rental_rate * days
        if days > 2:
            total *= 0.9
        return total


class Truck(Vehicle):

    #   Truck class

    def __init__(self, model, rental_rate, load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity  # In tons

    def calculate_rental(self, days):

        #   Truck rental with extra load charge

        extra_charge = self.load_capacity * 100
        return (self.rental_rate * days) + extra_charge


def main():

    #   Main function to test rentals

    vehicles = [
        Car("Innova Hycross", 5000, 7),
        Bike("NS 160", 1000, 200),
        Truck("Tata Lorry", 10000, 5)
    ]

    days = 10

    for vehicle in vehicles:
        cost = vehicle.calculate_rental(days)
        print(f"{vehicle.model} rental cost for {days} days: ₹{cost}")


if __name__ == "__main__":
    main()
