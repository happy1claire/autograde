#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 17, 2024
@author: happy1claire

"""

import pandas as pd
import re
import os

# Load grade book as pandas dataframe
grade_book = pd.read_csv('/Users/happy1claire/Desktop/inst377-lab-2-submissions/2024-02-18T0216_Grades-INST377.csv')
grade_book['lab2_comment'] = None
print(grade_book['Student'])

root_directory = '/Users/happy1claire/Desktop/inst377-lab-2-submissions'

def read_html_files(root_directory):
    # Iterate through all folders
    for subdir, dirs, files in os.walk(root_directory):
        for file in files:
            
            # Find the markdown file
            if file.endswith('.md'):
                file_path = os.path.join(subdir, file)

                # Open markdown 
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                    pattern = r'# Name \(Please Input your name\):([\w\s]+)'
                    matches = re.search(pattern, content)
                    print(subdir)

                    # Parse out student's name
                    student_arr = []
                    
                    if matches is not None:
                        matched_string = matches.group()
                        matched_string = matched_string.strip()
                        split_str = matched_string.split(' ')
           
                        for parts in split_str:
                            student_arr.append(parts) 
                        
                        # Remove all the non-alphbatical character in list
                        student_arr = [re.sub(r'[^a-zA-Z]', '', item) for item in student_arr]
                    else:
                        print('dd')
                    
                    student_arr = student_arr[-2:]
                    
                    # Transfer student name into string
                    student_name_list = []
                    student_name = ''

                    # Reverse students name to last+first name order to align with grade_book
                    for item in reversed(student_arr):
                        student_name_list.append(item)

                    student_name = ', '.join(student_name_list)
                    print(student_name)

                    # Student score and reason for score deduction
                    student_score = 0
                    dedection_reason = ''

                    # Find and read the html and csv file from the folder
                    if file.endswith('.html'):
                        file_path_html = os.path.join(subdir, file)
                        with open(file_path_html, 'r', encoding='utf-8') as html_file:
                            html_content = html_file.read()

                                if "</title>" not in html_content:
                                    points -= 1
                                    note += "No Title; "
                                if "<img" not in html_content:
                                    points -= 2
                                    note += "No Image; "
                                if "</h1>" not in html_content:
                                    points -= 1
                                    note += "No h1; "
                                if "</h2>" not in html_content:
                                    points -= 1
                                    note += "No h2; "
                                if "</h3>" not in html_content:
                                    points -= 1
                                    note += "No h3; "
                                if "</ul>" not in html_content and "</li>" not in html_content:
                                    points -= 2
                                    note += "No Unordered List; "
                                if "</ol>" not in html_content:
                                    points -= 2
                                    note += "No Ordered List; "

                                    
                                if "</table>" not in html_content:
                                    points -= 6
                                    note += "No Table; "
                                elif html_str.count("</tr>") < 2:
                                    points -= 2
                                    note += "Not Enough rows; "
                                elif html_str.count("</td>") < 2:
                                    points -= 2
                                    note += "Not Enough columns; "    
                                elif "</th>" not in html_str:
                                        points -= 2
                                        note += "No Row Heading; "
                                if "&#" not in html_str and len([dec for dec in html_str if ord(dec) > 127]) == 0:    
                                    points -= 1
                                    note += "No Emoji; "
                                if "background" not in html_str:
                                    points -= 1
                                    note += "No Background Color; "
                                if "</blockquote>" not in html_str:
                                    points -= 1
                                    note += "No Blockquote; "
                                if "</a>" not in html_str:
                                    points -= 1
                                    note += "No Hyperlink; "
                    
                    elif file.endswith('.css'):
                        file_path_csv = os.path.join(subdir, file)
                        with open(file_path_csv, 'r', encoding='utf-8') as css_file:)
                            css_content = css_file.read()
                        
                            if 
                
           
read_html_files(root_directory)

            