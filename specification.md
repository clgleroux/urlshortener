# Spécification d'application

## Objectif du document

Afin développer notre application nous allons au préalable la définir en utilisant les outils suivants.

## Description

Notre application nous permettra de partager plus simplement des URL de pages web en les hashant sur 4 caractères pour gagner en place (comme sur Twitter par exemple). Pour se faire nous rentrons une URL dans un formulaire qui nous donnera notre hash. Il y aura un notre formulaire qui nous fera l'inverse, rentrer le hash et nous redirige directement sur la page.

Se type de service est connu sous le nom d'url shortener, exemple :

- https://goo.gl/
- https://bitly.com/

## Diagramme d'interaction

[Wikipédia](https://en.wikipedia.org/wiki/Unified_Modeling_Language#Interaction_diagrams)

### Création d'une nouvelle URL raccourcis

```
________                          _______________                             _______
| User |                          | Application |                             | BDD |
|______|                          |_____________|                             |_____|
   |                                     |                                       |
   |------------------------------------>|                                       |
   |  se connect à l’URL du formulaire   |                                       |
   |                                     |                                       |
   |<------------------------------------|                                       |
   |  Retourne le formulaire de création |                                       |
   |                                     |                                       |
   |------------------------------------>|                                       |
   | Renseigne et renvoie le formulaire  |                                       |
   |                                     |----                                   |
   |                                     |   |                                   |
   |                                     |   | Crée un alias pour L’URL          |
   |                                     |   |                                   |
   |                                     |<---                                   |
   |                                     |                                       |
   |                                     |-------------------------------------->|
   |                                     | Enregistrer l'alias et l’URL en BDD   |
   |                                     |                                       |
   |<------------------------------------|                                       |
   | Retourne l’URL raccourcie            |                                       |
```

### Redirection

```
________                          _______________                             _______
| User |                          | Application |                             | BDD |
|______|                          |_____________|                             |_____|
   |                                     |                                       |
   |------------------------------------>|                                       |
   |  Se connect à l'alias de l’URL      |                                       |
   |                                     |                                       |
   |                                     |-------------------------------------->|
   |                                     | Recherche l'alias en database         |
   |                                     |                                       |
   |                                     |<--------------------------------------|
   |                                     | Retourne l’URL d’origine               |
   |                                     |                                       |
   |<------------------------------------|                                       |
   | Redirige vers l’URL d'origine       |                                       |
   |                                     |                                       |
   |                                     |<--------------------------------------|
   |                                     | Informe que l'alias n'est pas présent |
   |                                     |                                       |
   |<------------------------------------|                                       |
   | Retourne un message d'erreur 404    |                                       |
```


## Définition de classes

Définir les models de données avec leur champs et attributs, ainsi qu’éventuellement leurs méthodes

Classe : URL

Attributs:

- url : textField
- alias : charField [PK, maxLength = 4]

Méthode de Classe :

- `get_or_create` (permet de créer et d'ajouter le hash si besoin)


## Points d'entrée de l'application (endpoints)

Définir les points d'entrées de l'application :

### Création d'une nouvelle URL raccourcis

- HTTP Verb : POST
- Endpoint : `/`
- Payload parameter :
	- url:String

### Redirection vers URL d’origine

- HTTP Verb : GET
- Endpoint : `/<url 4 caractères alias>/`
