# It is similar like "Switch" in java.
# Write a program to ask the user which browser he wants to run automation

browser_name = input("Enter Browser Name:")
match browser_name:
    case "Firefox":
print("Starting Firefox!")
case  "chrome":
print("Starting Chrome!")
case "safari":
print("Starting Safari!")
case "opera":
print("Starting Opera!")
case_:
print("Browser Not Found!")
