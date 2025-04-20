import google.generativeai as genai

gemini_MODELS = {
    "gemini-pro": genai.GenerativeModel(model_name="gemini-1.5-pro"),
    # "gemini-flash": genai.GenerativeModel(model_name="gemini-1.5-pro"),
    # "gemini-ultra": genai.GenerativeModel(model_name="gemini-1.5-pro"),
}