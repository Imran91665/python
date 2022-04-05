print("Rock")
print("paper")
print("Scissors")
print("Welcome to gaming world......")
p1=input("player1: ")
p2=input("player2: ")
def check_winner(p1,p2):
    if p1=="rock" and p2=="scissor":
        print("player1 wins")
    elif p1=="rock" and p2=="paper":
        print("player2 wins")
    elif p1=="paper" and p2=="scissor":
        print("player2 wins")
    elif p1=="paper" and p2== "rock":
        print("player1 wins")
    elif p1=="scissor" and p2=="rock":
        print("player2 wins")
    elif p1=="scissor" and p2=="paper":
        print("player1 wins")
    else:
        print("The match is tied")    

result=check_winner(p1,p2)
print(result)                       