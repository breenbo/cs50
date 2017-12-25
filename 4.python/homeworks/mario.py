#  print a mario pyramid

height = input("Height : ")
# change string to int
height = int(height)

print("")
for space in range(height-1, -1, -1):
    dash = height - space
    line = space * " " + dash * "#" + "  " + dash * "#"
    print(line)

