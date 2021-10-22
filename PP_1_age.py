# Take [age] or [year] of birth as an input from the user. Store the input in one variable. 
# Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old.
# Here are a few instructions that you must have to follow:=>
# Do not use any type of modules like DateTime or date utils. 
# Users can optionally provide a year, and your program must tell their age in that particular year. 
# Your code should handle all sort of errors like:                   
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!
yearAge = int(input('What is is your Age/YOB :'))
isAge =  False
isYear = False
#Taking both age and year False by default and if inp_length ==4 then if statement ,nhi to else wali
if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if (isYear and yearAge < 1900):          #Means following the -> if statement.
    print('You seem to be the oldest person alive')
    exit()
if (yearAge > 2021 or yearAge < 0):
    print('You are not born yet or not valid input')
    exit()
if (isAge):           #Basically if age = 20 years we are just making it -> YOB by -> earAge = 2021 - yearAge   
    yearAge = 2021 - yearAge        

print(f'You will be 100 years old on : {yearAge + 100}')

# Next part =>
custom_year = int(input('Enter the custom year u want to know the age at :'))
print(f'You will be {custom_year - yearAge} yrs old in {custom_year}')