student = {
  'name': 'Ram',
  'age': 23,
  'city': 'Salem'
}
print(student.keys() >= {'age', 'name'})
print(student.keys() >= {'City', 'Ram'})
print(student.keys() >= {'city', 'Salem'})
print(student.keys() >= {'city', 'age'})
