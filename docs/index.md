# Présentation

L'objectif de ce projet est de dimensionner une cuve de récupération d'eau de pluie.

## Contexte

On étudie ici un hameau non raccordé au réseau d'eau, dont l'approvisionnement dépend entièrement d'une source. Par le passé, en période de sécheresse, celle-ci a vu son débit diminuer jusqu'à être quasiment nul. Aussi l'augmentation de la fréquence, l'intensité et la longueur des épisodes secs impose-t-il de réduire les usages et d'améliorer la conservation.

Une voie trouvée est de récupérer et stocker les eaux pluviales.

Ce procédé n'est pas nouveau : l'empereur Justinien en son temps faisait déjà construire une citerne de plusieurs milliers de mètres cubes près de Sainte-Sophie ; et dans les années 1870 le réservoir de Montsouris permettait à Paris d'être approvisionné en eau potable.

Plus modestement, l'objectif est ici de reproduire une citerne comme en faisaient les vénitiens :

![Coupe citerne Venise](assets/images/citerne-venise.jpg)

## Problématique

On cherche à déterminer le volume minimal de la cuve tel qu'elle puisse stocker suffisamment d'eau pour couvrir les besoins annuels, actuels *et* futurs.

## Protocole

### Paramètres

Le volume de la cuve dépend de trois paramètres :

* la pluviométrie ;
* la surface de récupération ;
* les usages.

### Modélisation

On prendra ici comme pas de temps la journée.

La surface est constante.
Les usages sont lissés et sont considérés comme ne présentant pas de variabilité d'une année sur l'autre.

La pluviométrie, elle, est considérée comme variable.
Dans un premier temps on simulera une année moyenne, puis on introduira des variations en intensité et en répartition des pluies.

## Données

Les données utilisées proviennent de Météo France pour la pluviométrie[@climat-clermont], le reste est donné par les propriétaires.
