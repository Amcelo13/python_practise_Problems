'''Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!
So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
Note: Rohan’s function returns a list of numbers like this
Rohan Das’s Function Input:
rohanMultiplication(6)

Rohan’s function returns this output:
[6, 12, 18, 26 ,..., 60]'''
import random

def rohanMultiplication(number):
    wrong_index = random.randint(0 ,9)        #Lets take a random index that is to be 
    table = [i*number for i in range(1 ,11)]  #Table indices 1 to 10
    #Now lets spoil the table by adding some random integer in the wrong_indx ,index of the table
    table[wrong_index] = table[wrong_index] + random.randint(0 ,10)
    return table

def is_Correct(table ,number):     #Passing the whole table as argument and the number also.
    for index in range(1 ,11):
        if table[index - 1] != (index*number):    #Means if the indices doesn'nt match i*number here : the return that flawed index
            return (index - 1)

    return None   #If list is shi 
if __name__ == '__main__':
    
     num = int(input('Enter a number whose table is required :'))
     myTable = rohanMultiplication(num)
     print(myTable)   #Stores a table

     wrongIndex = is_Correct(myTable ,num)
     print('The table is wrong at :', wrongIndex)