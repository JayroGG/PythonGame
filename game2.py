#Class Hero
class Hero:
  health = 100
  #Constructor
  def __init__(self, damage, target):
    self.damage = damage
    self.target = target

  #Methods
  def attack(self):
    self.target.get_damage(self.damage)
    print(f'you have attacked the monster, the monster has: {self.target.health} HP')
    if self.target.health > 0:
      if self.target.energy >= 20:
        self.target.autoAttack(self)
    else:
      print('The Monster is dead')
    

#Class Monster
class Monster:
  # #Attributes
  # auto_attack = 15
  # health = 100
  # energy = 100
  def __init__(self, auto_attack, health, energy):
    self.auto_attack = auto_attack
    self.health = health
    self.energy = energy
  
  #Dunder Methods
  def __call__(self):
    return 'The Monster has been summoned'
  
  def __str__(self):
    return 'A Monster'

  #Methods
  def get_damage(self, amount):
    self.health -= amount

  def autoAttack(self, target):
    target.health -= self.auto_attack * (self.energy/100)
    self.energy -= 20        
    print(f'The Monster has attacked you in response, now you have: {target.health} HP')  

  def move(self):
    print('The Monster has moved')


#Creating Shark lass with ineherence of the Monster class
class Shark(Monster):
  #Attributes
  #speed = 100

  def __init__(self, speed, auto_attack, health, energy):
    super().__init__(auto_attack, health, energy)
    self.speed = speed
  #Methods
  def bite(self, target):
    target.health -= 35


#Creating a monsters objects
shark = Shark(120, 30, 100, 100)
monster = Monster(15, 100, 100)

#Creating hero object with damage and target monster
hero = Hero(damage = 50, target = shark)
print(shark())
print(shark)

#Executing attack
hero.attack()
hero.attack()

print(shark.health)
print(monster.health)
