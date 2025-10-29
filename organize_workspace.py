import os
import shutil

def organize_workspace(base_dir):
    # Define the folder structure
    folder_structure = {
        "Planning": {
            "Checklists": ["story_writing_checklist.md"],
            "Correspondence": ["correspondence.txt", "correspondence_todos.txt", "email_draft.md", "email_templates.md"],
            "Interviews": ["interview_timeline.md"],
            "Misc": ["local_critics.md"],
            "Questions": ["questions.doc", "questions.docx", "questions.html"],
            "Reports": ["engagement_recommendation.md", "ola_action_plan.md", "ola_section_outline.md", "risk_assessment.md", "stakeholder_questions.md", "stories_relevance_report.md"]
        },
        "Research": {
            "Air quality and management in petroleum refining industry A review.pdf": "airquality.txt",
            "Aromatisation of n-pentane.pdf": "Aromatisation.txt",
            "Climate risks, balance-of-payments constraints and central banking in emerging economies.pdf": "Climaterisks.txt",
            "Details of column.pdf": "Details of column.txt",
            "Flood risk.pdf": "Flood risk.txt",
            "Future prospects towards attaining zero-emission of greenhouse gases from.pdf": "Future prospects towards attaining zero-emission of greenhouse gases from.txt",
            "Hydrogen use.pdf": "Hydrogen use.txt",
            "Nickel-tolerant zeolite boron catalysts.pdf": "Nickel-tolerant zeolite boron catalysts.txt",
            "Nigeria_s climate responsiveness Navigating energy-climate and techno-financial conundrums in the low-carbon energy transition.pdf": "Nigeria_s climate responsiveness Navigating energy-climate and techno-financial conundrums in the low-carbon energy transition.txt",
            "Unlocking renewable energy materials in Nigeria availability, application, and roadmap for sustainability.pdf": None
        }
    }

    # Organize files into folders
    for folder, contents in folder_structure.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

        if isinstance(contents, dict):
            for subfolder, files in contents.items():
                subfolder_path = os.path.join(folder_path, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
                for file in files:
                    src = os.path.join(base_dir, file)
                    dest = os.path.join(subfolder_path, file)
                    if os.path.exists(src):
                        shutil.move(src, dest)
        else:
            for file in contents:
                src = os.path.join(base_dir, file)
                dest = os.path.join(folder_path, file)
                if os.path.exists(src):
                    shutil.move(src, dest)

if __name__ == "__main__":
    base_directory = "c:\\Users\\user\\j-works\\DanRef"
    organize_workspace(base_directory)