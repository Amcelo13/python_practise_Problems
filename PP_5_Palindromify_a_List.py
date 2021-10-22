'''You are given a list that contains some numbers. 
You have to print a list of next palindromes only 
if the number is greater than 10;
 otherwise, you will print that number as it is.

Input:
[1, 6, 87, 43]
Output:
[1, 6, 88, 44]'''

def next_palindrome(n):  #say(21)
    n = n+1       #say(22)   #A number comes here increment by 1 and if not -> satisfy is_palindrome function then run a while loop ..add()

    while not is_palindrome(n):  #(22) will be in/satisy is_palindrome so while loop will not work here      
        n += 1   #It will incerement the number till it satisfy the is_palindrome function .
    return n    #(22) is returned as next_palindrome  
    
def is_palindrome(n):
    return str(n) == str(n)[::-1]                  

if __name__ == '__main__':

    size = int(input('Enter the number of test cases :'))
    li = []

    for i in range(size):  #This loops is for filling cases/elements in the lists
        inp = int(input('Enter a number whose next consecutive palindrome is to be found :'))
        li.append(inp)
    print(f"You have entered {li}")

    New_list = []
    for item in li:
        if item > 10:          #If greater than 10 then find its next palindrome by calling the function and storing it in 'a'
            a = next_palindrome(item)  
            New_list.append(a)   #Appending n in New_list
        else:
            New_list.append(item)    
print('Output list :',New_list)

# METHOD - 2 -> Or we  can do this by |Python comprehension also|

'''from Line - 30 we write'''

# list comprehension returns a list
print(f"Output list :{[li[i] if li[i] < 10 else next_palindrome(li[i]) for i in range(size)]}")