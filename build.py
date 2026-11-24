"""Tạo index.html (bản cho GitHub Pages) từ src/page.html.

src/page.html chứa nội dung trang: <title>, <style>, phần thân và <script>.
Bản trên Claude dùng thẳng file này. GitHub Pages thì cần một file HTML
đầy đủ, nên script này bọc thêm <!doctype html>, <html>, <head>, <body>.

Cách chạy (chỉ dùng thư viện có sẵn của Python):
    python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MARKER = "<!-- body -->"  # dấu chia phần <head> và phần thân trong src/page.html

# Biểu tượng trên tab trình duyệt: 4 ô tròn A B C D, ô thứ hai được tô (như phiếu trắc nghiệm)
FAVICON = (
    '<link rel="icon" href="data:image/svg+xml,'
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
    "%3Crect width='64' height='64' rx='14' fill='%23fbf7f8'/%3E"
    "%3Ccircle cx='13' cy='32' r='6' fill='none' stroke='%23c4385a' stroke-width='3'/%3E"
    "%3Ccircle cx='26' cy='32' r='7.5' fill='%232a2528'/%3E"
    "%3Ccircle cx='39' cy='32' r='6' fill='none' stroke='%23c4385a' stroke-width='3'/%3E"
    "%3Ccircle cx='52' cy='32' r='6' fill='none' stroke='%23c4385a' stroke-width='3'/%3E"
    '%3C/svg%3E">'
)


def main() -> None:
    source = (ROOT / "src" / "page.html").read_text(encoding="utf-8")
    if MARKER not in source:
        raise SystemExit("Không thấy dấu <!-- body --> trong src/page.html")

    head, body = source.split(MARKER, 1)
    html = (
        "<!doctype html>\n"
        '<html lang="vi">\n'
        "<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f"{FAVICON}\n"
        f"{head.strip()}\n"
        "</head>\n"
        "<body>\n"
        f"{body.strip()}\n"
        "</body>\n"
        "</html>\n"
    )
    out = ROOT / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"Đã tạo {out.name} ({len(html):,} ký tự)")


if __name__ == "__main__":
    main()
