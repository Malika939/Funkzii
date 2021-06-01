a = input('Имя файла')
def main():
	f = open (f'/users/mac/Desktop/{a}.txt', 'w')
	f.close
a = main()
print(a)
