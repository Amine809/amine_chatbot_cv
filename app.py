import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
from crewai import Task, Agent, Workflow  # Crewai imports

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Crewai Agents and Tasks Setup
class ATSAgent(Agent):
    def process(self, resume_text, job_description):
        prompt = input_prompt.format(text=resume_text, jd=job_description)
        response = get_gemini_response(prompt)
        return response

class ResumeAnalysisTask(Task):
    def execute(self, resume_text, job_description):
        ats_agent = ATSAgent()
        result = ats_agent.process(resume_text, job_description)
        return result

workflow = Workflow(name="ATS Resume Evaluation Workflow")
workflow.add_task(ResumeAnalysisTask())

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page_content = reader.pages[page]
        text += str(page_content.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of the tech field, software engineering, data science, data analysis, and big data engineering.
Your task is to evaluate the resume based on the given job description. You must consider the job market is very competitive and you should provide the best assistance for improving the resumes. Assign the percentage Matching based on JD and the missing keywords with high accuracy.
Provide recommendations to improve the resume. Additionally, assign a score out of 10 based on how well the resume matches the JD and include three specific recommendations for improvement.
Resume: {text}
Description: {jd}
I want the response in one single string having the structure:
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":"","Score":"/10","Recommendations":["", "", ""]}}
"""

# Streamlit app
st.set_page_config(page_title="Smart ATS Chatbot", layout="wide")
st.title("🤖 Smart ATS Chatbot")
st.markdown("<style>.chat-box {background-color: #f7f9fc; border-radius: 10px; padding: 15px; margin: 10px 0;} .user-message {background-color: #d1e7dd; text-align: left; padding: 10px; border-radius: 10px; margin-bottom: 10px; display: inline-block;} .bot-message {background-color: #fff3cd; text-align: left; padding: 10px; border-radius: 10px; margin-bottom: 10px; display: inline-block;}</style>", unsafe_allow_html=True)

st.text("Chat with our ATS bot to evaluate and improve your resume's compatibility with job descriptions!")

# Chat History
def chat_message(sender, message):
    if sender == "user":
        st.markdown(f'<div class="chat-box user-message">You: {message}</div>', unsafe_allow_html=True)
    elif sender == "bot":
        st.markdown(f'<div class="chat-box bot-message">ATS Bot: {message}</div>', unsafe_allow_html=True)

# User Input
jd = st.text_area("Paste the Job Description", help="Enter the job description for which your resume will be evaluated.")
user_message = st.text_input("Chat with the ATS Bot", help="Type your message here.")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF file containing your resume.")

# Chatbot Logic
if user_message:
    if "job description" in user_message.lower() and jd:
        chat_message("user", user_message)
        chat_message("bot", "Got it! Please share your CV so I can help.")
    elif uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        if jd.strip():
            chat_message("user", "Here is my CV.")

            # Execute Crewai Workflow
            try:
                result = workflow.run(resume_text=text, job_description=jd)
                parsed_response = json.loads(result)
                chat_message("bot", f"Your CV scored **{parsed_response['Score']}/10**. Here's how you can improve:")
                for rec in parsed_response['Recommendations']:
                    chat_message("bot", f"- {rec}")
            except Exception as e:
                chat_message("bot", f"An error occurred: {str(e)}")
        else:
            chat_message("bot", "Please paste the job description to proceed with the analysis.")
    else:
        chat_message("user", user_message)
        chat_message("bot", "Please upload your CV to proceed.")
