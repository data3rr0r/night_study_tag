import csv
import getch
from datetime import datetime
import os
import time
from nfc_uid import nfc_uid
student_id=""

def mainscreen():
    os.system('clear')
    global student_id
    while(True):
        print("관리자용 야자 출석 관리 시스템입니다.")
        print("1. 새 학생 등록")
        print("2. 기존 학생 삭제")
        print("3. 프로그램 종료")
        print("원하는 작업을 선택하고 엔터 키를 누르십시오.")
        print("학생과 연동된 카드를 변경하려면 기존 학생 정보를 삭제하고 새로 등록하십시오.")
        key = getch.getch()
        if key == '1':
            add_new_student()
            os.system('clear')
        if key == '2':
            student_id=""
            remove_student()
            time.sleep(3)
            os.system('clear')
        if key == '3':
            break
        else:    
            os.system('clear')

def read_card():
    global student_id, nfc_uid
    print("카드를 인식하세요.")
    nfc_userid = nfc_uid.NFC_UID()
    student_id = str(nfc_userid.read())
    del nfc_userid
    return student_id

def add_new_student():
    # File names
    student_info_file = 'studentlist.csv'
    # Get Info
    new_name = input("새 학생의 이름을 입력하고 엔터 키를 누르십시오: ").strip()
    new_number = input("새 학생의 학번을 입력하고 엔터 키를 누르십시오: ").strip()
    print("등록할 카드를 리더기에 대십시오.")
    new_id=read_card()
    data = [new_id, new_number, new_name]
    os.system('clear')
    print("추가할 학생 이름: ", new_name)
    print("추가할 학생 학번: ", new_number)
    print("추가할 학생 ID: ", new_id)
    print("위 정보로 등록합니다. 정보가 맞으면 1번을 누르십시오. 아니라면 다른 키를 누르고 메인 화면으로 돌아가 재시도하십시오.")
    key =  getch.getch()
    if key != '1':
        return
    # Read the student_info.csv file and add new student with id
    with open(student_info_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print(f"{new_name} 학생이 추가되었습니다.")
    time.sleep(3)
    
def remove_student():
    
    # Get Info
    target_name = input("삭제할 학생의 이름을 입력하고 엔터 키를 누르십시오: ")
    target_number = input("삭제할 학생의 학번을 입력하고 엔터 키를 누르십시오: ")
    input_file = open('studentlist.csv', 'r')
    output_file = open('studentlist_edit.csv', 'w+')
    os.system('clear')
    print("삭제할 학생 이름: ", target_name)
    print("삭제할 학생 학번: ", target_number)
    print("위 정보로 등록된 학생의 모든 등록 정보를 삭제합니다. 정보가 맞으면 1번을 누르십시오. 아니라면 다른 키를 누르고 메인 화면으로 돌아가 재시도하십시오.")
    key =  getch.getch()
    if key != '1':
        return
    writer = csv.writer(output_file)
    for row in csv.reader(input_file):
        if row[1]!=target_name:
            writer.writerow(row)
    input_file.close()
    output_file.close()
    os.remove('studentlist.csv')
    os.rename('studentlist_edit.csv', 'studentlist.csv')
    print(f"{target_name} 학생이 삭제되었습니다.")


mainscreen()