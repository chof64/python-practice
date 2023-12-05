
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

while not user_age.isdigit():
  print("Please enter a number.")
  user_age = input("Enter your age: ")

user_age = int(user_age)


print("Hello, " + user_name + "!")
print("You are", user_age, "years old.")

def check_age(age):
  if age < 18:
    return print("You are not old enough to vote.")
  if age == 18:
    return print("You are just old enough to vote.")
  return print("You are old enough to vote.")

check_age(user_age)
