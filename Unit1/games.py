# ask user to guess your secret number

#loops as long as user input is not equal to secret number 

#print a message if it is equal, then end loop

secret_number = 8
guess = int(input("Guess my secret number: "))

while guess != secret_number:
    print('Wrong number dummy')
    guess = int(input("Guess my secret number: "))
    if guess == secret_number:
        print('Wow you got it!')
