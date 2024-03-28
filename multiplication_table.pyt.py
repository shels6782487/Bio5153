# creating  a multiplication table
table = 10  #  table size
for i in range(1, table + 1):
    for j in range(1, table + 1):
        print(str(i * j).rjust(4), end=' ')
    print()  # Move this print statement to the outer loop to print a new line after each row


