from math import sqrt
from upemtk import *

# SAVANE Kévin, Groupe TP7
# TP4

RAYON = 4

# Initialisation et mise à jour de la fenetre
def initialise_fenetre():
	""" Fonction initialisant la fenetre principale crée par upemtk """
	#Creation de la fenetre et des cadres dans la fenetre
	cree_fenetre(1200, 800)
	rectangle(800, 0, 1200, 800, remplissage = '#00ffff')
	rectangle(0, 600, 800, 800, remplissage = '#00dddd')
	#Creation des boutons
	rectangle(860, 35, 1140, 85, remplissage = 'light grey')
	texte(1000, 60, "Ajouter un point", couleur = 'black', ancrage = 'center')
	rectangle(860, 120, 1140, 170, remplissage = 'light grey')
	texte(1000, 145, "Supprimer un point", couleur = 'black', ancrage = 'center')
	rectangle(860, 205, 1140, 255, remplissage = 'light grey')
	texte(1000, 230, "Selectionner un point", couleur = 'black', ancrage = 'center')
	rectangle(860, 290, 1140, 340, remplissage = 'light grey')
	texte(1000, 315, "Avancer d'un cran", couleur = 'black', ancrage = 'center')
	rectangle(860, 375, 1140, 425, remplissage = 'light grey')
	texte(1000, 400, "Reculer d'un cran", couleur = 'black', ancrage = 'center')
	rectangle(860, 460, 1140, 510, remplissage = 'light grey')
	texte(1000, 485, "Deplacer un point", couleur = 'black', ancrage = 'center')
	rectangle(860, 545, 1140, 595, remplissage = 'light grey')
	texte(1000, 570, "Tracer la courbe", couleur = 'black', ancrage = 'center')
	rectangle(860, 630, 1140, 680, remplissage = 'light grey')
	texte(1000, 655, "Effacer la courbe", couleur = 'black', ancrage = 'center')
	rectangle(860, 715, 1140, 765, remplissage = 'light grey')
	texte(1000, 740, "Quitter", couleur = 'black', ancrage = 'center')

def maj(points, present, pos_pt_select):
	""" Fonction mettant à jour la fenetre principale du programme

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	:Param present: booleen, indiquant si la courbe de Bezier est affichée ou non
	:Param pos_pt_select: int, indiquant la position dans la liste des points de contrôle
						  celui qui est actuellement selectionné
	"""
	rectangle(0, 0, 800, 600, remplissage = 'white')
	rectangle(0, 600, 800, 800, remplissage = '#00dddd')
	trace_points(points)
	if present:
		tracer(points)
	if pos_pt_select != -1:
		cercle(20 * (pos_pt_select + 1), 700, 8, couleur = 'red')

# Fonctions liées aux boutons
def ajoute_point(points, present, couleurs, pos_pt_select):
	""" Fonction permettant d'ajouter un point de contrôle à la courbe de Bezier

	Un point est représenté par un triplet composé de ses deux coordonnées et d'une
	couleur (ie une chaine de caractère).
	A l'issue de l'appel de cette fonction, la liste points est augmentée d'un point,
	tandis que la liste couleurs sera amputée de son premier éléments.

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	:Param present: booleen, indiquant si la courbe de Bezier est affichée ou non
	:Param couleurs: liste de string, représentant les couleurs encore disponibles
	:Param pos_pt_select: int, indiquant la position dans la liste des points de contrôle
						  celui qui est actuellement selectionné
	"""
	x, y, t = attente_clic()
	while not (0 <= x <= 800 and 0 <= y <= 600):
		x, y, t = attente_clic()
	points.append((x, y, couleurs[0]))
	couleurs.pop(0)

