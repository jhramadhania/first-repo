class Student:
  def __init__(self, name, year, enrolled, gpa):
    self.name = name
    self.year = year
    self.enrolled = enrolled
    self.gpa = gpa
  
  def display_info(self):
    print('The student ' + self.name + '\'s GPA is ' + str(self.gpa) + '!')
  
mitsuha = Student('宮水三葉', 11, False, 4.0)
taki = Student('立花瀧', 11, True, 3.8)

mitsuha.display_info()
taki.display_info()