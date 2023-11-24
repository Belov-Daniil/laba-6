#. У няни 7 разных фруктов (ф1,…ф7).
# Сформировать (вывести) все возможные варианты меню полдника
# (1 фрукт) для ребенка на неделю.
from itertools import *
import numpy as np

fruit_basket = ['apple', 'pineapple', 'orange', 'banana', 'pear', 'kiwi', 'avocado']

all_variants = []


def F_iter():
    for i in permutations(fruit_basket, 7):
        all_variants.append(i)
    return all_variants


def F_rec(a, k):
    if k == 1:
        return [[x] for x in a]
    else:
        return [[x] + y for x in a for y in F_rec(a, k - 1)]


def start():
    print('У няни 7 разных фруктов (ф1,…ф7). Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.')
    a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    while a != 'rec' and a != 'iter':
        a = input('Напишите rec для рекурсивного решения, iter для итеративного \n')
    if a == 'rec':
        p = 0
        fr = F_rec(fruit_basket, 7)
        for j in fr:
            if len(np.unique(j)) < 7:
                pass
            else:
                p += 1
                print(*j)
        print('общее кол-во вариантов меню на неделю : ' + str(p))
        b = ''
        while b != 'rerun' and b != 'exit':
            b = input('чтобы начать заного напишите rerun, чтобы закрыть программу напишите exit \n')
        if b == 'rerun':
            start()
        else:
            exit()
    else:
        p = 0
        fi = F_iter()
        for j in fi:
                p += 1
                print(*j)
        print('общее кол-во вариантов меню на неделю : ' + str(p))
        b = ''
        while b != 'rerun' and b != 'exit':
            b = input('чтобы начать заного напишите rerun, чтобы закрыть программу напишите exit \n')
        if b == 'rerun':
            start()
        else:
            exit()

start()
