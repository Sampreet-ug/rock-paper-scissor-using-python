import random

hands = ["rock","paper","scissors"]

play = int(input("Enter the number of plays : "))

ppoints = 0
cpoints = 0
while play != 0:
    player_hand = input("Enter your choice (rock, paper, scissors) : ").lower()
    cpu_hand = hands[random.randint(0,2)]
    print(">>CPU chose "+cpu_hand)
    if((player_hand == "rock" and cpu_hand == "scissors") or (player_hand == "scissors" and cpu_hand == "paper") or (player_hand == "paper" and cpu_hand == "rock")):
        ppoints+=1
        print(">>You won one point \n >>Player points :",ppoints)
        print(">>CPU points :",cpoints)
        print("-----------------------------------------------\n")
    elif((cpu_hand == "rock" and player_hand == "scissors") or (cpu_hand == "scissors" and player_hand == "paper") or (cpu_hand == "paper" and player_hand == "rock")):
        cpoints+=1
        print(">>CPU won one point \n >>Player points :",ppoints)
        print(">>CPU points : ",cpoints)
        print("-----------------------------------------------\n")
    else:
        print(">>Draw! Nobody gets a point")
        print(">>CPU won one point \n >>Player points :",ppoints)
        print(">>CPU points : ",cpoints)
        print("-----------------------------------------------\n")
    play-=1

print("You won the match") if ppoints > cpoints else print("CPU won the match")
