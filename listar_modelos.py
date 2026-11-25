import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6LREkuwh5MzExi1a_t1M8Kcb200PaAGYt6YzHjgHbvj2g")

for model in genai.list_models():
    print(model.name)