while True:
	try:
		num = int(input('Enter a number: \n'))
		print(100/num)
		break
	except ValueError:
		print('Please enter a number')
	except ZeroDivisionError:
		print('Please make sure the number is not zero')
	except:
		break
	finally:
		print('Loop complete')
	
