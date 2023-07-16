print("Ingesting data for CPMS, OJT Input, and Examinee tables.")
import names
import csv
import random
import datetime
import psycopg2
import json

provinces = ["Batangas", "Laguna", "Cavite", "Quezon", "Rizal"]
genders = ["M", "F"]
components = ["Hands-on Exam", "Diagnostic Exam", "User Assessment"]
venues = ["BSU Gym", "Tech4Ed Center", "Lipa Cultural Center", "Philippine Arena", "Rome Colosseum"]
time_choices=["AM", "PM"]
start_date = datetime.date(2022, 6, 1)
all_status = ["Passed", "Failed", "For checking", "For transmittal"]
categories = ["accepted at DICT Office", "endorsed by partners"]
universities = ["Batangas State University", "UP Los Banos", "University of Batangas", "De la Salle Lipa", "Polytechnic University", "Mapua Laguna"]
modes = ["Physical Reporting", "Hybrid Mode", "Online"]


conn = psycopg2.connect(**{
    'host': 'db',
    'database': 'ilcdb',
    'user': 'group1',
    'password': 'dict'
})
print("Connection to the database established")

all_ojt = []
for i in range(2000):
    gender = random.choice(genders)
    province = random.choices(provinces, weights = [0.4, 0.2, 0.1, 0.1, 0.1], k=1)[0]
    category = random.choice(categories)
    suc = random.choice(universities)
    duration = random.choice(range(100,300,5))
    school_address = "Batangas" if any(x in suc for x in ('Lipa', 'Batangas')) else "Laguna"
    name = names.get_full_name(gender = {'M': 'male', 'F':'female'}[gender])
    date = (start_date + datetime.timedelta(days=random.randint(1,365)))
    mode = random.choice(modes)
    resume = random.choice([True, False])
    endorsement = random.choice([True, False])
    moa = random.choice([True, False])

    all_ojt.append({
        "province": province,
        "category": category,
        "suc": suc,
        "duration": duration,
        "school_address": school_address,
        "representative": " ",
        "representative_contact": " ",
        "student_name": name,
        "sex": gender,
        "student_contact": " ",
        "start_date": date.strftime("%Y-%m-%d"),
        "end_date": (date + datetime.timedelta(hours = duration, days = duration // 8 + (duration // 20))).strftime("%Y-%m-%d"),
        "mode": mode,
        "resume": resume,
        "endorsement": endorsement,
        "moa": moa,
        "remarks": " "
    })
print(f"{len(all_ojt)} records generated for OJT relation")

all_examinees = []
for i in range(2000):
    gender = random.choice(genders)
    province = random.choices(provinces, weights = [0.4, 0.2, 0.1, 0.1, 0.1], k=1)[0]
    name = names.get_full_name(gender = {'M': 'male', 'F':'female'}[gender])
    date = (start_date + datetime.timedelta(days=random.randint(1,365)))
    venue = random.choice(venues)
    status = random.choices(all_status, weights = [0.7, 0.2, 0.05, 0.05], k=1)[0]
    component = random.choices(components, weights = [0.65, 0.1, 0.25], k=1)[0]
    time = random.choice(time_choices)
    if status == "Passed":
        remark = str(random.randint(75,100))
    else:
        remark = " "
    batch = f"{date.year}-{date.month:02d}"
    all_examinees.append({
        "province": province,
        "component": component,
        "name": name,
        'venue': venue,
        "gender": gender,        
        'date': date.strftime("%Y-%m-%d"),
        'time': time,
        'status': status,
        'remarks': remark,
        'batch': batch
    })
print(f"{len(all_ojt)} records generated for Examinee relation")
cpms = [
    {
        "program": "Project Click",
        "info": json.dumps({
            "Activity": [
                "Deployment of digital devices for the Project CLICK",
                "",
                "Conduct of Trainings on Digital Literacy and Cyber Hygiene"
            ],
            "Indicator": [
                "# of Trainings",
                "# of Beneficiaries",
                "# of Trainings on Digital Literacy and Cyber Hygiene"
            ],
            "Target": [
                None, None, None
            ],
            "Accomplishment": [
                None, None, None
            ],
            "Remarks": [
                "No target schedule of implementation provided by Project CLICK team",
                "",
                ""
            ]
        })
    },
    {
        'program': 'Digital Workforce / Training Management Division',
        'info': json.dumps({
            "Activity": [
                "Conduct of ToTs for SMEs on ICT Specialized Training Programs (Blended)",
                "Training on Digital Governance and Management",
                "Training on Digital Transformative Technologies (Advanced DL)",
                "Training on CyberSecurity",
                "Conduct of other Capacity Building/Digital Literacy Training/ Webinar",
            ],
            "Indicator": [
                "# of implementation donducted on ToTs for SMEs on ICT Specialized Training Programs (Blended)",
                "# of trainings conducted on Digital Governance and Management",
                "# of trainings conducted on Digital Transformative Technologies (Advanced DL)",
                "# of trainings conducted on CyberSecurity",
                "# of Other Digital Literacy Training/ Webinar conducted"
            ],
            "Target": [
                50, 100, 150, 100, None
            ],
            "Accomplishment": [
                51, 99, 65, None, None
            ],
            "Remarks": [
                "", "", "Python Programming Essentials April 12-25, 2023 Total Pax: 65 (42M 23F)", "", ""
            ]
        })
    },
    {
        "program": 'Certification Management',
        "info": json.dumps({
            "Activity": [
                "Conduct of ICT Diagnostic /Assessment Exam",
                "Competency based examinations Administered",
                "Conduct of ICT User Assessments",
                "Conduct of Digital Challenge",
                "Formulation of Curriculum Recognition Guidelines"
            ],
            "Indicator": [
                "# of ICT Diagnostic /Assessment Exam conducted",
                "#  of competency based examinations Administered",
                "# of ICT User Assessments administered",
                "# of Local Digital Challenge",
                "Formulation of Curriculum Recognition Guidelines"
            ],
            "Target": [
                75, 10, 10, None, None
            ], 
            "Accomplishment": [
                351, None, None, None, None
            ],
            "Remarks": [
                """
ICT Diagnostic Exam - Laguna
April 20, 2023
Total Pax: 44 (30M 14F)

ICT Diagnostic Exam - Laguna
April 26, 2023
Total Pax: 2M

ICT Diagnostic Exam - Batangas
April 26, 2023
Total Pax: 4M

ICT Diagnostic Exam - Rizal
April 26, 2023
Total Pax: 8M

ICT Diagnostic Exam - Quezon
April 26, 2023
Total Pax: 6 (4M 2F)
                """, "", "", "", ""
            ]
        })
    },
    {
        "program": "EPMD",
        "info": json.dumps({
            "Activity": [
                "Competency Needs Assessment (CNA)",
                "Training Needs Analysis (TNA)",
                "Evaluation of Training Guidelines",
                "Stakeholder Engagement",
                "",
                "Implementation of the DICT Apprenticeship Program",
                "Evaluation Program"
            ],
            "Indicator": [
                "Conduct survey for 3 sectors",
                "Conduct survey for 3 sectors",
                "Conduct of Evaluation of training programs",
                "Conduct of Partner Summit",
                "# of Partners made",
                "# of students accepted to be part of the program",
                "# of evaluation report submitted"
            ],
            "Target": [
                None, None, None, 1, 2, 10, 2
            ],
            "Accomplishment": [
                None, None, None, None, 10, 22, None
            ],
            "Remarks": ["", "", "", "", "", "", ""]
        })
    }
]
print("CPMS Data Prepared")

# Examinees Data
with open("examinees.csv", "w", newline="", encoding = "utf-8") as f:
    writer = csv.DictWriter(f, all_examinees[0].keys())
    writer.writeheader()
    writer.writerows(all_examinees)

with conn.cursor() as cursor:
    with open('examinees.csv') as f:
        cursor.copy_expert('COPY myapp_examinees(province, component, name, venue, gender, date, time, status, remarks, batch) FROM STDIN WITH HEADER CSV', f)
        conn.commit()
print(f"All {len(all_examinees)} records inserted to ilcdb.myapp_examinees")

# OJT Data
with open("ojt.csv", "w", newline="", encoding = "utf-8") as f:
    writer = csv.DictWriter(f, all_ojt[0].keys())
    writer.writeheader()
    writer.writerows(all_ojt)

with conn.cursor() as cursor:
    with open('ojt.csv') as f:
        cursor.copy_expert('COPY myapp_ojtinput(province, category, suc, duration, school_address, representative, representative_contact, student_name, sex, student_contact, start_date, end_date, mode, resume, endorsement, moa, remarks) FROM STDIN WITH HEADER CSV', f)
        conn.commit()
print(f"All {len(all_ojt)} records inserted to ilcdb.myapp_ojtinput")

# CPMS Data
with open("cpms.csv", "w", newline="", encoding = "utf-8") as f:
    writer = csv.DictWriter(f, cpms[0].keys())
    writer.writeheader()
    writer.writerows(cpms)
    
with conn.cursor() as cursor:
    with open('cpms.csv') as f:
        cursor.copy_expert('COPY myapp_cpms(program, info) FROM STDIN WITH HEADER CSV', f)
        conn.commit()
print("CPMS data also ingested")
print("Setup finished. Closing the app now")