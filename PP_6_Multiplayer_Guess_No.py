'''Generate a random integer from a to b. 
You and your friend have to guess a number between two numbers a and b. 
a and b are inputs taken from the user. 
Your friend is player 1 and plays first. 
He will have to keep choosing the number and your program must tell whether the number is greater than the actual number or less than the actual number. 
Log the number of trials it took your friend to arrive at the number. 
You play the same game and then the person with minimum number of trials wins!
Randomly generate -># actual number after taking a and b as input and don’t show that to the user.'''
import random
# import cowsay
# cowsay.daemon('Hi Daemon')

def guessGame(a ,b ,actual_no):
    guess = int(input(f'Guess a no. between {a} and {b} :'))
    no_of_guesses = 1

    while guess != actual_no:  #Means jab tak 'guess' same na ho 'actual_no ke' tabb takk chlega  
         if guess < actual_no:
             guess = int(input('Enter a greater no. :'))
             no_of_guesses += 1    
         else:
             guess = int(input('Enter a smaller no. :'))    
             no_of_guesses += 1
  # If guess == actaul_no then while loop will stop or won't even start if in starting they are equal
    print(f'<------You guessed the number in {no_of_guesses} guesses---------->')         
    return no_of_guesses

if __name__ == '__main__':

   a = int(input('Enter the min of range :'))
   b = int(input('Enter the max of range :'))
   actual_1 = random.randint(a ,b)

   print('Player 1 Turn !')
   g1 = guessGame(a ,b ,actual_1)        #  Returned value of no_of_guesses is stored  in g1

   actual_2 = random.randint(a ,b)     
   print('Player 2 Turn !')
   g2 = guessGame(a ,b ,actual_2)         #  Returned value of no_of_guesses is stored  in g2

   if g1 < g2:  #Means player 2 take more tries
       print('Player 1 Won !')
   elif g1 > g2:
       print('Player 2 Won !')
   else:
       print('Its a Tie')

   print(f'The actual no for Player 1 was => {actual_1} and for Player 2 was => {actual_2}')   