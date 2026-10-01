import fitz

pdf = fitz.open("entry/lorem-ipsum.pdf")

print("PDF aberto com sucesso")
print("Quantidade de páginas:", len(pdf))

for numero, pagina in enumerate(pdf):
    texto = pagina.get_text()

    print(f"\n===   PÁGINA {numero + 1}  ===")
    print(texto)