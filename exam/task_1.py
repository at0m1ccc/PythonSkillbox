def calculate_volume_water(n, array):
    max_post_left = n * [0]
    max_post_right = n * [0]
    result_water = 0

    max_post_left[0] = array[0]
    for i in range(1, n):
        max_post_left[i] = max(max_post_left[i-1], array[i])

    max_post_right[n-1] = array[n-1]
    for i in range(n-2, -1, -1):
        max_post_right[i] = max(max_post_right[i+1], array[i])

    for i in range(n):
        result_water += min(max_post_left[i], max_post_right[i]) - array[i]

    return result_water


n = int(input("Введите размер массива: "))
current_array = list(map(int, input("Введите высоту столбиков через пробел: ").split()))

print("Объем воды в фигуре =", calculate_volume_water(n, current_array))
