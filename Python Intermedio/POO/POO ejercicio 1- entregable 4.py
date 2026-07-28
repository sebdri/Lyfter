
class Head:
    def __init__(self):
        pass


class Torso:
    def __init__(self,head, arm,leg ):
        self.head = head
        self.arm = arm
        self.leg= leg

class Arm:
    def __init__(self,hand):
        self.hand = hand

class Hand: 
    def __init__(self):
        pass


class Leg:
    def __init__(self, feet):
        self.feet = feet
        

class Feet:
    def __init__(self):
        pass



class Human:
    def __init__(self,torso):
        self.torso = torso
      

hand = Hand()
feet = Feet()
head = Head()


arm = Arm(hand)
leg = Leg(feet)


torso = Torso(head, arm, leg)


new_human = Human(torso)


