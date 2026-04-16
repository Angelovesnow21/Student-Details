class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    def __init__(self, fname, lname, year):
        super(). __init__(fname, lname)
        self.birthdayyear = year

x = student("Oliver", "Ludwing", 1901)
x.printname()
print(x.birthdayyear)