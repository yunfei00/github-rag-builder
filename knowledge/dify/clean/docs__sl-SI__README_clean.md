---
source: dify
owner: langgenius
repo: dify
path: docs/sl-SI/README.md
url: https://github.com/langgenius/dify/blob/main/docs/sl-SI/README.md
---
📌 Predstavljamo nalaganje datotek Dify Workflow: znova ustvarite Google NotebookLM Podcast

  Dify Cloud ·
  Samostojno gostovanje ·
  Dokumentacija ·
  Pregled ponudb izdelkov Dify

    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

Dify je odprtokodna platforma za razvoj aplikacij LLM. Njegov intuitivni vmesnik združuje agentski potek dela z umetno inteligenco, cevovod RAG, zmogljivosti agentov, upravljanje modelov, funkcije opazovanja in več, kar vam omogoča hiter prehod od prototipa do proizvodnje.

## Hitri začetek

> Preden namestite Dify, se prepričajte, da vaša naprava izpolnjuje naslednje minimalne sistemske zahteve:
>
> - CPU >= 2 Core
> - RAM >= 4 GiB

Najlažji način za zagon strežnika Dify je prek docker compose . Preden zaženete Dify z naslednjimi ukazi, se prepričajte, da sta Docker in Docker Compose nameščena na vašem računalniku:

```bash
cd dify
cd docker
cp .env.example .env
docker compose up -d
```

Po zagonu lahko dostopate do nadzorne plošče Dify v brskalniku na http://localhost/install in začnete postopek inicializacije.

#### Iskanje pomoči

Prosimo, glejte naša pogosta vprašanja FAQ če naletite na težave pri nastavitvi Dify. Če imate še vedno težave, se obrnite na skupnost ali nas.

> Če želite prispevati k Difyju ali narediti dodaten razvoj, glejte naš vodnik za uvajanje iz izvorne kode

## Ključne značilnosti

**1. Potek dela**:
Zgradite in preizkusite zmogljive poteke dela AI na vizualnem platnu, pri čemer izkoristite vse naslednje funkcije in več.

**2. Celovita podpora za modele**:
Brezhibna integracija s stotinami lastniških/odprtokodnih LLM-jev ducatov ponudnikov sklepanja in samostojnih rešitev, ki pokrivajo GPT, Mistral, Llama3 in vse modele, združljive z API-jem OpenAI. Celoten seznam podprtih ponudnikov modelov najdete tukaj.

**3. Prompt IDE**:
intuitivni vmesnik za ustvarjanje pozivov, primerjavo zmogljivosti modela in dodajanje dodatnih funkcij, kot je pretvorba besedila v govor, aplikaciji, ki temelji na klepetu.

**4. RAG Pipeline**:
E Obsežne zmogljivosti RAG, ki pokrivajo vse od vnosa dokumenta do priklica, s podporo za ekstrakcijo besedila iz datotek PDF, PPT in drugih običajnih formatov dokumentov.

**5. Agent capabilities**:
definirate lahko agente, ki temeljijo na klicanju funkcij LLM ali ReAct, in dodate vnaprej izdelana orodja ali orodja po meri za agenta. Dify ponuja več kot 50 vgrajenih orodij za agente AI, kot so Google Search, DALL·E, Stable Diffusion in WolframAlpha.

**6. LLMOps**:
Spremljajte in analizirajte dnevnike aplikacij in učinkovitost skozi čas. Pozive, nabore podatkov in modele lahko nenehno izboljšujete na podlagi proizvodnih podatkov in opomb.

**7. Backend-as-a-Service**:
AVse ponudbe Difyja so opremljene z ustreznimi API-ji, tako da lahko Dify brez težav integrirate v svojo poslovno logiko.

## Uporaba Dify

- **Cloud **
  Gostimo storitev Dify Cloud za vsakogar, ki jo lahko preizkusite brez nastavitev. Zagotavlja vse zmožnosti različice za samostojno namestitev in vključuje 200 brezplačnih klicev GPT-4 v načrtu peskovnika.

- **Self-hosting Dify Community Edition**
  Hitro zaženite Dify v svojem okolju s tem začetnim vodnikom . Za dodatne reference in podrobnejša navodila uporabite našo dokumentacijo .

