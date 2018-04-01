import os
import psutil
import sys
import shutil

def Duplicatefile(filename):
if os.path.isfile(filename):
newfile = filename + ".dplct"
shutil.copy(filename, newfile)
if os.path.exists(newfile):
print("Файл ", newfile, "создан.")
return True
else:
print("Проблемы копирования")
return False

def Deletefile(dirname):
filelist = os.listdir(dirname)
i = 0
for f in filelist:
fullname = os.path.join(dirname, f)
if fullname.endswith(".dplct"):
os.remove(fullname)
if not os.path.exists(fullname):
print("Файл ", TempDel, " успешно удален.")
i += 1
print("Всего файлов удалено ", i, " дубликатов.")

def SysIinfoOS():
print("Текущая рабочая директория: ", os.getcwd())
print("Информация об операционной системе:", os.uname())
print("Кодировка файловой системы:", sys.getfilesystemencoding())
print("Имя текущего пользовтеля:", os.getlogin())
print("Количество CPU:", os.cpu_count())
print(psutil.pids())

print ("Привет хозяин!")
print ("С возвращением!")
name = input ("Ваше имя: ")
print(name, ", Добро пожаловать в мир Python")

answer = ''
while answer != 'Q':
answer = input("Давайте поработаем? (Y/N/Q)")
print("Отлично!")
print("Я могу:")
print(" [1] - Вывести список файлов")
print(" [2] - Вывести информацию о системе")
print(" [3] - Выведу список процессов")
print(" [4] - Продублировать файлы в дериктории")
print(" [5] - Удалить продублированные файлы в дериктории")
do = int(input("Укажите пожалуйста номер действия: "))

if do == 1:
print(os.listdir())

    elif do == 2:
        SysIinfoOS()

    elif do == 3:
print(psutil.pids())

    elif do == 4:
        print("Продублирование файлов в дериктории")
        filelist = os.listdir()
        filecount = 0
        for f in filelist:
            if os.path.isfile(f):
                filecount += 1
        print(filecount,"Файлов в директории.")
        i = 0
        for s in filelist:
            if os.path.isfile(s):
                Duplicatefile(s)
               i += 1
        print("Скопировано всего", i, " файлов.")

        elif do == 5:
        print("Удаление дубликатов в директории")
        dirname = input("Укажите имя директории: ")
        Deletefile(dirname)
    else:
        pass

elif answer.upper() == 'N':
    print("Пока")
else:
    print("Такого в коде нет!")