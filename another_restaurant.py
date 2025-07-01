class Student:
  student_id = 0
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False

wednesday = Student()
wednesday.student_id = 1113
wednesday.name = 'Wednesday Addams'
wednesday.year = 11
wednesday.gpa = 4.0
wednesday.enrolled = True

print(vars(wednesday))



class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = True

bobs_burger = Restaurant()
bobs_burger.name = 'Bob\'s Burgers'
bobs_burger.category = 'American Diner'
bobs_burger.rating = 4.7
bobs_burger.delivery = False

wingstop = Restaurant()
wingstop.name = 'Wingstop'
wingstop.category = 'Asian Cuisin'
wingstop.rating = 4.5
wingstop.delivery = True

kfc = Restaurant()
kfc.name = 'KFC Chicken'
kfc.category = 'American Diner'
kfc.rating = 4.8
kfc.delivery = True

print(vars(bobs_burger))
print(vars(wingstop))
print(vars(kfc))