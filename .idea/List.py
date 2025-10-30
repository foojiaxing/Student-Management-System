# Question 1
# Create a list of 5 different fruits.
list = ["Apple", "Banana", "Cherry", "Orange", "Kiwi"]
print(list)

# Convert the list into a tuple and display the tuple.
list = ["Apple", "Banana", "Cherry", "Orange", "Kiwi"]
my_tuple = tuple(list)
print(my_tuple)

# Uses a dictionary to map fruits to their colours
fruits_colour = {"Apple":"Red", "Banana":"Yellow", "Cherry":"Red",
                 "Orange":"Orange", "Kiwi":"Green"}

# Print the dictionary
print(fruits_colour)

# Question 2
# Create a list of 10 numbers
list = [1,2,3,4,5,6,7,8,9,10]

# Find the largest and smallest numbers in the list.
largest = max(list)
smallest = min(list)
print(largest)
print(smallest)

# Remove the last number from the list
list.remove(10)

# Add a new number to the beginning of the list - insert (beginning); append (end)
list.insert(0,5)

# Print the final list.
print(list)


# Question 3
# Create a tuple containing 5 names of cities.
cities = ("Paris", "London", "Tokyo", "Paris", "New York")

# Access the second and fourth cities from the tuple and print them.
second_city = cities[1]
fourth_city = cities[3]
print("second_city:", second_city)
print("fourth_city:", fourth_city)

# Check if a city (e.g., "Paris") is in the tuple and print the result.
if "Paris" in cities:  # paris need to be in quo, because is a string
    print("Yes, Paris is in the list")

# Count how many times a specific city appears in the tuple - count
city_count = cities.count("Paris")
print("How many time Paris appear in the list")


# Question 4
# Create a dictionary with 5 key-value pairs where keys are names of countries,
# and values are their capitals.
countries_capitals = {"United States":"Washington,D.C.", "France":"Paris",
                      "Japan":"Tokyo", "China":"Beijing", "Malaysia":"Kuala Lumpur"}

# Add two more countries and their capitals to the dictionary.
countries_capitals["Italy"] = "Rome"
countries_capitals["Germany"] = "Berlin"
print(countries_capitals)

# Remove one country from the dictionary - pop
countries_capitals.pop("Malaysia")
print(countries_capitals)

# Check if a specific country (e.g., "Germany") exists in the dictionary.
if "Japan" in countries_capitals:
    print("Yes, Japan is exits in the dictionary")

# Print the keys and values of the dictionary separately.
# Print the keys
print("Keys (Countries):")
for country in countries_capitals.keys():  # When u want to loop through all items in a collection like list and dict
    print(country)

# Print the values
print("\nValues (Capitals):")
for country in countries_capitals.values():  # When u want to loop through all items in a collection like list and dict
    print(country)
