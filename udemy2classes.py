class cookie:
    def __init__(self, color):pp
        self.color=color
    
    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color=color

cookie_one = cookie('green')
cookie_two = cookie('blue')

print("cookie one is",cookie_one.get_color())
print("cookie two is",cookie_two.get_color())

cookie_one.set_color('yellow')

print("cookie one is",cookie_one.get_color())
print("cookie two is",cookie_two.get_color())