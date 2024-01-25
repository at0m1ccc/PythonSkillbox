def nearest_multiple_of_ten(number: int) -> int:
    if number % 10 <= 5:
        return number // 10 * 10
    return ((number // 10) + 1) * 10


n = int(input("Введите целое число N: "))

print("Ближайшее число, которое кратно 10 =", nearest_multiple_of_ten(n))
