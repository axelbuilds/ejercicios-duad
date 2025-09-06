#Ejercicio OOP #4

class Head:
    def description(self):
        return "Cabeza"  #Returns the body part name


class Hand:
    def __init__(self, side):
        self.side = side  #Side left or right

    def description(self):
        return f"Mano {self.side}"  #Returns the side


class Arm:
    def __init__(self, hand, side):
        self.hand = hand  
        self.side = side  #Hand side

    def description(self):
        return f"{self.hand.description()}, Brazo {self.side}" #Returns arm side


class Feet:
    def __init__(self, side):
        self.side = side  #Feet side

    def description(self):
        return f"Pie {self.side}"  #Returns feet side


class Leg:
    def __init__(self, feet, side):
        self.feet = feet 
        self.side = side  #Leg side

    def description(self):
        return f"{self.feet.description()}, Pierna {self.side}" #Returns feet side


class Torso: #Class to connect all objects
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

    def description(self): #Calls all objects
        parts = [
            self.head.description(),
            self.right_arm.description(),
            self.left_arm.description(),
            self.right_leg.description(),
            self.left_leg.description()
        ]
        return ", ".join(parts) #Combines objets in one line separated with commas


class Human:
    def __init__(self, torso):
        self.torso = torso

    def body_parts(self):
        print(f"El cuerpo se compone de: {self.torso.description()}") #Prints objects description


#Creates objects
head = Head()
right_hand = Hand("derecho")
left_hand = Hand("izquierdo")
right_arm = Arm(right_hand, "derecho")
left_arm = Arm(left_hand, "izquierdo")
right_feet = Feet("derecha")
left_feet = Feet("izquierda")
right_leg = Leg(right_feet, "derecha")
left_leg = Leg(left_feet, "izquierda")
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)


human_body = Human(torso) #Create Human object
human_body.body_parts()