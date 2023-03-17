file=open('Собачки.txt','r',encoding='UTF-8')
data = file.read().replace(":", " ").split()
ft = list(filter(lambda x: x == "американский", data))
print(ft)
