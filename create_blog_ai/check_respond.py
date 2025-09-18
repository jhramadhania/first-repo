import google.generativeai as genai  # pyright: ignore[reportMissingImports]

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

    # Debug: print the full response structure
    print("Raw response:", response, "\n")

    if response.candidates:
        candidate = response.candidates[0]
        print("Finish reason:", candidate.finish_reason)
        print("Safety ratings:", candidate.safety_ratings)

        if candidate.content.parts:
            return candidate.content.parts[0].text
        else:
            return f"No text parts. Finish reason: {candidate.finish_reason}"
    else:
        return "No candidates generated."

print(generate_blog("Why NYC is better than your city."))