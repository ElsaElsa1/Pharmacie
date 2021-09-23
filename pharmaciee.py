class Client:
 
    def __init__(self, nom, credit):
        self.nom = nom
        self.credit = credit
 
    def affichage(self):
 
        print("Credit du client {} : {}".format(self.nom, self.credit))
 
    def approvisionnement(self, credit):
 
        self.credit += credit
 
 
 
class Medicament:
 
    def __init__(self, nom, prix, quantite):
 
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
 
 
    def affichage(self):
 
        print("quantite du medicament {} : {}".format(self.nom, self.quantite))
 
    def approvisionnement(self, quantite):
 
        self.quantite += quantite
 
 
 
class Pharmacie:
 
    def __init__(self, liste_clients, liste_medicaments):
 
        self.liste_medicaments = liste_medicaments
        self.liste_clients = liste_clients
 
    def __trouveClient(self):
 
        trouve = False
        while not trouve:
            client = input("Nom du client? ")
            for unclient in self.liste_clients:
                if unclient.nom == client:
                    trouve = True
                    break
            if not trouve:
                print("Client n'existe pas")
        return unclient
 
    def __trouveMedicament(self):
 
        trouve = False
        while not trouve:
            medicament = input("Nom du médicament? ")
            for unmedicament in self.liste_medicaments:
                if unmedicament.nom == medicament:
                    trouve = True
                    break
            if not trouve:
                print("Medicament n'existe pas")
        return unmedicament
 
    def achat(self):
 
        unclient = self.__trouveClient()
        unmedicament = self.__trouveMedicament()
        paiement = -1
        while paiement == -1:
            paiement = input("Quel le montant du paiement? ")
            
            try:
                paiement = int(paiement)
                assert paiement >= 0
            except ValueError:
                print("Rentrer un montant valide")
            except AssertionError:
                print("Rentrer un montant positif")
                paiement = -1
 
        quantite = -1

        while quantite == -1:
            quantite = input("Quel est la quantité souhaité? ")
            try:
                quantite = int(quantite)
                assert quantite >= 0
            except AssertionError:
                print("Rentrer une quantité positive")
                quantite = -1
            except ValueError:
                print("Rentrer une quantité valide")
 
        unmedicament.quantite -= quantite
        unclient.credit = unmedicament.prix * quantite - paiement
 
 
    def approvisionnement(self):
 
        unmedicament = self.__trouveMedicament()
        
        quantite = -1
        while quantite == -1 :
         quantite = input("Donner la quantité? ")
         quantite = int(quantite)
         if quantite>=0  :
             unmedicament.quantite += quantite
         else:
             print("Rentrer une quantité positive")
              
 
    def affichage(self):
 
        for i in self.liste_clients:
            i.affichage()
 
        for i in self.liste_medicaments:
            i.affichage()
 
 
 
def quitter():
    print("Programme terminé!")
    exit(0)
 
def menu():
    print("""1 : Achat de medicament
2 : Approvisionnement en liste_medicaments
3 : Etats des quantites et des credits
4 : Quitter""")
 
    while True:
        try:
            choix = int(input("Entrez votre choix: "))
            if choix in range(1, 5):
                break
        except ValueError:
            continue
 
    return choix
 
Malfichu = Client("Malfichu",0.0)
Palichon = Client("Palichon",0.0)
 
Aspiron = Medicament("Aspiron", 20.40, 5)
Rhinoplexil = Medicament("Rhinoplexil", 19.15, 5)
 
liste_clients = [Malfichu, Palichon]
liste_medicaments = [Aspiron, Rhinoplexil]
 
pharma = Pharmacie(liste_clients,liste_medicaments)
while True:
 
    choix = menu()
 
    if choix == 1:
        pharma.achat()
    elif choix == 2:
        pharma.approvisionnement()
    elif choix == 3:
        pharma.affichage()
    elif choix == 4:
        quitter()
    else:
        break





   