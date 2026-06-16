---
source: dify
owner: langgenius
repo: dify
path: docs/tr-TR/README.md
url: https://github.com/langgenius/dify/blob/main/docs/tr-TR/README.md
---
Dify Bulut ·
  Kendi Sunucunuzda Barındırma ·
  Dokümantasyon ·
  Dify ürün seçeneklerine genel bakış

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

Dify, açık kaynaklı bir LLM uygulama geliştirme platformudur. Sezgisel arayüzü, AI iş akışı, RAG pipeline'ı, ajan yetenekleri, model yönetimi, gözlemlenebilirlik özellikleri ve daha fazlasını birleştirerek, prototipten üretime hızlıca geçmenizi sağlar. İşte temel özelliklerin bir listesi:
 

**1. Workflow**:
Görsel bir arayüz üzerinde güçlü AI iş akışları oluşturun ve test edin, aşağıdaki tüm özellikleri ve daha fazlasını kullanarak.

**2. Kapsamlı model desteği**:
Çok sayıda çıkarım sağlayıcısı ve kendi kendine barındırılan çözümlerden yüzlerce özel / açık kaynaklı LLM ile sorunsuz entegrasyon sağlar. GPT, Mistral, Llama3 ve OpenAI API uyumlu tüm modelleri kapsar. Desteklenen model sağlayıcılarının tam listesine buradan ulaşabilirsiniz.

**3. Prompt IDE**:
Komut istemlerini oluşturmak, model performansını karşılaştırmak ve sohbet tabanlı uygulamalara metin-konuşma gibi ek özellikler eklemek için kullanıcı dostu bir arayüz.

**4. RAG Pipeline**:
Belge alımından bilgi çekmeye kadar geniş kapsamlı RAG yetenekleri. PDF'ler, PPT'ler ve diğer yaygın belge formatlarından metin çıkarma için hazır destek sunar.

**5. Ajan yetenekleri**:
LLM Fonksiyon Çağırma veya ReAct'a dayalı ajanlar tanımlayabilir ve bu ajanlara önceden hazırlanmış veya özel araçlar ekleyebilirsiniz. Dify, AI ajanları için Google Arama, DALL·E, Stable Diffusion ve WolframAlpha gibi 50'den fazla yerleşik araç sağlar.

**6. LLMOps**:
Uygulama loglarını ve performans metriklerini zaman içinde izleme ve analiz etme imkanı. Üretim ortamından elde edilen verilere ve kullanıcı geri bildirimlerine dayanarak, prompt'ları, veri setlerini ve modelleri sürekli olarak optimize edebilirsiniz. Bu sayede, AI uygulamanızın performansını ve doğruluğunu sürekli olarak artırabilirsiniz.

**7. Hizmet Olarak Backend**:
Dify'ın tüm özellikleri ilgili API'lerle birlikte gelir, böylece Dify'ı kendi iş mantığınıza kolayca entegre edebilirsiniz.

## Dify'ı Kullanma

- **Cloud **
  Herkesin sıfır kurulumla denemesi için bir Dify Cloud hizmeti sunuyoruz. Bu hizmet, kendi kendine dağıtılan versiyonun tüm yeteneklerini sağlar ve sandbox planında 200 ücretsiz GPT-4 çağrısı içerir.

- **Dify Topluluk Sürümünü Kendi Sunucunuzda Barındırma**
  Bu başlangıç kılavuzu ile Dify'ı kendi ortamınızda hızlıca çalıştırın.
  Daha fazla referans ve detaylı talimatlar için dokümantasyonumuzu kullanın.

- **Kurumlar / organizasyonlar için Dify**
  Ek kurumsal odaklı özellikler sunuyoruz. Kurumsal ihtiyaçları görüşmek için bize bir e-posta gönderin. 

  > AWS kullanan startuplar ve küçük işletmeler için, AWS Marketplace'deki Dify Premium'a göz atın ve tek tıklamayla kendi AWS VPC'nize dağıtın. Bu, özel logo ve marka ile uygulamalar oluşturma seçeneğine sahip uygun fiyatlı bir AMI teklifdir.

## Güncel Kalma

GitHub'da Dify'a yıldız verin ve yeni sürümlerden anında haberdar olun.

## Hızlı başlangıç

> Dify'ı kurmadan önce, makinenizin aşağıdaki minimum sistem gereksinimlerini karşıladığından emin olun:
>
> - CPU >= 2 Çekirdek
> - RAM >= 4GB

Dify sunucusunu başlatmanın en kolay yolu, docker-compose.yml dosyamızı çalıştırmaktır. Kurulum komutunu çalıştırmadan önce, makinenizde Docker ve Docker Compose'un kurulu olduğundan emin olun:

