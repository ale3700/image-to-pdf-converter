# Conversor de Imagens para PDF

Este é um script Python que permite selecionar múltiplas imagens e convertê-las em um único arquivo PDF. Além disso, o usuário pode escolher onde salvar o PDF final.

## Tecnologias Utilizadas
- Python 3
- Biblioteca `Pillow` para manipulação de imagens
- Biblioteca `tkinter` para seleção de arquivos

## Instalação

Antes de executar o script, instale a biblioteca necessária:
```bash
pip install pillow
```

## Como Usar
1. Execute o script `conversor.py`.
2. Uma janela será aberta para que você possa selecionar as imagens (`.jpg`, `.png`, `.jpeg`).
3. Após selecionar as imagens, outra janela aparecerá para que você escolha onde salvar o PDF gerado.
4. O PDF será criado no local escolhido e uma mensagem confirmará o salvamento.

## Estrutura do Código
- `selecionar_imagens()`: Abre um seletor de arquivos para escolher imagens.
- `salvar_pdf()`: Abre um seletor para definir o local e nome do PDF.
- `imagens_para_pdf(lista_imagens, pdf_path)`: Converte as imagens selecionadas para PDF e salva no local escolhido.

## Exemplo de Execução
```bash
python conversor.py
```

## Observação
Certifique-se de que as imagens que deseja converter estejam disponíveis e que você tenha permissão para acessar os arquivos.

## Licença
Este projeto está sob a licença MIT.

