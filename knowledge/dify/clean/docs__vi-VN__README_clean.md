---
source: dify
owner: langgenius
repo: dify
path: docs/vi-VN/README.md
url: https://github.com/langgenius/dify/blob/main/docs/vi-VN/README.md
---
Dify Cloud ·
  Tự triển khai ·
  Tài liệu ·
  Tổng quan các lựa chọn sản phẩm Dify

    
        
    
        
    
        
      
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

Dify là một nền tảng phát triển ứng dụng LLM mã nguồn mở. Giao diện trực quan kết hợp quy trình làm việc AI, mô hình RAG, khả năng tác nhân, quản lý mô hình, tính năng quan sát và hơn thế nữa, cho phép bạn nhanh chóng chuyển từ nguyên mẫu sang sản phẩm. Đây là danh sách các tính năng cốt lõi:
 

**1. Quy trình làm việc**:
Xây dựng và kiểm tra các quy trình làm việc AI mạnh mẽ trên một canvas trực quan, tận dụng tất cả các tính năng sau đây và hơn thế nữa.

**2. Hỗ trợ mô hình toàn diện**:
Tích hợp liền mạch với hàng trăm mô hình LLM độc quyền / mã nguồn mở từ hàng chục nhà cung cấp suy luận và giải pháp tự lưu trữ, bao gồm GPT, Mistral, Llama3, và bất kỳ mô hình tương thích API OpenAI nào. Danh sách đầy đủ các nhà cung cấp mô hình được hỗ trợ có thể được tìm thấy tại đây.

**3. IDE Prompt**:
Giao diện trực quan để tạo prompt, so sánh hiệu suất mô hình và thêm các tính năng bổ sung như chuyển văn bản thành giọng nói cho một ứng dụng dựa trên trò chuyện.

**4. Mô hình RAG**:
Khả năng RAG mở rộng bao gồm mọi thứ từ nhập tài liệu đến truy xuất, với hỗ trợ sẵn có cho việc trích xuất văn bản từ PDF, PPT và các định dạng tài liệu phổ biến khác.

**5. Khả năng tác nhân**:
Bạn có thể định nghĩa các tác nhân dựa trên LLM Function Calling hoặc ReAct, và thêm các công cụ được xây dựng sẵn hoặc tùy chỉnh cho tác nhân. Dify cung cấp hơn 50 công cụ tích hợp sẵn cho các tác nhân AI, như Google Search, DALL·E, Stable Diffusion và WolframAlpha.

**6. LLMOps**:
Giám sát và phân tích nhật ký và hiệu suất ứng dụng theo thời gian. Bạn có thể liên tục cải thiện prompt, bộ dữ liệu và mô hình dựa trên dữ liệu sản xuất và chú thích.

**7. Backend-as-a-Service**:
Tất cả các dịch vụ của Dify đều đi kèm với các API tương ứng, vì vậy bạn có thể dễ dàng tích hợp Dify vào logic kinh doanh của riêng mình.

## Sử dụng Dify

- **Cloud **
  Chúng tôi lưu trữ dịch vụ Dify Cloud cho bất kỳ ai muốn thử mà không cần cài đặt. Nó cung cấp tất cả các khả năng của phiên bản tự triển khai và bao gồm 200 lượt gọi GPT-4 miễn phí trong gói sandbox.

- **Tự triển khai Dify Community Edition**
  Nhanh chóng chạy Dify trong môi trường của bạn với hướng dẫn bắt đầu này.
  Sử dụng tài liệu của chúng tôi để tham khảo thêm và nhận hướng dẫn chi tiết hơn.

- **Dify cho doanh nghiệp / tổ chức**
  Chúng tôi cung cấp các tính năng bổ sung tập trung vào doanh nghiệp. Gửi email cho chúng tôi để thảo luận về nhu cầu doanh nghiệp. 

  > Đối với các công ty khởi nghiệp và doanh nghiệp nhỏ sử dụng AWS, hãy xem Dify Premium trên AWS Marketplace và triển khai nó vào AWS VPC của riêng bạn chỉ với một cú nhấp chuột. Đây là một AMI giá cả phải chăng với tùy chọn tạo ứng dụng với logo và thương hiệu tùy chỉnh.

## Luôn cập nhật

Yêu thích Dify trên GitHub và được thông báo ngay lập tức về các bản phát hành mới.

## Bắt đầu nhanh

> Trước khi cài đặt Dify, hãy đảm bảo máy của bạn đáp ứng các yêu cầu hệ thống tối thiểu sau:
>
> - CPU >= 2 Core
> - RAM >= 4GB

Cách dễ nhất để khởi động máy chủ Dify là chạy tệp docker-compose.yml của chúng tôi. Trước khi chạy lệnh cài đặt, hãy đảm bảo rằng Docker và Docker Compose đã được cài đặt trên máy của bạn:

```bash
cd docker
cp .env.example .env
docker compose up -d
```

