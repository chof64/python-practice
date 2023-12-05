classProfile = []

isContinue = True

print("Welcome to Class Profile!")

while isContinue:

  print("Enter your profile information")

  name = input("Enter your name: ")
  age = input("Enter your age: ")
  location = input("Enter your location: ")
  course = input("Enter your course: ")
  year = input("Enter your year: ")
  section = input("Enter your section: ")

  while not age.isdigit():
    print("Please enter a number.")
    age = input("Enter your age: ")
  age = int(age)

  while not year.isdigit():
    print("Please enter a number.")
    year = input("Enter your year: ")
  year = int(year)

  classProfile.append({
    "Name": name,
    "Age": age,
    "Location": location,
    "Course": course,
    "Year": year,
    "Section": section
  })

  continueInput = input("Do you want add another profile? (Y/N): ")
  if continueInput == "N":
    isContinue = False
    break


print("Class Profile")
print(classProfile)
print("=============")
for profile in classProfile:
  print("Name: " + profile["Name"])
  print("Age: " + str(profile["Age"]))
  print("Location: " + profile["Location"])
  print("Course: " + profile["Course"])
  print("Year: " + str(profile["Year"]))
  print("Section: " + profile["Section"])
  print("=============")
