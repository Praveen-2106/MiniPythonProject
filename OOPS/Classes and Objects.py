#class ==> any objects, data members, etc

#object ==> real world entity

class Sample:
    def __init__(self,obj,wheels, color, sheets, fuel, sp):
        print("constructor Called")
        self.obj = obj
        self.no_of_wheels = wheels
        self.colors = color
        self.no_of_sheets = sheets
        self.fuel_type = fuel
        self.speed = sp
    def __str__(self):
        return self.obj

    def __del__(self):
        print("DESTROYTED")

honda = Sample("HII""Honda", 4, "red", 5, "EV", 100)
print(honda.no_of_wheels)


