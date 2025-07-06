class Student:
    def __init__ (self, name, age, rank, Gender):
        self.name = name
        self.age = age
        self.rank = rank
        self.gender = Gender
    
    def student_details(self):
        print("Name of the student is", self.name)
        print("Age of the student is", self.age)
        print("Rank of the student is", self.rank)
        print("Gender of the student is", self.gender)
    
    def is_topper(self):
        if self.rank == 1:
            print(self.name, "is the topper")
        else:
            print(self.name, "is not the topper")

s1 = Student('Veronica', 18, 1, 'Female')
s1.student_details()
s1.is_topper()
