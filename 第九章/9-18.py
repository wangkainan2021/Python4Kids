class Dog () :

    def __init__(self, color, birthday, gender):
        self.color = color
        self.birthday = birthday
        self.gender = gender

    def barking (self):
        print("汪汪汪~")
        
pop = Dog("Black", "20201201", "male")

pop.barking()
