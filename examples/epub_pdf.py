from ebooklib import epub
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

def epub_to_pdf(epub_path, pdf_path):
    book = epub.read_epub(epub_path)
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    x_margin = 2 * cm
    y_position = height - 2 * cm
    max_width = width - 2 * x_margin

    c.setFont("Times-Roman", 12)

    for item in book.get_items():
        if item.get_type() == epub.EpubHtml:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text().strip().split('\n')

            for line in text:
                clean_line = line.strip()
                if clean_line:
                    for wrapped_line in split_line(clean_line, c, max_width):
                        if y_position < 2 * cm:
                            c.showPage()
                            c.setFont("Times-Roman", 12)
                            y_position = height - 2 * cm
                        c.drawString(x_margin, y_position, wrapped_line)
                        y_position -= 14  # line spacing

    c.save()
    print(f"✅ PDF gerado com sucesso: {pdf_path}")

def split_line(text, canvas_obj, max_width):
    """Quebra linhas longas respeitando a largura do PDF"""
    words = text.split()
    lines = []
    line = ''
    for word in words:
        if canvas_obj.stringWidth(line + ' ' + word) < max_width:
            line += ' ' + word if line else word
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines

# Exemplo de uso
epub_to_pdf("livro.epub", "livro_convertido.pdf")
