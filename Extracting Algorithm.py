import re
import os.path
import os

course_list = ['ACC', 'AES', 'ACE', 'AMS', 'ATH', 'APC', 'ASO', 'ARB', 'ARC', 'ART', 'CAS', 'AAA', 'BSC', 'BIO', 'BWS', 'BUS', 'BLS', 'CPB', 'CHM', 'CHI', 'CLS', 'CMR', 'CMA', 'CMS', 'CIT', 'CSE', 'CCA', 'CJS', 'CRE', 'DST', 'ECO', 'EDL', 'EDP', 'EHS', 'ECE', 'IMS', 'CEC', 'EGM', 'ENT', 'ENG', 'EGS', 'ESP', 'IES', 'FSW', 'FAS', 'FST', 'FIN', 'FRE', 'GEO', 'GLG', 'GER', 'GTY', 'GHS', 'GIC', 'GSC', 'GRK', 'HST', 'HON', 'ISA', 'BIS', 'IDS', 'ITS', 'ITL', 'JPN', 'JRN', 'KNH', 'KOR', 'LAS', 'LAT', 'LST', 'LUX', 'MGT', 'MKT', 'MTH', 'MME', 'MAC', 'MBI', 'MSC', 'MUS', 'NSC', 'NCS', 'NSG', 'ORG', 'PHL', 'PHY', 'POL', 'POR', 'PLW', 'PMD', 'PSS', 'PSY', 'REL', 'RUS', 'SJS', 'SOC', 'SPN', 'SPA',
               'STA', 'STC', 'EDT', 'THE', 'UNV', 'WST', 'WGS']



script_dir = os.path.dirname(os.path.abspath(__file__))
for course in course_list:
    #Read files from Beautiful Soup Code(raw text files)
    base_rel_path = r"\All Course - Base Name\\" + course + ".txt"
    base_file_path = script_dir + base_rel_path
    text_file = open(base_file_path, "r",  encoding="utf8")
    text = text_file.readlines()
    
    #Inititate variables
    course_dict = {}
    pre = {}
    co = {}
    course_code = "Blank"


    for line in text:
        # Search for course lines that has a code, a name and credit hours
        if line[0:3] == course and re.search(r"(?<=\.).*(?=\.)", line) is not None \
            and re.search(r"(?<=\().*(?=\))", line) is not None:
            course_code = line[0:7]
            name = re.search(r"(?<=\.).*(?=\.)", line).group(0)
            credit = re.search(r"(?<=\().*(?=\))", line).group(0)
            course_dict[course_code] = [name.strip(), credit[0]]
        elif course_code != "Blank":
            line_split = line.split(".")
            for i in line_split:
                prereq = re.search(r"(?i)Prerequisite", i)
                coreq = re.search(r"(?i)Co-requisite", i)
                if prereq is not None and coreq is None:
                    pre[course_code] = i.strip()
                    continue
                if coreq is not None:
                    co[course_code] = i.strip()
        else:
            pass
    #Write Info in Prereq File
    pre_rel_path = r"\Prereq\\" + course + ".txt"
    pre_file_path = script_dir + pre_rel_path
    pre_file = open(pre_file_path, "w", encoding="utf8")
    for i in pre:
        pre_file.writelines(pre[i] + "\n")
    pre_file.close()




