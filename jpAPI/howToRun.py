###fastapi 서버 실행 방법
# 1. 안드로이드스튜디오 home.dart에서 서버ip로 바꾸고
# 2. anaconda에서 base가상환경에서 이 프로젝트 경로 찾아간 다음,
# 서버랑 같은 컴에서 접속할거면 uvicorn main:app --reload
# 서버랑 다른 컴에서 접속할거면 uvicorn main:app --host 0.0.0.0 --port 8000
# 하면됨. application startup complete. uvicorn running on 되면 서버실행중.


#adb서버열기
#일단 케이블 연결하고
#cmd가서 C:\Users\kryrl\AppData\Local\Android\Sdk\platform-tools
#adb서버 끄는 방법 : adb kill-server
#adb서버 켜는 방법 : adb start-server
#연결된 디바이스 확인 : adb devices
#연결된 디바이스 ip주소 확인 : adb shell ip addr show wlan0
#디바이스 무선 연결 : adb  tcpip 5555 -> adb connect [ip주소]:5555
#usb케이블 분리 후 디버깅 가능한지 확인
