x = input().split()
with open('x.txt', 'w') as file:
    for num in x:
        file.write(num + '\n')