#task 34
s = 'пара-ра-рам рам-пам-папам па-ра-па-да'
s = s.lower()
alph = 'аиеёоуыэюя' 
liter = ''
count_liter_one_phrase = 0

for i in s:
    if i in alph:
        liter += i
        break
    
for i in s:
    if i == liter:
        count_liter_one_phrase += 1
    if i == ' ':
        break

        
phrases_count = s.count(' ') + 1

if s.count(liter) == count_liter_one_phrase * phrases_count:
     print('Парам пам-пам ')
else:
    print('Пам парам')

#task 36
def print_operation_table(f):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(f(i, j), end=' ')
        print()
 
num_rows = int(input())
num_columns = int(input())
print_operation_table(lambda x, y: x * y)
