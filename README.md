# 📄 Leitor de PDF com OCR + IA (FastAPI)

Esta aplicação é uma **API REST em Python** que recebe arquivos PDF escaneados, converte as páginas em imagem, aplica OCR (reconhecimento óptico de caracteres) com Tesseract e utiliza um modelo LLM via LangChain para **extrair dados estruturados de propostas de seguro auto** em formato JSON.

---

## 🚀 Como funciona

1. O PDF é enviado via `POST` para o endpoint `/extrair`
2. O arquivo é convertido em imagens usando `pdf2image` + Poppler
3. É aplicado OCR em cada imagem com `pytesseract`
4. O texto é analisado pelo LLM via LangChain para gerar um JSON estruturado com os dados da proposta

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/NathanBalmant/leitor-Pdf-Ocr-IA-Json.git
cd leitor-Pdf-Ocr-IA-Json
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Instale o [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) e o [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)

- **Tesseract**: após instalar, anote o caminho do executável (ex: `C:\Program Files\Tesseract-OCR\tesseract.exe`)
- **Poppler**: baixe e extraia. Use o caminho da pasta `Library/bin` (ex: `C:\poppler-xx\Library\bin`)

---

## 🔐 Variáveis de ambiente

Crie um arquivo `.env` com sua chave da API Groq:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Como rodar

```bash
uvicorn leitorPDF:app --reload
```

Depois, acesse:  
[http://localhost:8000/docs](http://localhost:8000/docs) para testar a API com Swagger.

---

## 📤 Como usar o endpoint

- **Rota**: `POST /extrair`
- **Corpo**: Envie um arquivo PDF (`multipart/form-data`)
- **Resposta**: JSON com os dados extraídos da proposta de seguro

---

## 📁 Estrutura esperada na resposta

```json
{
  "cliente": {
    "nome": "Fulano de Tal",
    "cpf": "000.000.000-00",
    "data_nascimento": "1990-01-01"
  },
  "veiculo": {
    "marca": "Ford",
    "modelo": "Fiesta"
  },
  "apolice": {},
  "parcelas": [],
  "documentos_cliente": [],
  "sinistro": null
}
```

---

## 💡 Tecnologias utilizadas

- FastAPI
- LangChain + Langchain-groq
- Tesseract OCR
- Poppler + pdf2image
- Python 3.11+

---

