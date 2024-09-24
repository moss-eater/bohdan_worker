class Pupil:
    def __init__(self, gender, surname, name, land, mark):
        self.gender = gender
        self.surname = surname
        self.name = name
        self.land = land
        self.mark = mark

pupil_amount = 0
best_pupils = []
sum = 0

pupils = []
def print_class(pupils):
    for pupil in pupils:
        print(pupil.gender, pupil.surname, pupil.name, "from", pupil.land, "-", pupil.mark)

def print_ten(pupils):
    print("Best students")
    for pupil in pupils:
        if pupil.mark > 9:
            print(pupil.surname)
    print("\n")

with open("pupil.txt", "r", encoding= "UTF-8") as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0], data[1], data[2], data[3], int(data[4]))
        pupils.append(pupil)

print_class(pupils)