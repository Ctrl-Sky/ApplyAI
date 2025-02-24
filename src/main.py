from dotenv import load_dotenv
from google import genai
import format_prompts
import helpers
import os

def generate_resume_and_cl():
    # Get resume and cover letter prompt
    resume_prompt = format_prompts.get_resume_prompt()
    cl_prompt = format_prompts.get_cl_prompt(phone_number, email)

    # Create conversation with gemini model
    client = genai.Client(api_key=gemini_api_token)
    chat = client.chats.create(model="gemini-2.0-flash")

    # Get response from prompt and write to docs
    response = chat.send_message(resume_prompt)
    helpers.formatted_text_to_docx(response.text, "resume.docx")
    response = chat.send_message(cl_prompt)
    helpers.formatted_text_to_docx(response.text, "cover_letter.docx")


if __name__=="__main__":
    # Load and get environment variables from .env
    load_dotenv()
    gemini_api_token = os.getenv("GEMINI_API_TOKEN")
    phone_number = os.getenv("PHONE_NUMBER")
    email = os.getenv("EMAIL")

    generate_resume_and_cl()

