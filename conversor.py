from PIL import Image
from tkinter import Tk, filedialog

def selecionar_imagens():
    root = Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    arquivos = filedialog.askopenfilenames(
        title="Selecione as imagens",
        filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")]
    )
    return list(arquivos)

def salvar_pdf():
    root = Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    pdf_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Salvar PDF como"
    )
    return pdf_path

def imagens_para_pdf(lista_imagens, pdf_path):
    if not lista_imagens:
        print("Nenhuma imagem selecionada.")
        return

    imagens = [Image.open(img).convert("RGB") for img in lista_imagens]  # Abre e converte todas as imagens para RGB
    imagens[0].save(pdf_path, save_all=True, append_images=imagens[1:])  # Salva a primeira imagem e adiciona as demais
    print(f"PDF salvo em: {pdf_path}")

# Selecionar imagens e gerar PDF
imagens_selecionadas = selecionar_imagens()
if imagens_selecionadas:
    pdf_destino = salvar_pdf()
    if pdf_destino:
        imagens_para_pdf(imagens_selecionadas, pdf_destino)
    else:
        print("Nenhum local foi selecionado para salvar o PDF.")
else:
    print("Nenhuma imagem foi selecionada.")
