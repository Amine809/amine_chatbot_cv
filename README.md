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
-pip install streamlit google-generativeai PyPDF2 python-dotenv crewai
Setup
For detailed setup instructions, check the SETUP.md file.

## How It Works
Upload Resume: Upload your resume in PDF format using the file uploader.
Paste Job Description: Enter the job description that you want to match your resume against. The job description will be compared to the content of your uploaded resume.
Chat with the ATS Bot: You can chat with the bot using the input text box. If the bot needs further information (like the job description or resume), it will ask you to provide it.
Receive Feedback:
JD Match Percentage: How well your resume aligns with the job description.
Missing Keywords: A list of important keywords that are missing from your resume.
Profile Summary: A brief summary of the resume's strengths and weaknesses.
Recommendations: Three actionable suggestions to improve your resume and increase its chances of being shortlisted.
## Example Interaction
Upload Resume: Select a PDF file of your resume.
Job Description: Paste the job description of a job you are applying to.
Chat with the Bot: The bot will analyze and provide feedback on how well your resume matches the job description.
Feedback: The bot will give a JD match percentage, list missing keywords, and provide a profile summary with recommendations.
## Contributing
We welcome contributions to the project! If you'd like to contribute, follow these steps:

Fork the repository.
Create a new branch.
Make your changes and commit them.
Open a pull request with a description of your changes.