- **Dify za podjetja/organizacije**
  Ponujamo dodatne funkcije, osredotočene na podjetja. Zabeležite svoja vprašanja prek tega klepetalnega robota ali nam pošljite e-pošto, da se pogovorimo o potrebah podjetja. 

  > Za novoustanovljena podjetja in mala podjetja, ki uporabljajo AWS, si oglejte Dify Premium na AWS Marketplace in ga z enim klikom uvedite v svoj AWS VPC. To je cenovno ugodna ponudba AMI z možnostjo ustvarjanja aplikacij z logotipom in blagovno znamko po meri.

## Staying ahead

Star Dify on GitHub and be instantly notified of new releases.

## Napredne nastavitve

Če morate prilagoditi konfiguracijo, si oglejte komentarje v naši datoteki .env.example in posodobite ustrezne vrednosti v svoji .env datoteki. Poleg tega boste morda morali prilagoditi docker-compose.yamlsamo datoteko, na primer spremeniti različice slike, preslikave vrat ali namestitve nosilca, glede na vaše specifično okolje in zahteve za uvajanje. Po kakršnih koli spremembah ponovno zaženite docker-compose up -d. Celoten seznam razpoložljivih spremenljivk okolja najdete tukaj .

### Spremljanje metrik z Grafana

Uvoz nadzorne plošče v Grafana, z uporabo Difyjeve PostgreSQL baze podatkov kot vir podatkov, za spremljanje metrike glede na podrobnost aplikacij, najemnikov, sporočil in drugega.

- Nadzorna plošča Grafana avtorja @bowenliang123

### Namestitev s Kubernetes

Če želite konfigurirati visoko razpoložljivo nastavitev, so na voljo Helm Charts in datoteke YAML, ki jih prispeva skupnost, ki omogočajo uvedbo Difyja v Kubernetes.

- Helm Chart by @LeoQuote
- Helm Chart by @BorisPolonsky
- YAML file by @Winson-030
- YAML file by @wyy-holding
- 🚀 NEW! YAML files (Supports Dify v1.6.0) by @Zhoneym

#### Uporaba Terraform za uvajanje

namestite Dify v Cloud Platform z enim klikom z uporabo terraform

##### Azure Global

- Azure Terraform by @nikawang

##### Google Cloud

- Google Cloud Terraform by @sotazum

#### Uporaba AWS CDK za uvajanje

Uvedite Dify v AWS z uporabo CDK

##### AWS

- AWS CDK by @KevinZhao (EKS based)
- AWS CDK by @tmokmss (ECS based)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Z enim klikom namestite Dify na Alibaba Cloud z Alibaba Cloud Data Management

#### Uporaba Azure Devops Pipeline za uvajanje v AKS

Z enim klikom namestite Dify v AKS z uporabo Azure Devops Pipeline Helm Chart by @LeoZhang

## Prispevam

Za tiste, ki bi radi prispevali kodo, si oglejte naš vodnik za prispevke. Hkrati vas prosimo, da podprete Dify tako, da ga delite na družbenih medijih ter na dogodkih in konferencah.

> Iščemo sodelavce za pomoč pri prevajanju Difyja v jezike, ki niso mandarinščina ali angleščina. Če želite pomagati, si oglejte i18n README za več informacij in nam pustite komentar v global-userskanalu našega strežnika skupnosti Discord .

## Skupnost in stik

- GitHub Discussion. Najboljše za: izmenjavo povratnih informacij in postavljanje vprašanj.
- GitHub Issues. Najboljše za: hrošče, na katere naletite pri uporabi Dify.AI, in predloge funkcij. Oglejte si naš vodnik za prispevke.
- Discord. Najboljše za: deljenje vaših aplikacij in druženje s skupnostjo.
- X(Twitter). Najboljše za: deljenje vaših aplikacij in druženje s skupnostjo.

**Contributors**

  

## Star history

## Varnostno razkritje

Zaradi zaščite vaše zasebnosti se izogibajte objavljanju varnostnih vprašanj na GitHub. Namesto tega pošljite vprašanja na security@dify.ai in zagotovili vam bomo podrobnejši odgovor.

## Licenca

To skladišče je na voljo pod odprtokodno licenco Dify , ki je v bistvu Apache 2.0 z nekaj dodatnimi omejitvami.
