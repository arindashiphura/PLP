# Base class
class Transport:
    def move(self):
        print("Moving...")

# Subclasses
class BodaBoda(Transport):
    def move(self):
        print("🏍️ BodaBoda is weaving through Kabale town.")

class Taxi(Transport):
    def move(self):
        print("🚐 Taxi is driving along the hilly roads of Kigezi.")

class Drone(Transport):
    def move(self):
        print("🚁 Drone is flying above Lake Bunyonyi.")

# Polymorphic function
def travel(transport):
    transport.move()

# Create objects
t1 = BodaBoda()
t2 = Taxi()
t3 = Drone()

# Call polymorphic function
travel(t1)
travel(t2)
travel(t3)