def selectionne_point(points, present):
	""" Fonction permettant de selectionner un point de contrôle de la courbe de Bezier

	Un point selectionné sera entouré dans la liste donnant l'ordre des points de controle.
	Un seul point peut être selectionné en même temps.

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	:Param present: booleen, indiquant si la courbe de Bezier est affichée ou non
	:Return value: int, qui est l'indice dans la liste des points de contrôle
				   du point selectionné par l'utilisateur
	"""
	x, y, t = attente_clic()
	while not (0 <= x <= 800 and 0 <= y <= 600):
		x, y, t = attente_clic()
	pos = 0
	while pos < len(points) and distance(points[pos], (x, y)) > RAYON + 1:
		pos += 1
	return pos

def supprime_point(points, present, pos_pt_select):
	""" Fonction permettant de supprimer un point de contrôle de la courbe de Bezier

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	:Param present: booleen, indiquant si la courbe de Bezier est affichée ou non
	:Param pos_pt_select: int, indiquant la position dans la liste des points de contrôle
						  celui qui est actuellement selectionné
	:Return value: int, qui est l'indice dans la liste des points de contrôle
				   du point supprimé par l'utilisateur
	"""
	pos = selectionne_point(points, present)
	if pos < len(points):
		points.pop(pos)
		if pos == pos_pt_select:
			return -1
		else:
			return pos_pt_select

def entoure(points, present, pos_pt_select):
	""" Fonction permettant d'entourer le point contrôle de la courbe de Bezier selectionné 
	dans la liste donnant l'ordre des points de controle.

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	:Param present: booleen, indiquant si la courbe de Bezier est affichée ou non
	:Param pos_pt_select: int, indiquant la position dans la liste des points de contrôle
						  celui qui est actuellement selectionné
	:Return value: int, qui est l'indice dans la liste des points de contrôle
				   du point selectionné par l'utilisateur
	"""
	select_avant = pos_pt_select
	pos_pt_select = selectionne_point(points, present)
	if pos_pt_select < len(points):
		cercle(20 * (pos_pt_select + 1), 700, 2 * RAYON, couleur = 'red')
		return pos_pt_select
	else:
		return select_avant

def avance_d_un_cran(points, pos_pt_select):
	""" Fonction permettant d'echanger le point contrôle selectionné 
	de la courbe de Bezier avec le suivant dans la liste donnant l'ordre
	des points de controle.

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	:Param pos_pt_select: int, indiquant la position dans la liste des points de contrôle
						  celui qui est actuellement selectionné
	:Return value: int, qui est l'indice dans la liste des points de contrôle
				   du point selectionné par l'utilisateur
	"""
	if pos_pt_select < len(points) - 1:
		tmp = points[pos_pt_select]
		points[pos_pt_select] = points[pos_pt_select + 1]
		points[pos_pt_select + 1] = tmp
		return pos_pt_select + 1
	else:
		return pos_pt_select

def reculer_d_un_cran(points, pos_pt_select):
	""" Fonction permettant d'echanger le point de contrôle selectionné 
	de la courbe de Bezier avec le précédent dans la liste donnant l'ordre
	des points de controle.

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	:Param pos_pt_select: int, indiquant la position dans la liste des points de contrôle
						  celui qui est actuellement selectionné
	:Return value: int, qui est l'indice dans la liste des points de contrôle
				   du point selectionné par l'utilisateur
	"""
	if pos_pt_select > 0:
		tmp = points[pos_pt_select]
		points[pos_pt_select] = points[pos_pt_select - 1]
		points[pos_pt_select - 1] = tmp
		return pos_pt_select - 1
	else:
		return pos_pt_select

def glisser(points, pos_pt_select):
	""" Fonction permettant de déplacer le point de contrôle selectionné 
	de la courbe de Bezier.

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	:Param pos_pt_select: int, indiquant la position dans la liste des points de contrôle
						  celui qui est actuellement selectionné
	"""
	x, y, t = attente_clic()
	while not (0 <= x <= 800 and 0 <= y <= 600):
		x, y, t = attente_clic()
	points[pos_pt_select] = (x, y, points[pos_pt_select][2])

