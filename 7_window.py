import pyautogui

pyautogui.sleep(2)
fw = pyautogui.getActiveWindow() # 현재 활성화된 창
print(fw.title)

# 모든 창 가져오기
for w in pyautogui.getAllWindows():
    print(w.title)

# 유니티 탭 이름
unity_tab_name = "Meum-master - SpaceTest - PC, Mac & Linux Standalone - Unity 2020.3.7f1 Personal* <OpenGL ES 3.2>"
# 포토샵 탭 이름
psd_tab_name = "asset-thumbnail-beforecropping.psd @ 25% (pedestal_c, RGB/8#) *"

unity_w = pyautogui.getWindowsWithTitle(unity_tab_name)[0]
print(unity_w)
if unity_w.isActive == False:
    unity_w.activate() # 활성화 (맨앞으로 가져오기)