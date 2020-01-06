n = input('請輸入西元年')
n = int(n)
def is_leap(n):
	if n%4 != 0:
		print('平年')
		return False
	elif n%100  == 0 and n%400 != 0:
		print('閏年')
		return True
	elif n%100  == 0 and n%400 != 0:
		print('平年')
		return False
	elif n%400  == 0 and n%3200 !=0 :
		print('閏年')
		return True
	else : print('MD')
is_leap(n)


