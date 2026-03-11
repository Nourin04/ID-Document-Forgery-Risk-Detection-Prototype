import google.generativeai as genai
from PIL import Image
from config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)


def analyze_with_gemini(image_path):

    try:
        image = Image.open(image_path)

        prompt = """
        Analyze this ID document image for possible signs of forgery or tampering.

        Check for:
        - inconsistent fonts
        - edited regions
        - unusual artifacts
        - misaligned text
        - suspicious layout

        Return a short explanation and fraud risk score.
        """

        response = model.generate_content([prompt, image])

        return response.text

    except Exception as e:
        return f"AI analysis unavailable: {str(e)}"