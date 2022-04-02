# nome = "Izabel"
# empresa = "VNW"
# qtde_funcionarios = 120
# mediaMensalidade = 1.250
# print(nome + "trabalha na empresa " + empresa)
# print("A média da mensalidade é " + str(mediaMensalidade))

nome = input()
empresa = input()
qtde_funcionarios = int(input())
mediaMensalidade = float(input())

print(nome, "trabalha na empresa", empresa, "que possui ", qtde_funcionarios, "funcionários")
print("A média da mensalidade é de", str(mediaMensalidade))