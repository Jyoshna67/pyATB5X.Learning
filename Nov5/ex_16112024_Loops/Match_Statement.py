#It is similar like "Switch" in java.
#Write a program to ask the user which browser he wants to run automation

browser_Name=input("Enter Browser Name:")
match browser_Name:
    case "firefox" :
print("Starting Firefox!")
case "chrome":
        print("Starting Chrome!")
        case "safari":
print("Starting Safari!")
case "opera":
print("Starting Opera!")
case _:
print("Browser Not Found!")
