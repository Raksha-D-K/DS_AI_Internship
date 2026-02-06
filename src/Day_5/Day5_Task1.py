def cal_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
length=float(input("Enter a length:"))
width=float(input("Enter a width:"))    
area, perimeter = cal_rectangle(length, width)
print("Area:", area)
print("Perimeter:", perimeter)
