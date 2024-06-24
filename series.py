n = int(input('Enter number of term: '))

term = 2
diff = 1
for i in range(n):
    print(f'{term} ',end='')
    term = term + diff
    diff += 1