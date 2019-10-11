arr = [1,2,3,4,5,6,7]
n = len(arr)
large = n-1
small = 0
flag = True

temp = n*[None]
for i in range(n):
	if flag is True:
		temp[i] = arr[large]
		large -= 1
	else:
		temp[i] = arr[small]
		small += 1
	flag = bool(1-flag)
	
print(temp)
