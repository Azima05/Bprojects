user_info = {}

user_info["name"] = input("Enter your name: ")

user_info["age"] = int(input("Enter your age: "))  

user_info["city"] = input("Enter your city: ")

user_info["has_pet"] = input("Do you have a pet? (yes/no): ").lower() == 'yes'  

print("\nUser Information:")
print(f"Name: {user_info['name']}")
print(f"Age: {user_info['age']}")
print(f"City: {user_info['city']}")
print(f"Has Pet: {user_info['has_pet']}")
