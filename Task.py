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
	i = 0
	while not check:
		if line[i] == n:
			check = True
		i  += 1
	return check


def min_in_the_segment(line, c, d):  # Подпрограмма проверки условия [C, D]
	check = False
	min = line[0]
	for i in range(row):
		if c <= line[i] <= d:
			if not check:
				min = line[i]
				flg = True
			elif line[i] < min:
				min = line[i]
	return check, min


def element_position_bigger_than_p(line, p):  # Подпрограмма нахождения числа большего P
	check = False
	i = 0
	while not check:
		if line[i] > p:
			check = True
		i += 1

	return check, i


array, num, c, d, p, row, col = read_data_from_file()  # Присваивание констант

print('Веденная матрица:')
matrix_output(array)  # Вывод матрицы

check = False
i = 0

while not check and i < row - 2:
	flg_p, func_bigger_p = element_position_bigger_than_p(array[i + 1], p)
	flg_seg, func_min_in_seg = min_in_the_segment(array[i + 1], c, d)  # Присваивание значения подпрограммы [C, D]
	if even_row_in_matrix(array[i], num) and flg_seg:  # Условие проверки выполнения первого условия
		num2 = min_in_the_segment(array[i + 1], c, d)  # Присваивание значения подпрограммы [C, D]
		print("Элемент, значение которого попадает в отрезок [{}, {}], равен: {}\n".format(c, d, num2))  # Вывод выходных данных
		check = True
	elif flg:
		num2 = func_bigger_p
		print("Позиция элемента большего, чем P, равна: {}\n".format(num2 + (i + 1) * col + 1))  # Вывод выходных данных
		check = True
	i += 2

if not check:
	print("Ни одно из условий ни разу не выполнилось!\n")
