import pyautogui

# 3초 후, 내 마우스 커서 위치 좌표찍기
pyautogui.sleep(3)
print(pyautogui.position())

# 사용할 변수 설정
# 회사컴 x=1502, y=249
unity_hierachy_firstobject_x = 1502 # hierachy 첫 오브젝트의 x값
unity_hierachy_firstobject_y = 249 # hierachy 첫 오브젝트의 y값

# 회사컴 x=1936, y=108
unity_inspector_x = 1936 # inspector 가시성 아이콘의 x값
unity_inspector_y = 108 # inspector 가시성 아이콘의 y값

# 회사컴 17
unity_hierachy_gap = 17 # hierachy의 오브젝트 사이 간격

# 회사컴 x=4317, y=1098
photoshop_tab_x = 4317
photoshop_tab_y = 1098

# 유니티 탭 이름
unity_tab_name = "Meum-master - SpaceTest - PC, Mac & Linux Standalone - Unity 2020.3.7f1 Personal* <OpenGL ES 3.2>"
# 포토샵 탭 이름
psd_tab_name = "asset-thumbnail-beforecropping.psd @ 25% (pedestal_c, RGB/8#) *"


# 유니티에서 오브젝트 가시성 ON
pyautogui.moveTo(unity_hierachy_firstobject_x,unity_hierachy_firstobject_y) # hierachy 첫 오브젝트의 위치로 이동 (절대좌표이동) 
p = pyautogui.position()
pyautogui.click(p) # hierachy 첫 오브젝트 클릭

pyautogui.moveTo(unity_inspector_x,unity_inspector_y, duration=1) # inspector 가시성 아이콘 위치로 이동
p = pyautogui.position()
pyautogui.click(p)  # inspector 가시성 아이콘 클릭

# printscreen으로 캡쳐하기
pyautogui.write(["printscreen"])
pyautogui.sleep(1)

# 유니티 오브젝트 가시성 OFF
pyautogui.click(p)  # inspector 가시성 아이콘 클릭

# 포토샵 탭 활성화
psd_w = pyautogui.getWindowsWithTitle(psd_tab_name)[0]
psd_w.activate() # 활성화 (맨앞으로 가져오기)

# 포토샵 탭으로 마우스 이동
pyautogui.moveTo(photoshop_tab_x,photoshop_tab_y,duration=1)
p = pyautogui.position()
pyautogui.click(p)

# 포토샵에 ctrl V
pyautogui.hotkey('ctrlleft', 'v')

# 포토샵 window title 초기화
pyautogui.sleep(1)
pyautogui.click(p)

# 유니티 탭 활성화
unity_w = pyautogui.getWindowsWithTitle(unity_tab_name)[0]
unity_w.activate() # 활성화 (맨앞으로 가져오기)

# 반복
num = 1
while num <= 6: #총 7개라서 6번만 반복하면 될 경우
    # 처음과 유일히 다름
    # 유니티 다음 오브젝트 가시성 ON
    pyautogui.moveTo(unity_hierachy_firstobject_x,unity_hierachy_firstobject_y, duration=1) # hierachy 첫 오브젝트의 위치로 이동 (절대좌표이동) 
    unity_hierachy_firstobject_y = unity_hierachy_firstobject_y + unity_hierachy_gap
    pyautogui.moveTo(unity_hierachy_firstobject_x, unity_hierachy_firstobject_y, duration=1) # 다음 오브젝트 마우스 커서위치 (상대좌표이동)
    p = pyautogui.position()
    pyautogui.click(p) # 다음 오브젝트 클릭
	# 처음과 동일
    # 유니티 오브젝트 가시성 ON
    pyautogui.moveTo(unity_inspector_x,unity_inspector_y, duration=1) # inspector 가시성 아이콘 위치로 이동
    p = pyautogui.position()
    pyautogui.click(p)  # inspector 가시성 아이콘 클릭
    
    # printscreen으로 캡쳐하기
    pyautogui.write("printscreen")

    # 유니티 오브젝트 가시성 OFF
    pyautogui.sleep(1)
    pyautogui.click(p)  # inspector 가시성 아이콘 클릭

    # 포토샵 탭 활성화
    psd_w = pyautogui.getWindowsWithTitle(psd_tab_name)[0]
    psd_w.activate() # 활성화 (맨앞으로 가져오기)

    # 포토샵 탭으로 마우스 이동
    pyautogui.moveTo(photoshop_tab_x,photoshop_tab_y,duration=1)
    p = pyautogui.position()
    pyautogui.click(p)

    # 포토샵에 ctrl V
    pyautogui.hotkey('ctrlleft', 'v')

    # 포토샵 window title 초기화
    pyautogui.sleep(1)
    pyautogui.click(p)

    # 유니티 탭 활성화
    unity_w = pyautogui.getWindowsWithTitle(unity_tab_name)[0]
    unity_w.activate() # 활성화 (맨앞으로 가져오기)
    
    num = num + 1
