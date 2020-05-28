# point = 0
# triangle = 0
# print('p',point)
# print('t',triangle)

# point = point +1
# triangle = triangle + point
# print('p',point)
# print('t',triangle)


print("-------------")

target = 23
point = 0
triangle = 0
listeNombre =[]
while point <= 50:
	point = point + 1
	triangle = triangle + point
	# print('p',point)
	# print('t',triangle)
	listeNombre.append(triangle)

print(listeNombre)

listeDiviseurs =[]

for x in range(listeNombre[-1]+1):
	# print(x)
	listeDiviseurs.append(x)

del listeDiviseurs[0]
print(listeDiviseurs)
nombre=0

listeSolution =[]
for i in listeNombre:
	print('item',i)
	listeResultat=[]
	for j in listeDiviseurs:
		# print('j',j)
		while nombre == i%j:
			note = i//j
			# print("n",note,'=', ' i',i,' //', 'j',j)
			listeResultat.insert(1, note)
			j = j + 1

			# print("listeResultat",listeResultat)
			listeZ = set(listeResultat)
			listeZ = list(listeZ)
			# if listeZ[0]==1:
			# 	del listeZ[0]
		# print("listeZo",listeZ)


		if len(listeZ)==target:
			# print('R',len(listeResultat))
			print(len(listeZ), '==', target)
			print('longeur :',len(listeZ))

			listeZ.sort()
			print('SolutionA',listeZ[-1])
			listeSolution.append(listeZ[-1])
				

# print('listeSolution',listeSolution)
listeSol = set(listeSolution)
listeS = list(listeSol)
listeS.sort()
print('Unique',listeS)

print('For target :',target, " Solution = ", listeS[0])
