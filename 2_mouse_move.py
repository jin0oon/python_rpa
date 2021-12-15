import pyautogui

# 3초 후, 내 마우스 커서 위치 좌표찍기
pyautogui.sleep(2)
print(pyautogui.position())

# 사용할 변수 설정
unity_hierachy_firstobject_x = 1500 # hierachy 첫 오브젝트의 x값
unity_hierachy_firstobject_y = 1000 # hierachy 첫 오브젝트의 y값

unity_property_x = 2000 # property 가시성 아이콘의 x값
unity_property_y = 1000 # property 가시성 아이콘의 y값

unity_hierachy_gap = 20 # hierachy의 오브젝트 사이 간격

photoshop_tab_x = 3218
photoshop_tab_y = 810

# 유니티에서 오브젝트 가시성 ON
pyautogui.moveTo(unity_hierachy_firstobject_x,unity_hierachy_firstobject_y) # hierachy 첫 오브젝트의 위치로 이동 (절대좌표이동) 
p = pyautogui.position()
pyautogui.click(p) # hierachy 첫 오브젝트 클릭

pyautogui.moveTo(unity_property_x,unity_property_y) # property 가시성 아이콘 위치로 이동
p = pyautogui.position()
pyautogui.click(p)  # property 가시성 아이콘 클릭

# printscreen으로 캡쳐하기
pyautogui.write("printscreen")

# 유니티 오브젝트 가시성 OFF
pyautogui.moveTo(unity_property_x,unity_property_y, duration=1) # property 가시성 아이콘 위치로 이동
p = pyautogui.position()
pyautogui.click(p)  # property 가시성 아이콘 클릭

# 포토샵 탭 클릭하여 활성화
pyautogui.moveTo(photoshop_tab_x,photoshop_tab_y,duration=1)
p = pyautogui.position()
pyautogui.click(p)

# 포토샵에 ctrl V
pyautogui.keyDown("ctrlleft")
pyautogui.keyDown("v")
pyautogui.keyUp("v")
pyautogui.keyUp("ctrlleft")

# 유니티 탭 클릭하여 활성화
pyautogui.moveTo(10,10)
p = pyautogui.position()
pyautogui.click(p)

# 반복
num = 1
while num <= 6: #총 7개라서 6번만 반복하면 될 경우
    # 처음과 유일히 다름
    # 유니티 다음 오브젝트 가시성 ON
    pyautogui.moveTo(unity_hierachy_firstobject_x,unity_hierachy_firstobject_y) # hierachy 첫 오브젝트의 위치로 이동 (절대좌표이동) 
    unity_hierachy_firstobject_y = unity_hierachy_firstobject_y + unity_hierachy_gap
    pyautogui.moveTo(unity_hierachy_firstobject_x, unity_hierachy_firstobject_y, duration=1) # 다음 오브젝트 마우스 커서위치 (상대좌표이동)
    p = pyautogui.position()
    pyautogui.click(p) # 다음 오브젝트 클릭
	# 처음과 동일
    # 유니티 오브젝트 가시성 ON
    pyautogui.moveTo(unity_property_x,unity_property_y, duration=1) # property 가시성 아이콘 위치로 이동
    p = pyautogui.position()
    pyautogui.click(p)  # property 가시성 아이콘 클릭
    
    # printscreen으로 캡쳐하기
    pyautogui.write("printscreen")

    # 유니티 오브젝트 가시성 OFF
    pyautogui.moveTo(unity_property_x,unity_property_y, duration=1) # property 가시성 아이콘 위치로 이동
    p = pyautogui.position()
    pyautogui.click(p)  # property 가시성 아이콘 클릭

    # 포토샵 탭 클릭하여 활성화
    pyautogui.moveTo(photoshop_tab_x,photoshop_tab_y,duration=1)
    p = pyautogui.position()
    pyautogui.click(p)

    # 포토샵에 ctrl V
    pyautogui.keyDown("ctrlleft")
    pyautogui.keyDown("v")
    pyautogui.keyUp("v")
    pyautogui.keyUp("ctrlleft")

    # 유니티 탭 클릭하여 활성화
    pyautogui.moveTo(10,10)
    p = pyautogui.position()
    pyautogui.click(p)
    
    num = num + 1
