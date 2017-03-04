# Grouping of similar variables and functions

class Enemy():
    life = 3 # each enemy has a life of 3

    def __init__ (self, life):
        self.life = life
        
    def Attack (self): # self-use something from this class
        print ("ouch!")
        self.life = self.life - 1

    def CheckLife (self):
        if (self.life <= 0):
            print ("I am Dead");
        else:
            print (str(self.life) + " life left")

EnemyObj1 = Enemy (20)
EnemyObj1.Attack ()
EnemyObj1.CheckLife ()

EnemyObj2 = Enemy (20)
EnemyObj2.CheckLife ()


class Tuna:
    # the init function gets called automatically when an object is created
    # need not call it
    
    def __init__(self, x):
        print ("Im Tuna")
        self.life = x
        print ("My life time is: " + str (self.life))

    def swim (self):
        print ("im swimming yo!")

TunaObj1 = Tuna (5)
BigTunaObj1 = Tuna (20)

# Class Variable --> present inside the class. its the same to all instances
# Instance Variable --> present inside init method. it is different for all instances

class Girl:
    gender = "female"

    def __init__ (self, name):
        self.name = name

r = Girl ("Penny <3")
a = Girl ("Amy :/")
print (r.gender + "  " + r. name)
print (a.gender + "  " + a. name)










































































































































        
        
    
