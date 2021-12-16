import pyautogui

pyautogui.sleep(3)

#커서 활성화 전제??
#이건 타이핑
pyautogui.write("12345")
#이건 키보드의 키 - automate the boring stuff with python - chap20 - keyboard attribute
pyautogui.write(["t","left","a","enter"])
pyautogui.sleep(1)
pyautogui.write(["printscreen"])

# # 단축키 첫번째 방법
# pyautogui.keyDown("ctrlleft")
# pyautogui.keyDown("v")
# pyautogui.keyUp("v")
# pyautogui.keyUp("ctrlleft")

# 단축키 두번째 방법
pyautogui.hotkey('ctrlleft', 'v')