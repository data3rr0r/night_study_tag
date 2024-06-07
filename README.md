# 야간자율학습 태그 시스템
이 프로젝트는 야간 자율학습 시 입/퇴실 시간을 원활히 기록할 수 있도록 RFID 태그를 사용합니다. workflow는 다음과 같습니다.

1. 사용자가 입/퇴실 여부를 선택한다
2. 사용자가 카드를 태그한다.
3. 카드 UID가 studentlist.csv에 있는지 확인한다. 있다면 4로, 아니면 3-1로 진행합니다.
3-1. 카드 정보와 연결된 정보가 없음을 알리고 초기 화면으로 되돌아간다.
4. attendance_history.csv에 카드 UID, 학생 이름, 시각, 입퇴실 여부를 기록한다.

# 설치 방법
loader.py 파일을 다운로드받고 적당한 위치에 저장한 다음, 터미널을 열고 python3 loader.py 명령어로 실행하고, 화면의 지침에 따르십시오. 자동으로 필요한 요소들을 다운로드받습니다. 약 5~10분 가량 소요되며, 안정적인 인터넷 환경에서 실행하십시오. 

# 부팅 시 자동 실행 설정


# 파일 구조 설명
## studentlist.csv
학생들의 이름과 그에 대응하는 카드 UID를 적어놓은 파일입니다. column 0에는 카드 UID, column 1에는 학번, column 2에는 학생 이름이 저장되어 있습니다.
아래는 예시 형식입니다.

|ID|Number|Name|
|---|---|---|
|BDCE2E09|10101|손흥민|
|65931E1B|10102|조규성|
|E9C08E52|10103|김민재|
|...|...|...|

## attendance_history.csv
학생들의 입출입 기록을 저장합니다. column 0부터 순서대로 UID, 학번, 이름, 시각, 입퇴실 여부를 기록합니다.
아래는 예시 형식입니다.

|ID|Number|Name|Time|I/O|
|---|---|---|---|---|
|BDCE2E09|10101|손흥민|2024-01-01 12:34:56|입실|
|65931E1B|10102|조규성|2024-01-01 12:35:46|퇴실|
|E9C08E52|10103|김민재|2024-01-01 12:36:16|입실|
|...|...|...|...|...|


# 자주 묻는 질문/버그 해결법
## 최초 실행 시 일부 환경에서 loader가 자동으로 getch 설치 도중 subprocess-exited-with-error 메시지가 표기됨
터미널을 열고 `sudo apt install python3-dev` 명령어를 입력한 다음, `pip install getch` 명령어를 입력하여 수동으로 설치하십시오.

## Dependency 수동 설치 방법
이 프로그램은 `getch, datetime, time, wget, nfc-uid, keyboard, smartcard, packaging, py122u`모듈을 사용합니다. 
터미널을 열고 `pip install [모듈명]`을 입력하여 필요한 요소를 설치하십시오. 
예시) `pip install getch`
위에 적힌 모든 모듈에 대해 설치 명령어를 입력하십시오. 그런 다음 loader.py를 다시 시작합니다.

## No module names 'smartcard.CardType' 오류 발생
일부 환경에서 pip으로 smartcard 모듈 설치 시 설치했음에도 인식되지 않는 경우가 있습니다. 이 경우 `sudo apt install python3-pyscard` 명령어로 smartcard와 pyscard를 같이 설치하십시오.

## loader 오류 발생 시
이 Repository에서 loader.py를 수동으로 다운로드받고 파일을 대치하십시오.