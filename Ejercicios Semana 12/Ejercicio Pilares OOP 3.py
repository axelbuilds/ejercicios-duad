#Ejercicio Pilares OOP #3

class Sword:
    def heavyslash(self):
        return "Ataque HeavySlash 30 Hit Points"


class Bow:
    def piercingshot(self):
        return "Ataque Piercing Shot 35 Hit Points"


class Staff:
    def flameburst(self):
        return "Ataque Flame Burst 40 Hit Points"
    

class Warrior(Sword, Bow, Staff): #Inherit weapons
    pass

character = Warrior()
print(character.heavyslash())
print(character.piercingshot())
print(character.flameburst())