'''
#writing loops
statement = "Hello world"
num = 3

for num in range(num): 
    print(statement)
'''
'''
#using mathematical operators and writing loops
num = 5
my_list = [1, 2, 3, 4]

for number, numerator in enumerate(my_list):
    my_list[number] = my_list[number] * num

print(my_list)
'''
'''
#using I/O, manipulating strings, and writing loops (Reversing a string, list, whatever)
#access last element = my_string[len(the start, the end, the steps]

my_string = 'This is a sentence'
for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i], end='')
'''
User_input = 'add'
number_1 = 5
number_2 = 6

if User_input == 'add':
    print('Your result is', number_1 + number_2, '. Calc U later!')
elif User_input == 'sub':
    print('Your result is', number_1 - number_2, '. Calc U later!')
elif User_input == 'mult':
    print('Your result is', number_1 * number_2, '. Calc U later!')
elif User_input == 'div':
    print('Your result is', number_1 / number_2, '. Calc U later!')
else:
    print('Type a valid operator idiot')