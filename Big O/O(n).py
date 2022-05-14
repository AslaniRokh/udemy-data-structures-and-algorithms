def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

# Drop Constants
def print_items_2(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items_2(10)
# this ran n + n times or 2n
# we can simplify O(2n) by Dropping the Constant, it doesn't matter if it's O(2n) or O(100n)
# we Drop the Constant  and we just write it O(n)