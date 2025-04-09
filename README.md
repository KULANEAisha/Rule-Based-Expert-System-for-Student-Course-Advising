# Rule-Based-Expert-System-for-Student-Course-Advising


> A Flask-based web application providing academic course recommendations using a rule-based engine and a decision tree, enhanced with interactive course descriptions fetched via a RESTful API.

## Overview

The Academic Course Advisor is a web application designed to guide students in selecting appropriate academic courses. It leverages a combination of a declarative rule engine and a structured decision tree, both implemented in Python, to generate personalized recommendations based on student-provided information. The user interface, built with HTML and styled using Bootstrap, features interactive course descriptions fetched dynamically from a backend API endpoint.

## Key Features

* **Rule-Based Recommendations:** Employs a predefined set of rules (defined in `advisor.py`) to suggest courses based on student attributes like completed courses, interests, GPA, learning style, and preferences.
* **Decision Tree Recommendations:** Implements a hierarchical decision tree (also within `advisor.py`) to navigate through student attributes and arrive at course recommendations.
* **Interactive Course Descriptions:** Provides detailed course descriptions in Bootstrap popovers, fetched asynchronously from the `/api/course_descriptions` RESTful API endpoint.
* **Clear Input Form:** A user-friendly HTML form (`index.html`) allows students to input their relevant academic information.
* **Organized Output:** Recommendations from both the rule-based system and the decision tree are presented clearly on the `recommendations.html` page.


## Tech Stack

* **Backend:** Python 3.7+, Flask
* **Frontend:** HTML, Jinja2, Bootstrap 5, JavaScript
* **Data Storage (Static):** JSON (`data/courses.json`, `data/course_descriptions.json`)

## Setup Instructions (For Developers)

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd academic_course_advisor_rule_based
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate  # Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install Flask
    ```

4.  **Ensure Data Directory:** Verify that a `data` directory exists in the project root and contains `courses.json` and `course_descriptions.json`.

5.  **Run the development server:**
    ```bash
    python app.py
    ```
    Access the application in your web browser at `http://127.0.0.1:5000/`.

## Architecture

The application follows a standard web application architecture:

* **Frontend (Presentation Layer):**
    <img width="948" alt="image" src="https://github.com/user-attachments/assets/4b04742d-e102-4f71-aded-16437dae09f1" />
    <img width="712" alt="image" src="https://github.com/user-attachments/assets/2d00cea8-643f-44ec-b0f6-69c0bb86e075" />
    <img width="649" alt="image" src="https://github.com/user-attachments/assets/348bb4c5-9345-4ef1-b396-efcb509005bc" />



* **Backend (Application and Data Layers):**
    * `app.py`: The main Flask application file. It defines the routes for the homepage (`/`) to handle student input and display recommendations, and the API endpoint (`/api/course_descriptions`) to serve course descriptions. It instantiates the `CourseAdvisor` class.
    * `advisor.py`: Contains the `CourseAdvisor` class, which encapsulates the core recommendation logic:
        * Loading course data and rules from JSON files.
        * Implementing the rule-based recommendation engine (`_rule_based_recommendations`).
        * Implementing the decision tree traversal logic (`_decision_tree_recommendations`).
        * Providing the `get_recommendations` method to orchestrate both recommendation strategies.
    * `data/courses.json`: Stores basic information about the available courses (e.g., course code, name, difficulty).
    * `data/course_descriptions.json`: Stores detailed descriptions for each course, used by the API endpoint.

## API Endpoint

* **/api/course\_descriptions**:
    * **Method:** `GET`
    * **Response:** A JSON object where keys are course codes and values are their corresponding descriptions. This data is read from `data/course_descriptions.json`.

## Recommendation Logic

* **Rule-Based System:** The `_rule_based_recommendations` method in `advisor.py` iterates through a predefined list of rules. Each rule specifies conditions based on student attributes (e.g., `completed`, `interests`, `gpa`) and a corresponding course recommendation. If a student's attributes satisfy the conditions of a rule, the associated course is recommended.
* **Decision Tree:** The `_decision_tree_recommendations` method in `advisor.py` traverses a hardcoded decision tree structure. Based on the student's answers to questions defined at each node (derived from their attributes), the traversal follows specific branches until a course recommendation is reached.

## Frontend Details

* **Jinja2 Templating:** Used in `recommendations.html` to dynamically display the student's input, the lists of rule-based and decision tree recommendations, and course names.
* **Bootstrap:** Provides the styling and layout for a responsive and visually appealing user interface.
* **JavaScript:** The script block in `recommendations.html` fetches course descriptions from the `/api/course_descriptions` endpoint using the Fetch API when a course code (with the class `course-code-hover` and `data-course-code` attribute) is clicked. It then initializes a Bootstrap popover to display the fetched description.

## Data Structures

* **`data/courses.json`:**
    ```json
    {
      "Math101": {"name": "Calculus I", "difficulty": "beginner"},
      "CS101": {"name": "Introduction to Programming", "difficulty": "beginner"},
      // ... more courses
    }
    ```

* **`data/course_descriptions.json`:**
    ```json
    {
      "Math101": "A foundational course in differential and integral calculus...",
      "CS101": "Covers the basic principles of programming...",
      // ... more detailed descriptions
    }
    ```

* **Rules (in `advisor.py`):** A list of dictionaries, each containing `"if"` (conditions as a dictionary), `"then"` (the recommended course code), and optional `"feedback"` (list of strings explaining the recommendation).

* **Decision Tree (in `advisor.py`):** A nested dictionary where keys represent questions or "recommend" actions, and values are further nested dictionaries representing answers or subsequent questions/recommendations.

## Future Enhancements

* Implement user authentication and session management.
* Persist student data and recommendation history in a database.
* Develop an administrative interface for managing courses, rules, and the decision tree.
* Integrate more sophisticated recommendation algorithms.
* Add unit and integration tests to ensure code quality.
* Improve the user interface and user experience.

