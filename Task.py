import sys


def read_data_from_file():
	name_file = sys.argv[1]  # Чтение с командной строки

	file = open(name_file, 'r')  # Открытие файла

	row, col = map(int, file.readline().split())  # Ввод количества строк и столбцов

	print("Количество строк равно: {}\nКоличество столбцов равно: {}".format(row, col))

	a = [[] for i in range(row)]  # инициализация массива

	for i in range(row):  # Ввод массива
		for elem in file.readline().split():
			a[i].append(int(elem))

	num = int(file.readline())  # Ввод заданного числа

	print("Заданное число равно: {}".format(num))

	c, d = map(int, file.readline().split())  # Ввод границ отрезка

	print("Отрезок = [{}, {}]".format(c, d))

	p = int(file.readline())  # Ввод числа P
	print("Число P равно: {}".format(p))

	return a, num, c, d, p, row, col  # Возврат значений в головной модуль


def matrix_output(a):  # Подпрограмма вывода матрицы
	for row in a:
		for col in row:
			print("%3d" % col, end=' ')
		print()


def even_row_in_matrix(row, n):  # Подпрограмма нахождения элемента равного num
	for elem in row:
		if elem == n:
			return True
	return False


def min_in_the_segment(row, c, d, p):  # Подпрограмма проверки условия [C, D]
	num = None
	min = d + 1
	for elem in row:
		if elem < min and c <= elem <= d:
			num = min = elem
	if num is not None:
		return num


def element_position_bigger_than_p(row, p):  # Подпрограмма нахождения числа большего P
	for i, elem in enumerate(row):
		if elem > p:
			return i


array, NUM, C, D, P, ROW, COL = read_data_from_file()  # Присваивание констант

print('Веденная матрица:')
matrix_output(array)  # Вывод матрицы

for i, row in enumerate(array):  # Основной цикл
	if i % 2 == 0 and even_row_in_matrix(row, NUM) and i < len(array) - 1:  # Условие проверки выполнения первого условия
		num = min_in_the_segment(array[i + 1], C, D, P)  # Присваивание значения подпрограммы [C, D]
		print("Элемент, значение которого попадает в отрезок [{}, {}], равен: {}\n".format(C, D, num))  # Вывод выходных данных
		break  # Выход из цикла
	elif element_position_bigger_than_p(array[i + 1], P) is not None:  # Если условие не выполняется
		num = element_position_bigger_than_p(array[i + 1], P)  # Присваивания значения подпрограммы > P
		print("Позиция элемента большего, чем P, равна: {}\n".format(num + (i + 1) * COL + 1))  # Вывод выходных данных
		break  # Выход из цикла
