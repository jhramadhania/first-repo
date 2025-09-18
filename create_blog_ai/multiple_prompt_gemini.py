import google.generativeai as genai #pyright: ignore[reportMissingImports]
from dotenv import dotenv_values

config = dotenv_values('.env')

genai.configure(api_key=config['API_KEY'])

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

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False