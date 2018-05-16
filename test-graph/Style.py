import datetime
import os
import random

# from heavy import special_commit

shakespeare = open('shakespeare.txt')
words = shakespeare.read().split(' ')
words_num = 0

def modify():
    global words_num
    file = open('shakespeare_append.txt', 'a+')
    for i in range(100):
        file.write(words[words_num])
        file.write(' ')
        words_num += 1
    file.close()


def commit():
    global words_num
    os.system('git add .')
    os.system('git commit -m "%s %s %s %s %s"' % (words[words_num], words[words_num + 1], words[words_num + 2], words[words_num + 3], words[words_num + 4]))


def set_sys_time(year, month, day):
    year1 = year - 2000
    hour = random.randint(0,23)
    minute = random.randint(0,59)
    os.system('date %02d%02d%02d%02d%02d' % (month, day, hour, minute, year1))


def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i)
        trick_commit(cur_date.year, cur_date.month, cur_date.day)



def modify_other(path):
    global words_num
    file = open(path, 'a+')
    for i in range(100):
        file.write(words[words_num])
        file.write(' ')
        words_num += 1
    file.close()


def hard_commit(path, year, month, day, times):
    set_sys_time(year, month, day)
    while times > 0:
        modify_other(path)
        os.chdir(os.path.dirname(path))
        commit()
        times -= 1


def special_commit(path, date, times):
    hard_commit(path, date.year, date.month, date.day, times)


def read_etc(path):
    idxes = []
    file = open(path, 'r')
    while True:
        word = file.readline()
        if not word:
            break
        else:
            idxes.extend(word.split())
    intIdxes = []
    for idx in idxes:
        intIdxes.append(int(idx))
    return intIdxes


def love_commit(start_date, path, etc_path):
    words = read_etc(etc_path)
    for index in words:
        #rand_times = random.randint(0,10)
        rand_times = 15
        cur_date = start_date + datetime.timedelta(days=index)
        special_commit(path, cur_date, rand_times)




if __name__ == '__main__':
    #daily_commit(datetime.date(2017, 5, 14), datetime.date(2018, 5, 16))
    love_commit(datetime.date(2017, 5, 14), '/Users/dengyouwang/Documents/GitHub/Style-Contributions-Graph/shakespeare_append', '/Users/dengyouwang/Documents/GitHub/Style-Contributions-Graph/etc/test')
