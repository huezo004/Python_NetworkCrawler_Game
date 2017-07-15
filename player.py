import random 
from socket import  * 

class Character():
 def __init__(self):
  self.hp =0
  self.strength =90
  self.defense =0
  self.pos=0
  self.p=[0,6,12,18,24] #player position 
  self.name=""

 def quit(self):
  print "Namaste!"
  
 def help(self):
   print "go[N,S,E or W]"
   print "quit"
   print "attack"
   print "health"

 def calc_damage(self, opp):
  damage = random.randint(0,6) + self.strength - opp.defense
  if damage <=0:
     print "{} evades {}'s attack.".format(opp.name, self.name)  
  else:
      opp.hp= opp.hp-damage 
      print "{} attacks {} for {} points of damage !".format(self.name, opp.name, str(damage))
   
class EvilRobot(Character):
 def __init__(self,socket):
  Character.__init__(self)
  self.hp=15 
  self.strength=9 
  self.defense= 7 
  self.name="Evil robot"
  self.s= socket
  self.pos=0
 
class Player(Character):
 def __init__(self):
  Character.__init__(self)
  self.hp=0
  self.strength=0
  self.defense=0
  self.pos=random.choice(self.p)
  self.s=socket
  self.pos=0

 def health(self):
   self.s.send(self.name + " has " + str(self.hp) + " HP")
   return self.health

 def goN(self):
  ln=[0,1,2,3,4,5]
  if self.pos not in ln:
     self.pos -=6 
     return self.pos
  else: 
   return 0 

 def goS(self):
  ln=[24,25,26,27,28,29]
  if self.pos not in ln:
     self.pos +=6 
     return self.pos 
  else: 
   return 0 

 def goW(self):
  ln=[0,6,12,18,24]
  if self.pos not in ln:
     self.pos -=1 
     return self.pos
  else: 
   return 0 

 def goE(self):
  ln=[5,11,17,23,29]
  if self.pos not in ln:
     self.pos +=1 
     return self.pos
  else: 
   return 0 
  
class CodeWarrior(Player):
 def __init__(self,socket):
  Player.__init__(self)
  self.hp=30
  self.strenght=10
  self.defense=8
  self.s = socket
  self.pos=0

class H4x0r(Player):
 def __init__(self,socket):
  Player.__init__(self)
  self.hp=30
  self.strength=8
  self.defense=10
  self.s=socket
  self.pos=0

