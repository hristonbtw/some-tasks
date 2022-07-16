from collections import deque
import time
from random import randint

# Задание 1

#Минусы:
#Решение не универсальное (числа больше 1000000 не будут проходить проверку)

#Плюсы:
#У нас есть список с кратными числами в диапазоне миллиона :)

class isEven:
	def __init__(self):
		self.nums = []

	def getNums(self):
		for num in range(1000000):
			if str(num).endswith('1') or str(num).endswith('3') or str(num).endswith('5') or str(num).endswith('7') or str(num).endswith('9'):
				pass
			else:
				self.nums.append(num)

	def evenCheck(self, value):
		if value in self.nums:
			return True

	def main(self):
		getNums()
		while True:
			i = input("Введите число: ")
			try:
				i = int(i)
				isEven(i)
			except:
				print("Пожалуйста, введите число!")
				continue

# Задание 2

# Минусы:
# Первый способ имет недостаток в виде меньшей эффективности доступа у элементов в середине структуры данных
# Второй способ имет недостаток в виде большей потребляемости ресурсов, если вопрос производительности является проблемой

# Плюсы:
# Первый способ делает операцию добавления более эффективной, если вопрос производительности является проблемой
# Второй способ является очень простым и понятным даже для начинающих

class FIFO:
	def __init__(self):
		self.num = 32

	def firstFIFO(self):
		d = deque(maxlen=7)
		d.extend([2,4,62,28,12,9,11])
		print "Массив до: ", d
		d.append(self.num)
		print "Массив после: ", d

	def secondFIFO(self):
		d = [2, 4, 62, 28, 12, 9, 11]
		print "Массив до: ", d
		d = d[1:] + [self.num]
		print "Массив после: ", d

# Задание 3 

# Объяснение:
# Метод "пузырька" является наиболее эффективным, т.к. сортирует массив чисел быстрее, чем все остальные методы.
# Функция соответствует заданным критериям потому что: 
# 1. Функция сортирует данный ей массив чисел 
# 2. Время выполнения выводится по процессорным тикам


# Источник с методами и подробным объяснением - https://is35-2020.susu.ru/blog/2020/10/30/algoritmy-sortirovki-na-python/

class sorting:
	def __init__(self):
		self.nums = []

	def getNums(self):
		for _ in range(1000000):
			self.nums.append(randint(1, 100000000))

	def bubble_sort(self, array):
		n = len(array)
		for i in range(n):
			for j in range(n - i - 1):
				already_sorted = True
				if array[j] > array[j + 1]:
					array[j], array[j + 1] = array[j + 1], array[j]
					already_sorted = False
			if already_sorted:
				break
		return array

	def insertion_sort(self, array):
		for i in range(1, len(array)):
			key_item = array[i]
			j = i - 1
			while j >= 0 and array[j] > key_item:
				array[j + 1] = array[j]
				j -= 1
			array[j + 1] = key_item
		return array

	def quicksort(self, array):
		if len(array) < 2:
			return array
		low, same, high = [], [], []
		pivot = array[randint(0, len(array) - 1)]
		for item in array:
			if item < pivot:
				low.append(item)
			elif item == pivot:
				same.append(item)
			elif item > pivot:
				high.append(item)
		return quicksort(low) + same + quicksort(high)

	def insertion_sort(self, array, left=0, right=None):
		if right is None:
			right = len(array) - 1
		for i in range(left + 1, right + 1):
			key_item = array[i]
			j = i - 1
			while j >= left and array[j] > key_item:
				array[j + 1] = array[j]
				j -= 1
			array[j + 1] = key_item
		return array


	def startSort(self):
		#Метод сортировки #1
		start_time = time.process_time()
		sorted(self.nums)
		print(f"[Метод сортировки #1] --- Время выполнения: {time.process_time() - start_time} секунд --- ")

		#Метод сортировки #2
		start_time = time.process_time()
		self.nums.sort()
		print(f"[Метод сортировки #2] --- Время выполнения: {time.process_time() - start_time} секунд --- ")

		#Метод сортировки #3
		start_time = time.process_time()
		insertion_sort(self.nums)
		print(f"[Метод сортировки #3] --- Время выполнения: {time.process_time() - start_time} секунд --- ")

		#Метод сортировки #4
		start_time = time.process_time()
		bubble_sort(self.nums)
		print(f"[Метод сортировки #4] --- Время выполнения: {time.process_time() - start_time} секунд --- ")

		#Метод сортировки #5
		start_time = time.process_time()
		quicksort(self.nums)
		print(f"[Метод сортировки #5] --- Время выполнения: {time.process_time() - start_time} секунд --- ")

		#Метод сортировки #6
		start_time = time.process_time()
		insertion_sort(self.nums)
		print(f"[Метод сортировки #6] --- Время выполнения: {time.process_time() - start_time} секунд --- ")