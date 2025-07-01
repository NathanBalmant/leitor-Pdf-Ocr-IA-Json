
# 🧠 OCR Inteligente de Propostas de Seguro

Este projeto realiza a **extração automática de informações de propostas de seguro** a partir de **PDFs escaneados**. Ele combina OCR com Tesseract e um modelo LLM via LangChain + Groq para entregar os dados estruturados em formato JSON.

---

## 🚀 Funcionalidades

- 🖼️ Conversão de PDFs escaneados em imagens usando `pdf2image` + Poppler
- 🔍 Extração de texto via OCR com `pytesseract`
- 🤖 Interpretação de dados com LangChain e Groq (LLM)
- 🔐 Variáveis sensíveis carregadas via `.env`
- ⚠️ Tratamento de erros com `try/except` para produção

---

## 🗂 Estrutura esperada

```
projeto/
├── pdfs/
│   └── PDF2.pdf          # PDF de entrada (não incluído no repositório)
├── leitorPDF.py          # Script principal
├── .env                  # Contém a variável GROQ_API_KEY
├── .gitignore            # Ignora arquivos sensíveis e temporários
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.9+
- Tesseract OCR
- Poppler (para pdf2image)
- Conta Groq e chave de API válida

---

## 📥 Como instalar Tesseract e Poppler (Windows)

### 🔤 Tesseract OCR

1. Baixe o instalador em:  
   https://github.com/UB-Mannheim/tesseract/wiki

2. Execute o instalador (`.exe`).

3. O executável será instalado em:  
   `C:\Program Files\Tesseract-OCR\tesseract.exe`

### 🖼️ Poppler

1. Baixe o pacote em:  
   https://github.com/oschwartz10612/poppler-windows/releases

2. Extraia o `.zip` para um local como:  
   `C:\poppler-xx.xx.x\`

3. Use o caminho da pasta `bin` no seu código, por exemplo:  
   `C:\poppler-xx.xx.x\Library\bin`

---

## 📦 Instalação do Projeto

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

pip install pdf2image pytesseract pillow python-dotenv langchain langchain-groq
```

---

## 🔐 Configuração do `.env`

Crie um arquivo `.env` com a sua chave Groq:

```
GROQ_API_KEY=sua_chave_aqui
```

---

## ▶️ Execução

```bash
python leitorPDF.py
```

---

## ✅ Saída esperada

O script imprime no console um objeto JSON com os seguintes dados extraídos do PDF:

- Informações do cliente
- Detalhes do veículo
- Dados da apólice
- Parcelas
- Documentos do cliente
- Dados de sinistro (se houver)

---

## ❗ Importante

- Os arquivos PDF **não devem ser versionados** (estão ignorados via `.gitignore`)
- A chave de API Groq deve estar **somente no `.env`**



