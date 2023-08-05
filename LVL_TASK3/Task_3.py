import random as r
def game(users,comps):
    user=users
    comp=comps
    print("\n user Selected: ",user)
    print("\n computer Selected: ",comp)
    if user==comp:
        print("************tie************")
    if comp=="rock":
        if user=="paper":
            print("************User won the game************ ")
        elif user=="scissors":
            print("************you lost the game,Computer won the game************")
    if comp=="paper":
        if user=="rock":
            print("************you lost the game,Computer won the game************")
        elif user=="scissors":
            print("************User won the game************ ")
    if comp=="scissors":
        if user=="rock":
            print("************User won the game************ ")
        elif user=="paper":
            print("************you lost the game,Computer won the game************")
       
def user_input():
    print("==========GAME:Rock Paper Scissors==========")
    i=1
    while(i==1):
        games=["Rock","Paper","Scissors"]
        user=input("Enter Your Choice(Rock,Paper,Scissors):").lower()
        comp=r.choice(games).lower()
        game(user,comp)
        i=int(input("\n Enter the Choice (1 to continue):"))

user_input()
print("-----Game Ended---------")        
        
    
    

    
        
    


        
    
    
