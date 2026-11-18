# Digital Twin - Pre-Manufacture Vehicle Testing
# Mohamed Gomaa - Simple Simulation

class DigitalTwinCar:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.temperature = 25
        self.brake_health = 100

    def test_acceleration(self):
        print(f"Testing {self.name} - Acceleration Test...")
        for i in range(0, 101, 20):
            self.speed = i
            print(f"Speed: {self.speed} km/h - OK")
        print("Acceleration Test Passed ✅")

    def test_braking(self):
        print(f"\nTesting {self.name} - Braking Test...")
        while self.speed > 0:
            self.speed -= 20
            if self.speed < 0:
                self.speed = 0
            self.brake_health -= 2
            print(f"Speed: {self.speed} km/h - Brake Health: {self.brake_health}%")
        print("Braking Test Passed ✅")

    def test_temperature(self):
        print(f"\nTesting {self.name} - Engine Temperature Test...")
        for temp in [25, 60, 85, 95]:
            self.temperature = temp
            status = "Normal" if temp < 90 else "Warning - High Temp!"
            print(f"Engine Temp: {temp}°C - {status}")
        print("Temperature Test Finished ✅")

# Run the simulation
if __name__ == "__main__":
    my_car = DigitalTwinCar("Test Vehicle V1")
    print("=== Starting Digital Twin Simulation ===")
    my_car.test_acceleration()
    my_car.test_braking()
    my_car.test_temperature()
    print("\n=== Simulation Finished - Car is ready for manufacturing ===")