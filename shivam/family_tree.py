class Grandparent:
    #This class represents attributes like surname,family_origin
    #It is an parent class 
    def __init__(self, surname, family_origin):
        self.surname = surname
        self.family_origin = family_origin

    def display_grandparent_info(self):
        print("Surname:",self.surname)
        print("Family Origin:",self.family_origin)

    # This is child class of Grandparent
class Parent(Grandparent):
    #In this child class we insert attribute like education and profession
    def __init__(self, surname, family_origin, education, profession):
        super().__init__(surname, family_origin)
        self.education = education
        self.profession = profession

    def display_parent_info(self):
        super().display_grandparent_info()
        print("Education: ",self.education)
        print("Profession:", self.profession)
    #This class inhertis by parent class
class Child(Parent):
    def __init__(self, surname, family_origin, education, profession, hobbies, current_school):
    #Here we use super function method to display additional information
        super().__init__(surname, family_origin, education, profession)
        self.hobbies = hobbies
        self.current_school = current_school

    def display_child_info(self):
        super().display_parent_info()
        print("Hobbies: ",self.hobbies)
        print(f"Current School:",self.current_school)

    def display_family_history(self):
        print("Family History:")
        super().display_parent_info()
        print("Hobbies:",self.hobbies)
        print("Current School:",self.current_school)
#called fucntion 
grandparent = Grandparent("Warner", "England")
grandparent.display_grandparent_info()
print("\n")

parent = Parent("CARTER", "England", "Bachelor's Degree", "Software Engineer")
parent.display_parent_info()

print("\n")

child = Child("Virat", "India", "High School Diploma", "Student", "Playing Guitar", "Local High School")
child.display_family_history()
