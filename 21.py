#Class Inheritance Example
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def     breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_fins = 2

    def swim(self):
        print("Moving in water")

# Example usage
nemo =Fish()
nemo.breathe()
nemo.swim()
print(f"Nemo has {nemo.num_eyes} eyes and {nemo.num_fins} fins.")


#slicing example
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3])  # Output: [2, 3]
print(my_list[:2])   # Output: [1, 2]    

