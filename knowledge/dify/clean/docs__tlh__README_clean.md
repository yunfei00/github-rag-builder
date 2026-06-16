---
source: dify
owner: langgenius
repo: dify
path: docs/tlh/README.md
url: https://github.com/langgenius/dify/blob/main/docs/tlh/README.md
---
Dify Cloud ·
  Self-hosting ·
  Documentation ·
  Dify product editions

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

# 

  

Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features (including Opik, Langfuse, and Arize Phoenix) and more, letting you quickly go from prototype to production. Here's a list of the core features:
 

**1. Workflow**:
Build and test powerful AI workflows on a visual canvas, leveraging all the following features and beyond.

**2. Comprehensive model support**:
Seamless integration with hundreds of proprietary / open-source LLMs from dozens of inference providers and self-hosted solutions, covering GPT, Mistral, Llama3, and any OpenAI API-compatible models. A full list of supported model providers can be found here.

**3. Prompt IDE**:
Intuitive interface for crafting prompts, comparing model performance, and adding additional features such as text-to-speech to a chat-based app.

**4. RAG Pipeline**:
Extensive RAG capabilities that cover everything from document ingestion to retrieval, with out-of-box support for text extraction from PDFs, PPTs, and other common document formats.

**5. Agent capabilities**:
You can define agents based on LLM Function Calling or ReAct, and add pre-built or custom tools for the agent. Dify provides 50+ built-in tools for AI agents, such as Google Search, DALL·E, Stable Diffusion and WolframAlpha.

**6. LLMOps**:
Monitor and analyze application logs and performance over time. You could continuously improve prompts, datasets, and models based on production data and annotations.

**7. Backend-as-a-Service**:
All of Dify's offerings come with corresponding APIs, so you could effortlessly integrate Dify into your own business logic.

## Using Dify

- **Cloud **
  We host a Dify Cloud service for anyone to try with zero setup. It provides all the capabilities of the self-deployed version, and includes 200 free GPT-4 calls in the sandbox plan.

- **Self-hosting Dify Community Edition**
  Quickly get Dify running in your environment with this starter guide.
  Use our documentation for further references and more in-depth instructions.

- **Dify for Enterprise / Organizations**
  We provide additional enterprise-centric features. Send us an email to discuss enterprise needs. 

  > For startups and small businesses using AWS, check out Dify Premium on AWS Marketplace and deploy it to your own AWS VPC with one-click. It's an affordable AMI offering with the option to create apps with custom logo and branding.

## Staying ahead

Star Dify on GitHub and be instantly notified of new releases.

## Quick Start

> Before installing Dify, make sure your machine meets the following minimum system requirements:
>
> - CPU >= 2 Core
> - RAM >= 4GB

The easiest way to start the Dify server is to run our docker-compose.yml file. Before running the installation command, make sure that Docker and Docker Compose are installed on your machine:

```bash
cd docker
cp .env.example .env
docker compose up -d
```

After running, you can access the Dify dashboard in your browser at http://localhost/install and start the initialization process.

> If you'd like to contribute to Dify or do additional development, refer to our guide to deploying from source code

## Next steps

If you need to customize the configuration, please refer to the comments in our .env.example file and update the corresponding values in your `.env` file. Additionally, you might need to make adjustments to the `docker-compose.yaml` file itself, such as changing image versions, port mappings, or volume mounts, based on your specific deployment environment and requirements. After making any changes, please re-run `docker-compose up -d`. You can find the full list of available environment variables here.

If you'd like to configure a highly-available setup, there are community-contributed Helm Charts and YAML files which allow Dify to be deployed on Kubernetes.

- Helm Chart by @LeoQuote
- Helm Chart by @BorisPolonsky
- Helm Chart by @magicsong
- YAML file by @Winson-030
- YAML file by @wyy-holding
- 🚀 NEW! YAML files (Supports Dify v1.6.0) by @Zhoneym

#### Terraform atorlugu pilersitsineq

wa'logh nIqHom neH ghun deployment toy'wI' terraform lo'laH.

##### Azure Global

- Azure Terraform mung @nikawang

##### Google Cloud

- Google Cloud Terraform qachlot @sotazum

#### AWS CDK atorlugh pilersitsineq

wa'logh nIqHom neH ghun deployment toy'wI' CDK lo'laH.

##### AWS

- AWS CDK qachlot @KevinZhao (EKS based)
- AWS CDK qachlot @tmokmss (ECS based)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Alibaba Cloud Data Management

#### AKS 'e' Deploy je Azure Devops Pipeline lo'laH

Azure Devops Pipeline Helm Chart by @LeoZhang lo'laH Dify AKS 'e' wa'DIch click 'e' Deploy

## Contributing

For those who'd like to contribute code, see our Contribution Guide.
At the same time, please consider supporting Dify by sharing it on social media and at events and conferences.

> We are looking for contributors to help with translating Dify to languages other than Mandarin or English. If you are interested in helping, please see the i18n README for more information, and leave us a comment in the `global-users` channel of our Discord Community Server.

**Contributors**

  

## Community & Contact

- GitHub Discussion. Best for: sharing feedback and asking questions.
- GitHub Issues. Best for: bugs you encounter using Dify.AI, and feature proposals. See our Contribution Guide.
- Discord. Best for: sharing your applications and hanging out with the community.
- X(Twitter). Best for: sharing your applications and hanging out with the community.

## Star History

## Security Disclosure

To protect your privacy, please avoid posting security issues on GitHub. Instead, send your questions to security@dify.ai and we will provide you with a more detailed answer.

## License

This repository is available under the Dify Open Source License, which is essentially Apache 2.0 with a few additional restrictions.
