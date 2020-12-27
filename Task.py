import sys


def read_data_from_file():
	name_file = sys.argv[1]  # Чтение с командной строки

	file = open(name_file, 'r')  # Открытие файла

	row, col = map(int, file.readline().split())  # Ввод количества строк и столбцов

	print("Количество строк равно: {}\nКоличество столбцов равно: {}".format(row, col))

	a = [0] * col
	a[len(a) - 1] = [0] * col

	for i in range(row):
		a[i] = [0] * col

	for i in range(row):  # Ввод массива
		line = file.readline().split()
		for j in range(col):
			a[i][j] = int(line[j])

	num = int(file.readline())  # Ввод заданного числа

	print("Заданное число равно: {}".format(num))

	c, d = map(int, file.readline().split())  # Ввод границ отрезка

	print("Отрезок = [{}, {}]".format(c, d))

	p = int(file.readline())  # Ввод числа P

	print("Число P равно: {}".format(p))

	return a, num, c, d, p, row, col  # Возврат значений в головной модуль


def matrix_output(a):  # Подпрограмма вывода матрицы
	for i in range(row):
		for j in range(col):
			print("%3d" % a[i][j], end=' ')
		print()


def even_row_in_matrix(line, n):  # Подпрограмма нахождения элемента равного num
	check = False
	for i in range(row):
		if line[i] == n:
			check = True
			break
		else:
			check = False
	return check


def min_in_the_segment(line, c, d):  # Подпрограмма проверки условия [C, D]
	num = None
	min = d + 1
	for i in range(row):
		if line[i] < min and c <= line[i] <= d:
			num = min = line[i]
	if num is not None:
		return num


def element_position_bigger_than_p(line, p):  # Подпрограмма нахождения числа большего P
	for i in range(row):
		if line[i] > p:
			return i


array, num, c, d, p, row, col = read_data_from_file()  # Присваивание констант

print('Веденная матрица:')
matrix_output(array)  # Вывод матрицы

for i in range(row):  # Основной цикл
	if i % 2 == 0 and even_row_in_matrix(array[i], num) and i < row:  # Условие проверки выполнения первого условия
		num2 = min_in_the_segment(array[i + 1], c, d)  # Присваивание значения подпрограммы [C, D]
		print("Элемент, значение которого попадает в отрезок [{}, {}], равен: {}\n".format(c, d, num2))  # Вывод выходных данных
		break  # Выход из цикла
	elif element_position_bigger_than_p(array[i + 1], p) is not None:  # Если условие не выполняется
		num2 = element_position_bigger_than_p(array[i + 1], p)  # Присваивания значения подпрограммы > P
		print("Позиция элемента большего, чем P, равна: {}\n".format(num2 + (i + 1) * col + 1))  # Вывод выходных данных
		break  # Выход из цикла
