"""
Lab 5
"""

#3.1
alien_color = "green"
if alien_color == "green": 
    print("the player earns five points")
    
#3.2
alien_color = "blue"
if alien_color == "green":
    print("the player earns five points")
else:
    print("the player earns ten points")

#3.3
favorite_fruits = {"apple", "pineapple", "strawberry"}
if "apple" in favorite_fruits:
    print("you are the apple of my eye")
if "pineapple" in favorite_fruits:
    print("if you like pina coladas")
if "strawberry" in favorite_fruits:
    print("strawberry fields forever")
    
#3.4
person_age = 24
if person_age<10:
    print("The person is a kid")
if person_age>65:
    print("The person is an elder")
elif person_age<=20:
    print("The person is a teenager")
else:
    print("The person is an adult")
