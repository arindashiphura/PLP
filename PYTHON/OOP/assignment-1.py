# Base class
class StudentAthlete:
    def __init__(self, name, age, sport, position):
        self.name = name
        self.age = age
        self.sport = sport
        self.position = position

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")
        print(f"I'm a {self.sport} player and I play as a {self.position}.")

    def train(self):
        print(f"{self.name} is training for {self.sport} 🏋️‍♀️.")

# Subclass - Inheriting from StudentAthlete
class TechStudent(StudentAthlete):
    def __init__(self, name, age, sport, position, tech_skill):
        super().__init__(name, age, sport, position)
        self.__tech_skill = tech_skill  # Encapsulated

    def show_skill(self):
        print(f"{self.name} is also skilled in {self.__tech_skill} 💻.")

    def train(self):  # Polymorphism (overriding)
        print(f"{self.name} balances coding and {self.sport} training! 🧠💪")

# Creating objects
arinda = TechStudent("Arinda Shiphura", 20, "Netball", "Center", "Full-Stack Web Development")

# Using the methods
arinda.introduce()
arinda.train()
arinda.show_skill()
