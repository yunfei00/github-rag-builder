---
source: dify
owner: langgenius
repo: dify
path: docs/de-DE/README.md
url: https://github.com/langgenius/dify/blob/main/docs/de-DE/README.md
---
📌 Einführung in Dify Workflow File Upload: Google NotebookLM Podcast nachbilden

  Dify Cloud ·
  Selbstgehostetes ·
  Dokumentation ·
  Überblick über die Dify-Produkte

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

Dify ist eine Open-Source-Plattform zur Entwicklung von LLM-Anwendungen. Ihre intuitive Benutzeroberfläche vereint agentenbasierte KI-Workflows, RAG-Pipelines, Agentenfunktionen, Modellverwaltung, Überwachungsfunktionen und mehr, sodass Sie schnell von einem Prototyp in die Produktion übergehen können.

## Schnellstart

> Bevor Sie Dify installieren, stellen Sie sicher, dass Ihr System die folgenden Mindestanforderungen erfüllt:
>
> - CPU >= 2 Core
> - RAM >= 4 GiB

Der einfachste Weg, den Dify-Server zu starten, ist über docker compose. Stellen Sie vor dem Ausführen von Dify mit den folgenden Befehlen sicher, dass Docker und Docker Compose auf Ihrem System installiert sind:

```bash
cd dify
cd docker
cp .env.example .env
docker compose up -d
```

Nachdem Sie den Server gestartet haben, können Sie über Ihren Browser auf das Dify Dashboard unter http://localhost/install zugreifen und den Initialisierungsprozess starten.

#### Hilfe suchen

Bitte beachten Sie unsere FAQ, wenn Sie Probleme bei der Einrichtung von Dify haben. Wenden Sie sich an die Community und uns, falls weiterhin Schwierigkeiten auftreten.

> Wenn Sie zu Dify beitragen oder zusätzliche Entwicklungen durchführen möchten, lesen Sie bitte unseren Leitfaden zur Bereitstellung aus dem Quellcode.

## Wesentliche Merkmale

**1. Workflow**:
Erstellen und testen Sie leistungsstarke KI-Workflows auf einer visuellen Oberfläche, wobei Sie alle der folgenden Funktionen und darüber hinaus nutzen können.

**2. Umfassende Modellunterstützung**:
Nahtlose Integration mit Hunderten von proprietären und Open-Source-LLMs von Dutzenden Inferenzanbietern und selbstgehosteten Lösungen, die GPT, Mistral, Llama3 und alle mit der OpenAI API kompatiblen Modelle abdecken. Eine vollständige Liste der unterstützten Modellanbieter finden Sie hier.

**3. Prompt IDE**:
Intuitive Benutzeroberfläche zum Erstellen von Prompts, zum Vergleichen der Modellleistung und zum Hinzufügen zusätzlicher Funktionen wie Text-to-Speech in einer chatbasierten Anwendung.

**4. RAG Pipeline**:
Umfassende RAG-Funktionalitäten, die alles von der Dokumenteneinlesung bis zur -abfrage abdecken, mit sofort einsatzbereiter Unterstützung für die Textextraktion aus PDFs, PPTs und anderen gängigen Dokumentformaten.

**5. Fähigkeiten des Agenten**:
Sie können Agenten basierend auf LLM Function Calling oder ReAct definieren und vorgefertigte oder benutzerdefinierte Tools für den Agenten hinzufügen. Dify stellt über 50 integrierte Tools für KI-Agenten bereit, wie zum Beispiel Google Search, DALL·E, Stable Diffusion und WolframAlpha.

**6. LLMOps**:
Überwachen und analysieren Sie Anwendungsprotokolle und die Leistung im Laufe der Zeit. Sie können kontinuierlich Prompts, Datensätze und Modelle basierend auf Produktionsdaten und Annotationen verbessern.

**7. Backend-as-a-Service**:
Alle Dify-Angebote kommen mit entsprechenden APIs, sodass Sie Dify mühelos in Ihre eigene Geschäftslogik integrieren können.

## Dify verwenden

- **Cloud **
  Wir hosten einen Dify Cloud-Service, den jeder ohne Einrichtung ausprobieren kann. Er bietet alle Funktionen der selbstgehosteten Version und beinhaltet 200 kostenlose GPT-4-Aufrufe im Sandbox-Plan.

- **Selbstgehostete Dify Community Edition**
  Starten Sie Dify schnell in Ihrer Umgebung mit diesem Schnellstart-Leitfaden. Nutzen Sie unsere Dokumentation für weiterführende Informationen und detaillierte Anweisungen.

