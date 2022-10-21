class Dog () :

    def __init__(self, color, birthday, gender):
        self.color = color
        self.birthday = birthday
        self.gender = gender
        
    def barking (self):
        print("汪汪汪~")
        
    def intimate (self):
        print("蹭蹭~")
    
    def wagging (self):
        print("摇尾巴")
        
pop = Dog("Black", "20201201", "male")
pop.barking()
pop.intimate()
pop.wagging()
