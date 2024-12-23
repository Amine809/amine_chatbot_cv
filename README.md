# Smart ATS Chatbot

This is a **Smart ATS (Application Tracking System) Chatbot** that helps evaluate and improve your resume based on a given job description. The bot leverages advanced AI technology for assessing the match between a resume and a job description, scoring the resume, and providing actionable recommendations for improvement.

## Features

- **Resume Evaluation**: Upload your resume (PDF format), and the bot will evaluate how well it matches the job description.
- **Job Description Matching**: Enter the job description, and the bot will compare it with your resume to calculate the JD match percentage.
- **Resume Recommendations**: The bot provides specific recommendations to improve your resume, highlighting missing keywords and suggesting ways to optimize it for the job market.
- **ATS-like Evaluation**: Simulates an ATS evaluation by analyzing your resume's content against the job description.

## Requirements

- Python 3.x
- Required Python Libraries:
  - `streamlit`: For building the web interface.
  - `google-generativeai`: For leveraging Google's generative AI model.
  - `PyPDF2`: For PDF text extraction.
  - `python-dotenv`: For managing environment variables.
  - `crewai`: For creating AI workflows and agents.

You can install the required libraries using the following:

```bash

pip install streamlit google-generativeai PyPDF2 python-dotenv crewai

## Setup

Setup
1-Clone the Repository (if applicable) or download the project files to your local machine.

2-Set up Environment Variables: Create a .env file in the project directory to store your Google API key.

```bash

GOOGLE_API_KEY=your_google_api_key_here

3-Run the App: Navigate to the project folder and run the Streamlit app using the following command:
```bash

streamlit run app.py

##How It Works
1. Upload Resume
Upload your resume in PDF format using the file uploader.

2. Paste Job Description
Enter the job description that you want to match your resume against. The job description will be compared to the content of your uploaded resume.

3. Chat with the ATS Bot
You can chat with the bot using the input text box. If the bot needs further information (like the job description or resume), it will ask you to provide it.

4. Receive Feedback
-JD Match Percentage: How well your resume aligns with the job description.
-Missing Keywords: A list of important keywords that are missing from your resume.
-Profile Summary: A brief summary of the resume's strengths and weaknesses.
-Recommendations: Three actionable suggestions to improve your resume and increase its chances of being shortlisted.





