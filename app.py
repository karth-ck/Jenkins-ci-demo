def greet(name):
    return f"Hello, {name}!"

# Call function directly
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)
