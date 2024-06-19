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


'''for loop special and break'''
#example 1
r_range = int(input('Enter range/sequence value (below 10)= '))
for i in range(10):
    if i == r_range:
        break
    else:
        print(i)

'''for keyword continue'''
#example 1
names: list[int] = ['Rahul', 'Sahil', 'Yash']

for nam in names:
    if nam == 'Yash':
        print(f'{nam} is Travel From Mehsana')
        continue
    print(f'{nam} is Travel from Gandhinagar')

'''for keyword delete''' #use to delete any object or variable
# print(names)
# del names
# print(names)

'''for keyword elif''' 
weather: list[int] = ['rainy', 'cloudy', 'sunny']
weather_select = str(input(f'Enter currunt weather from {weather} = '))

if weather_select == 'rainy':
    print('Please Take umbrella with you')
elif weather_select == 'cloudy':
    print('Please wear cloudcream')
elif weather_select == 'sunny':
    print('Please eat icecream')
else:
    print('entered weather is wrong')


'''for keyword _ (soft keyword)''' 
weather: list[int] = ['rainy', 'cloudy', 'sunny']
print(weather)
weather_select = str(input('Enter cur weather = '))

match weather_select:
    case 'rainy':
        print('Not Again, play with mud')
    case 'cloudy':
        print("Ohhh it's booring")
    case 'sunny':
        print("Roje roj moje moj!!!")
    case _:
        print("Hummmm go to sleep bro!")


exit ()
