text = input('Введите строку: ')
print(f'Развёрнутая последовательность между первым и последним h:'
      f' {text[text.rindex('h') - 1:text.index('h'):-1]}')
