def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)
# we got n * n printing out (n * n = n^2)

# one level deeper
def print_items_2(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

print_items_2(10)
# this ran n * n * n or n^3
# we're going to simplify this and we're going to call this O(n^2)
# it doesn't matter if it's  O(n^3) or O(n^10)
# we're going to simplify it O(n^2)