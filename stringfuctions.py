course='Python is the most simples and powerfull language'
print(course.upper()) #prints the cpatital letters
print(course)#prints normal letter, not capital
print(course.lower())
print(course.find('a')) #first index of the letter
print(course.find('simples')) #first index of the word
print(course.replace('simples','Hard'))

#How to use in operator in python?

#in operator responds the boolean values
isExist='Python' in course
print(isExist)# prints true
print('Motuma' in course)#print false, coz Motuma is not found in course
print(course.title())