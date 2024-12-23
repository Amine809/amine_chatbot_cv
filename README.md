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


