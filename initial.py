while True:
    de=int(input ("""Bienvenue sur Calculatrice  tapez 1 
                  Si vous desirez lire que la documentation
                  tapez 2 pour la suite: """))
    if de==1:
        print("""Calculatrice est une application 
              mise en place pour vous facilite
              les calcules sur les moyennes 
              de vos etudiants(e)""")
        break
    elif de==2:
        print("Commençant , entrez les etapes selon les instructions  ")
        break    
    else:
        print("Error de saisi")
    
g1= int(input("""En tenant compt du ministere d'Etudes;
              quelle est la note la plus elevee attribue a un etudiant:  """))
list(range(g1+1))
print("voici donc un liste des notes  :"+ str(list(range(g1+1))))

while True:
    n1=float(input("Entre votre premiere note:  "))
    if n1 not in list(range(g1)):
        print("Votre note doit etre dans l'intervale[0,20]")
    else :
        print(" LA suite ")
        break    
while True:
    n2=float(input("Entre votre deuxieme note:  "))
    if n2 not in list(range(g1)):
        print("Votre note doit etre dans l'intervale[0,20]")
    else :
        print(" LA suite ")
        break            
while True:
    n3=float(input("Entre votre troisieme note:  "))
    if n3 not in list(range(g1)):
        print("Votre note doit etre dans l'intervale[0,20]")
    else :
        print(" __ ")
        break    

rus1=n1+n2+n3
rus2=rus1/3
print(f"vous aviez obtenu{rus2}")
if rus2 < 10:
    print ("Faible ,Vous etes endessous de la moyenne")
elif rus2==10:
    print("Bien, vous aviez la moyenne")
else:
    print("exellent, vous etez au dessus de la moyenne ")        
    
