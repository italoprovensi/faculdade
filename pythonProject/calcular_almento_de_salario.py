salario_original = float(input("seu salario: "))
salario_desconto = salario_original

if salario_original <= 280.00:
    salario_desconto += salario_desconto * 0.2
    porcentagem = "20%"
    aumento = salario_original * 0.20

elif salario_original <= 700.00:
    salario_desconto += salario_desconto * 0.15
    porcentagem = "15%"
    aumento = salario_original * 0.15

elif salario_original <= 1500.00:
    salario_desconto += salario_desconto * 0.10
    porcentagem = "10%"
    aumento = salario_original * 0.10

elif salario_original > 1500.00:
    salario_desconto += salario_desconto * 0.05
    porcentagem = "5%"
    aumento = salario_original * 0.05

print("O salário antes do reajuste:", salario_original)
print("O percentual de aumento aplicado", porcentagem)
print("O valor do aumento", aumento)
print("novo salário, após o aumento", salario_desconto)