def tracer(points):
	""" Fonction permettant de tracer la courbe de Bezier dont les points de contrôle
	sont ceux qui sont dans la liste points.

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	"""
	bezier_casteljau(points)

# Fonctions préliminaires sur les points

def milieu(A, B):
	""" Fonction calculant le milieu des points A et B

	:Param A: couple de la forme (x, y) ou triplet de la forme (x, y, couleur)
			  où x et y sont les coordonnées de A
	:Param B: couple de la forme (x, y) ou triplet de la forme (x, y, couleur)
			  où x et y sont les coordonnées de B
	:Return Value: couple de la forme (x, y) où x et y sont les coordonnées du
				   milieu de A et de B
	"""
	return (A[0]+B[0])/2, (A[1]+B[1])/2


def distance(A, B):
	""" Fonction calculant la distance du point A au point B en utilisant la fonction
	sqrt du module math

	:Param A: couple de la forme (x, y) ou triplet de la forme (x, y, couleur)
			  où x et y sont les coordonnées de A
	:Param B: couple de la forme (x, y) ou triplet de la forme (x, y, couleur)
			  où x et y sont les coordonnées de B
	:Return Value: floattant
	"""
	return sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)

# Fonctions préliminaires sur les listes de points

def trace_points(points):
	""" Fonction dessinant en upemtk :
	* tous les points de contrôle de la courbe de Bezier dans la zone de dessin
	* l'ordre des points de contrôle de la courbe de Bezier en dessous de la zone de dessin
	Le lien d'un point de la zone de dessin à la zone en dessous se fait par la couleur
	des points.

	:Param points: liste de points, représentant la liste 
				   des points de contrôle de la courbe de Bezier 
	"""
	for pos in range(len(points)):
		cercle(points[pos][0], points[pos][1], RAYON,
			   epaisseur = RAYON, couleur = points[pos][2])
		cercle(20 * (pos + 1), 700, RAYON,
			   epaisseur = RAYON, couleur = points[pos][2]) 

def trace_ligne_brisee(points):
	""" Fonction dessinant en upemtk la ligne brisée passant par tous les points
	de la liste 'points' dans l'ordre de lecture de la liste

	:Param points: liste de points, ie liste de couples ou de triplets
	"""
	for position in range(len(points)-1):
		ligne(points[position][0], points[position][1], points[position+1][0], points[position+1][1], "red")

def distance_max(points):
	""" Fonction déterminant la distance maximale entre deux points successifs 
	de la liste 'points' dans l'ordre de lecture de la liste

	:Param points: liste de points, ie liste de couples ou de triplets
	:Return value: floattant
	"""
	max = distance(points[0], points[1])
	for pos in range(1, len(points) - 1):
		d = distance(points[pos], points[pos + 1])
		if d > max:
			max = d
	return max

# Implémentation de l'algorithme de Casteljau pour la construction d'une courbe de Bézier

def calculs_milieu_suites_points(points):
	""" Fonction déterminant les milieux de tous les couples de points successifs 
	dans la liste 'points'

	:Param points: liste de points, ie liste de couples ou de triplets
	:Return value: liste de points, plus précisément liste de couples de la forme (x, y)
	"""
	# indice = 1
	# listMilieu = []
	# while i < len(points):
	# 	milieu = milieu(points[i-1], points[i])
	# 	listMilieu.append(milieu)
	# 	i += 1
	# return listMilieu

	if len(points) == 1:
		return []

	else:
		middle = milieu(points[-1], points[-2])
		listeMilieu = calculs_milieu_suites_points(points[:-1])
		listeMilieu.append(middle)
		return listeMilieu


