run_player1=int(input("Enter the run scored by player1 in 60 balls: "))
run_player2=int(input("Enter the run scored by player2 in 60 balls: "))
run_player3=int(input("Enter the run scored by player3 in 60 balls: "))
strikerate1=run_player1 * 100/60
strikerate2=run_player2 * 100/60
strikerate3=run_player3 * 100/60
print("Strike rate of player1 is",strikerate1)
print("Strike rate of player2 is",strikerate2)
print("Strike rate of player3 is",strikerate3)
print("Runs scored by player1 if they played 60 more balls is", run_player1*2)
print("Runs scored by player2 if they played 60 more balls is", run_player2*2)
print("Runs scored by player3 if they played 60 more balls is", run_player3*2)
print("Maximum number of sixes player 1 could hit =",run_player1 //6)
print("Maximum number of sixes player 2 could hit =",run_player2 //6)
print("Maximum number of sixes player 3 could hit =",run_player3 //6)
