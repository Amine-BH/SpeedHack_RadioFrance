import xml.etree.ElementTree as ET

def analyze_speaking_time(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    male_time = 0
    female_time = 0

    for speaker in root.findall('.//Speaker'):
        duration = float(speaker.attrib['dur'])
        gender = int(speaker.attrib['gender'])

        if gender == 1:  # Male
            male_time += duration
        elif gender == 2:  # Female
            female_time += duration

    return male_time, female_time

file1 = "emissions/algerie.xml"
file2 = "emissions/environnement.xml"
file3 = "emissions/actualites.xml"

male_time1, female_time1 = analyze_speaking_time(file1)
male_time2, female_time2 = analyze_speaking_time(file2)
male_time3, female_time3 = analyze_speaking_time(file3)

total_male_time = male_time1 + male_time2 + male_time3
total_female_time = female_time1 + female_time2 + female_time3

def display_results(male_time, female_time, title="Results"):
    total = male_time + female_time
    if total == 0:
        print("No valid data found.")
    else:
        male_percentage = (male_time / total) * 100
        female_percentage = (female_time / total) * 100
        print(f"{title}")
        print(f"Speaking time for men: {male_time:.2f} seconds ({male_percentage:.2f}%)")
        print(f"Speaking time for women: {female_time:.2f} seconds ({female_percentage:.2f}%)\n")

display_results(male_time1, female_time1, "Results for program 1 (Algerie)")
display_results(male_time2, female_time2, "Results for program 2 (Environnement)")
display_results(male_time3, female_time3, "Results for program 3 (Actualités)")
display_results(total_male_time, total_female_time, "Cumulative Results")

