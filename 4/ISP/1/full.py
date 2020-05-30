"""This script solve the first lab"""

from collections import Counter
import random
import argparse


def task1(sentence):
    """This is method return all words in sentence"""
    split_sentence = sentence.split()
    dictionary = dict()
    for word in split_sentence:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    for item in dictionary:
        print("Word " + item + " used " + str(dictionary[item]) + " times")
    return dictionary


def task2(dictionary):
    """This is make sentence from 10 words in sentence"""
    word_count = Counter(dictionary)
    ans = word_count.most_common(10)
    print(ans)
    return ans


def task3(nums):
    """This is method sort array by quick sort"""
    if len(nums) < 2:
        return nums
    pivot = random.choice(nums)
    l_nums = [n for n in nums if n < pivot]
    e_nums = [pivot] * nums.count(pivot)
    r_nums = [n for n in nums if n > pivot]
    return task3(l_nums) + e_nums + task3(r_nums)


def task4(nums):
    """This is method sort array by merge sort"""
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        task4(left)
        task4(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    return nums


def task5(count):
    """This is method solve Fibonacci number"""
    number_1, number_2 = 1, 1
    for _ in range(count):
        yield number_1
        number_1, number_2 = number_2, number_1 + number_2


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
        description="Часть лабы, основанная на украинских нанотехнологиях"
    )
    PARSER.add_argument("--file", help="Укажите название файла, чтобы заработало")
    GROUP = PARSER.add_mutually_exclusive_group()
    GROUP.add_argument(
        "--word_counter",
        action="store_true",
        help="Посчитать количество слов в предложении. Вывести 10 слов",
    )
    GROUP.add_argument(
        "--quick_sort",
        action="store_true",
        help="Отсортировать данные быстрой сортировкой",
    )
    GROUP.add_argument(
        "--merge_sort",
        action="store_true",
        help="Отсортировать данные сортировкой слиянием",
    )
    GROUP.add_argument("--fib", type=int, help="Вывести n-первых чисел Фиббоначи")
    ARGS = PARSER.parse_args()

    if ARGS.file:
        if ARGS.wordcounter:
            with open(ARGS.file) as f:
                task2(task1(f.read()))

        elif ARGS.quicksort:
            with open(ARGS.file) as f:
                ARRAY = [int(i) for i in f.read().split()]
                print(task3(ARRAY))

        elif ARGS.mergesort:
            with open(ARGS.file) as f:
                ARRAY = [int(i) for i in f.read().split()]
                print(task4(ARRAY))

        elif ARGS.fib:
            for number in task5(ARGS.fib):
                print(number)
    else:
        print("Файл не обнаружен")
