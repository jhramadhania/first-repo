import google.generativeai as genai #pyright: ignore[reportMissingImports]

genai.configure(api_key="YOUR_GEMINI_TOKEN")

def generate_blog(paragraph_topic):
    model = genai.GenerativeModel('gemini-2.5-flash') 
    prompt = f"Write a paragraph about the following topic: {paragraph_topic}"

    response = model.generate_content(prompt)

    if response.candidates:
        return response.candidates[0].content.parts[0].text
    else:
        return "No response generated."

print(generate_blog('Why NYC is better than your city.'))