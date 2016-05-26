"""

# Week 2 Exercises
Write a program that enrolls student to different units as per the instructions below:
 - A student should be enrolled to a specific unit only once
 - Some of the units (core units) are mandatory to all students. Students should be enrolled to these units during registration (instantiation).
 - The rest of the units are optional. A student can be enrolled to these using a method `enroll_unit` which accepts the unit code
 - An error should be raised if a wrong unit code is entered

The units a student is enrolled to should be stored in a list which is empty during instantiation
"""
class Student(object):
    """docstring for Student"""



    def __init__(self, fname, lname, student_id):
        """Initialize instance variables. """
        self.units = []
        self.fname = fname
        self.lname = lname
        self.student_id = student_id
        self.core_units = {
    'UNIT001': {'unit_name': 'Unit 1', 'core': True},
    'UNIT002': {'unit_name': 'Unit 2', 'core': False},
    'CS001': {'unit_name': 'Introduction to Programming', 'core': False},
    'COMP12': {'unit_name': 'Intro to Python', 'core': False},
   
}

    def get_student_details(self):
        return "Student Details %s %s , Reg No : %s "  %(self.fname , self.lname , self.student_id)

    def enroll_unit(self, unit_code):
    	self.unit_code = unit_code
    	for key , value in self.core_units.items():
    		if self.unit_code == key:
    			self.units.append(value)
    		
    def get_enrolled_units(self):
    	for i in self.units:
    		for key,value in i.items():
    			return key

        


#test
new_student = Student('Eric', 'G', 'ST101-2016')
print new_student.get_student_details()
print new_student.enroll_unit('UNIT001')
print new_student.enroll_unit('COMP12')
print new_student.get_enrolled_units()