Sau khi chạy, bạn có thể truy cập bảng điều khiển Dify trong trình duyệt của bạn tại http://localhost/install và bắt đầu quá trình khởi tạo.

> Nếu bạn muốn đóng góp cho Dify hoặc phát triển thêm, hãy tham khảo hướng dẫn triển khai từ mã nguồn của chúng tôi

## Các bước tiếp theo

Nếu bạn cần tùy chỉnh cấu hình, vui lòng tham khảo các nhận xét trong tệp .env.example của chúng tôi và cập nhật các giá trị tương ứng trong tệp `.env` của bạn. Ngoài ra, bạn có thể cần điều chỉnh tệp `docker-compose.yaml`, chẳng hạn như thay đổi phiên bản hình ảnh, ánh xạ cổng hoặc gắn kết khối lượng, dựa trên môi trường triển khai cụ thể và yêu cầu của bạn. Sau khi thực hiện bất kỳ thay đổi nào, vui lòng chạy lại `docker-compose up -d`. Bạn có thể tìm thấy danh sách đầy đủ các biến môi trường có sẵn tại đây.

### Giám sát Số liệu với Grafana

Nhập bảng điều khiển vào Grafana, sử dụng cơ sở dữ liệu PostgreSQL của Dify làm nguồn dữ liệu, để giám sát số liệu theo mức độ chi tiết của ứng dụng, người thuê, tin nhắn và hơn thế nữa.

- Bảng điều khiển Grafana của @bowenliang123

### Triển khai với Kubernetes

Nếu bạn muốn cấu hình một cài đặt có độ sẵn sàng cao, có các Helm Charts và tệp YAML do cộng đồng đóng góp cho phép Dify được triển khai trên Kubernetes.

- Helm Chart bởi @LeoQuote
- Helm Chart bởi @BorisPolonsky
- Tệp YAML bởi @Winson-030
- Tệp YAML bởi @wyy-holding
- 🚀 MỚI! Tệp YAML (Hỗ trợ Dify v1.6.0) bởi @Zhoneym

#### Sử dụng Terraform để Triển khai

Triển khai Dify lên nền tảng đám mây với một cú nhấp chuột bằng cách sử dụng terraform

##### Azure Global

- Azure Terraform bởi @nikawang

##### Google Cloud

- Google Cloud Terraform bởi @sotazum

#### Sử dụng AWS CDK để Triển khai

Triển khai Dify trên AWS bằng CDK

##### AWS

- AWS CDK bởi @KevinZhao (EKS based)
- AWS CDK bởi @tmokmss (ECS based)

#### Alibaba Cloud

Alibaba Cloud Computing Nest

#### Alibaba Cloud Data Management

Triển khai Dify lên Alibaba Cloud chỉ với một cú nhấp chuột bằng Alibaba Cloud Data Management

#### Sử dụng Azure Devops Pipeline để Triển khai lên AKS

Triển khai Dify lên AKS chỉ với một cú nhấp chuột bằng Azure Devops Pipeline Helm Chart bởi @LeoZhang

## Đóng góp

Đối với những người muốn đóng góp mã, xem Hướng dẫn Đóng góp của chúng tôi.
Đồng thời, vui lòng xem xét hỗ trợ Dify bằng cách chia sẻ nó trên mạng xã hội và tại các sự kiện và hội nghị.

> Chúng tôi đang tìm kiếm người đóng góp để giúp dịch Dify sang các ngôn ngữ khác ngoài tiếng Trung hoặc tiếng Anh. Nếu bạn quan tâm đến việc giúp đỡ, vui lòng xem README i18n để biết thêm thông tin và để lại bình luận cho chúng tôi trong kênh `global-users` của Máy chủ Cộng đồng Discord của chúng tôi.

**Người đóng góp**

  

## Cộng đồng & liên hệ

- Thảo luận GitHub. Tốt nhất cho: chia sẻ phản hồi và đặt câu hỏi.
- Vấn đề GitHub. Tốt nhất cho: lỗi bạn gặp phải khi sử dụng Dify.AI và đề xuất tính năng. Xem Hướng dẫn Đóng góp của chúng tôi.
- Discord. Tốt nhất cho: chia sẻ ứng dụng của bạn và giao lưu với cộng đồng.
- X(Twitter). Tốt nhất cho: chia sẻ ứng dụng của bạn và giao lưu với cộng đồng.

## Lịch sử Yêu thích

## Tiết lộ bảo mật

Để bảo vệ quyền riêng tư của bạn, vui lòng tránh đăng các vấn đề bảo mật trên GitHub. Thay vào đó, hãy gửi câu hỏi của bạn đến security@dify.ai và chúng tôi sẽ cung cấp cho bạn câu trả lời chi tiết hơn.

## Giấy phép

Kho lưu trữ này có sẵn theo Giấy phép Mã nguồn Mở Dify, về cơ bản là Apache 2.0 với một vài hạn chế bổ sung.