def etape_casteljau(points):
	""" Fonction calculant les points P_i^j, où :
	* les points P_i^0, 0 <= i <= N, sont les points de controles de la courbe de Bezier,
	c'est-à-dire les points de la liste 'points'
	* le point P_i^j, si 0 < j <= N, est le milieu du segement reliant P_i^(j-1) à P_(i+1)^(j-1)

	:Param points: liste de points, ie liste de couples ou de triplets
	:Return value: couple de liste de points dont la première est la liste des P_0^i et
				   la seconde est la liste des P_i^(N-i)
	"""

	# etape_casteljau en récursif non fonctionnel
	# Problème: En plaçant les points et en traçant la courbe, seul le centre de gravité apparaissait. Je n'ai pas réussi à corriger le problème,
	# mais je pense que l'appel sur le tracé de courbe se fait uniquement sur une liste contenant le dernier milieu calculé, celui au sommet du triangle de point
	# de l'énoncé

	# if len(points) == 1:
	# 	return points, points

	# else:
	# 	liste = calculs_milieu_suites_points(points)
	# 	listeFin, listeDebut = etape_casteljau(liste)
	# 	listeFin.append(liste[-1])
	# 	listeDebut.append(liste[0])
	# 	return listeFin, listeDebut

	# etape_casteljau en intératif

	listeDebut = []
	listeFin = []

	if len(points) == 1:
		return points, points

	else:
		for compteur in range(len(points)):
			listeDebut.append(points[0])
			listeFin.append(points[-1])
			points = calculs_milieu_suites_points(points)

	return listeFin, listeDebut
		

def bezier_casteljau(points):
	""" Fonction dessinant la courbe de Bezier dont les points de la liste 'points'
	sont les points de controle de la courbe que la fonction dessine

	Cette fonction est récursive.
	-> Tant que la distance maximale entre deux points de controle successifs
	est "grande", on applique l'étape de Casteljau et on dessine alors la courbe
	de Bezier sur les deux familles de points de controle qu'elle produit.
	-> Si la distance maximale entre deux points de controle successifs
	est "petite", on dessine la ligne brisée joignant les points de controle.

	:Param points: liste de points, ie liste de couples ou de triplets
	"""
	if distance_max(points) <= 1:
		trace_ligne_brisee(points)

	else:
		listeFin, listeDebut = etape_casteljau(points)
		bezier_casteljau(listeFin)
		bezier_casteljau(listeDebut)
		





# Programme principal

if __name__ == '__main__':

	points = []
	present = False
	initialise_fenetre()
	pos_pt_select = -1
	couleurs = ['#000000', '#0000FF', '#FF00FF', '#008000', '#808080', '#00FF00', '#800000', 
				'#000080', '#808000', '#800080', '#FF0000', '#C0C0C0', '#008080', '#FFFF00']
	while True:
		maj(points, present, pos_pt_select)
		if couleurs == []:
			couleurs = ['#000000', '#0000FF', '#FF00FF', '#008000', '#808080', '#00FF00',
						'#800000', '#000080', '#808000', '#800080', '#FF0000', '#C0C0C0',
						'#008080', '#FFFF00']
		x, y, t = attente_clic()
		if 860 <= x <= 1140 and 35 <= y <= 85:
			ajoute_point(points, present, couleurs, pos_pt_select)
		if 860 <= x <= 1140 and 120 <= y <= 170:
			if len(points) >= 1:
				pos_pt_select = supprime_point(points, present, pos_pt_select)
		if 860 <= x <= 1140 and 205 <= y <= 255:
			if len(points) >= 1:
				pos_pt_select = entoure(points, present, pos_pt_select)
		if 860 <= x <= 1140 and 290 <= y <= 340:
			pos_pt_select = avance_d_un_cran(points, pos_pt_select)
		if 860 <= x <= 1140 and 375 <= y <= 425:
			pos_pt_select = reculer_d_un_cran(points, pos_pt_select)
		if 860 <= x <= 1140 and 460 <= y <= 510:
			glisser(points, pos_pt_select)
		if 860 <= x <= 1140 and 545 <= y <= 595:
			tracer(points)
			present = True
		if 860 <= x <= 1140 and 630 <= y <= 680:
			present = False
			maj(points, present, pos_pt_select)
		if 860 <= x <= 1140 and 715 <= y <= 765:
			break
	ferme_fenetre()
