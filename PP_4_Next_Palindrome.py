'''A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
676, 616, mom, 100001.
You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. 
Your <first input should be the number of test cases> and then <take all the cases as input from the user>.
Input:
3
[451
10
2133]
Output:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
Next palindrome for 2311 is 2222'''

def next_palindrome(n):  #say(21)
    n = n+1       #say(22)   #A number comes here increment by 1 and if not -> satisfy is_palindrome function then run a while loop ..add()

    while not is_a_palindrome(n):  #(22) will be in/satisy is_palindrome so while loop will not work here      
        n += 1   #It will incerement the number till it satisfy the is_palindrome function .

    return n    #(22) is returned as next_palindrome  
    
def is_a_palindrome(n):
    return str(n) == str(n)[::-1]  #Means returns bool

if __name__ == '__main__':
    no_of_test = int(input('Enter the number of test cases :'))
    li = []

    for i in range(no_of_test):  #This loops is for filling cases/elements in the lists
        inp = int(input('Enter a number whose next consecutive palindrome is to be found :'))
        li.append(inp)
    print(li)   

    for i in range(no_of_test):    
        #This loop is for printing the elements and their next palindromes by calling the next_palindrome functions
        print(f"Next palindrome for {li[i]} is => {next_palindrome(li[i])}")