<div align="center">

# Transfert de Hohmann

### Calculateur orbital · Python · Visualisation interactive

Explore un transfert entre deux orbites circulaires autour de la Terre : ses deux manœuvres, son coût en delta-v et son temps de vol.

[**Ouvrir le visualiseur interactif ↗**](https://you21293.github.io/transfert-de-hohmann/)

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Sans dépendance](https://img.shields.io/badge/dépendances-aucune-2E8B57)
![Modèle orbital](https://img.shields.io/badge/modèle-deux%20corps-5865F2)

</div>

---

## Le projet

Le transfert de Hohmann est une manœuvre idéale à deux impulsions. Le véhicule accélère pour rejoindre une ellipse de transfert, puis effectue une seconde impulsion à l’arrivée afin de circulariser son orbite.

Le dépôt propose deux façons d’explorer le calcul :

- **Visualiseur web** : règle les altitudes avec les curseurs ou les champs numériques et observe la géométrie du transfert ainsi que les résultats qui se mettent à jour.
- **Calculateur Python** : calcule les impulsions et la durée à partir de deux altitudes saisies en kilomètres.

## Résultats calculés

- Delta-v de l’impulsion de départ.
- Delta-v de circularisation à l’arrivée.
- Delta-v total de la manœuvre.
- Temps de vol, égal à une demi-période de l’ellipse de transfert.

## Utilisation

### Visualiseur web

Ouvre [le visualiseur interactif](https://you21293.github.io/transfert-de-hohmann/) dans un navigateur récent. Il fonctionne sans installation ni bibliothèque externe.

### Calculateur Python

Python 3.10 ou une version ultérieure est nécessaire. Depuis le dossier du projet :

```bash
python hohmann.py 200 35786
```

Les arguments sont les altitudes de départ et d’arrivée en kilomètres au-dessus de la surface terrestre. Pour calculer un transfert dans l’autre sens, inverse les deux valeurs.

## Modèle mathématique

Les rayons orbitaux sont mesurés depuis le centre de la Terre. Pour les orbites de rayons $r_1$ et $r_2$, l’ellipse de transfert a pour demi-grand axe :

$$
a_t = \frac{r_1+r_2}{2}
$$

La vitesse circulaire vaut $v_c=\sqrt{\mu/r}$. Les vitesses sur l’ellipse de transfert sont calculées avec l’équation de vis-viva :

$$
v = \sqrt{\mu\left(\frac{2}{r}-\frac{1}{a_t}\right)}
$$

Le coût total en delta-v est la somme des variations de vitesse aux deux points de manœuvre. La durée du transfert est :

$$
t = \pi\sqrt{\frac{a_t^3}{\mu}}
$$

Le calcul utilise $\mu_{\mathrm{Terre}}=398600.4418\;\mathrm{km^3/s^2}$ et un rayon terrestre moyen de $6378.1363\;\mathrm{km}$.

## Hypothèses et limites

Le modèle suppose deux orbites circulaires coplanaires et des manœuvres instantanées. Il ne prend pas en compte les pertes moteur, la traînée atmosphérique, l’aplatissement terrestre ni l’influence d’autres corps. Le schéma est volontairement **non à l’échelle** pour rendre les orbites visibles.

Les résultats sont des estimations pédagogiques à deux corps, pas un plan de mission opérationnel.

## Fichiers

| Fichier | Rôle |
|---|---|
| [`index.html`](index.html) | Visualiseur interactif autonome pour le navigateur |
| [`hohmann.py`](hohmann.py) | Calculateur Python en ligne de commande |

---

<div align="center">

Projet personnel d’apprentissage en mécanique orbitale et en programmation.

</div>
