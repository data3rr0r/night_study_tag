import csv
import getch
from datetime import datetime
import os
import time
import wget
from nfc_uid import nfc_uid 
now_studying = []


path = os.getcwd()
student_id=""
if os.path.exists('studentlist.csv') == False:
    url='https://raw.githubusercontent.com/data3rr0r/night_study_tag/main/studentlist.csv'
    wget.download(url, 'studentlist.csv')
if os.path.exists('attendance_history.csv') == False:
    url='https://raw.githubusercontent.com/data3rr0r/night_study_tag/main/attendance_history.csv'
    wget.download(url, 'attendance_history.csv')
    
def mainscreen():
    global student_id
    os.system('clear')
    while(True):
        print("야자 출석 시스템입니다.")
        print("입실하려면 1번을 누르고 카드를 인식하세요.")
        print("퇴실하려면 2번을 누르고 카드를 인식하세요.")
        key = getch.getch()
        if key == '1':
            student_id=""
            read_card()
            check_student_and_record_entry_time(student_id)
            time.sleep(5)
            os.system('clear')
        if key == '2':
            student_id=""
            read_card()
            check_student_and_record_exit_time(student_id)
            time.sleep(5)
            os.system('clear')
        else:    
            os.system('clear')

def read_card():
    global student_id
    print("카드를 인식하세요.")
    nfc_userid = nfc_uid.NFC_UID()
    student_id = str(nfc_userid.read())
    del nfc_userid
    return student_id


def check_student_and_record_entry_time(student_id):
    # File names
    student_info_file = path + '/studentlist.csv'
    attendance_history_file = path + '/attendance_history.csv'
    
    # Initialize student name as None
    student_name = None
    
    # Read the student_info.csv file
    with open(student_info_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_id:
                student_name = row[2]  
                student_number = row[1]  
    
    # Abort if student not found
    if student_name is None:
        print(f"학생 ID {student_id}를 찾을 수 없습니다. 등록된 카드인지 확인하십시오. 오류가 지속되면 담당 교사에게 문의하십시오.")
        return
    
    # Check if the student is already studying
    if student_id in now_studying:
        print(f"{student_name}님, 이미 입실하셨습니다.")
        return
    
    # Get current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_time_kr = datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
    
    # Prepare the attendance record
    attendance_record = [student_id, student_number, student_name, current_time, '입실']
    
    # append the record to attendance_history.csv
    with open(attendance_history_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(attendance_record)
    
    now_studying.append(student_id)
    print(f"{student_name}님, {current_time_kr}에 입실하셨습니다.")
    
def check_student_and_record_exit_time(student_id):
    # File names
    student_info_file = path + '/studentlist.csv'
    attendance_history_file = path + '/attendance_history.csv'
    
    # Initialize student name as None
    student_name = None
    
    # Read the student_info.csv file
    with open(student_info_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_id:
                student_number = row[1]
                student_name = row[2]    
    
    # Abort if student not found
    if student_name is None:
        print(f"학생 ID {student_id}를 찾을 수 없습니다. 등록된 카드인지 확인하십시오. 오류가 지속되면 담당 교사에게 문의하십시오.")
        return
    
    # Abort if student is not studying
    if student_id not in now_studying:
        print(f"{student_name}님, 입실기록이 없습니다.")
        return 
    
    # Get current time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_time_kr = datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
    
    # Prepare the attendance record
    attendance_record = [student_id, student_number, student_name, current_time, '퇴실']
    
    # append the record to attendance_history.csv
    with open(attendance_history_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(attendance_record)
    
    now_studying.remove(student_id)
    print(f"{student_name}님, {current_time_kr}에 퇴실하셨습니다.")
    

mainscreen()
