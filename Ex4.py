# Напишите программу, которая по заданному номеру четверти, показывает диапазон
#  возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите значение четверти: '))
if quarter == 1 and quarter <= 4:
    print(f'Диапазоон координат в {quarter} четверти (x и y)')
elif quarter == 2 and quarter <= 4:
    print(f'Диапазоон координат во {quarter} четверти (-x и y)')
elif quarter == 3 and quarter <= 4:
    print(f'Диапазоон координат в {quarter} четверти (-x и -y)')
elif quarter == 4:
    print(f'Диапазоон координат в {quarter} четверти (x и -y)')