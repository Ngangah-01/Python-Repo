my_list = []

new_values = [10,20,30,40]
for value in new_values:
    my_list.append(value)

print(my_list)

my_list.insert(2,15)
my_list.extend([50,60,70])

my_list.pop(-1)
sortedlist = sorted(my_list)

print(f"The index of the value 30 is:{my_list.index(30)}")
print(sortedlist)