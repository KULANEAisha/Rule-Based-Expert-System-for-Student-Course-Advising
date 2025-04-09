# Rule-Based-Expert-System-for-Student-Course-Advising



> A simple web application that provides personalized academic course recommendations based on a student's profile.

## What is This?

The Academic Course Advisor is designed to help students explore and identify courses that might be suitable for them. It uses a combination of predefined rules and a decision-making process to suggest courses based on information about the student's interests and academic background. Think of it as a basic digital academic advisor.

## How It Works (For a New User)

Imagine you're a student looking for course suggestions. This application takes some information (like your interests and any courses you've already taken) and then uses two main methods to recommend courses:

1.  **Rules:** It has a set of simple "if this, then that" rules. For example, "If you like math and haven't taken any advanced courses, we might suggest an introductory math course."
2.  **Decision Tree:** It also uses a series of questions to guide you towards recommendations. It's like a flowchart where your answers lead to different course suggestions.

To make the experience better, when you see a course code (like "Math101"), you can click on it to see a short description of what the course is about.

## Getting Started (Run It Yourself!)

Follow these instructions to get the application running on your computer. You don't need to be a coding expert!

### Prerequisites

Before you start, make sure you have these things installed on your computer:

1.  **Python:** If you don't have Python, go to [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest version for your operating system (Windows, macOS, Linux). Follow the installation instructions on the website.
2.  **pip:** This is a tool that comes with Python and helps install other software. You probably already have it if you installed Python correctly.

### Installation

1.  **Download the Project Files:**
    * If you have a GitHub account, the easiest way is to "clone" the project. If you see a green "Code" button on the project page, click it and choose how you want to download (e.g., "HTTPS" and then copy the link). Open your computer's terminal or command prompt, navigate to a folder where you want to save the project, and type:
      ```bash
      git clone <the_link_you_copied>
      cd <the_name_of_the_project_folder>
      ```
    * If you don't have Git, you can usually download the project files as a "ZIP" file from the platform where it's hosted. Download the ZIP, extract the files to a folder on your computer, and then open your terminal or command prompt and navigate into that extracted folder using the `cd` command (e.g., `cd AcademicCourseAdvisor-main`).

2.  **Install Necessary Software (Flask):**
    * Open your terminal or command prompt (make sure you are still inside the project folder you downloaded).
    * Type the following command and press Enter:
      ```bash
      pip install Flask
      ```
      This will download and install Flask, which is what helps the application run in your web browser.

### Running the Application

1.  **Open Your Terminal or Command Prompt:** Make sure it's open in the project folder where the `advisor.py` file is located.

2.  **Run the Application Command:** Type the following command and press Enter:
    ```bash
    python advisor.py
    ```
    You should see some messages appear in the terminal, usually indicating that the Flask development server has started. It will likely give you an address like `http://127.0.0.1:5000/`.

3.  **Open in Your Web Browser:** Open your favorite web browser (like Chrome, Firefox, Safari, Edge) and type the address you saw in the terminal (`http://127.0.0.1:5000/`) into the address bar. Press Enter.

4.  **Using the Application:** You should now see the Academic Course Advisor application in your web browser. Follow the instructions on the page (if any input is required) to get course recommendations. You should be able to see the recommendations and click on the course codes to view their descriptions.

## Screenshots

**(Include this section with clear screenshots of the key parts of the application as described in the previous README example.)**

## Understanding the Code and Data (Optional, but helpful for curious users)

If you're curious about how the application works behind the scenes, here's a quick overview:

* **`advisor.py`:** This file contains the main logic of the application. It has the rules for recommendations and the code that builds the decision tree. When you run `python advisor.py`, it starts the web server and handles the recommendations.
* **`courses.json`:** This file is like a small database that stores information about all the available courses, such as their names and descriptions.
* **`course_descriptions.json`:** This file contains more detailed descriptions that appear when you click on a course code in the application.
* **`recommendations.html`:** This file is the webpage you see in your browser that displays the course recommendations. It uses some special tags (from a template engine) to show the information generated by `advisor.py`.
* **`base.html`:** This is a basic structure for all the webpages in the application.
* **`static/`:** This folder might contain other files like CSS (for styling the look of the website).

## Contributing (If you want others to help)

If you're open to others contributing to your project, explain how they can do so (as in the previous README example).

## License

(As in the previous README example)

## Acknowledgments

(As in the previous README example)

---

**Key Improvements for Understandability and Running:**

* **Simplified Language:** Avoids overly technical terms in the initial sections.
* **Step-by-Step Running Instructions:** Provides very clear, actionable steps for installation and running, even for beginners.
* **Emphasis on Prerequisites:** Clearly lists what needs to be installed beforehand.
* **Explanation of Files:** Briefly describes the purpose of the key files in the project.
* **Clear "How It Works" for a New User:** Focuses on the user's perspective of interacting with the application.

Remember to replace the placeholder paths for your screenshots and customize the "Contributing" and "Acknowledgments" sections as needed. This README should make it much easier for someone to understand your project and run it on their own.
