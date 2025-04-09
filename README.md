# Rule-Based-Expert-System-for-Student-Course-Advising


> A Flask-based web application providing academic course recommendations using a rule-based engine and a decision tree, enhanced with interactive course descriptions fetched via a RESTful API.

## Overview

The  Rule-Based-Expert-System-for-Student-Course-Advising is a web application designed to guide students in selecting appropriate academic courses. It leverages a combination of a declarative rule engine and a structured decision tree, both implemented in Python, to generate personalized recommendations based on student-provided information. 

## Key Features

* **Rule-Based Recommendations:** Employs a predefined set of rules to suggest courses based on student attributes like completed courses, learning style, and preferences.
* **Decision Tree Recommendations:** Implements a hierarchical decision tree to navigate through student attributes and arrive at course recommendations.
* **Interactive Course Descriptions:** Provides detailed course descriptions in Bootstrap popovers, fetched asynchronously from the `/api/course_descriptions` RESTful API endpoint.
* **Organized Output:** Recommendations from both the rule-based system and the decision tree are presented clearly on the `recommendations.html` page.


## Tech Stack

* **Backend:** Python 3.7+, Flask
* **Frontend:** HTML, Jinja2, Bootstrap 5, JavaScript
* **Data Storage (Static):** JSON (`data/courses.json`, `data/course_descriptions.json`)

## Setup Instructions (For Developers)

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd # Rule-Based-Expert-System-for-Student-Course-Advising
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate  # Windows
    ```

3.  **Install dependencies:**
    ```bash
     pip install -r requirements.txt
    ```

4.  **Ensure Data Directory:** Verify that a `data` directory exists in the project root and contains `courses.json` and `course_descriptions.json`.

5.  **Run the development server:**
    ```bash
    python app.py
    ```
    Access the application in your web browser at `http://127.0.0.1:5000/`.

## Architecture



* **Frontend (Input Pages Layer):**
    <img width="948" alt="image" src="https://github.com/user-attachments/assets/4b04742d-e102-4f71-aded-16437dae09f1" />
    <img width="712" alt="image" src="https://github.com/user-attachments/assets/2d00cea8-643f-44ec-b0f6-69c0bb86e075" />
    <img width="649" alt="image" src="https://github.com/user-attachments/assets/348bb4c5-9345-4ef1-b396-efcb509005bc" />



* **Results Page**
* This the students profile
<img width="638" alt="image" src="https://github.com/user-attachments/assets/4b528eb8-963f-45a4-81b4-f9fcfabcb7d5" />
<img width="640" alt="image" src="https://github.com/user-attachments/assets/3296df0d-63a4-4445-9b8e-2a59645ac78a" />


clicking on the course that is recommended eg  Math102 gives u a small description about the course.






## Recommendation Logic

* **Rule-Based System:** The `_rule_based_recommendations` method iterates through a predefined list of rules. Each rule specifies conditions based on student attributes (e.g., `completed`, `interests`, `gpa`) and a corresponding course recommendation.  eg

* {
                "if": {
                    "completed": ["Math101"],
                    "not_completed": ["Math102"],
                    "interests": ["math", "calculus"],
                    "min_gpa": 2.5,
                    "difficulty_preference": ["intermediate", "advanced"]
                },
                "then": "Math102",
                "feedback": ["Completed Math101", "Interested in math/calculus", "GPA meets requirement", "Prefers intermediate/advanced level"]
            },
            
* **Decision Tree:** The `_decision_tree_recommendations` method in `advisor.py` traverses a hardcoded decision tree structure. Based on the student's answers to questions defined at each node, the traversal follows specific branches until a course recommendation is reached. eg
* {
            "question": "primary_interest",
            "answers": {
                "math": {
                    "question": "preferred_difficulty",
                    "answers": {
                        "beginner": {"recommend": "Math101"},
                        "intermediate": {
                            "question": "completed_math101?",
                            "answers": {
                                "yes": {"recommend": "Math102"},
                                "no": {"recommend": "Math101"}
                            }
                        },
                        "advanced": {
                            "question": "completed_math201?",
                            "answers": {
                                "yes": {"recommend": "Math301"},
                                "no": {"suggest": "Consider Math201"}
                            }

## Both the rule and decision tree must be satisfied to get a recommendation from both logics.

## Contributing

Contributions are welcome!

If you'd like to improve this project:

1.  Fork the repository.
2.  Make your changes and submit a pull request.

