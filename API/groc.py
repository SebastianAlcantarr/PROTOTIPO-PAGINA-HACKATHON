from groq import Groq
import json, os
from schemas import InversionParametros
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


client = Groq(api_key="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")

def analizar_oportunidades(params: InversionParametros) -> dict:
    prompt = f"""
    Eres un consultor de inversiones especializado en Hermosillo, Sonora, Mexico.
    Analiza el perfil de inversionista y responde UNICAMENTE en formato JSON valido.

    PARAMETROS DEL INVERSIONISTA:
    - Sector de interes: {params.sector}
    - Presupuesto: ${params.presupuesto_min}M - ${params.presupuesto_max}M
    - Plazo de retorno esperado: {params.plazo_retorno}
    - Tolerancia al riesgo: {params.riesgo}
    - Notas adicionales: {params.preferencias or "Ninguna"}

    Considera el contexto economico real de Hermosillo:
    - Parques industriales (FINSA, Tetakawi, San Carlos)
    - Industria automotriz (Ford, proveedores tier 1/2)
    - Mineria y agroindustria regional
    - Sector tecnologico emergente
    - Turismo y servicios

    Tu respuesta debe ser un JSON con esta estructura exacta:
    {{
      "empresas": [
        {{
          "nombre": "Nombre de empresa real o tipo de empresa sugerida",
          "sector": "sector especifico",
          "quienes_son": "descripcion breve de quienes son y a que se dedican",
          "origen": "ciudad/estado/pais de origen o presencia relevante",
          "por_que_encaja": "explicacion breve",
          "nivel_riesgo": "bajo/medio/alto",
          "potencial_retorno": "descripcion del retorno esperado"
        }}
      ],
      "resumen": "resumen ejecutivo de 2-3 oraciones"
    }}

    Reglas:
    - Sugiere entre 3 y 6 oportunidades relevantes.
    - Si no hay una empresa puntual, usa un tipo de empresa realista para el sector.
    - El campo "origen" debe venir siempre informado.
    """
    

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}  
    )

    return json.loads(response.choices[0].message.content)
