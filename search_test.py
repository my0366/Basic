from Search import search

print('실수를 검색합니다')
print('End를 입력하면 종료됩니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}] : ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

ky = float(input("검색할 값 : "))

idx = search(x,ky)

if idx == -1:
    print("검색한 원소가 존재하지않습니다.")

else:
    print(f'검색값은 x[{idx}]에 있습니다.')
