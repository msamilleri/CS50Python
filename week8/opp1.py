
class wizard:
    def __init__(self, name):
        if not name:
            raise  ValueError("Missing name")
        self.name = name

class Student(wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Profesor (wizard):
    def __init__(self,name, subject):
        super().__init__(name)
        self.subject= subject

class valut:
    def __init__(self, gallones=0, sickles=0, knuts=0):
        self.gallones = gallones
        self.sickles = sickles
        self.knuts = knuts



    def __str__(self):

        return f"gallonus = {self.gallones} sickles {self.sickles} knuts {self.knuts}"

    def __add__(self, other):
        gal = potter.gallones + pooter.gallones
        sic = potter.sickles + pooter.sickles
        knts = potter.knuts + pooter.knuts
        return valut(gal, sic, knts)


potter = valut(100, 20,30)
print(potter)
pooter = valut(152,456,23)
print(potter)

sum = potter + pooter
print(sum)
