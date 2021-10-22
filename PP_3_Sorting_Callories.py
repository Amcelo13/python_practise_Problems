#Basically we have to take input of elements of a list as input in sorted(increasing) way and reverse it by 3 method:
# 1.Inbuilt way of python revesinf
# 2.List-Slicing
# 3.Swapping first element with the last one and so on
lis = []
n = int(input('Enter the no. of food calories to be logged :'))        # Take the size of the list from the user

for i in range(n):
    inp_cal = int(input('Enter the calories in increasing order :'))   # Take the input from the user one by one
    lis.append(inp_cal)
# print(lis)      We have the list as a input now

print('Initially the list was :',lis,'\n')

                                    #Method - 1 ->Inbuilt function
lis1 = lis.copy()        #Making a the copies of the lis so that its own value won't change                                        
lis1.reverse()          
print('Reversing using inbuilt function :',lis1)

                                    #Method - 2 -> Slicing -List         
lis2 = lis.copy()[: : -1]      #IMP
print('Reversing using list slicing :',lis2)  

                                    #Method - 3 ->Swappping the first element with last and so on
lis3 = lis.copy()      
for i in range(len(lis3) // 2):      #No need to write 0   
#Now swapping the indices, first with last and so on with python signature trick 
      lis3[i] , lis3[len(lis3) -i -1] = lis3[len(lis3) -i -1] , lis3[i]
      print(f'reversed list at i={i} is {lis3}')

print('Reversing by swapping elements till mid-way :',lis3)      #It will run half only as i is going only till len(lis3) // 2

if lis1 == lis2 and lis2 == lis3:
    print('<-----------------------All reverse method has same answers----------------------->')