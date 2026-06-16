---
source: dify
owner: langgenius
repo: dify
path: docs/ko-KR/README.md
url: https://github.com/langgenius/dify/blob/main/docs/ko-KR/README.md
---
Dify 클라우드 ·
  셀프-호스팅 ·
  문서 ·
  Dify 제품 에디션 안내

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

Dify는 오픈 소스 LLM 앱 개발 플랫폼입니다. 직관적인 인터페이스를 통해 AI 워크플로우, RAG 파이프라인, 에이전트 기능, 모델 관리, 관찰 기능 등을 결합하여 프로토타입에서 프로덕션까지 빠르게 전환할 수 있습니다. 주요 기능 목록은 다음과 같습니다: 

**1. 워크플로우**:
다음 기능들을 비롯한 다양한 기능을 활용하여 시각적 캔버스에서 강력한 AI 워크플로우를 구축하고 테스트하세요.

**2. 포괄적인 모델 지원:**:

수십 개의 추론 제공업체와 자체 호스팅 솔루션에서 제공하는 수백 개의 독점 및 오픈 소스 LLM과 원활하게 통합되며, GPT, Mistral, Llama3 및 모든 OpenAI API 호환 모델을 포함합니다. 지원되는 모델 제공업체의 전체 목록은 여기에서 확인할 수 있습니다.

**3. 통합 개발환경**:
프롬프트를 작성하고, 모델 성능을 비교하며, 텍스트-음성 변환과 같은 추가 기능을 채팅 기반 앱에 추가할 수 있는 직관적인 인터페이스를 제공합니다.

**4. RAG 파이프라인**:
문서 수집부터 검색까지 모든 것을 다루며, PDF, PPT 및 기타 일반적인 문서 형식에서 텍스트 추출을 위한 기본 지원이 포함되어 있는 광범위한 RAG 기능을 제공합니다.

**5. 에이전트 기능**:
LLM 함수 호출 또는 ReAct를 기반으로 에이전트를 정의하고 에이전트에 대해 사전 구축된 도구나 사용자 정의 도구를 추가할 수 있습니다. Dify는 Google Search, DALL·E, Stable Diffusion, WolframAlpha 등 AI 에이전트를 위한 50개 이상의 내장 도구를 제공합니다.

**6. LLMOps**:
시간 경과에 따른 애플리케이션 로그와 성능을 모니터링하고 분석합니다. 생산 데이터와 주석을 기반으로 프롬프트, 데이터세트, 모델을 지속적으로 개선할 수 있습니다.

**7. Backend-as-a-Service**:
Dify의 모든 제품에는 해당 API가 함께 제공되므로 Dify를 자신의 비즈니스 로직에 쉽게 통합할 수 있습니다.

## Dify 사용하기

- **클라우드 **
  우리는 누구나 설정이 필요 없이 사용해 볼 수 있도록 Dify 클라우드 서비스를 호스팅합니다. 이는 자체 배포 버전의 모든 기능을 제공하며, 샌드박스 플랜에서 무료로 200회의 GPT-4 호출을 포함합니다.

- **셀프-호스팅 Dify 커뮤니티 에디션**
  환경에서 Dify를 빠르게 실행하려면 이 스타터 가이드를 참조하세요.
  추가 참조 및 더 심층적인 지침은 문서를 사용하세요.

- **기업 / 조직을 위한 Dify**
  우리는 추가적인 기업 중심 기능을 제공합니다. 잡거나 이메일 보내기를 통해 기업 요구 사항을 논의하십시오. 

  > AWS를 사용하는 스타트업 및 중소기업의 경우 AWS Marketplace에서 Dify Premium을 확인하고 한 번의 클릭으로 자체 AWS VPC에 배포하십시오. 맞춤형 로고와 브랜딩이 포함된 앱을 생성할 수 있는 옵션이 포함된 저렴한 AMI 제품입니다.

## 앞서가기

GitHub에서 Dify에 별표를 찍어 새로운 릴리스를 즉시 알림 받으세요.

## 빠른 시작

> Dify를 설치하기 전에 컴퓨터가 다음과 같은 최소 시스템 요구 사항을 충족하는지 확인하세요 :
>
> - CPU >= 2 Core
> - RAM >= 4GB

