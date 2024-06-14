# 야간자율학습 태그 시스템
이 프로젝트는 야간 자율학습 시 입/퇴실 시간을 원활히 기록할 수 있도록 RFID 태그를 사용합니다. workflow는 다음과 같습니다.

1. 사용자가 입/퇴실 여부를 선택합니다.
2. 사용자가 카드를 태그합니다.
3. 카드 UID가 studentlist.csv에 있는지 확인합니다. 있다면 4로, 아니면 3-1로 진행합니다.<br>
3-1. 카드 정보와 연결된 정보가 없음을 알리고 초기 화면으로 되돌아갑니다.다.
4. attendance_history.csv에 카드 UID, 학생 이름, 시각, 입퇴실 여부를 기록합니다.

# 설치 방법
터미널을 열고 다음 명령어를 복사하여 붙여넣습니다. 
```
wget https://raw.githubusercontent.com/data3rr0r/night_study_tag/main/loader.py
```
터미널에 복사/붙여넣기 시에는 일반적으로 복사/붙여넣기에 사용하는 Ctrl+C/Ctrl+V 대신 Ctrl+Shift+C/Ctrl+Shift+V 조합을 이용함에 유의하십시오. 그런 다음 `python3 loader.py` 명령어로 프로그램을 실행하십시오. 실행하면 자동으로 필요한 요소들을 다운로드받습니다. 최고 관리자 권한을 사용하는 부분이 포함되어 있으므로, 실행 직후 계정 비밀번호를 입력하시기 바랍니다. 설치에는 약 5~10분 가량 소요되며, 안정적인 인터넷 환경에서 실행하십시오. 인터넷 연결이 끊긴 경우 아래의 "Dependency 수동 설치 방법" 섹션을 참고하여 수동으로 설치하십시오.
# 부팅 시 자동 실행 설정
현재 작성중인 부분입니다. 완성되는 대로 업로드할 예정입니다.

# 파일 설명
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

## 최초 실행 시 일부 환경에서 loader가 자동으로 getch를 설치하는 도중 subprocess-exited-with-error 메시지가 표기됨
터미널을 열고 `sudo apt install python3-dev` 명령어를 입력하여 python3-dev를 설치하고, 아래의 'Dependency 수동 설치 방법' 섹션의 지시에 따르십시오.

## Dependency 수동 설치 방법
이 프로그램은 `getch, datetime, time, wget, nfc-uid, keyboard, pyscard, keyboard,packaging`모듈을 사용합니다. 
터미널을 열고 `pip install [모듈명]`을 입력하여 필요한 요소를 설치하십시오. 
예시) `pip install getch`
위에 적힌 모든 모듈에 대해 설치 명령어를 입력하십시오. 그런 다음 loader.py를 다시 시작합니다.

대부분의 경우 지켜야 할 순서 없이 바로 설치가 가능하지만, pyscard 모듈의 경우, 다음 명령어를 순서대로 입력하여 필요한 패키지를 설치한 다음  pyscard 모듈을 설치하십시오. 그렇지 않은 경우 빌드 과정에서 오류가 발생하여 설치가 중단됩니다. 명령어는 다음과 같습니다.
```
sudo apt install -y swig
sudo apt install -y libpcsclite-dev
sudo apt install -y pcscd
sudo apt install -y pcsc-tools
```

## loader 오류 발생 시
이 Repository에서 loader.py를 수동으로 다운로드받고 파일을 교체하십시오.

## Waiting For NFC-Card.. 메시지가 출력된 이후 카드를 인식시켜도 ID가 표시되지 않음
Ubuntu 22.04에 기본적으로 설치된 시스템 모듈과 충돌이 발생하여 수동으로 제거해야 합니다. 터미널을 열고 다음 명령어를 순서대로 입력하십시오. 이렇게 하면 해당 시스템 모듈을 제거하고 다시 자동으로 사용하지 않도록 블랙리스트 처리합니다.
```
printf 'blacklist pn533\nblacklist pn533_usb\nblacklist nfc\n' | sudo tee /etc/modprobe.d/blacklist-pn533.conf
sudo modprobe -r pn533_usb
sudo modprobe -r pn533
sudo modprobe -r nfc
sudo modprobe -b pn533_usb
sudo modprobe -b pn533
sudo modprobe -b nfc
```
## ~~최초 실행 시 모듈 설치 이후 "No module named 'wget'" 오류 메시지가 표시됨~~ 해결됨
~~다시 실행하면 정상적으로 진행됩니다. 현재 원인 조사 중에 있습니다.~~ wget 명령어를 파이썬 모듈로 불러오지 않고 바로 시스템 명령어로 처리하도록 변경하여 해결되었습니다.

# 입퇴실 데이터를 볼 수 있는 웹서버를 구동하는 방법
최초 설치 시 loader.py에서 자동으로 필요한 작업을 모두 수행합니다.