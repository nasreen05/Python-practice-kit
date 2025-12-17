class Student:
    def __init__(self,phy,chem, math):
        self.phy =phy
        self.math =math
        self.chem = chem
        self.percentage =str((self.phy + self.chem + self.math)/3)+"%"

        #def calcpercentage(Self):
           # self.percentage=str((self.phy +self.chem +self.math)/3)+"%"

@property
def percentage(self):
            return str((self.phy +self.chem +self.math)/3)+"%"

stu1 = Student(98,87,89)
print(stu1.percentage)


stu1.phy=85
print(stu1.percentage)