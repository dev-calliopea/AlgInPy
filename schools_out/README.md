1. Analyse du problème : 
Résumé : Il s'agit de déterminer le nombre minimal (et donc optimal) de salles nécessaires au déroulement de sessions d'activités sur une journée pour une école.

Input : Le chemin du fichier de sessions d'activités est passé en premier argument du programme. Il s'agit d'un fichier au format JSON.

Output : Le résultat (ie, le nombre minimal de salles nécessaires) doit être affiché sur la sortie standard du terminal et doit être un objet JSON.

Contexte : L'envoie de données concernant les sessions d'activités d'une journée doit permettre de connaître rapidemment le nombre minimal d'ouverture de salles de clases.

L'analyse du contexte du problème nous permet de comprendre que : 
- Il faut ouvrir et lire le fichier de données 
- Prévenir d'un fichier corrompu, manquant ou vide 
- Stocker certaines informations pour pouvoir comparer les sessions aux horaires des classes ouvertes 
- Retourner le nombre minimal de classes à ouvrir dans un objet JSON


2. Résolution du problème :
Pour déterminer la solution algorithmique à implémenter, il s'agit de comprendre quelle est la condition de l'ouverture d'une nouvelle salle de classe. 
Cette condition nous permet de savoir quelles informaitons il est nécessaire de garder en mémoire pour effectuer les tests de comparaison entre les sessions et les salles de classes. 

Condition d'une ouverture de salle de classe : 
- Une nouvelle classe est ouverte si une session commence à l'heure ou après l'heure de fin d'une session : 
 session['start'] >= end_time[session]

À garder en mémoire :
-  Les horaires de fin de session des classes ouvertes 
-  Les classes ouvertes 

Solution intermédiaire : 
Ma première intuition fut la bonne bien que je n'effectuais pas le bon test et j'ajoutais de la complexité en : 
- Ajoutant moi-même la première session dans le tableau de salle de classes 
- Supprimant ensuite la première session du tableau d'entrée de sessions 
- En construisant un tableau d'objets de salles de classes complexes et coûteux car j'ajoutais toutes les sessions aux salles de classes 
    classrooms = [
        "class" : 1
        "sessions" : {
            "start":
            "end":
            "session_name":
            "teacher_name":
        }, 
        ...
    ]


3. Évaluer la solution
Correction : Les résultats sont corrects et l'algorithme fonctionne avec une multitutes de données entrées différentes. 

Complexité : 
La complexité de l'algorithme réside dans le tri du tableau de session par ordre croissant d'heure de début de session. 
Aussi, elle est directement dépendante de la taille du fichier qui est difficile à gérer tant elle est aléatoire et conditionnée au fichier donné en argument du programme. 
--> Ajouter une condition pour diviser le fichier s'il dépasse une certaine taille ? 

Toutefois, la complexité spatiale est assez bien gérée puisque l'algorithme ne retient en mémoire que les sessions qui donnent lieu à des ouvertures de salles. Comme il s'agit du nombre minimal, l'algorithme garde en mémoire le nombre d'informations minimum pour effectuer des tests de comparaison.

Sensibilité aux données d'entrées : 
L'algorithme prévient des risques de fichier manquant, vide ou corrompu. 

Adaptabilité aux données d'entrés : 
Ensuite, grâce à son test sur les heures de début des nouvelles sessions et de fin de sessions dans une salle, l'algorithme prévient (ou anticipe) d'un changement possible sur les plages horaires des sessions entrées. 


Critères : 
- Correction (les résultats sont-ils corrects en terme d'allocations de salles) :
- Optimalité (comparaison avec une solution connue et optimale):
- Complexité temporalle et spatiale : 
- Scénarii de tests variés : 
- Sensibilité aux données d'entrées : 
- Adaptabilité aux contraintes supplémentaires éventuelles : 







