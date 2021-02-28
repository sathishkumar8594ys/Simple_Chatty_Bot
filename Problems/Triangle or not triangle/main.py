def is_triangle(a, b, c):
    sum_of_angle = a + b + c
    print("The triangle is valid!" if sum_of_angle == 180 else "The triangle is not valid!")

is_triangle(int(input()), int(input()), int(input()))