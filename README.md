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
```
## Setup
1. `Clone the Repository`: Download or clone the repository to your local machine.

2. `Set Up Environment Variables`: Create a .env file in the project directory to store sensitive information like your Google API key.

Example .env file:
```bash
GOOGLE_API_KEY=your_google_api_key_here

```
3. `Run the App`:After setting up, navigate to the project folder and run the Streamlit app using the following command:
```bash
streamlit run app.py


```
## Example Interaction:

- **Upload Resume:**: Upload your resume (PDF format), and the bot will evaluate how well it matches the job description.
- **Job Description**: Enter the job description, and the bot will compare it with your resume to calculate the JD match percentage.
- **Chat with the Bot**: The bot provides specific recommendations to improve your resume, highlighting missing keywords and suggesting ways to optimize it for the job market.
- **Feedback**: Simulates an ATS evaluation by analyzing your resume's content against the job description.







## Contributing

We welcome contributions to the project! If you'd like to contribute, follow these steps:

1- `Fork the repository`.

2- `Create a new branch`.

3- `Make your changes and commit them.
Open a pull request with a description of your changes`.



## License


### Key Points:
- You can continue to add sections after the `pip install` code block, as shown above.
- Use markdown syntax to format headings, bullet points, and code blocks.
- After the `pip install` command, I added more detailed instructions on setup, usage, and contributing.

















