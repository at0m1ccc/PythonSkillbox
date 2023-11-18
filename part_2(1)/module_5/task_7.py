address_IP = input('Введите IP: ').split('.')

for number in address_IP:
    if len(address_IP) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        break
    elif not number.isdigit():
        print(f'{number} - это не целое число.')
        break
    elif int(number) > 255:
        print(f'{number} превышает 255.')
    else:
        if number == address_IP[len(address_IP) - 1]:
            print('IP-адрес корректен.')
        else:
            continue
