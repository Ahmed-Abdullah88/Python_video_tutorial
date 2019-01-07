# Finished video No. 5

student = {'name': 'john', 'age': 25, 'courses': ['Math', 'CompSci']}

student.update({'name': 'Jane', 'age': 30, 'email': 'aa@aa.com'})
# print(student.get('phone', 'Not Found'))
print(student)

del student['email']

age = student.pop('age')
print(age)
print(student)
print(student.items())

print('*********************')

for key, value in student.items():
    print(key, value)
