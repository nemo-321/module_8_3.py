#IncorrectVinNumber и IncorrectCarNumbers:Это пользовательские исключения, унаследованные от класса Exception.
# У них должен быть конструктор __init__, который принимает параметр message и устанавливает его как атрибут

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
# класс Car представляет автомобиль и принимает параметры: model, vin и numbers.
# Конструктор __init__:Инициализирует атрибуты модели, номера VIN и автомобильных номеров.
# Вызывает два метода для проверки валидности VIN номера и номера автомобиля.

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)
# Метод __is_valid_vin:Принимает номер VIN, проверяет его тип (должен быть целым числом).
#  Проверяет диапазон VIN номера (должен находиться между 1,000,000 и 9,999,999).
#  Если проверки не пройдены, возникает соответствующее исключение IncorrectVinNumber.
    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return vin_number
# Метод __is_valid_numbers:Принимает номера автомобиля, проверяет, что они представлены в виде строки.
#  Проверяет длину номера (должна быть ровно 6 символов).
#  Если проверки не пройдены, возникает исключение IncorrectCarNumbers.
    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return numbers


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
