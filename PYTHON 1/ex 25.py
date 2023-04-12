cid = str(input('Em que cidade você nasceu? ')).strip()
# a tag strip elimina os espaços sobrando

#print(cid[:5] == 'Santo')
#Dessa forma fica ruim a sintaxe pois o python me retorna apenas a referencia da forma que ela é!

print(cid[:5].upper() == 'SANTO')

