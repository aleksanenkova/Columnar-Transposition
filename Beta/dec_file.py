# -*- encoding: utf-8 -*-

import sys
import random
import string

ALPH = u'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩШЫЬЪЭЮЯ0123456789:;.,'+'\n'+' '


def get_column_order(keyword, alph):
    def generate_symbol_position(sym, keyword):

        for i in range(len(keyword)):
            if keyword[i] == sym:
                yield i
    
    max_symbols = len(keyword)
    new_pos = 0

    for sym in alph:
        for old_pos in generate_symbol_position(sym, keyword):
            yield new_pos, old_pos, sym
            new_pos += 1

            if new_pos == (max_symbols):
                return


def transpose_columns(matr_from, matr_to, from_, to_):

    for i in range(len(matr_from)):
        matr_to[i][to_] = matr_from[i][from_]

def print_matr(m):
    for line in m:
        print('  '.join(line))



with open('key.txt', 'r') as F:
    keyword = F.read().replace('\n', '').replace('\r', '').upper()

print('Ключ: "%s"' % keyword)


source_text = ''
with open('code.txt', 'r') as F:
    source_text = ''.join([ x.upper() for x in F.read() if x.upper() in ALPH and x != '\n' ])

print('Сообщение: %s' % source_text)
list = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Щ','Ш','Ъ','Ь','Ы','Э','Ю','Я']
b=random.randint(0,7)
rand_ = list[b]
print(rand_)

M = []
M1 = []
current_line = []
for x in source_text:
    current_line.append(x)
    if len(current_line) == len(keyword):
        M.append(current_line)
        current_line = []
if len(current_line) > 0:
    while (len(keyword)-len(current_line)>0):
        #    current_line += [list[random.randint(0,7)]]*(len(keyword) - len(current_line))
        current_line += [list[random.randint(0,7)]]
    M.append(current_line)

for line in M:
    M1.append([' ']*len(line))


print('Первоначальная матрица:')
print_matr(M)

order = ''

for new_pos, old_pos, sym in get_column_order(keyword, ALPH):
#    print('Move %d to %d' % (old_pos, new_pos))
    order += sym
    transpose_columns(M, M1, new_pos, old_pos)
    # print_matr(M1)

print('Перестановка ключа: %s' % order)

print('Матрица:')
print_matr(M1)

with open("decode.txt", 'w') as F:
    for line in M1:
        F.write(''.join(line) )
