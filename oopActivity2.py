# Base class for Animal
class Animal:
    def move(self):
        """General move method, can be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement abstract method.")

# Dog subclass
class Dog(Animal):
    def move(self):
        """Override move method to define how a dog moves."""
        print("The dog is running on the ground 🐕🏃")

# Bird subclass
class Bird(Animal):
    def move(self):
        """Override move method to define how a bird moves."""
        print("The bird is flying in the sky 🦅✈️")

# Fish subclass
class Fish(Animal):
    def move(self):
        """Override move method to define how a fish moves."""
        print("The fish is swimming in the water 🐟🌊")

# Create instances and call move() on each
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()  # Polymorphism in action: the move() behavior changes based on the object
