nome = ["", "", ""]
ataque = [0, 0, 0]
defesa = [0, 0, 0]

for i in range(3):
    nome[i] = input()
    ataque[i] = int(input())
    defesa[i] = int(input())

personagens = [   
                
    [nome[0], (ataque[0], defesa[0])],
    [nome[1], (ataque[1], defesa[1])],
    [nome[2], (ataque[2], defesa[2])],
    
]

print(personagens)

#Encontrar maior ataque e defesa
maior_ataque = ataque[0]
maior_defesa = defesa[0]
nome_maior_ataque = nome[0]
nome_maior_defesa = nome[0]

for i in range(1, 3):
    if ataque[i] > maior_ataque:
        maior_ataque = ataque[i]
        nome_maior_ataque = nome[i]
    if defesa[i] > maior_defesa:
        maior_defesa = defesa[i]
        nome_maior_defesa = nome[i]

print("Ataque", nome_maior_ataque, maior_ataque) 
print("Defesa", nome_maior_defesa, maior_defesa)