def perc_calc(value, percent):
    f_value = value / 100 * percent
    return f_value

try:
    value = float(input("\nВведите число: "))
    percent = float(input("Введите процент: "))
    startresult = perc_calc(value, percent)
    finishresult = value - startresult
    finishresult = round(finishresult, 2)
    print(f"\nСумма с учетом процента будет равна: {finishresult}")
except ValueError:
    print("\nОшибка, повторите попытку вводя цифры\nПример цифр: 100.12; 123; 15 и так далее")
