course='This is the first python programming course'
print(course[0]) #print the first letter
print(course[-1])# print the end of the string letter
print(course[-2])# print the letter from the end and on second index
print(course[0:4])# prints from the beginig and exclude 4, eg This
print(course[0:])#print all
print(course[1:])# it ommits the first character

print(course[:])#print all.

anotherWord=course[:]# since course[:] copy/print all the sentence, it copies to anotherWord var.
print(anotherWord)