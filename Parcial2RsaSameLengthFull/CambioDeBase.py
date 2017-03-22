def Base10_BaseN(N, base, printProcess):

	if base < 2:
		return "Solo son admitidas bases mayores a 1"

	arr = []
	concatenacion = ""
	i = 0

	while (N > 0):
		residuo = N % base
		arr.append(residuo)
		if printProcess:
			print(str(N) + " = ",base,"(",int(N/base),") + ",residuo)
		N = int(N/base)

	lastPos = len(arr) - 1
	for i in range(lastPos, 0, -1):
		concatenacion += str(arr[i]) + ","
	concatenacion += str(arr[0])

	return concatenacion

def BaseN_Base10(base, N, printProcess):

	if (base > 1):
		N = N.lstrip('0')
		result = 0

		if (base > 10 ):
			arr = N.split(",")
		else:
			arr = list(N)

		j = 0
		lastPos = len(arr) - 1
		for i in range(lastPos, 0, -1):
			if printProcess:
				print(arr[i],"*(",str(base) + "^" + str(j),") +", end=" ")
			result += int(arr[i]) * pow(base,j)
			j += 1

		if printProcess:
			print(arr[0],"*(",str(base) + "^" + str(lastPos),")")
		
		result += int(arr[0]) * pow(base, lastPos)
			
		return str(result)
	else:
		return "Solo son admitidas bases mayores a 1"
