# Print a table
"""
table = 9
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")
print(f"{table}*5={table*5}")
print(f"{table}*6={table*6}")
print(f"{table}*7={table*7}")
print(f"{table}*8={table*8}")
print(f"{table}*9={table*9}")
print(f"{table}*10={table*10}")
"""
# Print a table using loop
# get user input
num = int(input("enter the number for which you want to print the table= "))
print(f"multiplication table for {num}:\n")
for i in range(1, 11):  # it print upto -1, if we have taken 11 it will print upto 10
    result = num * i
   # print(result)

    print(f"{num} x {i} = {result}")

