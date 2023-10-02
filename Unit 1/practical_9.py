# Write a menu driven python program which performs the following operations
'''
    1. find area of circle
    2. find area of triangle 
    3. find area of square
    4. find area of rectangle 
    5. exit
'''
import math

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area:.2f} square units")

def calculate_triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.2f} square units")

def calculate_square_area():
    side = float(input("Enter the length of a side of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area:.2f} square units")

def calculate_rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area:.2f} square units")

while True:
    print("\nMenu:")
    print("1. Find area of circle")
    print("2. Find area of triangle")
    print("3. Find area of square")
    print("4. Find area of rectangle")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        calculate_circle_area()
    elif choice == '2':
        calculate_triangle_area()
    elif choice == '3':
        calculate_square_area()
    elif choice == '4':
        calculate_rectangle_area()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")
