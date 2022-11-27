# Inicio da calculadora

print('-=-' * 16)
print('Seja muito bem vindo')
# Menu da escolha
print('Aqui estão as opções de escolha:')
# Opções

print('|Se quiser fazer uma conta basta apertar |+| 1°|'
      '\n|Se quiser fazer uma conta basta apertar |-| 2°|'
      '\n|Se quiser fazer uma conta basta apertar |/| 3°|'
      '\n|Se quiser fazer uma conta basta apertar |%| 4°|')
# Final do muno de escolha
# Escolha
escolha = complex(input('Qual conta gostaria de fazer :'))
print('-=-' * 16)

# conta de adição
if escolha == 1:
    n1 = float(input('Digite um número'))
    n2 = float(input('Digite um número'))
    s1 = n1 + n2
    print('Resultado: {:.1f}'.format(s1))
# final

# conta de subtração
if escolha == 2:
    n1 = float(input('Digite um número'))
    n2 = float(input('Digite um número'))
    s1 = n1 - n2
    print('Resultado: {:.1f}'.format(s1))
# fim

#conta de divisão
if escolha == 3:
      n1 = float(input('Digite um número'))
      n2 = float(input('Digite Um número'))
      s1 = n1 / n2
      print('Resultado: {:.1f}'.format(s1))
# fim
print('-=-' * 16)