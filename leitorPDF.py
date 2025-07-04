from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import pytesseract
from pdf2image import convert_from_bytes
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
import os

# Para rodar a API use: uvicorn leitorPDF:app --reload

# Inicializa
load_dotenv()
app = FastAPI()

# Caminhos locais
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
poppler_path = r"C:\\poppler-24.08.0\\Library\\bin"

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("Erro: variável GROQ_API_KEY não está definida no .env")

# Modelo LLM
llm = ChatGroq(
    api_key=api_key,
    model='meta-llama/llama-4-scout-17b-16e-instruct',
    temperature=0,
)

template = """
Prompt para Extração de Dados de Propostas de Seguro - Loja de Seguros (Multi-Tenant SaaS)

Sua tarefa é extrair as seguintes informações de uma proposta de seguro auto:

Campos a extrair:

- Cliente:
Nome, CPF, Data de Nascimento, Estado Civil, Profissão, Possui Empresa Própria (true/false), Nome da Empresa (se houver), Número da CNH, Categoria da CNH, Vencimento da CNH, Endereço, Telefone, Email, Observações.

- Veículo:
Marca, Modelo, Placa, Ano de Fabricação, Ano Modelo, Cor, Chassi, Renavam, Tipo de Combustível, Categoria, Valor FIPE.

- Apólice:
Número da Apólice, Vigência Início, Vigência Fim, Prêmio, Valor de Cobertura, Franquia, Bônus Percentual, e as seguintes coberturas adicionais (cada uma como true ou false):
Danos Materiais (DM), Danos Corporais (DC), APP, DMO, Carro Reserva, Reboque, Vidros.

- Parcelas:
Uma lista contendo cada parcela, com os campos: Número da Parcela, Valor, Data de Vencimento, Forma de Pagamento.

- Documentos do Cliente:
Uma lista (que pode estar vazia) com os seguintes campos para cada documento: Tipo de Documento, Nome do Arquivo, Caminho do Arquivo.

- Sinistro:
Se houver, inclua os dados de sinistro vinculados à apólice. Caso não exista, deixe o campo como null.

Formato de saída:
Retorne todas as informações dentro de um único objeto JSON, com os seguintes campos principais de nível superior:

Regras obrigatórias:
- Se algum campo estiver ausente no texto, preencha com null.
- Campos booleanos devem ser true ou false.
- Valores numéricos devem ser números, não strings.
- Datas devem estar no formato: AAAA-MM-DD.
- Retorne apenas o JSON, sem comentários ou explicações adicionais.

{text}
"""

prompt = PromptTemplate(
    input_variables=['text'],
    template=template,
)

@app.post("/extrair")
async def extrair_pdf(file: UploadFile = File(...)):
    try:
        pdf_bytes = await file.read()
        pages = convert_from_bytes(pdf_bytes, poppler_path=poppler_path)
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro ao converter PDF: {e}"})

    text_data = ''
    for page in pages:
        try:
            text_data += pytesseract.image_to_string(page) + '\n'
        except Exception as e:
            return JSONResponse(status_code=500, content={"erro": f"Erro no OCR: {e}"})

    try:
        chain = prompt | llm | JsonOutputParser()
        response = chain.invoke({"text": text_data})
        return response
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Erro ao rodar o modelo LLM: {e}"})
