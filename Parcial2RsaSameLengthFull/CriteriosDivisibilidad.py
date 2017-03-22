# sin recursividad
# recibe el numero a sacar su criterio y el limite para ello
# regresa el arreglo con el criterio de divisibilidad
def criterio(n,lim):
	results = []
	for i in range(lim):
		residuo = pow(10,i) % n
		residuoneg = residuo - n
		# abs = funcion para obtener el valor absoluto (+)
		if(residuo <= abs(residuoneg)):
			# append = push_back(elemento) en c++
			results.append(residuo)
		else:
			results.append(residuoneg)
	return results


def divisibilidad(n,nquedivide):
	n = str(n)[::-1]
	suma = 0
	results = criterio(nquedivide,len(n))

	i = 0
	for digit in n:
		suma += int(digit) * results[i]
		i +=1

	return suma % nquedivide == 0
