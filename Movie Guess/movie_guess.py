#Simple Movie Guessing Game

#importing libraries
from urllib.request import urlopen
import random

#introduction
print('Hello and welcome to the Movie Guessing game!')
print('You have to guess the name of the following movie. All your guesses should be either lower case alphabets or numeric')
print('Your can quit the game at any point by typing \'quit\' and hitting enter. You won\'t be evaluated if you do so')
print('Best of Luck!')

#importing movie names from a .txt file on Github
movies = urlopen('https://raw.githubusercontent.com/enilsen16/imdb-top-250/master/top_250.txt')

#Fixing the data

#Converting binary data to string
movie_list = []
for item in movies:
    movie_list.append(item.decode('utf-8'))    
    
#saving all movie names in a list, removing all \n characters in the raw file
temp=[]
for item in movie_list:
    temp.append(item.split('\n')[0])

#Removing the first line of the raw file, as it is not a movie name
temp.reverse()
temp.pop()

#Finally, saving the movie names in a list- removing all names with a length less than 3
movies = []
for item in temp:
    if len(item)>3:
        movies.append(item)

#Creating a list of valid characters to guess
valid_chars = [chr(y) for y in range(97, 124)]
for i in range(48, 58):
    valid_chars.append(chr(i))
for i in range(65, 91):
    valid_chars.append(chr(i))

#Now begins the fun part

replay=1
while replay==1:
    blank = ' _ '
    output=[]

    #Picking out a random movie from the list
    name = movies[random.randint(0,246)]        #I have passed (0,246) to the randint as there are 246 movies in the final list
    '''
    for item in n:
        name.append(item.split())
    '''
    #creating an output variable that will be displayed after each guess, it will show all the correctly guessed alphabets
    for i in range(0,len(name)):
        output.append(blank)                    
    for i in range(0,len(name)):
            if name[i] == ' ':
                output[i] = ' / '
            elif name[i] not in valid_chars:
                output[i] = name[i]
    temp_name = name.lower()    #this variable will make the game case-insensitive
    flag = 0
    score=0
    print("".join(output))    #since 'output' is a list, we have to use "".join() to print it as a string                  
    while flag == 0:
        score+=1    #score increases by 1 for each guess made
        guess = input('Your Guess : ')
        #checking if the player wants to quit the game
        if guess == 'quit':
            flag=2
            break

        #checking if the player made the correct guess
        for i in range(0,len(name)):
            if guess is temp_name[i]:
                if name[i].islower():
                    output[i] = guess
                elif name[i].isupper():
                    output[i] = guess.upper()
        print('\n\n')
        print("".join(output),'\n')
        #checking to see whether the player has guessed all alphabets in the movie name
        if ' _ ' not in output:
            flag = 1

    #Final message if the player won the game        
    if flag==1:
        print('\nCongratulations! You have guessed the movie name!')        
        print('\nCorrect Answer : ',name)
        print('You took {} guesses'.format(score))
        print('Your score : {:.2f}/100'.format((1-((score-len(name))/26))*100))
        
    #Final message if the player quit the game    
    elif flag==2:
        print('You quit the game\n')
        print('Correct Answer : ',name)

    replay = int(input('Do you want to play another round?\nYes- Type 1\nNo- Type 0'))
