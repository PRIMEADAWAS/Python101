print('Hello Py')
print('test')

values = ['a', 'b', 'c']
for value in values:
    print(value)

print('Try enumerate')
for count, value in enumerate(values):
    print(count, value)
print('Try count start=2')
for count, value in enumerate(values, start=2):
    print(count, value)
