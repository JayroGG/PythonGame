import os
from time import sleep

#Class Hero
class Hero:
  health = 100
  #Constructor
  def __init__(self, damage):
    self.damage = damage    

  #Methods
  def attack(self):
    self.target.get_damage(self.damage)
    print(f'\nYou have attacked the monster, the monster has: {self.target.health} HP')
    #Verifies if the target is still alive or if it have enough energy to attack
    if self.target.health > 0:
      if self.target.energy >= 20:
        self.target.autoAttack(self)
    else:
      print('The Monster is dead you have won')

  def setTarget(self, target):
    self.target = target
  
  def heal(self, amount):
    self.health += amount
    

#Class Monster
class Monster:
  # #Attributes
  # auto_attack = 15
  # health = 100
  # energy = 100
  def __init__(self, auto_attack, health, energy, **kwargs):
    self.auto_attack = auto_attack
    self.health = health
    self.energy = energy
    super().__init__(**kwargs)

  #Dunder Methods
  def __call__(self):
    return '\nThe Monster has been summoned'
  
  def __str__(self):
    return 'A Monster'

  #Methods
  def get_damage(self, amount):
    self.health -= amount

  def autoAttack(self, target):    
    if self.energy >= 20:
      target.health -= self.auto_attack * self.energy/100
      self.energy -= 20        
      print(f'\nThe Monster has attacked you in response, now you have: {target.health} HP')
    else:
      self.energy += 10  

  def move(self, speed):
    print('The Monster has moved')
    print(f'it has a speed of {speed}')
  
  def attributes(self):
    print(f'Monster damage: {self.auto_attack}')
    print(f'Monster health: {self.health}')
    print(f'Monster energy: {self.energy}')

#Creating class Fish
class Fish:
  def __init__(self, speed, has_scales, **kwargs):
    self.speed = speed
    self.has_scales =  has_scales
    super().__init__(**kwargs)

#Creating Shark lass with ineherence of the Monster class
class Shark(Monster, Fish):
  #Attributes
  #speed = 100

  def __init__(self, bite_strength, health, energy, speed, has_scales):
    self.auto_attack = bite_strength
    super().__init__(auto_attack = bite_strength, health = health, energy = energy, speed = speed, has_scales =  has_scales)
     
  #Methods
  def bite(self, target):
    target.health -= 35
  
  def move(self):
    print('The shark has moved')
    print(f'The speed of the shark is {self.speed}')

#Creating a Scorpion Monster class
class Scorpion(Monster):
  #Dunder methods
  def __init__(self, poison_damage, health, energy):
    super().__init__(poison_damage, health, energy)
    self.poison_damage = poison_damage

  #Methods
  def autoAttack(self, target):
    print(f'\nThe Scorpion has poisoned you back \nIt has deal: {self.auto_attack} of poison damage')
    target.health -= self.auto_attack
    print(f'\nNow you have: {target.health} HP')

#Creating a monsters objects
shark = Shark(
   bite_strength = 30,
   health = 120,
   energy = 100,
   speed =  30, 
   has_scales = False)

monster = Monster(15, 100, 100)
scorpion = Scorpion(25, 130, 100)

#Creating hero object with damage and target monster
hero = Hero(damage = 50)

#Creating a battle
def battle(hero, monster):
  os.system('clear')
  os.system('cls')
  print(monster())
  print(monster)
  hero.setTarget(monster)
  
  while monster.health > 0:
    print(f'\nHero health: {hero.health}') 
    if hero.health <= 0:
      print('\nYour HP have lowered to critic, you are diying, heal yourself and try again')
      return

    monster.attributes()
    print('\n1.Attack\n2.Defend\n3.Do nothing\n4.Escape')
    action = input('\nWhat you gonna do?\n\n')
    os.system('clear')
    os.system('cls')
    if action == '1':      
      hero.attack()
    if action == '2':
      print('\nThe monster has attack but has no effect on you\nYou have healed 2 HP') 
      hero.heal(2)
    if action == '3':
      monster.autoAttack(hero)
    if action == '4':
      if hero.damage > monster.auto_attack:
        print('\n\nYou have escpaped\n\n')
        return 
      else:
        print("\nYou can't escape\n")  

  print('\n\nThe battle has ended\n\n')    

battle(hero, shark)
# print(shark.speed)