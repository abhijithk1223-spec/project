class person:
    def __init__(self,name):
        self.name = name
        
    def greet(self):
        print("hello,my name is " + self.name)

p1 = person("emil")
p1.greet()