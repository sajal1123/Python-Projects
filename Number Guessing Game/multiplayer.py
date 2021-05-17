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
p2=Player(str(input("Enter Player 2 Name:")))
c=1
name1=p1.name
name2=p2.name
        
#Setting the difficulty of the game

print("Select the difficulty of the game:\n1)Low (0-9)\n2)Medium (0-99)\n3)High (0-999)")
diff=int(input())
if diff==1:
    l=9
elif diff==2:
    l=99
elif diff==3:
    l=999
else:
    print("Invalid input. Try again:")
    diff=int(input())
    
while c==1:
    import random
    a=random.randint(0,l)
    ctr=1
    p=2
    print("Player 1 turn:\n")
    print("Guess what number the computer has selected:")
    x=int(input())
    while 1:
        if x>a:
            print("Your guess is too high, player ",p," turn:")
            ctr+=1
        elif x<a:
            print("Your guess is too low, player ",p," turn:")
            ctr+=1
        else:
            print("Congratulations!You guessed right.")
            if p==1:
                p2.win()
                p1.display()
                p2.display()
            else:
                p1.win()
                p1.display()
                p2.display()    
            break
        if ctr%2==0:
            p=1
        else:
            p=2
        x=int(input())
    print("Another round?\n1)Yes\n2)No")
    c=int(input())
print("FINAL SCORE\n")
p1.display()
p2.display()
if p1.score>p2.score:
    print(name1+" WINS!")
elif p1.score<p2.score:
    print(p2.name+" WINS!")
    
    
