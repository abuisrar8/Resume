import json

def parse_resume(resume_text):
    resume_lines = resume_text.split('\n')
    
    resume_data = {
        "Name": None,
        "Contact Information": {
            "Phone": None,
            "Email": None,
            "LinkedIn": None,
            "GitHub": None
        },
        "Education": [],
        "Work Experience": [],
        "Projects": [],
        "Skills": [],
        "Certifications": []
    }
    
    section = None
    for line in resume_lines:
        line = line.strip()
        
        if line.startswith("Name:"):
            resume_data["Name"] = line.replace("Name:", "").strip()
        
        elif line.startswith("Phone:"):
            resume_data["Contact Information"]["Phone"] = line.replace("Phone:", "").strip()
        
        elif line.startswith("Email:"):
            resume_data["Contact Information"]["Email"] = line.replace("Email:", "").strip()
        
        elif line.startswith("LinkedIn:"):
            resume_data["Contact Information"]["LinkedIn"] = line.replace("LinkedIn:", "").strip()
        
        elif line.startswith("GitHub:"):
            resume_data["Contact Information"]["GitHub"] = line.replace("GitHub:", "").strip()
        
        elif line.startswith("Education:"):
            section = "Education"
            continue
        
        elif line.startswith("Work Experience:"):
            section = "Work Experience"
            continue
        
        elif line.startswith("Projects:"):
            section = "Projects"
            continue
        
        elif line.startswith("Skills:"):
            section = "Skills"
            continue
        
        elif line.startswith("Certifications:"):
            section = "Certifications"
            continue
        
        elif section:
            if section in ["Education", "Work Experience", "Projects", "Certifications"]:
                if line:
                    resume_data[section].append(line)
    
    return json.dumps(resume_data, indent=4)

resume_text = """
Name: Abu Israr
Phone: 8628984385
Email: abu.israr.khan.9@gmail.com
LinkedIn: linkedin.com/in/Abu-Israr/
GitHub: github.com/abuisrar8

Education:
1. M-Tech in Data Science and Analytics from Lovely Professional University, Punjab (2023-), CGPA: 8.1.
2. B-Tech in Computer Science and Engineering from Lovely Professional University, Punjab (2018-2022), CGPA: 7.21.

Work Experience:
- Data Science Intern at Oasis InfoByte (Jun 2024 - Aug 2024). Worked on machine learning projects like iris flower classification, spam email detection, and sales/car price prediction. Skills gained include predictive analytics, data application, feature engineering, Python, and remote collaboration.

Projects:
1. Daily Routine Predictor (Mar 2024) - Machine learning model to predict current workload based on historical data. Technologies: Python, Machine Learning Libraries.
2. Accent Access (May 2022) - Educational platform for learning English accents using text-to-speech and JSON. Technologies: Text-to-Speech API, JSON, Web Development Frameworks.

Skills:
Languages: C++, Python, Java, R, Rust.
Technologies/Frameworks: Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn, Apache Spark, Hadoop.
Tools/Platforms: Power BI, Excel, SQL, Jupyter Notebooks, Git, VS Code, RStudio, AWS.
Skills: Data Structures and Algorithms, Analytical Thinking, Problem-Solving, Time Management, Critical Thinking, Creativity.

Certifications:
1. Getting and Cleaning Data (May 2024) - Coursera.
2. Introduction to Big Data (May 2024) - Coursera.
3. Machine Learning With Big Data (May 2024) - Coursera.
4. DSA-Self Paced with Doubt Assistance (Aug 2022) - GeeksforGeeks.
"""

parsed_resume = parse_resume(resume_text)
print(parsed_resume)
