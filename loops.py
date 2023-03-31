numbers=[1,4,5,6]
for items in numbers:
    print(items)


for seq in range(5):
    print(seq)

#find maximum number:
find_max_number=[45,67,33,23,77,87]
max=find_max_number[0]
for maxnum in find_max_number:
    if maxnum>max:
       max= maxnum
    print(f'Maximum number is: {max}')