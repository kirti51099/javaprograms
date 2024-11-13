import abc
class car(abc):
    def mileage(self):
     pass
class tesla(car):
    def mileage(self):
        print("the mlge is 30 kmph")
class suzuki(car):
    def mileage(self):
       print("the mileage is 25kmph")

t=tesla()
t.mileage
s=suzuki()
s.mileage()
    