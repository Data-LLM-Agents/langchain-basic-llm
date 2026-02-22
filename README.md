# LangChain Basic LLM Tutorial - Juan Pablo Nieto Cortes

Este repositorio contiene la implementación básica de una cadena de LangChain, parte del Laboratorio 4 de AREP. Demuestra el uso de plantillas de prompts, modelos de chat y analizadores de salida.

## Arquitectura

La aplicación sigue el patrón LCEL (LangChain Expression Language):
`PromptTemplate` -> `LLM (Groq/OpenAI)` -> `StrOutputParser`

1.  **PromptTemplate**: Define la estructura del mensaje.
2.  **LLM**: El cerebro que procesa el texto (usamos Groq por velocidad y costo cero).
3.  **StrOutputParser**: Convierte la respuesta del modelo en un string limpio.

## Instalación

1.  **Clonar**: `git clone <repo_url>`
2.  **Dependencias**: `pip install -r requirements.txt`
3.  **Configuración**: Crea un `.env` con:
    ```
    GROQ_API_KEY=tu_api_key_aqui
    ```

## Ejecución

-   **Script**: `python llm_free.py`
-   **Libro Interactivo**: Abre `LIBRO_JUAN_PABLO.ipynb`

---
Desarrollado por **Juan Pablo Nieto Cortes**.
