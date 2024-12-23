Smart ATS Chatbot
This project is a smart chatbot powered by AI, designed to help job seekers assess how well their resumes align with job descriptions. It can give feedback on how to improve your resume for a better chance of catching a recruiter’s eye.

What the Bot Does
Evaluates Resume and Job Description: Compares your resume to a job description and tells you how well it fits.
Gives Feedback: Scores the resume on a scale from 1 to 10 and suggests improvements.
Highlights Missing Keywords: Looks for important keywords in the job description that may be missing from your resume.
Works with PDFs: You can upload your resume in PDF format.
Requirements
You'll need a few Python packages to run this chatbot:

streamlit: To create the web app.
google-generativeai: This is used for the AI part that compares resumes and job descriptions.
PyPDF2: For reading resumes that are uploaded as PDFs.
python-dotenv: To keep your API key secure.
crewai: For running tasks automatically.
To install the necessary libraries, just run:

bash
Copier le code
pip install streamlit google-generativeai PyPDF2 python-dotenv crewai
How to Set It Up
1. Get Your API Key
To use Google’s generative AI, you'll need an API key from Google Cloud:

Go to the Google Cloud Console and create a project.
Enable the Gemini API for your project.
Copy the API Key and use it in the next step.
2. Set Up Your Environment
Create a file called .env and add your API key like this:

plaintext
Copier le code
GOOGLE_API_KEY=your_google_api_key_here
3. Run the Application
Once you’ve got the dependencies and your API key set up, you can start the app by running:

bash
Copier le code
streamlit run app.py
This will open the chatbot in your web browser, and you can start interacting with it.

Files in the Project
Here's a quick rundown of the project files:

plaintext
Copier le code
.
├── app.py                # The main Streamlit app
├── .env                  # The file where you store your API key
├── requirements.txt      # The list of packages you'll need to install
└── README.md             # This file
How to Use the Bot
Once the app is up and running, here's what you need to do:

Enter the Job Description: Paste the job description into the text box.
Upload Your Resume: Upload a PDF version of your resume.
Ask the ATS Bot for Help: Type your message, and the bot will give you feedback on your resume.
How the Chat Works
Step 1: Paste the Job Description.
Step 2: Upload your resume (PDF format).
Step 3: The bot will evaluate your resume and give it a score out of 10.
Step 4: It will suggest ways to improve your resume based on the JD.
Example Walkthrough
Job Description:
The job description could look something like this:

Job Title: Data Scientist
Responsibilities: Analyze data, build predictive models, work with large datasets, and visualize data.

Resume Evaluation:
The bot will check the job description and compare it to your resume.
It will tell you what’s missing, how much of the description your resume matches, and suggest ways to improve it.
How the Bot Works
The AI engine, powered by Google’s Gemini model, evaluates your resume based on a custom prompt. It checks for:

The match between the resume and job description (how many key points line up).
Missing keywords that should be added to improve the match.
Improvement suggestions to help you optimize your resume for that specific role.
Contributing
If you want to help improve the project, feel free to fork the repo and submit a pull request. Just make sure to write clear, understandable code, and include any new tests for features you add.

License
The project is open-source and licensed under the MIT License.

Thanks To
Google Gemini for making AI evaluations possible.
Streamlit for providing an easy way to build the app.
PyPDF2 for reading PDF files.
CrewaI for making it easier to automate tasks.

