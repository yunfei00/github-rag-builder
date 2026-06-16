---
source: dify
owner: langgenius
repo: dify
path: docs/fr-FR/README.md
url: https://github.com/langgenius/dify/blob/main/docs/fr-FR/README.md
---
Dify Cloud ·
  Auto-hébergement ·
  Documentation ·
  Présentation des différentes offres Dify

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

# 

  

Dify est une plateforme de développement d'applications LLM open source. Sa interface intuitive combine un flux de travail d'IA, un pipeline RAG, des capacités d'agent, une gestion de modèles, des fonctionnalités d'observabilité, et plus encore, vous permettant de passer rapidement du prototype à la production. Voici une liste des fonctionnalités principales:
 

**1. Flux de travail** :
Construisez et testez des flux de travail d'IA puissants sur un canevas visuel, en utilisant toutes les fonctionnalités suivantes et plus encore.

**2. Prise en charge complète des modèles** :
Intégration transparente avec des centaines de LLM propriétaires / open source offerts par dizaines de fournisseurs d'inférence et de solutions auto-hébergées, couvrant GPT, Mistral, Llama3, et tous les modèles compatibles avec l'API OpenAI. Une liste complète des fournisseurs de modèles pris en charge se trouve ici.

**3. IDE de prompt** :
Interface intuitive pour créer des prompts, comparer les performances des modèles et ajouter des fonctionnalités supplémentaires telles que la synthèse vocale à une application basée sur des chats.

**4. Pipeline RAG** :
Des capacités RAG étendues qui couvrent tout, de l'ingestion de documents à la récupération, avec un support prêt à l'emploi pour l'extraction de texte à partir de PDF, PPT et autres formats de document courants.

**5. Capacités d'agent** :
Vous pouvez définir des agents basés sur l'appel de fonctions LLM ou ReAct, et ajouter des outils pré-construits ou personnalisés pour l'agent. Dify fournit plus de 50 outils intégrés pour les agents d'IA, tels que la recherche Google, DALL·E, Stable Diffusion et WolframAlpha.

**6. LLMOps** :
Surveillez et analysez les journaux d'application et les performances au fil du temps. Vous pouvez continuellement améliorer les prompts, les ensembles de données et les modèles en fonction des données de production et des annotations.

**7. Backend-as-a-Service** :
Toutes les offres de Dify sont accompagnées d'API correspondantes, vous permettant d'intégrer facilement Dify dans votre propre logique métier.

## Utiliser Dify

- **Cloud **
  Nous hébergeons un service Dify Cloud pour que tout le monde puisse l'essayer sans aucune configuration. Il fournit toutes les capacités de la version auto-hébergée et comprend 200 appels GPT-4 gratuits dans le plan bac à sable.

- **Auto-hébergement Dify Community Edition**
  Lancez rapidement Dify dans votre environnement avec ce guide de démarrage.
  Utilisez notre documentation pour plus de références et des instructions plus détaillées.

- **Dify pour les entreprises / organisations**
  Nous proposons des fonctionnalités supplémentaires adaptées aux entreprises. Envoyez-nous un e-mail pour discuter des besoins de l'entreprise. 

  > Pour les startups et les petites entreprises utilisant AWS, consultez Dify Premium sur AWS Marketplace et déployez-le dans votre propre VPC AWS en un clic. C'est une offre AMI abordable avec la possibilité de créer des applications avec un logo et une marque personnalisés.

## Rester en avance

Mettez une étoile à Dify sur GitHub et soyez instantanément informé des nouvelles versions.

## Démarrage rapide

> Avant d'installer Dify, assurez-vous que votre machine répond aux exigences système minimales suivantes:
>
> - CPU >= 2 cœurs
> - RAM >= 4 Go

La manière la plus simple de démarrer le serveur Dify est d'exécuter notre fichier docker-compose.yml. Avant d'exécuter la commande d'installation, assurez-vous que Docker et Docker Compose sont installés sur votre machine:

```bash
cd docker
cp .env.example .env
docker compose up -d
```

