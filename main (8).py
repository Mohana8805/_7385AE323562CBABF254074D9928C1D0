class player :
 def playetr(self):
   print("the player is playing cricket:")
#def the derived class Batsman
class Batsman(player):
  def play(self) :
    print("the Batsman is batting")
#def the derived class Bowlers
class Bowlers(player):
  def play(self) :
    print("the Bowlers is bowling")
#create objects of Batsman and bowlers claases
batsman=Batsman()
bowlers= Bowlers()
#call the play() method for each object
batsman.play()
bowlers.play()
   