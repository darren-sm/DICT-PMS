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
tmd_categories = ['ToT', 'Digital Governance and Management', 'Digital Transformative Technologies', 'Cyber Security']
epmd_categories = ['NGA', 'LGU', 'Industry', 'SUC', 'Training Institution']

conn = psycopg2.connect(**{
    'host': 'db',
    'database': 'ilcdb',
    'user': 'group1',
    'password': 'dict'
})
print("Connection to the database established")

all_ojt = []
for i in range(500):
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
for i in range(500):
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
print(f"{len(all_examinees)} records generated for Examinee relation")

all_epmd = []
industry_names = ["2GO", "2GO (cargo airline)", "2GO Group", "Aboitiz Equity Ventures", "ABS-CBN Corporation", "ABS-CBN Convergence", "ABS-CBN Publishing", "Advanced Contact Solutions", "Adventist Medical Center Manila", "AirAsia Zest", "Al-Amanah Islamic Bank", "Alaska Milk Corporation", "Aliw Broadcasting Corporation", "All Youth Channels", "Allied Bank", "Armscor", "Asia Brewery", "Asia United Bank", "Asian Hospital and Medical Center", "Asian Television Content Corporation", "Asian Vision", "Ayala Corporation", "Ayala Land", "Banco de Oro", "Bank of Commerce", "Bank of the Philippine Islands", "Bayan Telecommunications", "Bombo Radyo Philippines", "Brigada Mass Media Corporation", "Broadcast Enterprises and Affiliated Media", "Cebgo", "Cebu Pacific", "Cebu Landmasters", "Cebuana Lhuillier", "Century Properties", "Cherry Mobile", "Chinabank", "Chooks-to-Go", "Chowking", "Christian Era Broadcasting Service International", "CIBI Information, Inc", "Cignal TV", "Citystate Savings Bank", "Converge ICT Solutions", "Cotabato Light and Power Company", "Creative Programs", "Davao Doctors Hospital", "Davao Light and Power Company", "De La Salle Medical and Health Sciences Institute", "Del Monte Motors", "Delta Motors Corporation", "Destiny Cable", "Development Bank of the Philippines", "Digify Inc.", "Digital5", "Digital Telecommunications Philippines", "Dito Telecommunity", "DMCI Homes", "Dream Satellite TV", "DWAO-TV", "DZCE-TV", "Eagle Broadcasting Corporation", "Eastern Telecommunications Philippines", "EastWest Bank", "Energy Development Corporation", "Enfant Philippines", "ePLDT Ventus", "Ever Gotesco Malls", "Fil-Asian Airways", "Filinvest", "First Philippine Holdings Corporation", "G Sat", "Gerry\'s Grill", "Globe Telecom", "GMA Music", "GMA Network Films", "GMA New Media", "GMA Network", "GMA Worldwide", "Go Nuts Donuts", "Integrated Micro-Electronics, Inc.", "Intercontinental Broadcasting Corporation", "Interisland Airlines", "Isetann Department Store", "JG Summit Holdings", "Jollibee", "Land Bank of the Philippines", "LBC Express", "Lopez Holdings Corporation", "Lung Center of the Philippines", "Macay Holdings", "Makati Medical Center", "Malaya", "Mang Inasal", "Manila Broadcasting Company", "Manila Bulletin", "Manila Hotel", "Manila North Tollways Corporation", "Manila Standard", "Manila Times", "Manila Water", "Max\'s of Manila", "Maynilad Water Services", "MediaQuest Holdings", "Megaworld Corporation", "Megaworld Lifestyle Malls", "Meralco", "Mercury Drug", "Metro Retail Stores Group", "Metropolitan Bank and Trust Company", "Metropolitan Medical Center", "Mighty Corporation", "Monde Nissin", "MyPhone", "Nation Broadcasting Corporation", "National Book Store", "National Grid Corporation of the Philippines", "National Kidney and Transplant Institute", "National Power Corporation", "National Transmission Corporation", "Negros Navigation", "Net 25", "Nicanor Reyes Medical Foundation", "Nine Media Corporation", "Now Corporation", "One Network Bank", "Ospital ng Maynila Medical Center", "Our Lady of Lourdes Hospital", "Ovation Productions", "O Shopping", "Pacific Pearl Airways", "PAL Express", "People\'s Television Network", "Petron Corporation", "Philippine Airlines (PAL)", "Philippine Amusement and Gaming Corporation", "Philippine Bank of Communications", "Philippine Broadcasting Service", "Philippine Business Bank", "Philippine Collective Media Corporation", "Philippine Daily Inquirer", "Philippine General Hospital", "Philippine Heart Center", "Philippine National Bank", "Philippine National Construction Corporation", "Philippine National Oil Company", "Philippine Postal Corporation", "Philippines AirAsia", "Philippine Savings Bank", "Philippine Telegraph and Telephone Corporation", "Philippine Veterans Bank", "Philtrust Bank", "Phoenix Petroleum", "Planters Development Bank", "Play Innovations", "PLDT", "PMFTC", "Progressive Broadcasting Corporation", "Property Company of Friends", "Quest Broadcasting", "Radio Corporation of the Philippines", "Radio Mindanao Network", "Radio Philippines Network", "Rajah Broadcasting Network", "Rappler", "Red Mobile", "Red Ribbon", "Regal Entertainment", "Republic Biscuit Corporation", "RFM Corporation", "Rizal Commercial Banking Corporation", "Robinsons Malls", "San Juan de Dios Hospital", "San Miguel Brewery", "San Miguel Corporation", "Sarao Motors", "Seaoil", "Security Bank", "Sky", "Sky Pasada", "SkyJet Airlines", "SM Investments Corporation", "SM Prime Holdings", "SM Supermalls", "Smart Communications", "Solar Entertainment Corporation", "Sonshine Media Network International", "South Star Drug", "Southern Broadcasting Network", "Southern Philippines Medical Center", "Sparkle GMA Artist Center", "Spirit of Manila Airlines", "St. Luke\'s Medical Center", "Sta. Lucia Land Inc.", "Star Cinema", "Star Magic", "Star Music", "Starmobile", "Summit Media", "Sun Cellular", "Supercat Fast Ferry Corporation (SFFC)", "SuperFerry", "TAPE Inc.", "TAP Digital Media Ventures Corporation", "The Daily Tribune", "The Philippine Star", "The SM Store", "Tiger 22 Media Corporation", "TM", "TNT", "Tokyo Tokyo", "Top Frontier Investment Holdings", "TV5 Network", "Udenna Corporation", "Union Bank of the Philippines", "United Coconut Planters Bank", "Universal Robina", "University of Mindanao Broadcasting Network", "University of Santo Tomas Hospital", "Upstream", "Viva Entertainment", "ZOE Broadcasting Network", "Asia Amalgamated Holdings Corporation", "Atok-Big Wedge Co., Inc.", "AbaCore Capital Holdings, Inc.", "Asiabest Group International Inc.", "ABS-CBN Corporation", "ABS-CBN Holdings Corporation", "Ayala Corporation", "Acesite (Phils.) Hotel Corporation", "ACEN CORPORATION", "Alsons Consolidated Resources, Inc.", "Aboitiz Equity Ventures, Inc.", "Alliance Global Group, Inc.", "Arthaland Corporation", "Anchor Land Holdings, Inc.", "Ayala Land, Inc.", "AllDay Marts, Inc.", "AyalaLand Logistics Holdings Corp.", "Alternergy Holdings Corporation", "AgriNurture, Inc.", "A. Soriano Corporation", "Aboitiz Power Corporation", "APC Group, Inc.", "Apollo Global Capital, Inc.", "Anglo Philippine Holdings Corporation", "Altus Property Ventures, Inc.", "Apex Mining Co., Inc.", "Abra Mining and Industrial Corporation", "Araneta Properties, Inc.", "AREIT, Inc.", "Raslag Corp.", "Atlas Consolidated Mining and Development Corporation", "Asian Terminals, Inc.", "ATN Holdings, Inc.", "Asia United Bank Corporation", "Axelum Resources Corp.", "Balai Ni Fruitas Inc.", "Benguet Corporation", "Berjaya Philippines Inc.", "BDO Unibank, Inc.", "Belle Corporation", "BHI Holdings, Inc.", "Boulevard Holdings, Inc.", "Bright Kindle Resources & Investments Inc.", "Bloomberry Resorts Corporation", "Bogo-Medellin Milling Company, Inc.", "Bank of Commerce", "Bank of the Philippine Islands", "A Brown Company, Inc.", "Basic Energy Corporation", "Chelsea Logistics and Infrastructure Holdings Corp.", "Concrete Aggregates Corporation", "Central Azucarera de Tarlac, Inc.", "Cityland Development Corporation", "Cebu Air, Inc.", "Crown Equities, Inc.", "Centro Escolar University", "Cebu Holdings, Incorporated", "China Banking Corporation", "Cemex Holdings Philippines, Inc.", "Concepcion Industrial Corporation", "Chemical Industries of the Philippines, Inc.", "Cebu Landmasters, Inc.", "Century Pacific Food, Inc.", "Converge Information and Communications Technology Solutions, Inc.", "Coal Asia Holdings Incorporated", "COL Financial Group, Inc.", "Cosco Capital, Inc.", "Century Properties Group, Inc.", "Century Peak Holdings Corporation", "Citicore Energy REIT Corp.", "Crown Asia Chemicals Corporation", "Citystate Savings Bank, Inc.", "CTS Global Equity Group, Inc.", "Cyber Bay Corporation", "DoubleDragon Corporation", "DDMP REIT, Inc.", "Del Monte Pacific Limited", "DFNN, Inc.", "Dominion Holdings, Inc.", "DITO CME Holdings Corp.", "Dizon Copper-Silver Mines, Inc.", "DMCI Holdings, Inc.", "D.M. Wenceslao & Associates, Incorporated", "Philab Holdings Corp.", "D&L Industries, Inc.", "Discovery World Corporation", "EasyCall Communications Philippines, Inc.", "East Coast Vulcan Corporation", "EEI Corporation", "IP E-Game Ventures, Inc.", "Empire East Land Holdings, Inc.", "Emperador Inc.", "ENEX Energy Corp.", "Euro-Med Laboratories Phil., Inc.", "Ever-Gotesco Resources and Holdings, Inc.", "East West Banking Corporation", "First Abacus Financial Holdings Corporation", "San Miguel Food and Beverage, Inc.", "Figaro Coffee Group, Inc.", "Filinvest Development Corporation"]
for i in range(1, 300):
    
    province = random.choices(provinces, weights = [0.4, 0.2, 0.1, 0.1, 0.1], k=1)[0]
    category = random.choice(epmd_categories)
    name = industry_names[i]
    address = " "
    representative = names.get_full_name(gender="female")
    email = " "
    number = " "
    date = (start_date + datetime.timedelta(days=random.randint(1,365))).strftime("%Y-%m-%d")
    mou = random.choice([True, False])
    loi = random.choice([True, False])
    designation = " "
    remarks = "new partner"
   
    all_epmd.append({
        "province": province,
        "category": category,
        "name": name,
        "address": address,
        "representative": representative,
        "email": email,
        "number": number,
        "date": date,
        "mou": mou,
        "loi": loi,
        "signatory": " ",
        "designation": designation,
        "remarks": remarks
    })

