#open the csv file and read the file as string and save in names
f = open('unisex_names_table.csv', 'r')
names = f.read()
#we split the string by '\n' and save as a list
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)
#we gonna split the list again by ',' and append in nested_list
nested_list = []
for i in names_list:
    comma_list = i.split(',')
    nested_list.append(comma_list)
print(nested_list)
#we covert the index[1] to float and save in numerical_list
numerical_list = []
for i in nested_list:
    line = i[0]
    float_num = float(i[1])
    new_list = [line,float_num]
    numerical_list.append(new_list)
    
numerical_list[0:5]

# The last value is ~100 people
numerical_list[len(numerical_list)-1]

thousand_or_greater = []
for line in numerical_list:
    if line[1] >= 1000:
        thousand_or_greater.append(line[0])
print(thousand_or_greater[0:10])