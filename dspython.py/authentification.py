#projet ecole 
import cowsay
def valid(email):
    import re 
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex,email):
        return True
    else: 
        return False    
def enregistrement():
    global email
    print("\n************************************Enregistrement***********************************")
    while True:
        email= input("\nentrez votre adresse-mail: ") 
        if valid(email):
            print("adresse e-mail valide")
            break
        else:
            print("merci d'introduire une adresse email valide.")
    return email    

                             
def introduire_pwd():
    import string
    import maskpass
    global p
    while True:
        p = maskpass.askpass()
        if len(p)== 8:
            if any(x in string.ascii_uppercase for x in p):
               if any(x in string.ascii_lowercase for x in p ):
                  if any(x in string.digits for x in p):
                      if any(x in string.punctuation for x in p):
                        return p
                      else :
                        print(" introduire un caractere special ")
                  else:
                    print(" introduire un chiffre ")
               else:
                print(" introduire une lettre minuscule ")   
            else:
               print(" introduire une lettre majuscule ")
        else:
           print(" introduire un password de taille 8 ")


def save():
   import maskpass
   print("\n************************************Authentification***********************************")
   z=email 
   y = p
   with open("kd.txt",'w') as file :
      file.write(f"{y}et{z}")
   with open("kd.txt",'r') as fi:
      f=fi.readline().strip().split("et")[0]
   with open("kd.txt",'r') as file:
      w=file.readline().strip().split("et")[1]  
   while True:
      b=str(input("\nveuiller saisir votre email: "))
      x = maskpass.askpass("veuiller saisir votre mot de passe: ")
      if (b==w) and (x==f):
         break
      print("Erreur d'authentification.")

          
def Main():
   print("\n********Menu Principale**********")
   print("A- Jouer a la roulette")
   print("B- Decalage par cesar")
   while True:
      choix= input("\nSaisir soit A soit soit B :  ")
      if choix == 'A':
         roue2()
         break
      elif choix == 'B': 
         decal()
         break
      else:
         print("ereur de saisie. ")                  
def roue2():
  print("\na- Commencer a jouer")
  print("b- Revenir au menu principale")

  while True:
      choix1 = input("\nsaisir soit a soit b: ")
      if choix1 == 'a':
         from roulette import roue
         roue()
         break
      elif choix1 == 'b' :
         Main() 
         break
      else:
          print("erreur de saisie,saisir soit a soit b: ")
def decal():
    while True :
        print("\na- Donnez un mot a chiffrer")
        print("b- Revenir au menu principale")
        choix2= input("\nsaisir soit a soit b: ")
        if choix2 == 'a':
            mot  = input("Donnez un mot à chiffrer :")
            while True:
                try :
                    print("\n1- Cesar avec code ASCII")
                    print("2- Cesar dans les 26 lettres")
                    choix3 = int(input("\nSélectionnez l'option (1 ou 2) : "))
                    while True:
                        try : 
                            decalage = int(input("\nEntrez le décalage (un entier) : "))
                            break
                        except ValueError :
                            print("Veuillez saisir un entier\n")
                    if choix3== 1:
                        from decalag import cesar_ascii
                        cesar_ascii(mot, decalage)
                        break
                    elif choix3 == 2:
                        from decalag import cesar_lettres
                        cesar_lettres(mot, decalage)
                        break
                except ValueError:
                    print("Option invalide, veuillez choisir 1 ou 2.")   
            break   
        elif choix2 == 'b':
            Main()
            break
        else :
            print("erreur de saiSie . veuillez introduire soit a soit b") 
enregistrement()
introduire_pwd()
save()
Main()       


    