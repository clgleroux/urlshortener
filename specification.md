# Spécification d'application

## Objectif du document

Affin developer notre application nous alons au préalable la définir en utilisant les outils suivants.

## Description

Notre application nous permettra de partager plus simplement des URL de pages web en les hashant sur 4 caracteres pour gagner en place (comme sur Twitter par exemple). Pour se faire nous rentrons une url dans un formulaire qui nous donnera notre hash. Il y aura un notre formulaire qui nous fera l'inverse, rentrer le hash et nous redirige directement sur la page.

Se type de service est connu sous le nom d'url shortener, exemple :

- https://goo.gl/
- https://bitly.com/

## Diagrame d'interaction

[wikipedia](https://en.wikipedia.org/wiki/Unified_Modeling_Language#Interaction_diagrams)

### Creation d'une nouvelle url raccourcis

```
________                          _______________                             _______
| User |                          | Application |                             | BDD |
|______|                          |_____________|                             |_____|
   |                                     |                                       |
   |------------------------------------>|                                       |
   |  se connect à l'url du formulaire   |                                       |
   |                                     |                                       |
   |<------------------------------------|                                       |
   |  Retourne le formulaire de creation |                                       |
   |                                     |                                       |
   |------------------------------------>|                                       |
   | Renseigne et renvoie le formulaire  |                                       |
   |                                     |----                                   |
   |                                     |   |                                   |
   |                                     |   | Crée un alias pour l'url          |
   |                                     |   |                                   |
   |                                     |<---                                   |
   |                                     |                                       |
   |                                     |-------------------------------------->|
   |                                     | Enregistrer l'alias et l'url en BDD   |
   |                                     |                                       |
   |<------------------------------------|
   | Retourne l'url raccourie            |
```

### Redirection

```
________                          _______________                             _______
| User |                          | Application |                             | BDD |
|______|                          |_____________|                             |_____|
   |                                     |                                       |
   |------------------------------------>|                                       |
   |  Se connect à l'alias de l'url      |                                       |
   |                                     |                                       |
   |                                     |-------------------------------------->|
   |                                     | Recherche l'alias en database         |
   |                                     |                                       |
   |                                     |<--------------------------------------|
   |                                     | Retourne l'url d'origne               |
   |                                     |                                       |
   |<------------------------------------|
   | Redirige vers l'url d'origine       |
   |                                     |                                       |
   |                                     |<--------------------------------------|
   |                                     | Informe que l'alias n'est pas présent |
   |                                     |                                       |
   |<------------------------------------|
   | Retourne un message d'erreur 404    |
```


## Diagrame de classes

Définir les models de données avec leur champs et attributs, ainsi qu'éventulement leur methodes

Classe : URL

Attributes:

- url : textField
- alias : charField [PK, maxLength = 4]

Methode de Classe : 

- `get_or_create` (permet de creer et d'ajouter le hash si besoin)


## Points d'entrée de l'application (endpoints)

Définir les points d'entrées de l'application :

### Creation d'une nouvelle url racourcis

- HTTP Verb : POST
- Endpoint : `/new`
- Payload parameter :
	- url:String

### Redirection vers url d'origne

- HTTP Verb : GET
- Endpoint : `/<url 4 caratère alias>/`
