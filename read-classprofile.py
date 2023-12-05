with open("./class-profile.txt", "r") as file:
  contents = file.read()

classProfile = eval(contents)

for profile in classProfile:
  print("Name: " + profile["Name"])
  print("Age: " + str(profile["Age"]))
  print("Location: " + profile["Location"])
  print("Course: " + profile["Course"])
  print("Year: " + str(profile["Year"]))
  print("Section: " + profile["Section"])
  print("=============")
