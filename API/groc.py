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
    Pero no hables como el mismo , no eres la persona , eres una IA que predice e informa no 
    la persona no primera persona
    Analiza el perfil de inversionista y responde UNICAMENTE en formato JSON valido.

    PARAMETROS DEL INVERSIONISTA:
    - Sector de interes: {params.sector}
    - Presupuesto: ${params.presupuesto_min}M - ${params.presupuesto_max}M
    - Plazo de retorno esperado: {params.plazo_retorno}
    - Tolerancia al riesgo: {params.riesgo}
    - Notas adicionales: {params.preferencias or "Ninguna"}
   
    
    Considera el contexto economico real de Hermosillo:
    - Parques industriales (nombres de parques en hermosillo)
    - Industria automotriz (empresas con presencia en hermosillo)
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
          "origen": "ciudad/estado/pais de origen o presencia relevante , de preferencia el origen que sea americano , al buscar inversion
          mas aprxomiado a sonora ",
          "por_que_encaja": "explicacion breve",
          "nivel_riesgo": "bajo/medio/alto",
          "potencial_retorno": "descripcion del retorno esperado"
        }}
      ],
      Despues haras un resumen que diga , como tu como empresa del sector  :{params.sector} puede ofrecer para las empresas extranjeras ,
       no una por una si no , como el empresario/gobierno que usa el software podria hacer para que dichas empresas vengan a hermosillo , que ventajas
       le ofreceria moverse para aca 
      "resumen": "resumen ejecutivo de 5-6 oraciones"
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
