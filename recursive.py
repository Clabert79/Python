def stampa_n(s, n):
	if n <= 0:
		return
	print(s + str(n))
	stampa_n(s, n-1)

stampa_n("pippo",7)