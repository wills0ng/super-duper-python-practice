# 1 - Lists
# Create a list 'movies' that contains the names of at least six movies you like
fav_movies = ["John Wick", "John Wick 2", "John Wick 3", "The Dark Knight", "Tenet", "Interstellar"]
print(fav_movies)

# Use slicing, and create a list of three first movies in the list
top_three = fav_movies[:3]
print(top_three)

# Use slicing and list concatenation to create a list of the first two and the last two movies
mod_list = fav_movies[:2] + fav_movies[-2:]
print(mod_list)
print()

# 2 - Loops
# Create a list 'numbers' that is the numbers 70 through 79 in the following manner: create an empty list
# and add numbers to it in a loop (do not use list comprehension or 'list' function here!)
# Approach 1: While loop with a break
numbers = []
i = 70
while True:
    numbers.append(i)
    i += 1
    if i >= 80:
        break
print(numbers)
print()

# Approach 2: While loop with a condition that changes
numbers = []
i = 70
while i < 80:
    numbers.append(i)
    i += 1
print(numbers)
print()

# Approach 3: For loop over a sequence
numbers = []
for i in range(70,80):
    numbers.append(i)
print(numbers)
print()

# Approach 4: Doing what I'm not supposed to be doing
mylist = (list(range(70, 80)))
print(mylist)
print()

# 3 - Comprehensions
# Use list comprehension to create a list of squares of numbers 1..10 (i.e. 1, 4, 9, ..., 100)
squares_list = [i**2 for i in range(11)]
print(squares_list)
print()

# Use dict comprehension to create a dict of numbers 1..10 and their squares (i.e. 1:1, 2:4, ..., 10:100).
squares_dict = {i: i**2 for i in range(1, 11)}
print(squares_dict)
print()

# 4 - Functions
# Write a function that takes in time in the numeric form (i.e. not a string) of HHMM (hours-minutes, and
# returns it in the numeric form of HH.HH (hours + fractions of hours). For instance, 1015 -> 10.25 (
# 10 hrs 15 mins -> 10.25 hrs)). Demonstrate it works using values 1015 and 345.
# The function should return (not print) the result as a number.
# Hint: use modulo operator % and integer division operator //. Modulo of 100 gives you minutes and integer
# division by 100 gives you hours

def to_hour_frac(hhmm_numeric):
    hours = hhmm_numeric // 100
    minutes = hhmm_numeric % 100
    fraction = minutes / 60
    return hours + fraction

print(to_hour_frac(1015))
print(to_hour_frac(345))
print()
