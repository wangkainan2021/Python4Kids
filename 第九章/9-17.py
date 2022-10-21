class Dog () :
    def __init__(self, color, birthday, gender):
        self.color = color
        self.birthday = birthday
        self.gender = gender
        
pop = Dog("Black", "20201201", "male")
print(pop.color, pop.birthday, pop.gender)
