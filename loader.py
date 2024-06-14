# Interactive Program Loader
# Do not execute interactive.py directly, use loader.py instead
# make sure to automatically load this file from bashrc

import os
import time
import socket


# Print Title
print("야간자율학습 출석 시스템 로더 v1.1")
# Get local version info, create .version if not exists, otherwise read the version
if not os.path.exists('.version'):
    local_version = float(0)
    username = os.getlogin()
    print('최초 실행입니다. 비밀번호를 입력하여 프로그램에 실행한 라이브러리를 다운받으십시오. 인터넷 연결이 도중에 끊기지 않도록 안정적인 온라인 환경에서 진행하십시오.')
    print('프로그램 실행을 위한 모듈 설치 중...')
    os.system('sudo apt update')
    os.system('sudo apt install -y python3-pip')
    os.system('sudo apt install -y swig')
    os.system('sudo apt install -y libpcsclite-dev')
    os.system('sudo apt install -y pcscd')
    os.system('sudo apt install -y pcsc-tools')
    os.system('pip install getch')
    os.system('pip install datetime')
    os.system('pip install wget')
    os.system('pip install nfc-uid')
    os.system('pip install keyboard')
    os.system('pip install packaging')
    os.system('pip install pyscard')
    print("웹 서버 동작을 위한 모듈 설치 중...")
    os.system('sudo apt -y install apache2')
    os.system('sudo chown ' + username + ' /var/www/html')
    os.system('sudo chmod 777 /var/www/html')
    print("파일 복사 중...")
    os.system('git clone https://github.com/data3rr0r/night_study_tag_web')
    os.system('cp -r night_study_tag_web/* /var/www/html')
    os.system('sudo systemctl restart apache2')
    print("충돌 문제가 있는 모듈 비활성화 중...")
    os.system("printf 'blacklist pn533\nblacklist pn533_usb\nblacklist nfc\n' | sudo tee /etc/modprobe.d/blacklist-pn533.conf")
    os.system("sudo modprobe -r pn533_usb")
    os.system("sudo modprobe -r pn533")
    os.system("sudo modprobe -r nfc")
    os.system("sudo modprobe -b pn533_usb")
    os.system("sudo modprobe -b pn533")
    os.system("sudo modprobe -b nfc")
else:
    with open('.version', 'r') as f:
        local_version = float(f.read())

def online_update():
    #get remote version info
    if os.path.exists('.server_version'):
        os.remove('.server_version')
    os.system('wget https://raw.githubusercontent.com/data3rr0r/night_study_tag/main/.server_version' )
    with open('.server_version', 'r') as f:
        remote_version = float(f.read())
        
    time.sleep(1)
    print(f"\n최신 버전: {remote_version}")
    time.sleep(1)

    if remote_version > local_version:
        print(f"새로운 버전({remote_version}) 발견됨. 업데이트중...")
        if os.path.exists('night_study_interactive.py'):
            os.remove('night_study_interactive.py')
        os.system('wget https://raw.githubusercontent.com/data3rr0r/night_study_tag/main/night_study_interactive.py' )
        print("\n업데이트 완료.")
        with open('.version', 'w') as f:
            f.write(str(remote_version))
    else:
        print("이미 최신 버전을 사용중입니다.")

time.sleep(1)
print(f"\n현재 버전: {local_version}")

# Check internet connection
print("인터넷 연결 확인 중...")
time.sleep(1)
try:
    socket.create_connection(('www.google.com', 80))
    print("인터넷 연결 확인됨.")
    online_update()
except OSError:
    print("인터넷 연결이 확인되지 않았습니다. 인터넷 연결을 확인하십시오. 업데이트 확인 없이 시스템을 시작합니다.")


time.sleep(3)
print("시스템 시작 중...")
time.sleep(5)
os.system('python3 night_study_interactive.py')
