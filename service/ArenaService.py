
import random
from entity.Dice import Dice

class ArenaService:
    def __init__(self, playerA, playerB):
        if not playerA or not playerB:
            raise ValueError("Player cannot be null")
        self.playerA = playerA
        self.playerB = playerB

    def choose_initial_attacker(self, playerA, playerB):
        if playerA.health == playerB.health:
            return random.choice([playerA, playerB])
        elif playerA.health < playerB.health:
            return playerA
        else:
            return playerB
    
    def play_match(self):
        attacker = self.choose_initial_attacker(self.playerA, self.playerB)
        if attacker == self.playerA:
            attacker_name = "PlayerA"
            defender_name = "PlayerB"
            defender = self.playerB
        else:
            defender = self.playerA
            attacker_name = "PlayerB"
            defender_name = "PlayerA"
        random_roll = Dice()
        turn = 1
        while attacker.health > 0 and defender.health > 0:
            print(f"Round {turn}")
            attack_dice = random_roll.roll()
            defend_dice = random_roll.roll()
            print(f"{attacker_name} attacks with a roll of {attack_dice}.")
            print(f"{defender_name} defends with a roll of {defend_dice}.")
            attack_damage = attack_dice * attacker.attack
            defended_damage = defend_dice * defender.strength
            actual_damage = max(0, attack_damage - defended_damage)
            print(f"Attack damage = {attack_damage}")
            print(f"Defended damage = {defended_damage}")
            print(f"Actual damage = {actual_damage}")
            defender.take_damage(actual_damage)
            print(f"{defender_name}'s health after the round = {defender.get_health()}")
            attacker, defender = defender, attacker
            attacker_name, defender_name = defender_name, attacker_name
            turn += 1
            print("************************************************\n")
    
        if self.playerA.get_health()>0:
            print("Player A wins")
        else:
            print("Player B wins")


