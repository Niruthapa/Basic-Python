def greet_user():
    try:
        # Prompt the user for their name
        name = input("Please enter your name: ")
        
        # Check if the name is empty
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        
        # Print a greeting message
        print(f"Hello, {name}! Welcome!")
        
    except ValueError as e:
        # Handle the case where the input is invalid
        print(f"Error: {e}")

# Call the function
greet_user()