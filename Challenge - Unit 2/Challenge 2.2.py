'''Implement a class called Player that represents a cricket player. the player should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the player class. override the play() moethod in each derived class to print "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and bowler classes and call the play() method for each object'''


# Define the base class Player
class Player:
  def play(self):
    print("The player is playing cricket")

# Define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting")

# Create objects of Player and Batsman classes
player = Player()
batsman = Batsman()

# Call the play() method for each object
player.play()
batsman.play()