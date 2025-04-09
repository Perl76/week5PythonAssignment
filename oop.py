# Base class for a general Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
        self.power_on = False

    def power_on_phone(self):
        """Turns on the phone."""
        self.power_on = True
        print(f"{self.brand} {self.model} is now powered on.")

    def charge_phone(self, charge_amount):
        """Charges the phone by the specified amount."""
        self.battery_life = min(100, self.battery_life + charge_amount)
        print(f"{self.brand} {self.model} is now at {self.battery_life}% battery.")

    def check_battery(self):
        """Checks the battery level."""
        print(f"{self.brand} {self.model} has {self.battery_life}% battery remaining.")

    def use_phone(self, battery_consumed):
        """Simulate using the phone and draining the battery."""
        if self.battery_life >= battery_consumed:
            self.battery_life -= battery_consumed
            print(f"Using {self.brand} {self.model}... {self.battery_life}% battery remaining.")
        else:
            print(f"Not enough battery to use the {self.brand} {self.model}.")

# Derived class for a Smartphone with a Camera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_resolution):
        # Initialize base class attributes
        super().__init__(brand, model, battery_life)
        self.camera_resolution = camera_resolution

    def take_photo(self):
        """Take a photo with the camera."""
        if self.power_on:
            print(f"Taking a {self.camera_resolution} MP photo with {self.brand} {self.model}.")
        else:
            print("Power on the phone first to take a photo.")

# Example usage
smartphone1 = Smartphone("Apple", "iPhone 13", 85)
smartphone1.power_on_phone()
smartphone1.check_battery()
smartphone1.use_phone(10)
smartphone1.charge_phone(15)

# Inherited Smartphone with Camera
smartphone2 = SmartphoneWithCamera("Samsung", "Galaxy S21", 90, 108)
smartphone2.power_on_phone()
smartphone2.check_battery()
smartphone2.take_photo()  # Showcasing camera functionality
