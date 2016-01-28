# Crypto
Script Python crypting message
def Alphabet():

	Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return Alphabet
	
def Afficher(Saisie):

	Indice = 0
	
	for lettre in Saisie :
		print(lettre, end='')
		Indice += 1	
		if Indice == 5 :
			print(" ", end='')
			Indice = 0
			
def Nettoyer(Saisie):	

	Reponse = ''
	for Caractere in Saisie :
		for Maj in 'AZERTYUIOPQSDFGHJKLMWXCVBN' :
			if Caractere == Maj :
				Reponse = Reponse + Caractere
		for Min in 'azertyuiopqsdfghjklmwxcvbn' :
			if Caractere == Min :
				Reponse = Reponse + Caractere.upper()
	return Reponse
	
def Menu() :
	
	while True :
	
		print("1. Choisir la clé \n")
		print("2. Chiffrer \n")
		print("3. Déchiffrer \n")
		print("4. Quitter \n")
		
		choix = int(input())
		
		if choix == 1 :
		
#	======== Création de l'Alphabet de de Substitution ========
		
			CleChiffrage = input("Clé : ")
			Substitution = ''
			for lettre in CleChiffrage :
				if lettre not in Substitution :
					Substitution += lettre
				
			DerniereLettre = Substitution[len(Substitution)-1:len(Substitution)]
			DebutRemplissage = False
	
			while len(Substitution) < 26 :
			
				for lettreAlphabet in Alphabet() :
					if DebutRemplissage == False :
						if lettreAlphabet == DerniereLettre :
							DebutRemplissage = True
					
					if DebutRemplissage == True :
						DerniereLettre = lettreAlphabet
						if lettreAlphabet not in Substitution :
							Substitution += lettreAlphabet
						
#	===========================================================
		
		if choix == 2 :
		
			Saisie = Nettoyer(input("Message à chiffrer : "))
			MessageChiffrer = ''
			
			for lettre in Saisie :
				if lettre not in Alphabet() :
					MessageChiffrer += Substitution[Substitution.index(lettre)]
	
			for lettre in Saisie :
				MessageChiffrer += Substitution[Substitution.index(lettre)]
				
			print(MessageChiffrer)
			
		if choix == 3 :
		
			Saisie = input("Message à Déchiffrer : ")
			Reponse = ''
	
		for lettre in Saisie :
			Reponse += Alphabet[Substitution]
		
		if choix == 4 :
			
			break

def Chiffrer() :

	Saisie = Nettoyer(input("Message à chiffrer : "))
	Reponse = ''
	
	for lettre in Saisie :
		if lettre not in Alphabet() :
			Reponse += Substitution[Substitution.index(lettre)]

def Dechiffrement() :

	Saisie = input("Message à Déchiffrer : ")
	Reponse = ''
	
	for lettre in Saisie :
		Reponse += Alphabet[Substitution]

Menu()
