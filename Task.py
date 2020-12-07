import sys


def read_data_from_file():
	name_file = sys.argv[1]  # Чтение с командной строки

	file = open(name_file, 'r')  # Открытие файла

	row, col = map(int, file.readline().split())  # Ввод количества строк и столбцов

	print("row = %d, col = %d" % (row, col))

	a = [[] for i in range(row)]  # инициализация массива

	for i in range(row - 1):  # Ввод массива
		for elem in file.readline().split():
			a[i].append(int(elem))

	num = int(file.readline())  # Ввод заданного числа

	print("num = %d" % num)

	c, d = map(int, file.readline().split())  # Ввод границ отрезка

	print("c = %d, d = %d" % (c, d))

	p = int(file.readline())  # Ввод числа P

	return a, num, c, d, p


def matrix_output(a):
	for row in a:
		for col in row:
			print("%3d" % col, end=' ')
		print()


def even_row_in_matrix(row, n):
	for elem in row:
		if elem == n:
			return True
	return False


def min_in_the_segment(row, c, d, p):
	num = None
	min = d + 1
	for elem in row:
		if elem < min and c <= min <= d:
			num = min = elem
	if num is not None:
		return num


def element_position_bigger_than_p(row, p):
	for i, elem in enumerate(row):
		if elem > p:
			return i


array, NUM, C, D, P = read_data_from_file()

print('Веденная матрица:')
matrix_output(array)

str = ''
num = 0

for i, row in enumerate(array):
	if i % 2 == 0 and even_row_in_matrix(row, NUM) and i < len(array) - 1:
		print("Элемент, значение которого попадает в отрезок [{}, {}] равен: {}".format(C, D, min_in_the_segment(array[i + 1], C, D, P)))
		break
	else:
		print("Позиция элемента большего, чем P, равна: {}".format(element_position_bigger_than_p(array[i], P)))
