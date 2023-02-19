lang = input("What's the programming language you want to learn? ")
match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

        
vehicle = input("Enter the vehicle slogan")
match vehicle:
    case "Tata":
        print("connecting aspirations, Driver your own car")
    case "Fiat":
        print("Driven by passion")
    case "Kia":
        print("Movement that inspries")
    case "Renault":
        print("Passion for life, capture your senses")
    case "Toyoto":
        print("Let's go places")
    case "Honda":
        print("The power of dreams")
        
        