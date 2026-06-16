---
source: dify
owner: langgenius
repo: dify
path: docs/tr-TR/CONTRIBUTING.md
url: https://github.com/langgenius/dify/blob/main/docs/tr-TR/CONTRIBUTING.md
---
# KATKIDA BULUNMAK

Demek Dify'a katkıda bulunmak istiyorsunuz - bu harika, ne yapacağınızı görmek için sabırsızlanıyoruz. Sınırlı personel ve finansmana sahip bir startup olarak, LLM uygulamaları oluşturmak ve yönetmek için en sezgisel iş akışını tasarlama konusunda büyük hedeflerimiz var. Topluluktan gelen her türlü yardım gerçekten önemli.

Bulunduğumuz noktada çevik olmamız ve hızlı hareket etmemiz gerekiyor, ancak sizin gibi katkıda bulunanların mümkün olduğunca sorunsuz bir deneyim yaşamasını da sağlamak istiyoruz. Bu katkı rehberini bu amaçla hazırladık; sizi kod tabanıyla ve katkıda bulunanlarla nasıl çalıştığımızla tanıştırmayı, böylece hızlıca eğlenceli kısma geçebilmenizi hedefliyoruz.

Bu rehber, Dify'ın kendisi gibi, sürekli gelişen bir çalışmadır. Bazen gerçek projenin gerisinde kalırsa anlayışınız için çok minnettarız ve gelişmemize yardımcı olacak her türlü geri bildirimi memnuniyetle karşılıyoruz.

Lisanslama konusunda, lütfen kısa Lisans ve Katkıda Bulunan Anlaşmamızı okumak için bir dakikanızı ayırın. Topluluk ayrıca davranış kurallarına da uyar.

## Başlamadan Önce

Üzerinde çalışacak bir şey mi arıyorsunuz? İlk katkıda bulunanlar için iyi sorunlarımıza göz atın ve başlamak için birini seçin!

Eklenecek harika bir yeni model runtime'ı veya aracınız mı var? Eklenti depomuzda bir PR açın ve ne yaptığınızı bize gösterin.

Mevcut bir model runtime'ını, aracı güncellemek veya bazı hataları düzeltmek mi istiyorsunuz? Resmi eklenti depomuza gidin ve sihrinizi gösterin!

Eğlenceye katılın, katkıda bulunun ve birlikte harika bir şeyler inşa edelim! 💡✨

PR açıklamasında mevcut bir sorunu bağlamayı veya yeni bir sorun açmayı unutmayın.

### Hata Raporları

> [!IMPORTANT]
> Lütfen bir hata raporu gönderirken aşağıdaki bilgileri dahil ettiğinizden emin olun:

- Net ve açıklayıcı bir başlık
- Hata mesajları dahil hatanın ayrıntılı bir açıklaması
- Hatayı tekrarlamak için adımlar
- Beklenen davranış
- Mümkünse **Loglar**, backend sorunları için, bu gerçekten önemlidir, bunları docker-compose loglarında bulabilirsiniz
- Uygunsa ekran görüntüleri veya videolar

Nasıl önceliklendiriyoruz:

| Sorun Türü | Öncelik |
| ------------------------------------------------------------ | --------------- |
| Temel işlevlerdeki hatalar (bulut hizmeti, giriş yapamama, çalışmayan uygulamalar, güvenlik açıkları) | Kritik |
| Kritik olmayan hatalar, performans artışları | Orta Öncelik |
| Küçük düzeltmeler (yazım hataları, kafa karıştırıcı ama çalışan UI) | Düşük Öncelik |

### Özellik İstekleri

> [!NOTE]
> Lütfen bir özellik isteği gönderirken aşağıdaki bilgileri dahil ettiğinizden emin olun:

- Net ve açıklayıcı bir başlık
- Özelliğin ayrıntılı bir açıklaması
- Özellik için bir kullanım durumu
- Özellik isteği hakkında diğer bağlamlar veya ekran görüntüleri

Nasıl önceliklendiriyoruz:

| Özellik Türü | Öncelik |
| ------------------------------------------------------------ | --------------- |
| Bir ekip üyesi tarafından etiketlenen Yüksek Öncelikli Özellikler | Yüksek Öncelik |
| Topluluk geri bildirim panosundan popüler özellik istekleri | Orta Öncelik |
| Temel olmayan özellikler ve küçük geliştirmeler | Düşük Öncelik |
| Değerli ama acil olmayan | Gelecek-Özellik |

## PR'nizi Göndermek

### Pull Request Süreci

1. Depoyu fork edin
1. Bir PR taslağı oluşturmadan önce, yapmak istediğiniz değişiklikleri tartışmak için lütfen bir sorun oluşturun
1. Değişiklikleriniz için yeni bir dal oluşturun
1. Lütfen değişiklikleriniz için uygun testler ekleyin
1. Kodunuzun mevcut testleri geçtiğinden emin olun
1. Lütfen PR açıklamasında sorunu bağlayın, `fixes #`
1. Kodunuzu birleştirin!

### Projeyi Kurma

#### Frontend

Frontend hizmetini kurmak için, lütfen `web/README.md` dosyasındaki kapsamlı rehberimize bakın. Bu belge, frontend ortamını düzgün bir şekilde kurmanıza yardımcı olacak ayrıntılı talimatlar sağlar.

#### Backend

Backend hizmetini kurmak için, lütfen `api/README.md` dosyasındaki detaylı talimatlarımıza bakın. Bu belge, backend'i sorunsuz bir şekilde çalıştırmanıza yardımcı olacak adım adım bir kılavuz içerir.

#### Dikkat Edilecek Diğer Şeyler

Kuruluma geçmeden önce bu belgeyi dikkatlice incelemenizi öneririz, çünkü şunlar hakkında temel bilgiler içerir:

- Ön koşullar ve bağımlılıklar
- Kurulum adımları
- Yapılandırma detayları
- Yaygın sorun giderme ipuçları

Kurulum süreci sırasında herhangi bir sorunla karşılaşırsanız bizimle iletişime geçmekten çekinmeyin.

## Yardım Almak

Katkıda bulunurken takılırsanız veya yanıcı bir sorunuz olursa, sorularınızı ilgili GitHub sorunu aracılığıyla bize gönderin veya hızlı bir sohbet için Discord'umuza katılın.
