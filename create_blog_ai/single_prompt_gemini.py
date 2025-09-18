import google.generativeai as genai #pyright: ignore[reportMissingImports]

genai.configure(api_key="YOUR_GEMINI_TOKEN")

def generate_blog(paragraph_topic):
    model = genai.GenerativeModel('gemini-2.5-flash') 
    prompt = f"Write a paragraph about the following topic: {paragraph_topic}"

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.3,
            "max_output_tokens": 2048
        }
    )

    retrieve_blog = response.candidates[0].content.parts[0].text
    return retrieve_blog

print(generate_blog('Why NYC is better than your city.'))