def main():
    first_name = "Chinonso"
    last_name = "Ibekwe"
    full_name = first_name + " " + last_name

    print(full_name)

    #boolean variable
    neha_has_a_big_head = True 

    #null/none variable (no value; value is missing completely)
    cars = None 

    #modulus operator (mostly used with integers; tests if number is odd or even)

def conditionals(): 
    #given a range of grades 0 - 100
    #if grade is between 80 and 100 - print "A"
    #if grade is between 60 and 79 - print "B"
    # grade is between 50-59 - print "C"
    # if grade is 0-49 - print "You're a dummy lol"

    grade = 49
    if grade >= 80:
        print("A")
    elif grade >= 60: 
        print("B")
    elif grade >=50:
        print("C")
    else: 
        print("You're a dummy lol") 

def fizzbuzz():
    '''
    for the number 1 to 50
    print 'fizz' if the number is a multiple of 3
    print 'buzz' if the number is a multiple of 5 
    print 'fizzbuzz' if the number is a multiple of 15
    otherwise print number
    '''
# use range for this 
# range()
#for num in range()
#print num 
# used % to find if number is a multiple of 3 or 5

    for num in range(1, 51): 
        if num%3 == 0 and num%5 == 0: 
            print("fizzbuzz")
        elif num%3 == 0:
            print("fizz")
        elif num%5 == 0:
            print("buzz")
        else:
            print(num)


if __name__ == "__main__": 
    fizzbuzz()


