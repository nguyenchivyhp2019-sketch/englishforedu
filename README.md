# EnglishForEdu

Trang web miễn phí giúp học sinh lớp 12 ôn thi tiếng Anh tốt nghiệp THPT 2027.

**Xem trang:** https://nguyenchivyhp2019-sketch.github.io/englishforedu/

## Trang có gì

- **Lộ trình ôn thi**: cấu trúc đề 40 câu, tự xác định mức (A, B, C, D) từ số câu đúng, 5 giai đoạn từ nay đến ngày thi, và danh sách web học miễn phí kèm mức độ phù hợp.
- **Trợ lý tra từ**: tra từ, cụm từ, hoặc dán cả câu rồi bấm vào từ cần tra. Trợ lý cho nghĩa tiếng Việt, nghĩa tiếng Anh, phiên âm, từ đồng nghĩa và trái nghĩa, và luôn ghi nguồn. Từ tra được có thể lưu vào sổ từ rồi xuất sang Quizlet hoặc Anki.

## Trợ lý tra từ lấy dữ liệu ở đâu

| Nguồn | Dùng cho |
|---|---|
| [Wiktionary tiếng Việt](https://vi.wiktionary.org) | Nghĩa tiếng Việt, câu ví dụ có dịch |
| [Datamuse API](https://www.datamuse.com/api/) | Nghĩa tiếng Anh, từ đồng nghĩa, trái nghĩa, gợi ý chính tả |
| [Free Dictionary API](https://dictionaryapi.dev) | Phiên âm, file phát âm, câu ví dụ |

Dữ liệu Wiktionary dùng giấy phép CC BY-SA.

Bản web này **không dùng AI**. Mọi nghĩa đều lấy từ từ điển; từ nào từ điển không có thì trợ lý báo là không tìm thấy, không tự đoán nghĩa.
Khi mở trang trong Claude (artifact), trợ lý có thêm chế độ AI để giải thích nghĩa theo ngữ cảnh. Chế độ này dùng lượt Claude của chính người xem.

## Thư mục

| File | Là gì |
|---|---|
| `src/page.html` | Mã nguồn trang: HTML, CSS và JavaScript trong một file |
| `build.py` | Tạo `index.html` từ `src/page.html` |
| `index.html` | File GitHub Pages hiển thị. File này được tạo tự động, đừng sửa trực tiếp |

## Sửa trang

1. Sửa `src/page.html`.
2. Chạy `python3 build.py`. Script chỉ dùng thư viện có sẵn của Python, không cần cài thêm gì.
3. Xem thử: chạy `python3 -m http.server` trong thư mục này rồi mở http://localhost:8000.
4. Đưa lên GitHub: `git add -A`, `git commit -m "..."`, `git push`. GitHub Pages tự cập nhật sau khoảng 1 phút.

## Lưu ý

Thông tin về kỳ thi được tổng hợp ngày 24/11/2026 từ LangGo, VnExpress và HOCMAI. Mục tiêu điểm, cách chia thời gian và lộ trình chỉ là gợi ý ôn tập, không phải quy định. Khi Bộ GD&ĐT công bố quy chế hoặc đề tham khảo năm 2027, hãy kiểm tra lại.
