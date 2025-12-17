class Student:
 college_name = "ABC College"


def _init_(self, name, marks):
    self.name = name  #obj attr > class attr
    self.marks = marks

    def welcome(self):
       print("welcome student", self.name)

       def get_marks(self):
          return self.marks
  
    s1 = Student("karan", 98)
    s1.welcome()
    print(s1.get_marks())


#create a student class  that takes name & marks  of 3 subject as argument in constructor.Then  creat a method to print the average.

class Student:
  def _init_(self, name, marks):
    self.name = name  #obj attr > class attr
    self.marks = marks

  def get_avg(self):
     sum=0
     for val in self.marks:
        sum += val
        print("h1", self.name, "your avg score is:", sum/3)

        s1 = Student("shark tank ",[ 99,89,78])
        s1.get_avg()

        s1.name ="ironman"
        s1.get_avg()