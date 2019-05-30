'''
#Function with a single argument 
def say_hi(message):
    print(message)

say_hi('Hello World!')
'''

'''
#functions that return a result

def square(value):
    result  = value * value
    return result 

answer = square(10)

print(answer)
#print(answer)

print(square(50))
'''

'''
#function with multiple arguments
def greetings(name, job, hobby): 
    print(f'Hello {name}, your job is {job}, and you like to {hobby}')

greetings('Chinonso', 'exist', 'browse reddit')
'''

'''
def reverse_list(my_list): 
# iterate over list in reverse order
    new_list = []
    for numbers in range(len(my_list) - 1, -1, -1): 
        # add each element to a new list
        new_list.append(my_list[numbers])

    return new_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reverse_list(numbers)

print(result)
'''

'''
def is_palindrome(word):
    #check if word is the same forwards as backwards
    letter
    for letters in word:
        if letters == letters[-1]:
            return ('True')
    #return true if it is, false otherwise 
        else:
            return ('False')

print(is_palindrome('jeff'))
'''

def is_palindrome(word):
    letters = list(word)
    for letters in word:
        if letters == letters[-1]:
            return True
        return False

print(is_palindrome('jeff'))