#define the base class player  
class player:
 def player(self):
    print("the player is playing cricket")
#define tha derived class batsman
class batsman(player):
  def play(self):
    print("the batsman is batting")
#define the derived class bowler
class Bowler(player):
  def play(self):
    print("the bowler is bowling")
#create object of batsman and bowler classes
batsman=batsman()
bowler=Bowler()
#call tha play()method for each object 
batsman.play()
bowler.play()

