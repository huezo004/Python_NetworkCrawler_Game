"""
Denyse Huezo 
dah12
"""
from player import * 
from socket import *
import threading 


def start_game(c):
 vmatrix=[1,2,3,4,5,7,8,9,10,11,13,14,15,16,17,19,20,21,
 22,23,25,26,27,28,29]
 matrix=  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
22,23,24,25,26,27,28,29]
 backpack = random.choice(vmatrix) 
 vmatrix.remove(backpack)
 rat= random.choice(vmatrix) 
 vmatrix.remove(rat)
 e1= EvilRobot(c)
 e1.pos=random.choice(vmatrix) 
 vmatrix.remove(e1.pos)

 e2= EvilRobot(c)
 e2.pos=random.choice(vmatrix) 
 vmatrix.remove(e2.pos)
 e3= EvilRobot(c)
 e3.pos=random.choice(vmatrix) 
 vmatrix.remove(e3.pos)
 e4= EvilRobot(c)
 e4.pos=random.choice(vmatrix) 
 vmatrix.remove(e4.pos)
 
 c.send("Prepare! the game has just began!")
 c.send("Enter your warrior's name:")
 war=c.recv(20).strip()

 c.send("Are you a CodeWarrior or 1337H4x0r?")
 c.send("Enter [c] or [h]:")
 name = c.recv(20).strip()

 
 if name == "c":
  p=CodeWarrior(c)
  p.name= war

 if name == "h":
  p=H4x0r(c)
  p.name=war 


 p.pos = 12 
 
 ee= str(p.pos)

 while True: 
  op=c.recv(1000).strip()
  if op== "go N":
   result=p.goN()
   if result==0:
    c.send("You have hit a wall, try another direction!")
    continue 
   if result == rat:
     c.send("You have encountered the ultimate evil force")
     c.send("try in your next life!")
     p.quit()
   if result == backpack:
     c.send("You have accomplished your mission! You win!") 
     p.quit()
   if result== e1.pos:
     fight(c,p, e1)
   if result== e2.pos: 
     fight(c,p, e2)
   if result== e3.pos: 
     fight(c,p, e3)
   if result == e4.pos:
     fight(c,p, e4)
  if op== "go S":
   result=p.goS()
   if result==0:
      c.send("You have hit a wall, try another direction!")
      continue 
   if result == rat:
     c.send("You have encountered the ultimate evil force")
     c.send("try in your next life!")
     p.quit()
   if result == backpack:
     c.send("You have accomplished your mission! You win!") 
     p.quit()
   if result== e1.pos:
      fight(c,p, e1)
   if result== e2.pos: 
     fight(c,p, e2)
   if result== e3.pos: 
     fight(c,p, e3)
   if result == e4.pos:
     fight(c,p, e4) 
  if op== "go E":
   result=p.goE()
   if result==0:
    c.send("You have hit a wall, try another direction!")
    continue 
   if result == rat:
     c.send("You have encountered the ultimate evil force")
     c.send("try in your next life!")
     p.quit()  #
     c.close()
   if result == backpack:
     c.send("You have accomplished your mission! You win!") 
     p.quit() #
     c.close()
   if result== e1.pos:
     fight(c,p, e1)
   if result== e2.pos: 
     fight(c,p, e2)
   if result== e3.pos: 
     fight(c,p, e3)
   if result == e4.pos:
     fight(c,p, e4) 
  if op== "go W":
   result=p.goW()
   if result==0:
    c.send("You have hit a wall, try another direction!")
    continue 
   if result == rat:
     c.send("You have encountered the ultimate evil force")
     c.send("try in your next life!")
     p.quit() # 
     c.close()
   if result == backpack:
     c.send("You have accomplished your mission! You win!") 
     p.quit() #
     c.close()
   if result== e1.pos:
     fight(c,p, e1)
   if result== e2.pos: 
     fight(c,p, e2)
   if result== e3.pos:
     fight(c,p, e3)
   if result == e4.pos:
     fight(c,p, e4) 
  if op== "quit":
    c.send("Namaste!")
    c.close()
  if op == "help":
    p.help() #
    continue 
  if op== "attack":
    c.send("Stay Zen there are no enemies near you!")
    continue
  if op=="health":
    p.health() #
    continue 
 
def fight(c, pp, e):
 c.send("Prepare to attack, you have encountered an enemy!")
 while True: 
  f= c.recv(1000).strip()
  if f== "attack":
    pp.calc_damage(e) 
    e.calc_damage(pp)
    if pp.hp <= 0:
     c.send(e.name + "has killed you")
     pp.quit() 
     c.close()
    if e.hp <=0:
     c.send(pp.name + " wins! Evil robot has died; Keep going!")
     e.pos=-1 
     return 1
  if f== "quit" : 
    c.send("Giving up? ... fine..")
    pp.quit()
    c.close()
  if f=="go N" or f== "go S" or f== "go E" or f== "go W":
    c.send("You are in middle of a battle, you cannot move!") 
    continue 

#quit, backpack, health ...
if __name__ == "__main__":
  s= socket(AF_INET, SOCK_STREAM)
  s.bind(("",9000))
  s.listen(5) 
  while True:
    c,a= s.accept()
    t= threading.Thread(target=start_game, args=(c,))
    t.start() 
 