Dify 서버를 시작하는 가장 쉬운 방법은 docker-compose.yml 파일을 실행하는 것입니다. 설치 명령을 실행하기 전에 Docker 및 Docker Compose가 머신에 설치되어 있는지 확인하세요.

```bash
cd docker
cp .env.example .env
docker compose up -d
```

실행 후 브라우저의 http://localhost/install 에서 Dify 대시보드에 액세스하고 초기화 프로세스를 시작할 수 있습니다.

> Dify에 기여하거나 추가 개발을 하고 싶다면 소스 코드에서 배포에 대한 가이드를 참조하세요.

## 다음 단계

구성을 사용자 정의해야 하는 경우 .env.example 파일의 주석을 참조하고 `.env` 파일에서 해당 값을 업데이트하십시오. 또한 특정 배포 환경 및 요구 사항에 따라 `docker-compose.yaml` 파일 자체를 조정해야 할 수도 있습니다. 예를 들어 이미지 버전, 포트 매핑 또는 볼륨 마운트를 변경합니다. 변경 한 후 `docker-compose up -d`를 다시 실행하십시오. 사용 가능한 환경 변수의 전체 목록은 여기에서 찾을 수 있습니다.

### Grafana를 사용한 메트릭 모니터링

Dify의 PostgreSQL 데이터베이스를 데이터 소스로 사용하여 앱, 테넌트, 메시지 등에 대한 세분화된 메트릭을 모니터링하기 위해 대시보드를 Grafana로 가져옵니다.

- @bowenliang123의 Grafana 대시보드

### Kubernetes를 통한 배포

Dify를 Kubernetes에 배포하고 프리미엄 스케일링 설정을 구성했다는 커뮤니티가 제공하는 Helm Charts와 YAML 파일이 존재합니다.

- Helm Chart by @LeoQuote
- Helm Chart by @BorisPolonsky
- Helm Chart by @magicsong
- YAML file by @Winson-030
- YAML file by @wyy-holding
- 🚀 NEW! YAML files (Supports Dify v1.6.0) by @Zhoneym

#### Terraform을 사용한 배포

terraform을 사용하여 단 한 번의 클릭으로 Dify를 클라우드 플랫폼에 배포하십시오

##### Azure Global

- nikawang의 Azure Terraform

##### Google Cloud

- sotazum의 Google Cloud Terraform

#### AWS CDK를 사용한 배포

CDK를 사용하여 AWS에 Dify 배포

##### AWS

- KevinZhao의 AWS CDK (EKS based)
- tmokmss의 AWS CDK (ECS based)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Alibaba Cloud Data Management를 통해 원클릭으로 Dify를 Alibaba Cloud에 배포할 수 있습니다

#### AKS에 배포하기 위해 Azure Devops Pipeline 사용

Azure Devops Pipeline Helm Chart by @LeoZhang을 사용하여 Dify를 AKS에 원클릭으로 배포

## 기여

코드에 기여하고 싶은 분들은 기여 가이드를 참조하세요.
동시에 Dify를 소셜 미디어와 행사 및 컨퍼런스에 공유하여 지원하는 것을 고려해 주시기 바랍니다.

> 우리는 Dify를 중국어나 영어 이외의 언어로 번역하는 데 도움을 줄 수 있는 기여자를 찾고 있습니다. 도움을 주고 싶으시다면 i18n README에서 더 많은 정보를 확인하시고 Discord 커뮤니티 서버의 `global-users` 채널에 댓글을 남겨주세요.

**기여자**

  

## 커뮤니티 & 연락처

- GitHub 토론. 피드백 공유 및 질문하기에 적합합니다.
- GitHub 이슈. Dify.AI 사용 중 발견한 버그와 기능 제안에 적합합니다. 기여 가이드를 참조하세요.
- 디스코드. 애플리케이션 공유 및 커뮤니티와 소통하기에 적합합니다.
- 트위터. 애플리케이션 공유 및 커뮤니티와 소통하기에 적합합니다.

## Star 히스토리

## 보안 공개

개인정보 보호를 위해 보안 문제를 GitHub에 게시하지 마십시오. 대신 security@dify.ai로 질문을 보내주시면 더 자세한 답변을 드리겠습니다.

## 라이선스

이 저장소는 기본적으로 몇 가지 추가 제한 사항이 있는 Apache 2.0인 Dify 오픈 소스 라이선스에 따라 사용할 수 있습니다.
