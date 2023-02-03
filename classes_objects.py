# custom classes and objects

# hash table, hash map

# class NewClass:
# inheritance, polymorphism, encapsulation

class Student:

    def __init__(self, first, last, courses=None) :
        self.first_name = first
        self.last_name = last
        
        if courses == None:
            self.courses = []
        else:
            self.courses = courses
            
    def __str__(self) :
        # temp = 
        return f"{self.first_name.capitalize()}{self.last_name.capitalize()}{', '.join(map(str.capitalize, self.courses))}"
        # join runs as method on string
            
    def add_course(self, course) :
        if course not in self.courses :
            self.courses.append(course)
        else:
            print(f"{self.first_name} already in {course}")
            
    def remove_course(self, course) :
        if course in self.courses :
            self.courses.remove(course)
        else :
            print(f"{self.first_name} not in {course}")
            
    def __len__(self) :
        # print(len(self.courses))
        return len(self.courses)
        # len(pass
        
    def __repr__(self) :
        return f"Student('{self.first_name}','{self.last_name}', '{self.courses})'"
        
courses_1 = ['python', 'rails', 'javascript']
courses_2 = ['java','rails','C']
mashrur = Student('mashrur','hossain', courses_1)
john = Student('john','doe', courses_2)

mashrur.add_course('java')
mashrur.add_course('rails')
# print(mashrur.first_name, mashrur.last_name, mashrur.courses)
john.remove_course('C') # first time, will remove
john.remove_course('C') # second time, course no longer there
# print(john)
# print(john)
# print(john.__dict__)
print(repr(john))
# print(len(john.courses))
#map apply function on left to each of the shit in the list to the right
#join first element stuffed in between the list of the rest of the shit

# repr is how you represent your object, you'll get the same output as line 44
# if no str, python will look for repr