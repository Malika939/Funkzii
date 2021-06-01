def delitel():
	a = input().split()
	print((list(reversed(a[:(int(len(a)) // 2 )])))
		+(list(reversed(a[(int(len(a)) // 2)::]))))

delitel()
