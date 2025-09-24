Système d'Exécution de Workflows
1. Analyse du Problème
Résumé
On m'a confié la mission de développer un système permettant d'automatiser l'exécution de traitements de données récurrents. Ce système doit être capable de gérer deux types de tâches : les primitives et les workflows. Chaque tâche peut recevoir un input et renvoyer un output.

Input
Pour que le système fonctionne correctement, il est nécessaire de lui fournir les chaînes de caractères dans lesquels effectuer les recherches. Cela se fait en fournissant des instructions au programme. Les données à gérer sont des chaînes de caractères.

Output
Le résultat doit être renvoyé sous forme de données JSON affichées sur le terminal. Le résultat comprend une liste d'objets représentant les endroits où les motifs ont été trouvés dans le texte. Chaque objet contient des informations telles que le motif trouvé et sa position.

Contexte
Le développement de ce système n'est pas trivial. Il implique la gestion des cas où des arguments sont manquants, la recherche efficace des motifs, la récupération de leur position dans le texte et la mise en forme du résultat.

2. Résolution du Problème
Difficultés Rencontrées
Le processus de développement n'a pas été sans difficultés. 
Le sujet initial était assez flou, ce qui a compliqué la compréhension de certaines exigences. Par exemple, la définition des tâches primitives et des workflows était un peu vague. Il a fallu faire plusieurs aller-retours pour clarifier ces concepts et s'assurer que l'implémentation correspondait bien aux attentes.

La spécification concernant la simulation de l'exécution des tâches sans les implémenter a également posé problème. Il n'était pas clair comment réaliser cette simulation de manière efficace tout en garantissant des résultats fiables. Des discussions supplémentaires ont été nécessaires pour définir une approche adéquate.

 La description de la façon dont l'output d'un workflow devait être calculé était un peu ambiguë. Il a fallu interpréter correctement cette spécification pour s'assurer que le résultat final correspondait aux attentes du PoC.
Au départ, j'ai envisagé d'utiliser l'algorithme de Boyer-Moore, mais j'ai rapidement réalisé que ses performances ne seraient pas suffisantes. Après des recherches approfondies, j'ai opté pour l'algorithme de Knuth-Morris-Pratt (KMP).

Solution Intermédiaire
Le choix de KMP s'est avéré judicieux, mais son implémentation a nécessité un travail approfondi. J'ai dû comprendre en détail le fonctionnement de cet algorithme et trouver comment l'adapter à notre problème.

Le Principe
KMP utilise une approche intelligente en pré-traitant le motif pour créer une table de préfixe. Cela lui permet de sauter des positions dans le texte lorsqu'une correspondance partielle est trouvée. Ainsi, moins de comparaisons inutiles sont effectuées, ce qui améliore considérablement les performances.

Compléxité 
En termes de complexité, l'algorithme utilisé pour exécuter les workflows a une complexité temporelle de O(n + m), où n est le nombre total de tâches et m est la taille du workflow le plus long. Cette complexité est relativement efficace, surtout lorsque les workflows sont composés principalement de tâches primitives.

3. Évaluation de la Solution
Défis Continus
Malgré la mise en place de KMP, quelques problèmes sont survenus lors des tests. Certains cas particuliers n'étaient pas correctement gérés. Cependant, avec du débogage et des tests approfondis, j'ai réussi à corriger ces erreurs.

Conclusion
Dans l'ensemble, les résultats obtenus sont satisfaisants et l'algorithme se comporte bien avec différentes données d'entrée. KMP s'est avéré être un choix judicieux en termes de performances et d'efficacité, malgré les défis rencontrés lors du développement.