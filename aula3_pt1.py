contador = 1
while(contador <= 10):
  print (contador)
  contador = contador +1

#laço for
fruta = "morango"
print(fruta)
fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

#Lista
frutas = ["morango", "laranja", "pêra"]

#mostra todas
print(frutas)
#exibir apenas terceira fruta
print (frutas[1])
#incluir nova fruta
frutas.append("manga")
print (len(frutas))
frutas.append("uva")

print ("Exemplo das frutas com WHILE:")
i = 0
while(i < len(frutas)):
    print(frutas[i])
    i = i +1

print("Exemplo das frutas com FOR:")
for fruta in frutas:
    print(fruta)