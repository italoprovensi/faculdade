nota_1 = float(input("insira sua primeira nota de 0.00 a 10.00:"))
nota_2 = float(input("insira sua segunda nota de 0.00 a 10.00:"))
soma = nota_1 + nota_2
media = soma / 2


if media >= 9.0:
    print("sua media é ", media)
    print("sua nota é A")
    print("APROVADO")
elif media >= 7.5:
    print("sua media é ", media)
    print("sua nota é B")
    print("APROVADO")

elif media >= 6.0:
    print("sua media é ", media)
    print("sua nota é C")
    print("APROVADO")

elif media >= 4.0:
    print("sua media é ", media)
    print("sua nota é D")
    print("REPROVADO")

else:
    print("sua media é ", media)
    print("sua nota é F")
    print("REPROVADO")
