array = [7, 3, 5, 9, 11, 0, 12, 1, 12, 21,
         22, 16, 13, 14, 18, 21, 19, 15, 17, 17]

print("Масив 20 елементів:")
print(*array)
c = int(input("Введіть ціле число c: "))
d = int(input("Введіть ціле число d: "))
result = []
for num in array:
    if c <= num <= d:
        result.append(num)

print(f"Елементи із інтервалу [{c} {d}]:")
print(*result)

print("Їх кількість:", len(result))