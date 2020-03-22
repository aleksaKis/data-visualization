import pdftotext

with open('books/hamlet.pdf', 'rb') as f:
    pdf = pdftotext.PDF(f)

with open('books/hamlet.txt', 'w') as f:
    f.write('\n'.join(pdf))