print(f"{len(all_epmd)} records generated for EMPD relation")

all_tmd = [
    {
        "province": random.choices(provinces, weights = [0.4, 0.2, 0.1, 0.1, 0.1], k=1)[0],
        "category": random.choice(tmd_categories),
        "title": "Web Development for Web Developers",
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date" : (start_date + datetime.timedelta(days=random.randint(1,365))).strftime("%Y-%m-%d"),
        "start_time": "1:00 pm",
        "end_time": "5:00 pm",
        "duration": random.choice(range(50,100,5)),
        "resource_person": names.get_full_name(gender="male"),
        "facilitator": names.get_full_name(gender="female"),
        "female": 50,
        "male": 70,
        "cavite": 10,
        "laguna": 21,
        "batangas": 59,
        "rizal": 15,
        "quezon": 15,
        "other": 0,

    },
    {
        "province": random.choices(provinces, weights = [0.4, 0.2, 0.1, 0.1, 0.1], k=1)[0],
        "category": "Cyber Security",
        "title": "Penetration Testing",
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date" : (start_date + datetime.timedelta(days=random.randint(1,365))).strftime("%Y-%m-%d"),
        "start_time": "1:00 pm",
        "end_time": "5:00 pm",
        "duration": random.choice(range(50,100,5)),
        "resource_person": names.get_full_name(gender="male"),
        "facilitator": names.get_full_name(gender="female"),
        "female": 100,
        "male": 70,
        "cavite": 20,
        "laguna": 31,
        "batangas": 69,
        "rizal": 25,
        "quezon": 25,
        "other": 0,

    },
    {
        "province": random.choices(provinces, weights = [0.4, 0.2, 0.1, 0.1, 0.1], k=1)[0],
        "category": random.choice(tmd_categories),
        "title": "Python Fundamentals",
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date" : (start_date + datetime.timedelta(days=random.randint(1,365))).strftime("%Y-%m-%d"),
        "start_time": "1:00 pm",
        "end_time": "5:00 pm",
        "duration": random.choice(range(50,100,5)),
        "resource_person": names.get_full_name(gender="male"),
        "facilitator": names.get_full_name(gender="female"),
        "female": 20,
        "male": 55,
        "cavite": 5,
        "laguna": 5,
        "batangas": 50,
        "rizal": 15,
        "quezon": 0,
        "other": 0,

    }
]

