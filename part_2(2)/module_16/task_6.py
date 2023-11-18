import time


class LoggerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        arguments_str = ", ".join([repr(x) for x in args])
        result_func = self.func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time

        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: ({arguments_str}), {kwargs}")
        print(f"Результат: {result_func}")
        print(f"Время выполнения: {run_time:.10f} секунд")

        return result_func


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется “сложный” алгоритм
    result = 0
    for i_arg_1 in range(arg1):
        for j_arg_2 in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as out_file:
                out_file.write(str(i_arg_1 + j_arg_2))
                result += i_arg_1 + j_arg_2
    # Можете попробовать вынести создание файла из циклов и проверить, сколько времени алгоритм будет работать в этом
    # случае
    return result


result = complex_algorithm(10, 50)
