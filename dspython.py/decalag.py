
def cesar_ascii(texte, decalage):
    texte_chiffre = ""
    for caractere in texte:
        if caractere.isalpha():
            decalage_caractere = ord(caractere) + decalage
            if caractere.islower():
                if decalage_caractere > ord('z'):
                    decalage_caractere -= 26
            elif caractere.isupper():
                if decalage_caractere > ord('Z'):
                    decalage_caractere -= 26
            caractere_chiffre = chr(decalage_caractere)
            texte_chiffre += caractere_chiffre
        else:
            texte_chiffre += caractere
    print(f"Le mot ascii chiffre de {texte} est {texte_chiffre}")

def cesar_lettres(texte, decalage):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    texte = texte.upper()  # Convertir le texte en majuscules
    texte_chiffre = ""
    for caractere in texte:
        if caractere in alphabet:
            index = alphabet.index(caractere)
            index_chiffre = (index + decalage) % 26
            caractere_chiffre = alphabet[index_chiffre]
            texte_chiffre += caractere_chiffre
        else:
            texte_chiffre += caractere
    print(f"Le mot 26 lettres chiffre de {texte} est {texte_chiffre}")


