from abc import ABC, abstractmethod
# abc is a builtin module, we have to import ABC and abstractmethod

class Animal(ABC): # Inherit from ABC(Abstract base class)
    @abstractmethod  # Decorator to define an abstract method
    def feed(self):
        pass
    @abstractmethod  # Decorator to define an abstract method
    def getName(self) -> str:
        pass
    @abstractmethod  # Decorator to define an abstract method
    def getAge(self) -> int:
        pass
    
class lion(Animal):
    def __init__(self, x):
        self.x = x
        self.name = "Hoi"
        self.age = 43
        
    def feed(self):
        print(self.x)
    
    # instantiate
    def getName(self):
        return self.name
    
    # instantiate
    def getAge(self):
        return self.age
    
    def __str__(self):
        return f"{self.getName()}({self.getAge()})"

x = lion(42)
x.feed()
print(x)