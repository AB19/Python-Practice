class Parent1:
    def last_name (self):
        print ("Dafflings")

class Parent2:
    def last_name (self):
        print ("Jafflings")

class Child (Parent2, Parent1):
    pass

child1 = Child()
child1.last_name()
