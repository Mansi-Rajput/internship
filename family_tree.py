#### TASK: Family Tree ####
# Objective: Model a family tree using multilevel inheritance where 
# each generation inherits traits from the previous one.
# Challenge: Add a method in the Child class that displays the entire family 
# history by accessing attributes and methods from all ancestors.

class Grandparent:
    """Superclass"""
    def __init__(self, surname, origin):
        """__init__ method is used here for initializing instance variables"""
        self.surname = surname
        self.origin = origin

    def family_origin(self):
        return f"The {self.surname} Family originates from {self.origin}"

class Parent(Grandparent):
    """Intermediate class"""
    def __init__(self, surname, origin, education, profession):
        """__init__ method is used here for initializing instance variables"""
        super().__init__(surname, origin)
        self.education = education 
        self.profession = profession

    def profession_info(self):
        return f"Parent's profession is {self.profession}"
    
class Child(Parent):
    """Child class"""
    def __init__(self, surname, origin, education, profession, hobbies, school):
        """__init__ method is used here for initializing instance variables"""
        super().__init__(surname, origin, education, profession)
        self.hobbies = hobbies
        self.school = school

    def current_school(self):
        return f"Child's current school is {self.school}"
    
    def display_family_history(self):
        return (
            f"{self.family_origin()}\n"
            f"Educaiton: {self.education}\n"
            f"{self.profession_info()}\n"
            f"Hobbies: {self.hobbies}\n"
            f"{self.current_school()}\n"
            )
     
child = Child(surname="Smith", origin="England", education="Bachelor's Degree", 
        profession="Engineer", hobbies="Reading, Painting", school="Greenwood High")

print(child.display_family_history())