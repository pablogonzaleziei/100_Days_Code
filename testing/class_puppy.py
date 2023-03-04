

class Puppy:
    def __init__(self, name, favorite_toy):
        self.name = name
        self.favorite_toy = favorite_toy
    
    def play(self):
        print(f"{self.name} is playing with their favorite toy, {self.favorite_toy}!")

# Create three different instances of the Puppy class
puppy1 = Puppy("Max", "ball")
puppy2 = Puppy("Buddy", "frisbee")
puppy3 = Puppy("Charlie", "rope")

# Call the play method for each puppy
puppy1.play()
puppy2.play()
puppy3.play()
