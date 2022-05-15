def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
        
    for k in range(n):
        print(k)

print_items(10)

# nested for loops ran O(n^2)
# single for loop ran O(n)
# O(n^2) + O(n) = O(n^2 + n)
# in this equation n^2 is Dominant term and n is Non-Dominant term
# we Drop the n because it is insignificant