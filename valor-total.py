macas = int(input('Quantas maçãs foram compradas? '))
if macas < 12:
	ValorTotal= macas * 1.30
	print(ValorTotal)
else:
	ValorTotal = macas * 1.00
	print(ValorTotal)
