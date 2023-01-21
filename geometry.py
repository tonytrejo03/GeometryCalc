# Tony Trejo
# Calculates the area and perimeter of cricles and rectangles according
# to what the user chooses from menu


import math

def calc_circle_area(radius):
    area = math.pi * radius * radius
    return area

def calc_circle_permin(radius):
    return 2 * math.pi * radius

def calc_rect_area(length,width):
    return length * width

def calc_rect_perim(length,width):
    return 2 * (length + width)

def print_banner_block(width,message):
    print("-"*width)
    print(message.center(width))
    print("-"*width)
    print()
    
def print_welcome():
    print_banner_block(60,"Geometry Calculator V1.0")
    print("This program is a menu-driven application that computes the")
    print("area and perimeter of circles and rectangles. It is high-tech.")
    print()

def print_goodbye():
    print("-"*60)
    print("Thank you for using this program.".center(60))
    print("-"*60)

def print_menu():
    print("Here are your choices: ")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Exit")
    
# main

print_welcome()
choice = 0
while choice != 3:
    print_menu()
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        radius = float(input("Enter the radius: "))
        area = calc_circle_area(radius)
        circ = calc_circle_perim(radius)
        print("the area is %.2f and the circumfernce is %.2f." % (area, circ))
    elif choice == 2:
        length = float(input("Enter the length: "))
        width = float(input("enter th3 width: "))
        area = calc_rect_area(length,width)
        permin = calc_rect_permin(length,width)
        print("The area of the rectangle is %.2f and the perimeter is %.2f." % (area, permin)



print_goodbye()