print(f"{len(all_tmd)} records generated for TMD relation")

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

# TMD Data
# with open("tmd.csv", "w", newline="", encoding = "utf-8") as f:
#     writer = csv.DictWriter(f, all_tmd[0].keys())
#     writer.writeheader()
#     writer.writerows(all_tmd)
    
# with conn.cursor() as cursor:
#     with open('tmd.csv') as f:
#         cursor.copy_expert('COPY myapp_tmd(province, category, title, start_date, end_date, start_time, end_time, duration, resource_person, facilitator, female, male, cavite, laguna, batangas, rizal, quezon, other) FROM STDIN WITH HEADER CSV', f)
#         conn.commit()
# print("TMD data ingested")

# EPMD Data
with open("epmd.csv", "w", newline="", encoding = "utf-8") as f:
    writer = csv.DictWriter(f, all_epmd[0].keys())
    writer.writeheader()
    writer.writerows(all_epmd)
    
with conn.cursor() as cursor:
    with open('epmd.csv') as f:
        cursor.copy_expert('COPY myapp_epmd(province, category, name, address, representative, email, number, date, mou, loi, signatory, designation, remarks) FROM STDIN WITH HEADER CSV', f)
        conn.commit()
print("EPMD data ingested")
print("Setup finished. Closing the app now")