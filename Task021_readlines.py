# получим объект файла
file1=open("my_file1.txt","r")
# считываем все строки
lines=file1.readlines()
# итерация по строкам
for line in lines:
    print(line.strip())
# закрываем файл
file1.close
