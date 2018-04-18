# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    # Oswaldo: Changed to return each row as a dictionary instead of list
    reader = csv.DictReader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Oswaldo: Now the first...
# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Oswaldo: ...and the second rows display column and data as key and value as all other rows, since it's a dictionary
# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# Let's change the data_list to remove the header from it.
# Oswaldo: I commented the line of code below because it's no longer necessary since I'm using a dictionary
# data_list = data_list[1:]

for index in range(20):
    print(data_list[index])

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")
for index in range(20):
    if data_list[index]['Gender']:
        print(data_list[index]['Gender'])
    else:
        print('--')
# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")


# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """
    Function to add the columns of a list in another list in the same order.
    Args:
      data: List of data.
      index: Column name.
    Returns:
      List with the columns of a list in the same order

    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for sample in data:
        column_list.append(sample[index])
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, 'Gender')[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, 'Gender')) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, 'Gender')) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, 'Gender')[0] == "" and column_to_list(data_list, 'Gender')[
    1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

for sample in data_list:
    if sample['Gender'] == 'Male':
        male += 1
    elif sample['Gender'] == 'Female':
        female += 1
# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")


# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    Function to count the genders.
    Args:
      data_list: List of data from spreadsheet.
    Returns:
      List with the totals of male and female

    """
    male = 0
    female = 0
    for sample in data_list:
        if sample['Gender'] == 'Male':
            male += 1
        elif sample['Gender'] == 'Female':
            female += 1
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")


# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    Function to get the most popular gender.
    Args:
      data_list: List of data from spreadsheet.
    Returns:
      Most popular gender from the list

    """
    users_by_gender = count_gender(data_list)
    if users_by_gender[0] > users_by_gender[1]:
        answer = "Male"
    elif users_by_gender[0] < users_by_gender[1]:
        answer = "Female"
    else:
        answer = "Equal"

    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, "Gender")
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")


def count_user_type(data_list):
    """
    Function to count user types registers.
    Args:
      data_list: list containing user type records.
    Returns:
      List with subscriber, customer and dependent count

    """
    subscriber = 0
    customer = 0
    dependent = 0
    for sample in data_list:
        if sample['User Type'] == 'Subscriber':
            subscriber += 1
        elif sample['User Type'] == 'Customer':
            customer += 1
        elif sample['User Type'] == 'Dependent':
            dependent += 1
    return [subscriber, customer, dependent]


user_type_list = column_to_list(data_list, "User Type")
user_type_types = ["Subscriber", "Customer", "Dependent"]
user_type_quantity = count_user_type(data_list)
user_type_y_pos = list(range(len(user_type_types)))
plt.bar(user_type_y_pos, user_type_quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(user_type_y_pos, user_type_types)
plt.title('Quantity by User Type')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because there are some rows with the unfilled genre."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, "Trip Duration")
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
total_trip_duration = 0.

# Oswaldo: iterate the list to find min, max and total trip values
for trip_duration in trip_duration_list:
    if float(trip_duration) < min_trip or min_trip == 0:
        min_trip = float(trip_duration)
    elif float(trip_duration) > max_trip or max_trip == 0:
        max_trip = float(trip_duration)
    total_trip_duration += float(trip_duration)

mean_trip = total_trip_duration / (len(trip_duration_list) - 1)

# Oswaldo: convert the list elements to float
trip_duration_list = list(map(float,trip_duration_list))

list_len = len(trip_duration_list)
list_sorted = sorted(trip_duration_list)

# Oswaldo: calculation to get the median value...
if list_len % 2 == 0:  # ...if it's even...
    median_trip = (list_sorted[int((list_len / 2))] + list_sorted[int((list_len / 2) + 1)]) / 2.0
else: # ...or if it's odd
    median_trip = list_sorted[int(((list_len + 1) / 2))]

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
start_stations = set(column_to_list(data_list, "Start Station"))

print("\nTASK 10: Printing start stations:")
print(len(start_stations))
print(start_stations)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(start_stations) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
  param1: The first parameter.
  param2: The second parameter.
Returns:
  List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"


def count_items(column_list):
    """
    Function to count user types.
    Args:
      column_list: The list with user types.
    Returns:
      The user types and count of each type.

    """
    item_types = []
    count_items = []

    for user_type in column_list:
        if user_type not in item_types:
            item_types.append(user_type)
            count_items.append(1)
        else:
            index = item_types.index(user_type)
            count_items[index] += 1

    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, "Gender")
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
