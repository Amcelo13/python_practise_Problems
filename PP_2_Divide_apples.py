'''Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. 
These “n” number of apples is provided to his friends, and he can request for few more or few less apples.
You need to print whether a number is in range mn to mx, is a divisor of “n” or not.
Input:
1.Take input n, mn, and mx from the user.
Output: Print whether the numbers between mn and mx are divisor of “n” or not. 
If mn=mx , show that this is not a range, and mn is equal to mx. Show the result for that number.
Example:
If n is 20 and mn=2 and mx=5
2 is a divisor of20
3 is not a divisor of 20
5 is a divisor of 20'''

apples = int(input('Enter the no. of apples :'))
min = int(input('Enter the minimum no. to check :'))  #These are min no. of friends
max = int(input('Enter the maximum no. to check :'))  #These are max no. of friends

if min >= max :
    print('This is not allowed max should only be like max > min')
for i in range( min , max + 1):
    if apples%i == 0:
        print(f'{i} is a divisor of {apples}')
    else:
        print(f'{i} is not a divisor of {apples}')   

print('<-----------------------------------Commenters solution--------------------------------->') 
try:       
    apples = int(input('Enter the no. of apples :'))
    min    = int(input('Enter the minimum no. to check :'))
    max    = int(input('Enter the maximum no. to check :'))

except ValueError as e:               #Using ValueError as if value is not int it shows except statement
    print('Enter integers only')   
    exit() 

if min >= max:
    print('This is not allowed max should only be like max > min ')

for i in range(min ,max + 1):
   if apples%i == 0:
        print(f'{i} is a divisor of {apples}')
   else:
        print(f'{i} is not a divisor of {apples}')  
