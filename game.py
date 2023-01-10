#Create the class Monster
class Monster:
  def __init__(self, attack, name):
    self.attack = attack
    self.name = name

  def __call__(self):
    return f'The {self.name} has been summoned'

  def __str__(self):
    return self.name

#Create the class Attacks
class Attacks:
  #Methods
  def bite(self):
    print('The Monster has bitten you')

  def strike(self):
    print('The Monster has struck you')

  def slash(self):
    print('The Monster has slashed you')

  def kick(self):
    print('The Monster has kicked you')

#Creating an attacks object

#Creating monster Object
monster = Monster(Attacks().bite(), 'weakMonster')

print(monster())

print(monster)