# Про эффективное решение этой задачи можно прочитать, например, тут: http://e-maxx.ru/algo/export_diofant_2_equation
n = int(input())
a = -1
for b in range(n // 5 + 1):
    remain = n - 5 * b
    if remain >= 0 and remain % 3 == 0:
        a = remain // 3
if a == -1:
    print("IMPOSSIBLE")
else:
    b = (n - 3 * a) // 5
    print(f"{a} {b}")