---
source: dify
owner: langgenius
repo: dify
path: docs/pt-BR/README.md
url: https://github.com/langgenius/dify/blob/main/docs/pt-BR/README.md
---
📌 Introduzindo o Dify Workflow com Upload de Arquivo: Recrie o Podcast Google NotebookLM

  Dify Cloud ·
  Auto-hospedagem ·
  Documentação ·
  Visão geral das edições do Dify

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

Dify é uma plataforma de desenvolvimento de aplicativos LLM de código aberto. Sua interface intuitiva combina workflow de IA, pipeline RAG, capacidades de agente, gerenciamento de modelos, recursos de observabilidade e muito mais, permitindo que você vá rapidamente do protótipo à produção. Aqui está uma lista das principais funcionalidades:
 

**1. Workflow**:
Construa e teste workflows poderosos de IA em uma interface visual, aproveitando todos os recursos a seguir e muito mais.

**2. Suporte abrangente a modelos**:
Integração perfeita com centenas de LLMs proprietários e de código aberto de diversas provedoras e soluções auto-hospedadas, abrangendo GPT, Mistral, Llama3 e qualquer modelo compatível com a API da OpenAI. A lista completa de provedores suportados pode ser encontrada aqui.

**3. IDE de Prompt**:
Interface intuitiva para criação de prompts, comparação de desempenho de modelos e adição de recursos como conversão de texto para fala em um aplicativo baseado em chat.

**4. Pipeline RAG**:
Extensas capacidades de RAG que cobrem desde a ingestão de documentos até a recuperação, com suporte nativo para extração de texto de PDFs, PPTs e outros formatos de documentos comuns.

**5. Capacidades de agente**:
Você pode definir agentes com base em LLM Function Calling ou ReAct e adicionar ferramentas pré-construídas ou personalizadas para o agente. O Dify oferece mais de 50 ferramentas integradas para agentes de IA, como Google Search, DALL·E, Stable Diffusion e WolframAlpha.

**6. LLMOps**:
Monitore e analise os registros e o desempenho do aplicativo ao longo do tempo. É possível melhorar continuamente prompts, conjuntos de dados e modelos com base nos dados de produção e anotações.

**7. Backend como Serviço**:
Todas os recursos do Dify vêm com APIs correspondentes, permitindo que você integre o Dify sem esforço na lógica de negócios da sua empresa.

## Usando o Dify

- **Nuvem **
  Oferecemos o serviço Dify Cloud para qualquer pessoa experimentar sem nenhuma configuração. Ele fornece todas as funcionalidades da versão auto-hospedada, incluindo 200 chamadas GPT-4 gratuitas no plano sandbox.

- **Auto-hospedagem do Dify Community Edition**
  Configure rapidamente o Dify no seu ambiente com este guia inicial.
  Use nossa documentação para referências adicionais e instruções mais detalhadas.

- **Dify para empresas/organizações**
  Oferecemos recursos adicionais voltados para empresas. Você pode falar conosco por e-mail para discutir necessidades empresariais. 

  > Para startups e pequenas empresas que utilizam AWS, confira o Dify Premium no AWS Marketplace e implemente no seu próprio AWS VPC com um clique. É uma oferta AMI acessível com a opção de criar aplicativos com logotipo e marca personalizados.

## Mantendo-se atualizado

Dê uma estrela no Dify no GitHub e seja notificado imediatamente sobre novos lançamentos.

## Início rápido

> Antes de instalar o Dify, certifique-se de que sua máquina atenda aos seguintes requisitos mínimos de sistema:
>
> - CPU >= 2 Núcleos
> - RAM >= 4 GiB

A maneira mais fácil de iniciar o servidor Dify é executar nosso arquivo docker-compose.yml. Antes de rodar o comando de instalação, certifique-se de que o Docker e o Docker Compose estão instalados na sua máquina:

```bash
cd docker
cp .env.example .env
docker compose up -d
```

Após a execução, você pode acessar o painel do Dify no navegador em http://localhost/install e iniciar o processo de inicialização.

> Se você deseja contribuir com o Dify ou fazer desenvolvimento adicional, consulte nosso guia para implantar a partir do código fonte.

## Próximos passos

Se precisar personalizar a configuração, consulte os comentários no nosso arquivo .env.example e atualize os valores correspondentes no seu arquivo `.env`. Além disso, talvez seja necessário fazer ajustes no próprio arquivo `docker-compose.yaml`, como alterar versões de imagem, mapeamentos de portas ou montagens de volumes, com base no seu ambiente de implantação específico e nas suas necessidades. Após fazer quaisquer alterações, execute novamente `docker-compose up -d`. Você pode encontrar a lista completa de variáveis de ambiente disponíveis aqui.

### Monitoramento de Métricas com Grafana

Importe o dashboard para o Grafana, usando o banco de dados PostgreSQL do Dify como fonte de dados, para monitorar métricas na granularidade de aplicativos, inquilinos, mensagens e muito mais.

- Dashboard do Grafana por @bowenliang123

### Implantação com Kubernetes

Se deseja configurar uma instalação de alta disponibilidade, há Helm Charts e arquivos YAML contribuídos pela comunidade que permitem a implantação do Dify no Kubernetes.

- Helm Chart de @LeoQuote
- Helm Chart de @BorisPolonsky
- Helm Chart de @magicsong
- Arquivo YAML por @Winson-030
- Arquivo YAML por @wyy-holding
- 🚀 NOVO! Arquivos YAML (Compatível com Dify v1.6.0) por @Zhoneym

#### Usando o Terraform para Implantação

Implante o Dify na Plataforma Cloud com um único clique usando terraform

##### Azure Global

- Azure Terraform por @nikawang

##### Google Cloud

- Google Cloud Terraform por @sotazum

#### Usando AWS CDK para Implantação

Implante o Dify na AWS usando CDK

##### AWS

- AWS CDK por @KevinZhao (EKS based)
- AWS CDK por @tmokmss (ECS based)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Implante o Dify na Alibaba Cloud com um clique usando o Alibaba Cloud Data Management

#### Usando Azure Devops Pipeline para Implantar no AKS

Implante o Dify no AKS com um clique usando Azure Devops Pipeline Helm Chart by @LeoZhang

## Contribuindo

Para aqueles que desejam contribuir com código, veja nosso Guia de Contribuição.
Ao mesmo tempo, considere apoiar o Dify compartilhando-o nas redes sociais e em eventos e conferências.

> Estamos buscando contribuidores para ajudar na tradução do Dify para idiomas além de Mandarim e Inglês. Se você tiver interesse em ajudar, consulte o README i18n para mais informações e deixe-nos um comentário no canal `global-users` em nosso Servidor da Comunidade no Discord.

**Contribuidores**

  

## Comunidade e contato

- Discussões no GitHub. Melhor para: compartilhar feedback e fazer perguntas.
- Problemas no GitHub. Melhor para: relatar bugs encontrados no Dify.AI e propor novos recursos. Veja nosso Guia de Contribuição.
- Discord. Melhor para: compartilhar suas aplicações e interagir com a comunidade.
- X(Twitter). Melhor para: compartilhar suas aplicações e interagir com a comunidade.

## Histórico de estrelas

## Divulgação de segurança

Para proteger sua privacidade, evite postar problemas de segurança no GitHub. Em vez disso, envie suas perguntas para security@dify.ai e forneceremos uma resposta mais detalhada.

## Licença

Este repositório está disponível sob a Licença de Código Aberto Dify, que é essencialmente Apache 2.0 com algumas restrições adicionais.
