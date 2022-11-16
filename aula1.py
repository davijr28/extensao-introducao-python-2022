# Meu primeiro projeto em python  print() = comando de saída
print("Alo mundo!")

#Para guardar uma string
nome = "Davi"
#Para guardar um número inteiro
idade = 18

#Exibir o meu nome (dentro da variável nome)
print(nome)

#Para exibir a frase "Minha idade é " completando com o conteúdo da variável idade  print("Meu nome é "+nome)
print("Minha idade é "+str(idade)+" anos")
print(f"Minha idade é {idade} anos")
print("Minha idade é {} anos".format(idade))

#Para exibir "Meu nome é ... e tenho ... anos.." trocando pelas variáveis nome e idade
print("Meu nome é {} e tenho {} anos".format(nome, idade))