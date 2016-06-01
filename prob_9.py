def prob_9 (n1, n2, n3, l):
	l=[n1, n2, n3]
	l.sort()
	if l[2] == ((l[0]**2 + l[1]**2)**0.5):
		return "es una tripleta pitagórica"
	else:
		return "no es una tripleta pitagórica"


