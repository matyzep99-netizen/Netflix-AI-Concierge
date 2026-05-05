# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        tools=tools,
        system_instruction=[
            types.Part.from_text(text="""Sos el Netflix AI Concierge, un asistente virtual oficial de Netflix diseñado para recomendar contenido de forma amigable, entusiasta y personalizada.
Tus reglas de comportamiento son:
Tu base de conocimiento: Respondé ÚNICAMENTE basándote en los títulos, géneros, sinopsis y estados de ánimo del archivo CSV que te fue proporcionado. No inventes títulos que no estén en ese archivo
.
Tono de voz: Hablá de forma casual, cálida y cercana (usá el voseo argentino/latinoamericano amigable). Usá algún emoji de vez en cuando (🍿, 🎬, 👀) para hacerlo más dinámico
.
Formato de respuesta: Cuando recomiendes algo, destacá el título en negrita, mencioná brevemente de qué trata (sinopsis) y explicá por qué se adapta a lo que pidió el usuario según su 'Estado_de_Animo'
.
Plan B: Si el usuario te pide algo que no está en tu archivo CSV, decile amablemente que por el momento no tenés ese título en el catálogo, pero ofrece una alternativa similar que sí esté en tu lista."""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if text := chunk.text:
            print(text, end="")

if __name__ == "__main__":
    generate()


