import json
from typing import Dict, List

class CourseAdvisor:
    def __init__(self):
        self.courses = self.load_courses()
        self.rules = self.load_rules()
        self.decision_tree = self.build_decision_tree()

    def load_courses(self) -> Dict[str, Dict]:
        try:
            with open('data/courses.json') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: 'data/courses.json' not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Could not decode 'data/courses.json'. Check for syntax errors.")
            return {}

    def load_rules(self) -> List[Dict]:
        return [
            {
                "if": {
                    "completed": [],
                    "not_completed": ["Math101"],
                    "interests": ["math", "calculus"],
                    "difficulty_preference": ["beginner"]
                },
                "then": "Math101",
                "feedback": ["No prior math courses", "Interested in math/calculus", "Prefers beginner level"]
            },
            {
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
            {
                "if": {
                    "completed": [],
                    "not_completed": ["CS101"],
                    "interests": ["programming", "computer science"],
                    "difficulty_preference": ["beginner"],
                    "learning_style": ["applied", "visual"]
                },
                "then": "CS101",
                "feedback": ["No prior CS courses", "Interested in programming/CS", "Prefers beginner level", "Learning style aligns"]
            },
            {
                "if": {
                    "completed": ["CS101"],
                    "not_completed": ["CS201"],
                    "interests": ["programming", "algorithms"],
                    "min_gpa": 2.7,
                    "difficulty_preference": ["intermediate"]
                },
                "then": "CS201",
                "feedback": ["Completed CS101", "Interested in programming/algorithms", "GPA meets requirement", "Prefers intermediate level"]
            },
            {
                "if": {
                    "completed": [],
                    "not_completed": ["Phys101"],
                    "interests": ["science", "physics"],
                    "difficulty_preference": ["beginner"],
                    "learning_style": ["theoretical", "visual"]
                },
                "then": "Phys101",
                "feedback": ["No prior physics courses", "Interested in science/physics", "Prefers beginner level", "Learning style aligns"]
            },
            {
                "if": {
                    "completed": ["Phys101"],
                    "not_completed": ["Phys102"],
                    "interests": ["science", "physics"],
                    "min_gpa": 3.0,
                    "difficulty_preference": ["intermediate", "advanced"]
                },
                "then": "Phys102",
                "feedback": ["Completed Phys101", "Interested in science/physics", "GPA meets requirement", "Prefers intermediate/advanced level"]
            },
            {
                "if": {
                    "completed": [],
                    "not_completed": ["Eng101"],
                    "interests": ["writing", "literature"],
                    "difficulty_preference": ["beginner", "intermediate"],
                    "min_gpa": 2.0,
                    "learning_style": ["auditory", "visual"]
                },
                "then": "Eng101",
                "feedback": ["No prior English courses", "Interested in writing/literature", "Prefers beginner/intermediate level", "GPA meets requirement", "Learning style aligns"]
            },
            {
                "if": {
                    "completed": ["Eng101"],
                    "not_completed": ["Eng201"],
                    "interests": ["writing", "analysis"],
                    "difficulty_preference": ["intermediate", "advanced"],
                    "min_gpa": 2.5,
                    "learning_style": ["auditory", "visual", "theoretical"]
                },
                "then": "Eng201",
                "feedback": ["Completed Eng101", "Interested in writing/analysis", "Prefers intermediate/advanced level", "GPA meets requirement", "Learning style aligns"]
            },
            {
                "if": {
                    "completed": ["Math102", "CS101"],
                    "not_completed": ["DS301"],
                    "interests": ["data science"],
                    "min_gpa": 3.2,
                    "difficulty_preference": ["advanced"],
                    "career_goals": ["data scientist", "machine learning engineer"]
                },
                "then": "DS301",
                "feedback": ["Completed Math102 & CS101", "Interested in data science", "GPA meets requirement", "Prefers advanced level", "Career goals align"]
            },
            {
                "if": {
                    "completed": [],
                    "not_completed": ["GameDev201"],
                    "interests": ["programming", "game development"],
                    "learning_style": ["applied", "kinesthetic"],
                    "time_commitment": ["more_than_15"],
                    "group_projects": ["yes"],
                    "difficulty_preference": ["intermediate", "advanced"]
                },
                "then": "GameDev201",
                "feedback": ["Interested in programming/game development", "Learning style aligns", "High time commitment", "Prefers group projects", "Prefers intermediate/advanced level"]
            },
            {
                "if": {
                    "completed": [],
                    "not_completed": ["IntroToGameDev"],
                    "interests": ["game development", "interactive media"],
                    "difficulty_preference": ["beginner", "intermediate"],
                    "learning_style": ["applied", "visual"]
                },
                "then": "IntroToGameDev",
                "feedback": ["Interested in game development/interactive media", "Prefers beginner/intermediate level", "Learning style aligns"]
            },
            {
                "if": {
                    "completed": [],
                    "not_completed": ["GeneralStudies101"],
                    "difficulty_preference": ["beginner"],
                    "time_commitment": ["less_than_5"],
                    "min_gpa": 1.5
                },
                "then": "GeneralStudies101",
                "feedback": ["Prefers beginner level", "Low time commitment", "GPA meets requirement"]
            },
            {
                "if": {
                    "completed": [],
                    "not_completed": ["Bio101"],
                    "interests": ["biology", "life sciences"],
                    "difficulty_preference": ["beginner", "intermediate"],
                    "learning_style": ["visual", "auditory", "kinesthetic"],
                    "group_projects": ["yes"]
                },
                "then": "Bio101",
                "feedback": ["Interested in biology/life sciences", "Prefers beginner/intermediate level", "Learning style aligns", "Prefers group projects"]
            },
            {
                "if": {
                    "completed": [],
                    "not_completed": ["Chem101"],
                    "interests": ["chemistry", "science"],
                    "difficulty_preference": ["beginner", "intermediate"],
                    "learning_style": ["theoretical", "applied", "visual"],
                    "group_projects": ["yes"]
                },
                "then": "Chem101",
                "feedback": ["Interested in chemistry/science", "Prefers beginner/intermediate level", "Learning style aligns", "Prefers group projects"]
            },
            {
                "if": {
                    "completed": ["Math102"],
                    "not_completed": ["Math301"],
                    "interests": ["math", "analysis", "advanced calculus"],
                    "difficulty_preference": ["advanced"],
                    "min_gpa": 3.5,
                    "learning_style": ["theoretical"]
                },
                "then": "Math301",
                "feedback": ["Completed Math102", "Interested in advanced math", "Prefers advanced level", "GPA meets requirement", "Learning style aligns"]
            },
            {
                "if": {
                    "completed": ["Eng201"],
                    "not_completed": ["Eng301"],
                    "interests": ["writing", "creative writing", "storytelling"],
                    "difficulty_preference": ["advanced"],
                    "learning_style": ["auditory", "kinesthetic"],
                    "group_projects": ["yes"]
                },
                "then": "Eng301",
                "feedback": ["Completed Eng201", "Interested in creative writing", "Prefers advanced level", "Learning style aligns", "Prefers group projects"]
            }
        ]

    def build_decision_tree(self) -> Dict:
        return {
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
                        }
                    }
                },
                "programming": {
                    "question": "preferred_learning_style",
                    "answers": {
                        "applied": {"recommend": "CS101"},
                        "theoretical": {"recommend": "CS101"}, # Could branch further
                        "visual": {"recommend": "CS101"} # Could branch further
                    }
                },
                "science": {
                    "question": "specific_science_interest",
                    "answers": {
                        "physics": {"recommend": "Phys101"},
                        "biology": {"recommend": "Bio101"},
                        "chemistry": {"recommend": "Chem101"} # Assuming Chem101 exists
                    }
                },
                "writing": {
                    "question": "preferred_difficulty",
                    "answers": {
                        "beginner": {"recommend": "Eng101"},
                        "intermediate": {
                            "question": "completed_eng101?",
                            "answers": {
                                "yes": {"recommend": "Eng201"},
                                "no": {"recommend": "Eng101"}
                            }
                        },
                        "advanced": {"recommend": "Eng301"} # Assuming Eng301 exists
                    }
                },
                "data science": {
                    "question": "completed_math_and_cs?",
                    "answers": {
                        "yes": {
                            "question": "gpa_ok_data_science?",
                            "answers": {
                                "yes": {"recommend": "DS301"},
                                "no": {"suggest": "Focus on foundational math/CS"}
                            }
                        },
                        "no": {"suggest": "Complete introductory Math and CS"}
                    }
                },
                "game development": {
                    "question": "time_commitment_high?",
                    "answers": {
                        "yes": {
                            "question": "prefers_group_projects?",
                            "answers": {
                                "yes": {"recommend": "GameDev201"},
                                "no": {"recommend": "IntroToGameDev"} # Assuming IntroToGameDev exists
                            }
                        },
                        "no": {"suggest": "Consider introductory game dev courses"}
                    }
                },
                "unknown": {"recommend": "GeneralStudies101"} # Default recommendation
            }
        }

    def check_prerequisites(self, course: str, completed: List[str]) -> bool:
        return all(p in completed for p in self.courses.get(course, {}).get("prerequisites", []))

    def get_recommendations(self, student: Dict) -> Dict:
        return {
            "rule_based": self._rule_based_recommendations(student),
            "decision_tree": self._decision_tree_recommendations(student)
        }

    def _rule_based_recommendations(self, student: Dict) -> List[Dict]:
        recommendations = []
        for rule in self.rules:
            if self._meets_conditions(rule["if"], student):
                course = rule["then"]
                if course in self.courses and self.check_prerequisites(course, student.get("completed", [])) and course not in student.get("completed", []):
                    recommendations.append({"course": course, "feedback": rule.get("feedback", [])})
        return recommendations

    def _meets_conditions(self, conditions: Dict, student: Dict) -> bool:
        completed_check = all(c in student.get("completed", []) for c in conditions.get("completed", []))
        not_completed_check = all(nc not in student.get("completed", []) for nc in conditions.get("not_completed", [])) if conditions.get("not_completed") else True
        interests_check = any(i in student.get("interests", []) for i in conditions.get("interests", [])) if conditions.get("interests") else True
        gpa_check = student.get("gpa", 0) >= conditions.get("min_gpa", 0) if conditions.get("min_gpa") is not None else True
        learning_style_check = student.get("learning_style") in conditions.get("learning_style", [student.get("learning_style")]) if conditions.get("learning_style") else True
        difficulty_preference_check = student.get("difficulty_preference") in conditions.get("difficulty_preference", [student.get("difficulty_preference")]) if conditions.get("difficulty_preference") else True
        time_commitment_check = student.get("time_commitment") in conditions.get("time_commitment", [student.get("time_commitment")]) if conditions.get("time_commitment") else True
        career_goals_check = any(goal.lower() in student.get("career_goals", "").lower() for goal in conditions.get("career_goals", [])) if conditions.get("career_goals") else True
        group_projects_check = student.get("group_projects") in conditions.get("group_projects", [student.get("group_projects")]) if conditions.get("group_projects") else True

        return (
            completed_check and
            not_completed_check and
            interests_check and
            gpa_check and
            learning_style_check and
            difficulty_preference_check and
            time_commitment_check and
            career_goals_check and
            group_projects_check
        )

    def _decision_tree_recommendations(self, student: Dict) -> List[str]:
        recommendations = []
        current_node = self.decision_tree

        while True:
            if "recommend" in current_node:
                course = current_node["recommend"]
                if course in self.courses and self.check_prerequisites(course, student.get("completed", [])) and course not in student.get("completed", []):
                    recommendations.append(course)
                break

            question = current_node.get("question")
            if not question:
                break

            answer = self._answer_question(question, student)
            current_node = current_node.get("answers", {}).get(answer, {})
            if not current_node:
                break

        return recommendations

    def _answer_question(self, question: str, student: Dict) -> str:
        q_map = {
            "primary_interest": lambda: next(
                (i for i in student.get("interests", [])
                 if i in ["math", "programming", "science", "writing", "data science", "game development"]), "unknown"),
            "preferred_learning_style": lambda: student.get("learning_style", ""),
            "preferred_difficulty": lambda: student.get("difficulty_preference", ""),
            "completed_math101?": lambda: "yes" if "Math101" in student.get("completed", []) else "no",
            "completed_math201?": lambda: "yes" if "Math201" in student.get("completed", []) else "no",
            "gpa_ok_math?": lambda: "yes" if student.get("gpa", 0) >= 2.5 else "no",
            "completed_cs101?": lambda: "yes" if "CS101" in student.get("completed", []) else "no",
            "specific_science_interest": lambda: next(
                (i for i in student.get("interests", []) if i in ["physics", "biology", "chemistry"]), "unknown"),
            "completed_eng101?": lambda: "yes" if "Eng101" in student.get("completed", []) else "no",
            "gpa_ok_data_science?": lambda: "yes" if student.get("gpa", 0) >= 3.2 else "no",
            "completed_math_and_cs?": lambda: "yes" if "Math102" in student.get("completed", []) and "CS101" in student.get("completed", []) else "no",
            "time_commitment_high?": lambda: "yes" if student.get("time_commitment") == "more_than_15" else "no",
            "prefers_group_projects?": lambda: student.get("group_projects", "any").lower()
        }
        return q_map.get(question, lambda: "")()

if __name__ == '__main__':
    advisor = CourseAdvisor()
    student_data = {
        "completed": ["Math101", "CS101"],
        "interests": ["programming", "math", "data science"],
        "gpa": 3.5,
        "learning_style": "applied",
        "difficulty_preference": "intermediate",
        "time_commitment": "5_to_10",
        "career_goals": "Data Scientist",
        "group_projects": "yes"
    }
    recommendations = advisor.get_recommendations(student_data)
    print("Recommendations:", recommendations)