```bash
cd docker
cp .env.example .env
docker compose up -d
```

Çalıştırdıktan sonra, tarayıcınızda http://localhost/install adresinden Dify kontrol paneline erişebilir ve başlangıç ayarları sürecini başlatabilirsiniz.

> Eğer Dify'a katkıda bulunmak veya ek geliştirmeler yapmak isterseniz, kaynak koddan dağıtım kılavuzumuza başvurun.

## Sonraki adımlar

Yapılandırmayı özelleştirmeniz gerekiyorsa, lütfen .env.example dosyamızdaki yorumlara bakın ve `.env` dosyanızdaki ilgili değerleri güncelleyin. Ayrıca, spesifik dağıtım ortamınıza ve gereksinimlerinize bağlı olarak `docker-compose.yaml` dosyasının kendisinde de, imaj sürümlerini, port eşlemelerini veya hacim bağlantılarını değiştirmek gibi ayarlamalar yapmanız gerekebilir. Herhangi bir değişiklik yaptıktan sonra, lütfen `docker-compose up -d` komutunu tekrar çalıştırın. Kullanılabilir tüm ortam değişkenlerinin tam listesini burada bulabilirsiniz.

### Grafana ile Metrik İzleme

Uygulamalar, kiracılar, mesajlar ve daha fazlasının granularitesinde metrikleri izlemek için Dify'nin PostgreSQL veritabanını veri kaynağı olarak kullanarak panoyu Grafana'ya aktarın.

- @bowenliang123 tarafından Grafana Panosu

### Kubernetes ile Dağıtım

Yüksek kullanılabilirliğe sahip bir kurulum yapılandırmak isterseniz, Dify'ın Kubernetes üzerine dağıtılmasına olanak tanıyan topluluk katkılı Helm Charts ve YAML dosyaları mevcuttur.

- @LeoQuote tarafından Helm Chart
- @BorisPolonsky tarafından Helm Chart
- @Winson-030 tarafından YAML dosyası
- @wyy-holding tarafından YAML dosyası
- 🚀 YENİ! YAML dosyaları (Dify v1.6.0 destekli) @Zhoneym tarafından

#### Dağıtım için Terraform Kullanımı

Dify'ı bulut platformuna tek tıklamayla dağıtın terraform kullanarak

##### Azure Global

- Azure Terraform tarafından @nikawang

##### Google Cloud

- Google Cloud Terraform tarafından @sotazum

#### AWS CDK ile Dağıtım

CDK kullanarak Dify'ı AWS'ye dağıtın

##### AWS

- AWS CDK tarafından @KevinZhao (EKS based)
- AWS CDK tarafından @tmokmss (ECS based)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Alibaba Cloud Data Management kullanarak Dify'ı tek tıkla Alibaba Cloud'a dağıtın

#### AKS'ye Dağıtım için Azure Devops Pipeline Kullanımı

Azure Devops Pipeline Helm Chart by @LeoZhang kullanarak Dify'ı tek tıkla AKS'ye dağıtın

## Katkıda Bulunma

Kod katkısında bulunmak isteyenler için Katkı Kılavuzumuza bakabilirsiniz.
Aynı zamanda, lütfen Dify'ı sosyal medyada, etkinliklerde ve konferanslarda paylaşarak desteklemeyi düşünün.

> Dify'ı Mandarin veya İngilizce dışındaki dillere çevirmemize yardımcı olacak katkıda bulunanlara ihtiyacımız var. Yardımcı olmakla ilgileniyorsanız, lütfen daha fazla bilgi için i18n README dosyasına bakın ve Discord Topluluk Sunucumuzdaki `global-users` kanalında bize bir yorum bırakın.

**Katkıda Bulunanlar**

  

## Topluluk & iletişim

- GitHub Tartışmaları. En uygun: geri bildirim paylaşmak ve soru sormak için.
- GitHub Sorunları. En uygun: Dify.AI kullanırken karşılaştığınız hatalar ve özellik önerileri için. Katkı Kılavuzumuza bakın.
- Discord. En uygun: uygulamalarınızı paylaşmak ve toplulukla vakit geçirmek için.
- X(Twitter). En uygun: uygulamalarınızı paylaşmak ve toplulukla vakit geçirmek için.

## Star history

## Güvenlik açıklaması

Gizliliğinizi korumak için, lütfen güvenlik sorunlarını GitHub'da paylaşmaktan kaçının. Bunun yerine, sorularınızı security@dify.ai adresine gönderin ve size daha detaylı bir cevap vereceğiz.

## Lisans

Bu depo, temel olarak Apache 2.0 lisansı ve birkaç ek kısıtlama içeren Dify Açık Kaynak Lisansı altında kullanıma sunulmuştur.
