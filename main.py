from ascii_art import logo
import random
# Step 1 - Ask the player to enter first 5 numbers between 1 and 69
#print(logo)
while True:
  print("Please provide 5 numbers between 1 and 69 with space in between:")
  input_string=input("> ")
  input_list=list(input_string.split())
  #TODO 1 - Check that the player entered 5 things
  if len(input_list)!=5:
    print("Please enter 5 numbers!")
    continue
  #TODO 2 - Convert the strings into integers
  try:
    for i in range(5):
      input_list[i]=int(input_list[i])
  except ValueError:
    print("Please enter numbers, like 4, 6, 29 etc.")
  #TODO 3 - Check that the numbers are between 1 and 69
  between_1_69=True
  for item in input_list:
    if not( 1<= item <= 69):
      print("Please enter numbers between 1 and 69!")
      between_1_69=False
      break
  if not between_1_69:
    continue
  
#TODO 4 - Check that the numbers are unique
  newset=set(input_list)
  if len(newset)!=5:
    print("please provie 5 unique numbers!")
    continue
  break

## Step 2 - Ask the player to select the powerball between 1 to 26
while True:
  print("Enter the power ball number between 1 and 26.")
  response=input("> ")
  try:
    powerball=int(response)
  except ValueError:
    print("Please enter a number, like 5, 10 20 etc.")
    continue
  if not( 1<= powerball <=26):
    print("Please enter numbers between 1 and 26!")
    continue
  break
## Step 3 - Enter the number of times you want to play
while True:
  print("How many times do you want to play this game? (1 to 1000000)")
  user_time=input("> ")
  try:
    times=int(user_time)
  except ValueError:
    print("Please enter a numeric number!")
    continue
  if not (1<= times <= 1000000):
    print("Please enter a value between 1 and 1000000!")
    continue
  break

## Step 4 - Run the simulation
price="$" + str(2*times)
print(f"It cost {price} to play {times} times, but don't\nworry, I'm sure you will win it all back.")
print("Press Enter to start...")
possibleNumbers=list(range(1,70))
for i in range(times):

  random.shuffle(possibleNumbers)
  winningNumbers=possibleNumbers[0:5]
  winningpowerball=random.randint(1,26)
  #display winning numbers
  print("The winning numbers are: ", end="")
  allWinningNumbers=""
  for num in winningNumbers:
    allWinningNumbers+=str(num) + " "
  allWinningNumbers+="and "+ str(winningpowerball)
  print(allWinningNumbers, end="")
  #check for winner
  if set(input_list)==set(winningNumbers) and powerball==winningpowerball:
    print("You have won the powerball lottery! Congratulations!")
    break#need to exit game after winning
  else:
    print("You lost!")
print(f"You have wasted {price}")
print("Thanks for playing.")