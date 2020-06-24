"""class Domino:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def affichePoints(self):
    print("Face A : "+ str(self.x) + " Face B : "+ str(self.y))

  def valeur(self):
    return self.x + self.y

d1 = Domino(5,1)
d1.affichePoints()
print(d1.valeur())"""


"""class CompteBancaire:
  def __init__(self,nom='Dupont',solde=1000):
    self.nom = nom
    self.solde = solde

  def depot(self, montant):
    self.solde+= montant

  def retrait(self, montant):
    self.solde-= montant

  def affiche(self):
    return "Le solde du compte bancaire de " + self.nom + " est de " + str(self.solde) + " euros"

cpt1 = CompteBancaire()
print(cpt1.affiche())
cpt1.depot(100)
print(cpt1.affiche())
cpt1.retrait(1000)
print(cpt1.affiche())"""


"""class Voiture:
  def __init__(self,marque='Ford',couleur='rouge'):
    self.marque = marque
    self.couleur = couleur
    self.pilote = 'Personne'
    self.vitesse = 0

  def choixConducteur(self,nom):
    self.pilote = nom

  def accelerer(self,taux, duree):
    if (self.pilote != 'Personne'):
      self.vitesse += taux*duree
      if (self.vitesse < 0):
        self.vitesse = 0
    else :
      print("Le vehicule n'as pas de conducteur")

  def afficheTout(self):
    return self.marque +" " + self.couleur + " pilotée par " + self.pilote + ", vitesse = " + str(self.vitesse) + " m/s." 

v1 = Voiture("Renault","bleue")
v1.choixConducteur("Lise")
print(v1.afficheTout())
v1.accelerer(1.3,20)
print(v1.afficheTout())"""


