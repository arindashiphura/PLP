# Ask user to input numbers separated by spaces
user_input = input("Enter integers separated by spaces: ")

# Convert input string to a list of integers
numbers = [int(num) for num in user_input.split()]

# Calculate the sum
total = sum(numbers)

print("The sum of the integers is:", total)



# Create a tuple with 5 favorite books
favorite_books = ("The Alchemist", "1984", "To Kill a Mockingbird", "Harry Potter", "The Hobbit")

# Print each book name on a new line
for book in favorite_books:
    print(book)



# Create an empty dictionary
person_info = {}

# Ask user for input
person_info["name"] = input("Enter your name: ")
person_info["age"] = input("Enter your age: ")
person_info["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print("Person Information:", person_info)



# Get input for set 1
set1_input = input("Enter integers for Set 1 (separated by spaces): ")
set1 = set(map(int, set1_input.split()))

# Get input for set 2
set2_input = input("Enter integers for Set 2 (separated by spaces): ")
set2 = set(map(int, set2_input.split()))

# Find common elements
common_elements = set1.intersection(set2)

print("Common elements:", common_elements)



# List of words
words = ["apple", "banana", "cat", "dog", "elephant", "fish"]

# Create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Words with odd number of characters:", odd_length_words)
