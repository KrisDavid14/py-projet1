import random
def roue():
  while True:
    try:
        somme=float(input("\nentrez votre somme de depart : "))
        if somme>0:
         break
        print("saisir une somme superieur a 0")
    except ValueError:
        print("erreur de saisie")

  Continuer_partie = True
  while Continuer_partie == True:
    x=random.randrange(1000)
    while True:
      try:
        somme_mise=float(input("\nsaisir le montant a miser :  "))
        if somme_mise<=somme and somme_mise>0:
          while True:
            try:
              numero_mise=int(input("\nsaisir un numero entre 0 et 999 :  "))
              if numero_mise >=0 and numero_mise <=999:
                break
              print("saisir un nombre entre 0 et 999")
            except ValueError:
                print("erreur de saisie") 
          print(f"\nla valeur gagnante est {x}")     
          if numero_mise == x:
            print("\nfelicitations. vous avez trouve le bon numero.")
            somme= somme +(somme_mise*3)
            print(f"\nvotre solde actuel est {somme}")
            break
          elif numero_mise%2 == 0 and x%2 == 0:
            print("\nvous n'avez pas trouver le bon numero mais vous avez trouve une bonne couleur de case (rouge).")
            somme=somme+somme_mise+(somme_mise*0.5)
            print(f"\nvotre solde actuel est {somme}")
            break
          elif numero_mise%3==0 and x%3 == 0:
            print("\nvous n'avez pas trouver le bon numero mais vous avez trouve une bonne couleur de case (noir). ")  
            somme=somme+somme_mise+(somme_mise*0.5)
            print(f"\nvotre solde actuel est {somme}")  
            break   
          else:
            print("\nvous avez perdu") 
            somme=somme-somme_mise
            print(f"\nvotre solde actuel est de {somme} ")
            break 
        print(f"saisir la mise entre 0 et {somme}")    
      except ValueError:
          print("erreur de saisie")
    if somme ==0 :
      print("\nmalheureusement vous n'avez plus d'argent")
      Continuer_partie=False
      break
    else:
      while True:
        choix = input("\nvoulez-vous continuer la partie ? (oui/non): ")
        if choix == 'non' :
            Continuer_partie=False
            break
        elif choix == 'oui':
            Continuer_partie=True
            break
        else:
          print("veuillez saisir soit non soit oui")
  print(f"\nmerci d'avoir donner votre argent , ce fut un plaisir . vous repartez cependant avec {somme}") 
roue()  
 