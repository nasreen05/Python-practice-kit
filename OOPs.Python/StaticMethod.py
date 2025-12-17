class Student:
  def _init_(self, name, marks):
    self.name = name  #obj attr > class attr
    self.marks = marks

@staticmethod
def hello ():
       print("hello")

def get_avg(self):
     sum=0
     for val in self.marks:
        sum += val
        print("h1", self.name, "your avg score is:", sum/3)

        s1 = Student("shark tank ",[ 99,89,78])
        s1.get_avg()
        s1.hello()

        s1.name ="ironman"
        s1.get_avg()
       