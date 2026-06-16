---
source: dify
owner: langgenius
repo: dify
path: docs/it-IT/README.md
url: https://github.com/langgenius/dify/blob/main/docs/it-IT/README.md
---
📌 Introduzione a Dify Workflow File Upload: ricreando il podcast di Google NotebookLM

  Dify Cloud ·
  Self-Hosted ·
  Documentazione ·
  Panoramica dei prodotti Dify

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

Dify è una piattaforma open-source per lo sviluppo di applicazioni LLM. La sua interfaccia intuitiva combina flussi di lavoro AI basati su agenti, pipeline RAG, funzionalità di agenti, gestione dei modelli, funzionalità di monitoraggio e altro ancora, permettendovi di passare rapidamente da un prototipo alla produzione.

## Avvio Rapido

> Prima di installare Dify, assicuratevi che il vostro sistema soddisfi i seguenti requisiti minimi:
>
> - CPU >= 2 Core
> - RAM >= 4 GiB

Il modo più semplice per avviare il server Dify è tramite docker compose. Prima di eseguire Dify con i seguenti comandi, assicuratevi che Docker e Docker Compose siano installati sul vostro sistema:

```bash
cd dify
cd docker
cp .env.example .env
docker compose up -d
```

Dopo aver avviato il server, potete accedere al dashboard di Dify tramite il vostro browser all'indirizzo http://localhost/install e avviare il processo di inizializzazione.

#### Richiedere Aiuto

Consultate le nostre FAQ se riscontrate problemi durante la configurazione di Dify. Contattateci tramite la community se continuano a verificarsi difficoltà.

> Se desiderate contribuire a Dify o effettuare ulteriori sviluppi, consultate la nostra guida al deployment dal codice sorgente.

## Caratteristiche Principali

**1. Workflow**:
Create e testate potenti flussi di lavoro AI su un'interfaccia visuale, utilizzando tutte le funzionalità seguenti e oltre.

**2. Supporto Completo dei Modelli**:
Integrazione perfetta con centinaia di LLM proprietari e open-source di decine di provider di inferenza e soluzioni self-hosted, che coprono GPT, Mistral, Llama3 e tutti i modelli compatibili con l'API OpenAI. L'elenco completo dei provider di modelli supportati è disponibile qui.

**3. Prompt IDE**:
Interfaccia intuitiva per creare prompt, confrontare le prestazioni dei modelli e aggiungere funzionalità aggiuntive come text-to-speech in un'applicazione basata su chat.

**4. Pipeline RAG**:
Funzionalità RAG complete che coprono tutto, dall'acquisizione dei documenti alla loro interrogazione, con supporto pronto all'uso per l'estrazione di testo da PDF, PPT e altri formati di documenti comuni.

**5. Capacità degli Agenti**:
Potete definire agenti basati su LLM Function Calling o ReAct e aggiungere strumenti predefiniti o personalizzati per l'agente. Dify fornisce oltre 50 strumenti integrati per gli agenti AI, come Google Search, DALL·E, Stable Diffusion e WolframAlpha.

**6. LLMOps**:
Monitorate e analizzate i log delle applicazioni e le prestazioni nel tempo. Potete migliorare continuamente prompt, dataset e modelli basandovi sui dati di produzione e sulle annotazioni.

**7. Backend-as-a-Service**:
Tutte le offerte di Dify sono dotate di API corrispondenti, permettendovi di integrare facilmente Dify nella vostra logica di business.

## Utilizzo di Dify

- **Cloud **
  Ospitiamo un servizio Dify Cloud che chiunque può provare senza configurazione. Offre tutte le funzionalità della versione self-hosted e include 200 chiamate GPT-4 gratuite nel piano sandbox.

- **Dify Community Edition Self-Hosted**
  Avviate rapidamente Dify nel vostro ambiente con questa guida di avvio rapido. Utilizzate la nostra documentazione per ulteriori informazioni e istruzioni dettagliate.

