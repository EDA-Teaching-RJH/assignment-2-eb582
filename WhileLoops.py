### Part Two -- your code goes here. 
import random                                                                   ### inport random library
random_num = random.randint(1,100)                                              ### random number 1-100 generator
user_guess = None                                                               ### user guess variable
print("Welcome to the guessing game!","Guess a number between 1 and 100.")      ### welcoming propmt
while user_guess != random_num:                                                 ### loop that keeps going as long as they dont get the answer
    user_guess = int(input("Enter your guess: "))                               ### input to guess
    if user_guess == random_num:                                                ### correct answer condition
       print("Correct the number was: ",random_num)                             ### GUI Correct answer                                                              
    elif user_guess < random_num:                                               ### too low answer condition
      print("Too Low!","Try Again: ")                                           ### print too low propmts another attempt
    elif user_guess > random_num:                                               ### too high answer condition
      print("Too High!","Try Again: ")                                          ### print too low propmts another attempt
       
