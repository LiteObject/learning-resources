number = 9
guess_count = 2

while guess_count > 0:
  guess = int(input("Enter your guess:  "))
  if guess != number:
  
    if guess_count > 1:
    
      print("Wrong! You can try " + str(guess_count - 1) + " more time")
    else:
      print("You have failed! No more attempts left.") 
  
    guess_count = guess_count - 1 
  else: 
    print("Correct!")
    guess_count = 0