- **Dify per Aziende / Organizzazioni**
  Offriamo funzionalità aggiuntive specifiche per le aziende. Potete scriverci via email per discutere le vostre esigenze aziendali. 

  > Per startup e piccole imprese che utilizzano AWS, date un'occhiata a Dify Premium su AWS Marketplace e distribuitelo con un solo clic nel vostro AWS VPC. Si tratta di un'offerta AMI conveniente con l'opzione di creare app con logo e branding personalizzati.

## Resta Sempre Aggiornato

Mettete una stella a Dify su GitHub e ricevete notifiche immediate sui nuovi rilasci.

## Configurazioni Avanzate

Se dovete personalizzare la configurazione, leggete i commenti nel nostro file .env.example e aggiornate i valori corrispondenti nel vostro file `.env`. Inoltre, potrebbe essere necessario apportare modifiche al file `docker-compose.yaml`, come cambiare le versioni delle immagini, le mappature delle porte o i mount dei volumi, a seconda del vostro ambiente di distribuzione specifico e dei vostri requisiti. Dopo aver apportato le modifiche, riavviate `docker-compose up -d`. L'elenco completo delle variabili d'ambiente disponibili è disponibile qui.

### Monitoraggio delle Metriche con Grafana

Importate la dashboard in Grafana, utilizzando il database PostgreSQL di Dify come origine dati, per monitorare le metriche a livello di app, tenant, messaggi e altro ancora.

- Dashboard Grafana di @bowenliang123

### Distribuzione con Kubernetes

Se desiderate configurare un'installazione ad alta disponibilità, ci sono Helm Charts e file YAML forniti dalla community che consentono di distribuire Dify su Kubernetes.

- Helm Chart di @LeoQuote
- Helm Chart di @BorisPolonsky
- Helm Chart di @magicsong
- File YAML di @Winson-030
- File YAML di @wyy-holding
- 🚀 NUOVO! File YAML (Supporta Dify v1.6.0) di @Zhoneym

#### Utilizzo di Terraform per la Distribuzione

Distribuite Dify con un solo clic su una piattaforma cloud utilizzando terraform.

##### Azure Global

- Azure Terraform di @nikawang

##### Google Cloud

- Google Cloud Terraform di @sotazum

#### Utilizzo di AWS CDK per la Distribuzione

Distribuzione di Dify su AWS con CDK

##### AWS

- AWS CDK di @KevinZhao (basato su EKS)
- AWS CDK di @tmokmss (basato su ECS)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Distribuzione con un clic di Dify su Alibaba Cloud con Alibaba Cloud Data Management

#### Utilizzo di Azure DevOps Pipeline per la Distribuzione su AKS

Distribuite Dify con un clic in AKS utilizzando Azure DevOps Pipeline Helm Chart di @LeoZhang

## Contribuire

Se desiderate contribuire con codice, leggete la nostra Guida ai Contributi. Allo stesso tempo, vi chiediamo di supportare Dify condividendolo sui social media e presentandolo a eventi e conferenze.

> Cerchiamo collaboratori che aiutino a tradurre Dify in altre lingue oltre al mandarino o all'inglese. Se siete interessati a collaborare, leggete il README i18n per ulteriori informazioni e lasciate un commento nel canale `global-users` del nostro server della community Discord.

## Community & Contatti

- GitHub Discussion. Ideale per: condividere feedback e porre domande.
- GitHub Issues. Ideale per: bug che riscontrate durante l'utilizzo di Dify.AI e proposte di funzionalità. Consultate la nostra Guida ai Contributi.
- Discord. Ideale per: condividere le vostre applicazioni e interagire con la community.
- X(Twitter). Ideale per: condividere le vostre applicazioni e interagire con la community.

**Collaboratori**

  

## Storia delle Stelle

## Divulgazione sulla Sicurezza

Per proteggere la vostra privacy, evitate di pubblicare problemi di sicurezza su GitHub. Inviate invece le vostre domande a security@dify.ai e vi forniremo una risposta più dettagliata.

## Licenza

Questo repository è disponibile sotto la Dify Open Source License, che è essenzialmente Apache 2.0 con alcune restrizioni aggiuntive.
