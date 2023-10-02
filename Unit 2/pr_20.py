# write a program to create a dictionary from the user and display the elements

# Initialize an empty dictionary
user_dict = {}

# Prompt the user to enter key-value pairs
while True:
    key = input("Enter a key (or 'exit' to finish): ")
    
    # Check if the user wants to exit
    if key.lower() == 'exit':
        break
    
    value = input("Enter a value: ")
    
    # Add the key-value pair to the dictionary
    user_dict[key] = value

# Display the dictionary
print("\nDictionary created by the user:")
for key, value in user_dict.items():
    print(f"{key}: {value}")
