# declare an empty list
classmates = []

# add items to list
classmates.append('Sue')
classmates.append('Shad')
classmates.append('Mayank')
classmates.append('Gus')
classmates.append('Chin')
classmates.append('Eva')
classmates.append('Jeremy')
classmates.append('Dan')
classmates.append('Julian')
classmates.append('Aaron')
'''
#print(classmates[0])

#access an item at specific spot^

#size of list
#print(len(classmates))
print(classmates)
#remove an item from the end of the list
classmates.pop()

print(classmates)

#insert at a specific spot
classmates.insert(1, "Neha")
print(classmates)

#edit an item in the list
classmates[0] = "Sue Work"
print(classmates)
'''
'''
#iterate over a list
for classmate in classmates: 
    if(classmate == 'Gus'):
        print('Great, Gus is in the class!')

print(classmates)
'''

'''
#edit elements while iterating
for index, classmate in enumerate(classmates):
    classmates[index] = classmate.upper()

print(classmates)
'''

#create a list of all the marvel movies from Iron man to End Game 
#Go thru list and create a second list with the titles that have 'The' in their names

marvel_movies = ['Iron man', 'The Incredible Hulk', 'Iron Man 2', 'Thor', 'Captain America: The First Avenger', 'Marvel\'s The Avengers', 'Iron Man 3', 'Thor: The Dark World', 'Captain America: The Winter Soldier', 'Guardians of the Galaxy', 'Avengers: Age of Ultron', 'Ant-Man', 'Captain America: Civil War', 'Doctor Strange', 'Guardians of the Galaxy II', 'Black Panther', 'Infinity War', 'Ant-Man and the Wasp', 'Captain Marvel', 'Avengers: Endgame']
The_marvel_movies = []
'''
for movie in marvel_movies:
    if 'The' in movie:
        The_marvel_movies.append(movie)

print(The_marvel_movies)
'''
'''
#get index of list
for index in range(len(marvel_movies)):
        print(index)
'''
statement = "Hello world"
num = 10 

for num in range(num): 
    print(statement)