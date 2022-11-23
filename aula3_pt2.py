#Criação de funções
preco = 1999.90

#cacular apenas 5% de imposto, guardar e exibir
imposto = preco * 0.05
print(f"o valor é {imposto:.2f}")

preco2 = 100
imposto2 = preco2 * 0.05
print(f"o valor é {imposto2}")

#Criar função calcular_imposto() que calcula 5% de imposto e retorna a quem pediu
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#Uso da função criada
preco = 299
imposto = calcular_imposto(preco)
print(f"O valor do imposto é {imposto:.2f}")

#Agora a alíquota passou de 5% para 7%
precos = [1.99, 24.50, 78.27, 1515.5]
for valor in precos:
  print(f"o imposto de {valor} é {calcular_imposto(valor):.2f}")

#Declarar um função calcular_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.
def calcular_imposto_aliquota(valor, aliquota = 7):
  imposto = valor * aliquota / 100
  return imposto

for valor in precos:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor):.2f}")

for valor in precos:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7):.2f}")

#Se o imposto for 10%
for valor in precos:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10):.2f}")