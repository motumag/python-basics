numbers=[1,4,4,5,7,8]
print(numbers.count(4))

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

originalNumber=numbers.copy()
numbers.append(20)
print(numbers)
print(originalNumber)# this numbers are safe from updating when we add a value to it