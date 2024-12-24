<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart ATS Chatbot</title>
    <style>
        /* General Styles */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f7fa;
            margin: 0;
            padding: 0;
            color: #333;
        }

        h1, h2, h3 {
            color: #2c3e50;
            margin-bottom: 10px;
        }

        p {
            line-height: 1.6;
            margin-bottom: 10px;
        }

        a {
            color: #3498db;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* Container */
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 40px 0;
        }

        /* Header */
        header {
            background-color: #2980b9;
            color: white;
            padding: 20px 0;
            text-align: center;
        }

        header h1 {
            margin: 0;
        }

        header p {
            font-size: 18px;
        }

        /* Features Section */
        .features {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        .feature {
            width: 48%;
            background-color: #fff;
            margin: 10px 0;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .feature h3 {
            margin-top: 0;
        }

        /* Setup Section */
        .setup, .how-it-works, .contributing, .license {
            margin-top: 40px;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .setup pre, .how-it-works pre {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            word-wrap: break-word;
        }

        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
            margin-top: 40px;
        }

        footer a {
            color: #3498db;
        }
    </style>
</head>

<body>
    <header>
        <div class="container">
            <h1>Smart ATS Chatbot</h1>
            <p>An AI-powered chatbot that helps evaluate and improve your resume based on a job description.</p>
        </div>
    </header>

    <div class="container">
        <!-- Features Section -->
        <section class="features">
            <div class="feature">
                <h3>Resume Evaluation</h3>
                <p>Upload your resume (PDF format), and the bot will evaluate how well it matches the job description.</p>
            </div>
            <div class="feature">
                <h3>Job Description Matching</h3>
                <p>Enter the job description, and the bot will compare it with your resume to calculate the JD match percentage.</p>
            </div>
            <div class="feature">
                <h3>Resume Recommendations</h3>
                <p>The bot provides specific recommendations to improve your resume, highlighting missing keywords and suggesting ways to optimize it for the job market.</p>
            </div>
            <div class="feature">
                <h3>ATS-like Evaluation</h3>
                <p>Simulates an ATS evaluation by analyzing your resume's content against the job description.</p>
            </div>
        </section>

        <!-- Setup Section -->
        <section class="setup">
            <h2>Setup Instructions</h2>
            <p>Follow these steps to set up the environment and run the project:</p>
            <pre>
1. Clone the Repository:
   git clone https://github.com/yourusername/repository-name.git

2. Create a Virtual Environment:
   python -m venv venv

3. Activate the Virtual Environment:
   - Windows: .\venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate

4. Install Required Dependencies:
   pip install -r requirements.txt

5. Set up Environment Variables:
   - Create a .env file in the root of the project.
   - Add your Google API key to the .env file:
     GOOGLE_API_KEY=your_google_api_key_here

6. Run the Application:
   streamlit run app.py
            </pre>
        </section>

        <!-- How It Works Section -->
        <section class="how-it-works">
            <h2>How It Works</h2>
            <p>Here's how the Smart ATS Chatbot works:</p>
            <ol>
                <li><strong>Upload Resume:</strong> Upload your resume in PDF format using the file uploader.</li>
                <li><strong>Paste Job Description:</strong> Enter the job description that you want to match your resume against.</li>
                <li><strong>Chat with the ATS Bot:</strong> You can chat with the bot using the input text box. It will ask you for further information if necessary.</li>
                <li><strong>Receive Feedback:</strong>
                    <ul>
                        <li><strong>JD Match Percentage:</strong> How well your resume aligns with the job description.</li>
                        <li><strong>Missing Keywords:</strong> A list of important keywords that are missing from your resume.</li>
                        <li><strong>Profile Summary:</strong> A brief summary of the resume's strengths and weaknesses.</li>
                        <li><strong>Recommendations:</strong> Three actionable suggestions to improve your resume and increase its chances of being shortlisted.</li>
                    </ul>
                </li>
            </ol>
        </section>

        <!-- Contributing Section -->
        <section class="contributing">
            <h2>Contributing</h2>
            <p>If you'd like to contribute to the Smart ATS Chatbot, follow these steps:</p>
            <ol>
                <li>Fork the repository.</li>
                <li>Create a new branch.</li>
                <li>Make your changes and commit them.</li>
                <li>Open a pull request with a description of your changes.</li>
            </ol>
        </section>

        <!-- License Section -->
        <section class="license">
            <h2>License</h2>
            <p>This project is licensed under the MIT License - see the <a href="LICENSE.md">LICENSE.md</a> file for details.</p>
        </section>
    </div>

    <footer>
        <p>&copy; 2024 Smart ATS Chatbot. All rights reserved. | <a href="https://github.com/yourusername/repository-name">GitHub Repository</a></p>
    </footer>
</body>

</html>










