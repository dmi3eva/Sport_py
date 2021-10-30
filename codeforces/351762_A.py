# Пример, когда строки сортируются не как числа
# s = ['2', '1', '10']
# print(sorted(s))

print('+'.join(map(str, sorted(map(int, input().split('+'))))))