class Student:
  def __init__(self, name, year, gpa, enrolled):
    self.name = name
    self.year = year
    self.gpa = gpa
    self.enrolled = enrolled

daniel = Student('Daniel Li', 10, 4.0, True)
ladybird = Student('Christine McPherson', 12, 4.0, True)
kyle = Student('Kyle Scheible', 12, 3.4, True)

print(vars(daniel))
print(vars(ladybird))
print(vars(kyle))



class City:
  def __init__(self, name, country, population, landmarks, nickname, mayor):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.nickname = nickname
    self.mayor = mayor

mlg = City('Malang', 'Indonesia', 950000.0, ["Tugu Malang"], 'Ngalam', 'Tuan')
seoul = City('Seoul', 'South Korea', 970000.0, ["Hanggang River"], 'Seoul', 'Ahjussi')

print(vars(mlg))
print(vars(seoul))