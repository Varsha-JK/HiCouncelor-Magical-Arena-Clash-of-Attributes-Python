class Player:
    def __init__(self, health, strength, attack):
        if health > 0:
            self.health = health
        else: raise ValueError("Health must be greater than 0")
        if strength > 0:
            self.strength = strength 
        else: raise ValueError("Strength must be greater than 0")
        if attack > 0:
            self.attack = attack
        else: raise ValueError("Attack value must be greater than 0")

        print("Player created successfully")
    
    def get_health(self):
        return self.health
    
    def get_strength(self):
        return self.strength

    def get_attack(self):
        return self.attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0