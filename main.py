import os
import time
import pyautogui

# Открываем калькулятор в зависимости от операционной системы


def open_calculator():
    if os.name == 'nt':  # Windows
        os.system('start calc')
    elif os.name == 'posix':  # macOS или Linux
        os.system('open -a Calculator')  # Для macOS
        
    time.sleep(2)  

# Функция для нажатия кнопок на калькуляторе


def press_buttons(buttons):
    for button in buttons:
        # Ищем кнопку на экране
        location = pyautogui.locateOnScreen(f'{button}.png', confidence=0.9)
        if location is not None:
            pyautogui.click(location)  
            time.sleep(2)  
        else:
            print(f'Кнопка {button} не найдена на экране.')


# Основная программа
if __name__ == '__main__':
    open_calculator()

    # Кнопки для ввода 12 + 7 =
    buttons_to_press = ['1', '2', '+', '7', '=']

    press_buttons(buttons_to_press)
