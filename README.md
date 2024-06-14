# 야간자율학습 태그 시스템
이 프로젝트는 야간 자율학습 시 입/퇴실 시간을 원활히 기록할 수 있도록 RFID 태그를 사용합니다. workflow는 다음과 같습니다.

1. 사용자가 입/퇴실 여부를 선택합니다.
2. 사용자가 카드를 태그합니다.
3. 카드 UID가 studentlist.csv에 있는지 확인합니다. 있다면 4로, 아니면 3-1로 진행합니다.<br>
3-1. 카드 정보와 연결된 정보가 없음을 알리고 초기 화면으로 되돌아갑니다.다.
4. attendance_history.csv에 카드 UID, 학생 이름, 시각, 입퇴실 여부를 기록한다.

# 설치 방법
loader.py 파일을 다운로드받고 적당한 위치에 저장한 다음, 터미널을 열고 python3 loader.py 명령어로 실행하고, 화면의 지침에 따르십시오. 자동으로 필요한 요소들을 다운로드받습니다. 약 5~10분 가량 소요되며, 안정적인 인터넷 환경에서 실행하십시오. 인터넷 연결이 끊긴 경우 아래의
 "Dependency 수동 설치 방법" 섹션을 참고하여 수동으로 설치하십시오.
# 부팅 시 자동 실행 설정


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

대부분의 경우 지켜야 할 순서 없이 바로 설치가 가능하지만, pyscard 모듈의 경우, `sudo apt install swig libpcsclite-dev pcscd` 명령어로 필요한 패키지를 설치한 다음 설치하십시오. 그렇지 않은 경우 빌드 과정에서 오류가 발생하여 설치가 중단됩니다.

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
## 최초 실행 시 모듈 설치 이후 "No module named 'wget'" 오류 메시지가 표시됨
다시 실행하면 정상적으로 진행됩니다. 현재 원인 조사 중에 있습니다.

# 입퇴실 데이터를 볼 수 있는 웹서버를 구동하는 방법
이 장에서는 기기에 저장된 입퇴실 기록을 보여주는 웹서버를 여는 방법에 대해 다룹니다.
현재 작성 중에 있습니다.