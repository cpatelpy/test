courses = ['rahul', 'Math', 'Physics', 'CompSci']
popped_subs = courses.pop(-1)
print(popped_subs)

'''if condition special'''
#example 1
a, b, c = 1, 2, 3
if c > b and c > a:
    print('Both conditions are True! Enjoy!')
else:
    print('Both conditions are False! Do some thing!')

#example 2
name = input('Please Enter Your Name = ')
age = input('please enter Your Age! = ')
age_val = int(age)

if len(name) > 0 and age_val > 18:
    print('User is eligible to Drink!!!')
else:
    print('Please Go to Home!')

exit ()
