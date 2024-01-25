def sort_colors(arr):
    count_0, count_1, count_2 = 0, 0, 0

    for element in arr:
        if element == 0:
            count_0 += 1
        elif element == 1:
            count_1 += 1
        elif element == 2:
            count_2 += 1

    for i in range(len(arr)):
        if count_0 > 0:
            arr[i] = 0
            count_0 -= 1
        elif count_1 > 0:
            arr[i] = 1
            count_1 -= 1
        elif count_2 > 0:
            arr[i] = 2
            count_2 -= 1


n = int(input("Введите количество элементов массива: "))
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

sort_colors(arr)

print("Отсортированный массив:", arr)
