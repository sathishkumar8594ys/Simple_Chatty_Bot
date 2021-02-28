number_of_halls = int(input().strip())
capacity = int(input().strip())
number_of_viewers = int(input().strip())

total_capacity = number_of_halls * capacity
print(number_of_viewers<=total_capacity)