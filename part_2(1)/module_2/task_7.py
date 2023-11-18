word = input('Введите слово: ').lower()
palindrome_list = list(word)
isPalindrome = 0

for index in range(len(palindrome_list)):
    if palindrome_list[-index - 1] != palindrome_list[index]:
        isPalindrome = 0
        break
    else:
        isPalindrome = 1

if isPalindrome:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
