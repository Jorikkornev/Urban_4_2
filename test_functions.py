# Домашняя работа по уроку "Пространство имен."
def test_function() -> None:
    """Тестовая функция для проверки пространства имен"""
    def inner_function():
        print(f"Я в области видимости функции {test_function.__name__}")
    inner_function()

def test_function_return(x = None) -> None:
    """Тестовая функция для проверки вызова функции из функции"""

    def inner_function():
        print(f"Я в области видимости функции {test_function_return.__name__}")
    if x:
        return inner_function()
    else:
        return print('test_function_return')

if __name__ == "__main__":

    test_function()
     #  Stackoverflow help
    test_function_return()
    test_function_return(1)

    #  test_function_return()()