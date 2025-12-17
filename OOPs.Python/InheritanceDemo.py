class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")

        @staticmethod
        def stop():
            print("Car stopped")


            class ToyotaCar(Car):
                def __init__(self,  name) :
                    self.name = __name__


                    car1 =ToyotaCar("fortuner")
                    car2 =ToyotaCar("prius")
                    
                    print(car1.color())
                        