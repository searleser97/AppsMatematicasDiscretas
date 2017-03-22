from math import sqrt

def cribaPrimos(N):

	arr = [False] * (N + 1)
	primos = [2,3]

	arr[2] = True
	arr[3] = True

	i = 5
	w = 2
	while (i <= N):
		arr[i] = True;
		i += w
		w = 6 - w

	i = 5
	w = 2
	sqrtn = sqrt(N)
	while (i <= sqrtn):
		if(arr[i]):
			h = 5
			while (i * h <= N):
				arr[i * h] = False
				h += 1
		i += w;
		w = 6 - w

	i = 5
	w = 2
	while (i < N):
		if (arr[i]):
			primos.append(i)
		i += w;
		w = 6 - w

	return primos