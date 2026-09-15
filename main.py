class TemperatureConverter:

    def __init__(self, first=0.0, second="C"):
        self._first = first
        self._second = second

    def read(self):
        try:
            self._first = float(input("Введите температуру: "))
            self._second = input("Введите шкалу ('C' или 'F'): ").upper()

            if self._second not in ("C", "F"):
                raise ValueError("Шкала должна быть 'C' или 'F'!")

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            self._first = 0.0
            self._second = "C"

    def display(self):
        print(f"Температура: {self._first}°{self._second}")

    def convert_to_fahrenheit(self):
        if self._second != "C":
            raise ValueError("Шкала должна быть 'C'!")
        return self._first * 9 / 5 + 32

    def convert_to_celsius(self):
        if self._second != "F":
            raise ValueError("Шкала должна быть 'F'!")
        return (self._first - 32) * 5 / 9


print("=== Конвертер температур ===")

t = TemperatureConverter()
t.read()
t.display()

try:
    if t._second == "C":
        print(f"Результат: {t.convert_to_fahrenheit():.2f}°F")
    elif t._second == "F":
        print(f"Результат: {t.convert_to_celsius():.2f}°C")
    else:
        print("Ошибка: шкала должна быть 'C' или 'F'!")
except ValueError as e:
    print(f"Ошибка: {e}")