Après l'exécution, vous pouvez accéder au tableau de bord Dify dans votre navigateur à http://localhost/install et commencer le processus d'initialisation.

> Si vous souhaitez contribuer à Dify ou effectuer un développement supplémentaire, consultez notre guide de déploiement à partir du code source

## Prochaines étapes

Si vous devez personnaliser la configuration, veuillez vous référer aux commentaires dans notre fichier .env.example et mettre à jour les valeurs correspondantes dans votre fichier `.env`. De plus, vous devrez peut-être apporter des modifications au fichier `docker-compose.yaml` lui-même, comme changer les versions d'image, les mappages de ports ou les montages de volumes, en fonction de votre environnement de déploiement et de vos exigences spécifiques. Après avoir effectué des modifications, veuillez réexécuter `docker-compose up -d`. Vous pouvez trouver la liste complète des variables d'environnement disponibles ici.

### Surveillance des Métriques avec Grafana

Importez le tableau de bord dans Grafana, en utilisant la base de données PostgreSQL de Dify comme source de données, pour surveiller les métriques avec une granularité d'applications, de locataires, de messages et plus.

- Tableau de bord Grafana par @bowenliang123

### Déploiement avec Kubernetes

Si vous souhaitez configurer une configuration haute disponibilité, la communauté fournit des Helm Charts et des fichiers YAML, à travers lesquels vous pouvez déployer Dify sur Kubernetes.

- Helm Chart par @LeoQuote
- Helm Chart par @BorisPolonsky
- Helm Chart par @magicsong
- Fichier YAML par @Winson-030
- Fichier YAML par @wyy-holding
- 🚀 NOUVEAU ! Fichiers YAML (compatible avec Dify v1.6.0) par @Zhoneym

#### Utilisation de Terraform pour le déploiement

Déployez Dify sur une plateforme cloud en un clic en utilisant terraform

##### Azure Global

- Azure Terraform par @nikawang

##### Google Cloud

- Google Cloud Terraform par @sotazum

#### Utilisation d'AWS CDK pour le déploiement

Déployez Dify sur AWS en utilisant CDK

##### AWS

- AWS CDK par @KevinZhao (EKS based)
- AWS CDK par @tmokmss (ECS based)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Déployez Dify en un clic sur Alibaba Cloud avec Alibaba Cloud Data Management

#### Utilisation d'Azure Devops Pipeline pour déployer sur AKS

Déployez Dify sur AKS en un clic en utilisant Azure Devops Pipeline Helm Chart by @LeoZhang

## Contribuer

Pour ceux qui souhaitent contribuer du code, consultez notre Guide de contribution.
Dans le même temps, veuillez envisager de soutenir Dify en le partageant sur les réseaux sociaux et lors d'événements et de conférences.

> Nous recherchons des contributeurs pour aider à traduire Dify dans des langues autres que le mandarin ou l'anglais. Si vous êtes intéressé à aider, veuillez consulter le README i18n pour plus d'informations, et laissez-nous un commentaire dans le canal `global-users` de notre Serveur communautaire Discord.

**Contributeurs**

  

## Communauté & Contact

- Discussion GitHub. Meilleur pour: partager des commentaires et poser des questions.
- Problèmes GitHub. Meilleur pour: les bogues que vous rencontrez en utilisant Dify.AI et les propositions de fonctionnalités. Consultez notre Guide de contribution.
- Discord. Meilleur pour: partager vos applications et passer du temps avec la communauté.
- X(Twitter). Meilleur pour: partager vos applications et passer du temps avec la communauté.

## Historique des étoiles

## Divulgation de sécurité

Pour protéger votre vie privée, veuillez éviter de publier des problèmes de sécurité sur GitHub. Au lieu de cela, envoyez vos questions à security@dify.ai et nous vous fournirons une réponse plus détaillée.

## Licence

Ce référentiel est disponible sous la Licence open source Dify, qui est essentiellement l'Apache 2.0 avec quelques restrictions supplémentaires.
