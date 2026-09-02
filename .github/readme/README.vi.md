<p align="center">
  <img src="../../logo.png" alt="i-have-adhd" width="140" />
</p>
<p align="center">
  <strong align="center">Đầu ra thân thiện với người có ADHD. Không cần chẩn đoán ADHD!</strong>
</p>
<p align="center">
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/ayghri/i-have-adhd?style=flat" alt="Giấy phép"></a>
</p>

<p align="center">
  <a href="../../README.md" title="English" aria-label="English">🇬🇧</a> ·
  <a href="README.zh-CN.md" title="简体中文" aria-label="简体中文">🇨🇳</a> ·
  <a href="README.pt-BR.md" title="Português (Brasil)" aria-label="Português (Brasil)">🇧🇷</a> ·
  <a href="README.ja.md" title="日本語" aria-label="日本語">🇯🇵</a> ·
  <strong title="Tiếng Việt" aria-label="Tiếng Việt">🇻🇳</strong> ·
  <a href="README.ko.md" title="한국어" aria-label="한국어">🇰🇷</a>
</p>


## Cài đặt

🔗 [Hướng dẫn cài đặt](../install/INSTALL.vi.md)

## Skill này làm gì

Một skill đưa kết quả đã xác minh, quyết định cần thiết hoặc hành động tiếp theo lên trước mà không che khuất bằng chứng hay giới hạn an toàn. Không có câu “Hy vọng điều này hữu ích!”


## Những gì thay đổi


<table>
<tr>
<td width="50%">

## Trước khi dùng

> Câu hỏi rất hay! Để tôi suy nghĩ về điều này. Luồng xác thực của bạn gồm vài thành phần liên quan: middleware, việc xác minh token và xử lý cookie. Nhìn vào `src/auth.ts`, hàm `verifyToken` (khoảng dòng 42-58) có vẻ đang dùng API `jsonwebtoken` cũ hơn. Một cách tiếp cận là cập nhật package và viết lại hàm đó. Sau khi thay đổi, bạn sẽ muốn chạy các bài kiểm thử phần xác thực để xác nhận không có gì bị hỏng. Nhân tiện, bạn cũng có thể muốn xem xét tổng thể phiên bản các dependency. Hy vọng điều này hữu ích! Cho tôi biết nếu bạn muốn đi sâu hơn.

</td>

<td width="50%">

## Sau khi dùng

> Lỗi xác thực nằm ở `src/auth.ts:42`: `verifyToken` đang dùng API `jsonwebtoken` cũ. Chưa có thay đổi nào được thực hiện.
>
> - Bằng chứng: việc xác minh token thất bại tại điểm gọi này.
> - Rủi ro: phiên bản đích tương thích chưa được xác nhận.
>
> Bước tiếp theo: xác nhận phiên bản `jsonwebtoken` được hỗ trợ trước khi cập nhật dependency và chạy `npm test -- auth.spec.ts`.

</td>
</tr>
</table>


## Các quy tắc

10 quy tắc. Nội dung chi tiết tại [SKILL.md](../../skills/i-have-adhd/SKILL.md).

1. Đưa kết quả đã xác minh, quyết định cần thiết hoặc hành động tiếp theo lên trước.
2. Bổ sung bằng chứng, điều chưa biết, rủi ro và kết quả xác minh khi cần.
3. Chỉ đánh số những hành động phải thực hiện theo thứ tự.
4. Giữ đầy đủ mọi thông tin quan trọng và đối chiếu số lượng trong phần tóm tắt với các mục nguồn.
5. Chỉ nhắc lại trạng thái khi hữu ích và không tạo nhiệm vụ tiếp theo sau khi đã hoàn tất.
6. Chỉ ước tính khi thời gian ảnh hưởng đến quyết định và có cơ sở đáng tin cậy.
7. Làm rõ nội dung đã hoàn tất và kết quả xác minh.
8. Báo lỗi khách quan, phân biệt nguyên nhân đã xác nhận với giả thuyết.
9. Kiểm soát nội dung lan man mà không che giấu vấn đề phụ quan trọng.
10. Loại bỏ mở đầu và lặp lại không cần thiết; kết thúc khi câu trả lời đã đủ.

## Tùy chỉnh

Fork repo, chỉnh sửa `skills/i-have-adhd/SKILL.md`, sau đó chuyển sang dùng bản của bạn:

```bash
claude plugin uninstall i-have-adhd            # gỡ bản chính trước:
claude plugin marketplace remove i-have-adhd   # bản fork và bản chính dùng chung tên
claude plugin marketplace add <username-của-bạn>/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```

Khởi động lại Claude Code, sau đó gọi lại `/i-have-adhd`.

## Ghi nhận tác giả (Credits)

Lấy cảm hứng một phần từ cuốn *The Adult ADHD Tool Kit* của J. Russell Ramsay và Anthony L. Rostain. Được điều chỉnh cho cách một LLM nên phản hồi, chứ không phải cách con người nên tổ chức một ngày của mình.

## Giấy phép

MIT.

Hãy ⭐ repo nếu nó giúp bạn khỏi phải cuộn qua thêm một câu “Câu hỏi rất hay!”