- **Dify für Unternehmen / Organisationen**
  Wir bieten zusätzliche, unternehmensspezifische Funktionen. Über diesen Chatbot können Sie uns Ihre Fragen mitteilen oder senden Sie uns eine E-Mail, um Ihre unternehmerischen Bedürfnisse zu besprechen. 

  > Für Startups und kleine Unternehmen, die AWS nutzen, schauen Sie sich Dify Premium on AWS Marketplace an und stellen Sie es mit nur einem Klick in Ihrer eigenen AWS VPC bereit. Es handelt sich um ein erschwingliches AMI-Angebot mit der Option, Apps mit individuellem Logo und Branding zu erstellen.

## Immer einen Schritt voraus

Star Dify auf GitHub und lassen Sie sich sofort über neue Releases benachrichtigen.

## Erweiterte Einstellungen

Falls Sie die Konfiguration anpassen müssen, lesen Sie bitte die Kommentare in unserer .env.example-Datei und aktualisieren Sie die entsprechenden Werte in Ihrer `.env`-Datei. Zusätzlich müssen Sie eventuell Anpassungen an der `docker-compose.yaml`-Datei vornehmen, wie zum Beispiel das Ändern von Image-Versionen, Portzuordnungen oder Volumen-Mounts, je nach Ihrer spezifischen Einsatzumgebung und Ihren Anforderungen. Nachdem Sie Änderungen vorgenommen haben, starten Sie `docker-compose up -d` erneut. Eine vollständige Liste der verfügbaren Umgebungsvariablen finden Sie hier.

### Metriküberwachung mit Grafana

Importieren Sie das Dashboard in Grafana, wobei Sie die PostgreSQL-Datenbank von Dify als Datenquelle verwenden, um Metriken in der Granularität von Apps, Mandanten, Nachrichten und mehr zu überwachen.

- Grafana-Dashboard von @bowenliang123

### Bereitstellung mit Kubernetes

Falls Sie eine hochverfügbare Konfiguration einrichten möchten, gibt es von der Community bereitgestellte Helm Charts und YAML-Dateien, die es ermöglichen, Dify auf Kubernetes bereitzustellen.

- Helm Chart by @LeoQuote
- Helm Chart by @BorisPolonsky
- Helm Chart by @magicsong
- YAML file by @Winson-030
- YAML file by @wyy-holding
- 🚀 NEW! YAML files (Supports Dify v1.6.0) by @Zhoneym

#### Terraform für die Bereitstellung verwenden

Stellen Sie Dify mit nur einem Klick mithilfe von terraform auf einer Cloud-Plattform bereit.

##### Azure Global

- Azure Terraform by @nikawang

##### Google Cloud

- Google Cloud Terraform by @sotazum

#### Verwendung von AWS CDK für die Bereitstellung

Bereitstellung von Dify auf AWS mit CDK

##### AWS

- AWS CDK by @KevinZhao (EKS based)
- AWS CDK by @tmokmss (ECS based)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Ein-Klick-Bereitstellung von Dify in der Alibaba Cloud mit Alibaba Cloud Data Management

#### Verwendung von Azure Devops Pipeline für AKS-Bereitstellung

Stellen Sie Dify mit einem Klick in AKS bereit, indem Sie Azure Devops Pipeline Helm Chart by @LeoZhang verwenden

## Contributing

Falls Sie Code beitragen möchten, lesen Sie bitte unseren Contribution Guide. Gleichzeitig bitten wir Sie, Dify zu unterstützen, indem Sie es in den sozialen Medien teilen und auf Veranstaltungen und Konferenzen präsentieren.

> Wir suchen Mitwirkende, die dabei helfen, Dify in weitere Sprachen zu übersetzen – außer Mandarin oder Englisch. Wenn Sie Interesse an einer Mitarbeit haben, lesen Sie bitte die i18n README für weitere Informationen und hinterlassen Sie einen Kommentar im `global-users`-Kanal unseres Discord Community Servers.

## Gemeinschaft & Kontakt

- GitHub Discussion. Am besten geeignet für: den Austausch von Feedback und das Stellen von Fragen.
- GitHub Issues. Am besten für: Fehler, auf die Sie bei der Verwendung von Dify.AI stoßen, und Funktionsvorschläge. Siehe unseren Contribution Guide.
- Discord. Am besten geeignet für: den Austausch von Bewerbungen und den Austausch mit der Community.
- X(Twitter). Am besten geeignet für: den Austausch von Bewerbungen und den Austausch mit der Community.

**Mitwirkende**

  

## Star-Geschichte

## Offenlegung der Sicherheit

Um Ihre Privatsphäre zu schützen, vermeiden Sie es bitte, Sicherheitsprobleme auf GitHub zu posten. Schicken Sie Ihre Fragen stattdessen an security@dify.ai und wir werden Ihnen eine ausführlichere Antwort geben.

## Lizenz

Dieses Repository steht unter der Dify Open Source License, die im Wesentlichen Apache 2.0 mit einigen zusätzlichen Einschränkungen ist.
