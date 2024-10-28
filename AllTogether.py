### Part Four -- your code goes here. 
import random                                                  ### inport random library
variables = [random.randint(1,100) for None in range(10)]      ### generates 10 random number variable's
checker = 0                                                    ### starts at 1st generated variable
while checker < len(variables):                                ### while there are more variables in the list then the checking variable loop
 if variables[checker] % 2 == 0:                               ### if variable divisable by 2 (even)
    variables.pop(checker)                                     ### pop (delete variable)
 else:                                                         ### if not divisable by 2 (odd)
    checker += 1                                               ### go too the next generated variable
print("List:", variables)                                      ### prints the list of variable's