# Interactive Program Loader
# Do not execute interactive.py directly, use loader.py instead
# make sure to automatically load this file from bashrc

import wget
import os
import time

# Print Title
print("야간자율학습 출석 시스템 로더 v1.0")
# Get local version info, create .version if not exists, otherwise read the version
if not os.path.exists('.version'):
    local_version = float(0)
else:
    with open('.version', 'r') as f:
        local_version = float(f.read())
        
time.sleep(1)
print(f"\n현재 버전: {local_version}")

#get remote version info
url = 'https://raw.githubusercontent.com/data3rr0r/night_study_tag/main/.server_version'
if os.path.exists('.server_version'):
    os.remove('.server_version')
wget.download(url, '.server_version')
with open('.server_version', 'r') as f:
    remote_version = float(f.read())
    
time.sleep(1)
print(f"\n최신 버전: {remote_version}")
time.sleep(1)

if remote_version > local_version:
    print(f"새로운 버전({remote_version}) 발견됨. 업데이트중...")
    url = 'https://raw.githubusercontent.com/data3rr0r/night_study_tag/main/night_study_interactive.py'
    os.remove('night_study_interactive.py')
    wget.download(url, 'night_study_interactive.py')
    print("\n업데이트 완료.")
    with open('.version', 'w') as f:
        f.write(str(remote_version))
else:
    print("이미 최신 버전을 사용중입니다.")
    

time.sleep(3)
print("시스템 시작 중...")
time.sleep(5)
os.system('python3 night_study_interactive.py')

