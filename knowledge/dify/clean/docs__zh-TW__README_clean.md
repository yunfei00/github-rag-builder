---
source: dify
owner: langgenius
repo: dify
path: docs/zh-TW/README.md
url: https://github.com/langgenius/dify/blob/main/docs/zh-TW/README.md
---
📌 介紹 Dify 工作流程檔案上傳功能：重現 Google NotebookLM Podcast

  Dify 雲端服務 ·
  自行託管 ·
  說明文件 ·
  產品方案概覽

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

Dify 是一個開源的 LLM 應用程式開發平台。其直觀的界面結合了智能代理工作流程、RAG 管道、代理功能、模型管理、可觀察性功能等，讓您能夠快速從原型進展到生產環境。

## 快速開始

> 安裝 Dify 之前，請確保您的機器符合以下最低系統要求：
>
> - CPU >= 2 核心
> - 記憶體 >= 4 GiB

啟動 Dify 伺服器最簡單的方式是透過 docker compose。在使用以下命令運行 Dify 之前，請確保您的機器已安裝 Docker 和 Docker Compose：

```bash
cd dify
cd docker
cp .env.example .env
docker compose up -d
```

運行後，您可以在瀏覽器中通過 http://localhost/install 訪問 Dify 儀表板並開始初始化過程。

### 尋求幫助

如果您在設置 Dify 時遇到問題，請參考我們的 常見問題。如果仍有疑問，請聯絡 社區和我們。

> 如果您想為 Dify 做出貢獻或進行額外開發，請參考我們的 從原始碼部署指南

## 核心功能

**1. 工作流程**：
在視覺化畫布上建立和測試強大的 AI 工作流程，利用以下所有功能及更多。

**2. 全面的模型支援**：
無縫整合來自數十個推理提供商和自託管解決方案的數百個專有/開源 LLM，涵蓋 GPT、Mistral、Llama3 和任何與 OpenAI API 兼容的模型。您可以在此處找到支援的模型提供商完整列表。

**3. 提示詞 IDE**：
直觀的界面，用於編寫提示詞、比較模型性能，以及為聊天型應用程式添加文字轉語音等額外功能。

**4. RAG 管道**：
廣泛的 RAG 功能，涵蓋從文件擷取到檢索的全部流程，內建支援從 PDF、PPT 和其他常見文件格式提取文本。

**5. 代理功能**：
您可以基於 LLM 函數調用或 ReAct 定義代理，並為代理添加預構建或自定義工具。Dify 為 AI 代理提供 50 多種內建工具，如 Google 搜尋、DALL·E、Stable Diffusion 和 WolframAlpha。

**6. LLMOps**：
監控並分析應用程式日誌和長期效能。您可以根據生產數據和標註持續改進提示詞、數據集和模型。

**7. 後端即服務**：
Dify 的所有功能都提供相應的 API，因此您可以輕鬆地將 Dify 整合到您自己的業務邏輯中。

## 使用 Dify

- **雲端服務 **
  我們提供 Dify Cloud 服務，任何人都可以零配置嘗試。它提供與自部署版本相同的所有功能，並在沙盒計劃中包含 200 次免費 GPT-4 調用。

- **自託管 Dify 社區版**
  使用這份快速指南在您的環境中快速運行 Dify。
  使用我們的文檔獲取更多參考和深入指導。

- **企業/組織版 Dify**
  我們提供額外的企業中心功能。通過這個聊天機器人記錄您的問題或發送電子郵件給我們討論企業需求。

  > 對於使用 AWS 的初創企業和小型企業，請查看 AWS Marketplace 上的 Dify Premium，並一鍵部署到您自己的 AWS VPC。這是一個經濟實惠的 AMI 產品，可選擇使用自定義徽標和品牌創建應用。

## 保持領先

在 GitHub 上為 Dify 加星，即時獲取新版本通知。

## 進階設定

如果您需要自定義配置，請參考我們的 .env.example 文件中的註釋，並在您的 `.env` 文件中更新相應的值。此外，根據您特定的部署環境和需求，您可能需要調整 `docker-compose.yaml` 文件本身，例如更改映像版本、端口映射或卷掛載。進行任何更改後，請重新運行 `docker-compose up -d`。您可以在這裡找到可用環境變數的完整列表。

### 使用 Grafana 進行指標監控

將儀表板匯入 Grafana，使用 Dify 的 PostgreSQL 資料庫作為資料來源，以監控應用程式、租戶、訊息等顆粒度的指標。

- 由 @bowenliang123 提供的 Grafana 儀表板

### 使用 Kubernetes 部署

如果您想配置高可用性設置，社區貢獻的 Helm Charts 和 Kubernetes 資源清單（YAML）允許在 Kubernetes 上部署 Dify。

- 由 @LeoQuote 提供的 Helm Chart
- 由 @BorisPolonsky 提供的 Helm Chart
- 由 @Winson-030 提供的 YAML 文件
- 由 @wyy-holding 提供的 YAML 文件
- 🚀 NEW! YAML 檔案（支援 Dify v1.6.0）by @Zhoneym

### 使用 Terraform 進行部署

使用 terraform 一鍵部署 Dify 到雲端平台

### Azure 全球

- 由 @nikawang 提供的 Azure Terraform

### Google Cloud

- 由 @sotazum 提供的 Google Cloud Terraform

### 使用 AWS CDK 進行部署

使用 CDK 部署 Dify 到 AWS

### AWS

- 由 @KevinZhao 提供的 AWS CDK (EKS based)
- 由 @tmokmss 提供的 AWS CDK (ECS based)

#### 使用 阿里云计算巢進行部署

阿里云

#### 使用 阿里雲數據管理DMS 進行部署

透過 阿里雲數據管理DMS，一鍵將 Dify 部署至阿里雲

#### 使用 Azure Devops Pipeline 部署到AKS

使用Azure Devops Pipeline Helm Chart by @LeoZhang 將 Dify 一鍵部署到 AKS

## 貢獻

對於想要貢獻程式碼的開發者，請參閱我們的貢獻指南。
同時，也請考慮透過在社群媒體和各種活動與會議上分享 Dify 來支持我們。

> 我們正在尋找貢獻者協助將 Dify 翻譯成中文和英文以外的語言。如果您有興趣幫忙，請查看 i18n README 獲取更多資訊，並在我們的 Discord 社群伺服器 的 `global-users` 頻道留言給我們。

## 社群與聯絡方式

- GitHub Discussion：最適合分享反饋和提問。
- GitHub Issues：最適合報告使用 Dify.AI 時遇到的問題和提出功能建議。請參閱我們的貢獻指南。
- Discord：最適合分享您的應用程式並與社群互動。
- X(Twitter)：最適合分享您的應用程式並與社群互動。

**貢獻者**

  

## 星星歷史

## 安全揭露

為保護您的隱私，請避免在 GitHub 上發布安全性問題。請將您的問題發送至 security@dify.ai，我們將為您提供更詳細的答覆。

## 授權條款

本代碼庫採用 Dify 開源授權，這基本上是 Apache 2.0 授權加上一些額外限制條款。
