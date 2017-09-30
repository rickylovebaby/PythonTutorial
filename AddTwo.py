
# example 1
# add two functions
num1 = input('A=: ')
num2 = input('B=: ')

sum = float(num1) + float(num2)

print("the sum of {0} and {1} is {2}".format(num1,num2,sum))

# example 2
# primer number


num = int(input("enter number: "))



if num > 1:
	for i in range(2,num):
		if(num % i) == 0:
			print(num,"is not a primer number")
			print(i,"times",num//i,"is",num)
			break
	else:
		print(num,"is a primer number")

else:
	print(num,"is not a primer number")
