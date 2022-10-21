class Husky (Dog) :
    def naughty (self) :
        print("拆沙发")
        print("拆电视")
        print("拆一切")
        
pop = Husky("Black", "20201201", "male")

print(pop.color)
pop.barking()

pop.naughty()
