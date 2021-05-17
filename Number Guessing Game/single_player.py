
class Player():
    def __init__(self,name,score=0):
        self.name=name
        self.score=score
    def win(self):
        self.score+=1
    def display(self):
        print(f"{self.name}-{self.score}")
print("Welcome to the Guessing Game")

#Setting up player names
        
p1=Player(str(input("Enter Player 1 Name:")))
c=1
name1=p1.name
        
#Setting the difficulty of the game
while c==1:    
    turns=1
    print("Select the difficulty of the game:\n1)Very Easy\n2)Easy\n3)Medium\n4)High\n5)Very High\n")
    diff=int(input())
    if diff==1:
        l=9
    elif diff==2:
        l=99
    elif diff==3:
        l=999
    elif diff==4:
        l=9999
    elif diff==5:
        l=99999
    else:
        print("Invalid input. Try again:")
        diff=int(input())
        
    #selecting a random integer from the given range based on difficulty level    
    
    import random
    a=random.randint(0,l)   
    
    #Taking input from the player and evaluating his guess
    
    ctr=1
    print(f"Guess what number the computer has selected:(Range:0-{l})")
    x=int(input())
    while 1:
        if x>a:
            print("Your guess is too high, try again:")
            ctr+=1
            x=int(input())
            turns+=1
        elif x<a:
            print("Your guess is too low, try again:")
            ctr+=1
            x=int(input())
            turns+=1
        else:
            print("You guessed correctly!")
            p1.win()
            p1.display()
            print(f"Turns taken:{turns}")
            break
    print(f"Do you want to play again {name1}?\n1)Yes\n2)No")
    c=int(input())

#Displaying player's final score

print("FINAL SCORE\n")
p1.display()
print(f"Well played {name1}.") 
