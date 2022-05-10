import random
import time

import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab, Image
import pyautogui
from mss import mss
import pytesseract


def click_start():
    while True:
        time.sleep(3)
        if find_dock_button() == True:

            click_exit_station()
            click_window_mine()
            click_icon_belt()
            click_btn_warp()
            click_drons_output()
            click_window_type()

            while True:
                if check_inventar() == 'True':
                    print('Инвентарь полон. Окончили цикл добычи.')
                    break
                else:
                    print('Инвентарь не полон.Продолжаем работу.')
                    click_veldspar_ore()
                    click_btn_go()
                    click_btn_target()
                    click_btn_mod1()
                    click_btn_mod2()
                    click_misc()
                    time.sleep(1360)
                    click_btn_target()
                    click_btn_mod1()
                    click_btn_mod2()

            # Окончили добычу. Домой.
            click_drons_input()
            click_window_station()
            click_station()
            # По прибытию на станцию
            take_ore()

def click_exit_station():
    # Клик для выхода со станции
    pause = random.randint(50, 60)
    x = random.randint(1183, 1318)
    y = random.randint(179, 206)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(0.2)
    pyautogui.moveTo(670, 385)
    time.sleep(pause)
def click_misc():
    pause = random.randint(1, 3)
    pyautogui.keyDown('ctrl')
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.keyUp('ctrl')
    time.sleep(pause)
def click_window_mine():
    # Ищем вкладку добыча и его координаты.
    res_x, res_y = find_window_mine()
    if res_x == 'Не найдена вкладка "Добыча".':
        print(res_x)
        return 'Бот остановлен. Не найдена вкладка "Добыча".'

    # Клик на вкладку Добыча
    pause = random.randint(1, 3)
    x = random.randint(res_x + 5, res_x + 42)
    y = random.randint(res_y + 8, res_y + 16)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(0.2)
    pyautogui.moveTo(670, 385)
    time.sleep(pause)
def click_window_station():
    # Ищем вкладку добыча и его координаты.
    res_x, res_y = find_window_station()
    if res_x == 'Не найдена вкладка "Станции".':
        print(res_x)
        return 'Бот остановлен. Не найдена вкладка "Станции".'

    # Клик на вкладку станция
    pause = random.randint(8, 11)
    x = random.randint(res_x + 10, res_x + 40)
    y = random.randint(res_y + 4, res_y + 9)
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click(x, y)
    time.sleep(pause)
def click_station():
    # Ищем вкладку добыча и его координаты.
    res_x, res_y = find_window_station()
    if res_x == 'Не найдена вкладка "Станции".':
        print(res_x)
        return 'Бот остановлен. Не найдена вкладка "Станции".'

    # Клик на вкладку Добыча
    pause = random.randint(70, 90)
    x = random.randint(res_x, res_x + 40)
    y = random.randint(res_y + 44, res_y + 46)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(button='right')
    y += 66
    time.sleep(0.7)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(button='right')
    time.sleep(pause)
def click_dock():
    # Ищем вкладку добыча и его координаты.
    res_x, res_y = find_dock_btn()
    if res_x == 'Не найдена кнопка "Док".':
        print(res_x)
        return 'Бот остановлен. Не найдена кнопка "Док".'

    # Клик на вкладку Добыча
    pause = random.randint(60, 75)
    x = random.randint(res_x + 2, res_x + 16)
    y = random.randint(res_y + 2, res_y + 15)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(pause)
def click_icon_belt():
    # Ищем астероидное поле и его координаты.
    res_x, res_y = find_icon_belt()
    if res_x == 'Астероидное поле не найдено.':
        print(res_x)
        exit()

    # Клик на астероидное поле
    pause = random.randint(1, 3)
    x = random.randint(res_x, res_x + 320)
    y = random.randint(res_y, res_y + 11)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(0.2)
    pyautogui.moveTo(670, 385)
    time.sleep(pause)
def click_btn_warp():
    # Клик на варп
    pause = random.randint(45, 60)
    pyautogui.press('s')
    time.sleep(pause)
def click_window_type():
    # Ищем вкладку тип и его координаты.
    res_x, res_y = find_window_type()
    if res_x == 'Вкладка тип не найдена':
        print(res_x)
        return 'Бот остановлен. Вкладка тип не найдена'

    # Клик на "тип"
    pause = random.randint(1, 4)
    x = random.randint(res_x, res_x + 60)
    y = random.randint(res_y + 8, res_y + 10)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(0.2)
    pyautogui.moveTo(670, 385)
    time.sleep(pause)
def click_veldspar_ore():
    # Ищем астероид и его координаты.
    res_x, res_y = find_veldspar_ore()
    if res_x == 'Астероид с рудой veldspar не найден.':
        print(res_x)
        return 'Бот остановлен. Астероид с рудой veldspar не найден.'

    # Клик на астероид
    pause = random.randint(1, 3)
    x = random.randint(res_x, res_x + 60)
    y = random.randint(res_y, res_y + 10)
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(0.2)
    pyautogui.moveTo(670, 385)
    time.sleep(pause)
def click_drons_output():
    pause = random.randint(1, 3)
    pyautogui.keyDown('shift')
    pyautogui.press('f')
    time.sleep(1)
    pyautogui.keyUp('shift')
    time.sleep(pause)
def click_drons_input():
    pause = random.randint(1, 3)
    pyautogui.keyDown('shift')
    pyautogui.press('r')
    time.sleep(1)
    pyautogui.keyUp('shift')
    time.sleep(pause)
def click_btn_go():
    # Клик на кнопку "сблизиться"
    pause = random.randint(60, 75)
    pyautogui.keyDown('q')
    time.sleep(1)
    pyautogui.keyUp('q')
    time.sleep(pause)
def click_btn_target():
    # Ищем вкладку тип и его координаты.
    res_x, res_y = find_btn_target()
    if res_x == 'Кнопка выбрать цель не найдена':
        print(res_x)
        return 'Бот остановлен. Кнопка выбрать цель не найдена'

    # Клик на "тип"
    pause = random.randint(3, 5)
    x = random.randint(res_x - 110, res_x - 90)
    y = random.randint(res_y - 13, res_y - 7)
    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.click(button='right')
    x += random.randint(20, 100)
    y += random.randint(80, 85)
    time.sleep(0.5)
    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.click(button='right')
    time.sleep(0.2)
    pyautogui.moveTo(670, 385)
    time.sleep(pause)
def click_btn_mod1():
    # Клик на кнопку "сблизиться"
    pause = random.randint(1, 2)
    pyautogui.press('f1')
    time.sleep(pause)
def click_btn_mod2():
    # Клик на кнопку "сблизиться"
    pause = random.randint(1, 2)
    pyautogui.press('f2')
    time.sleep(pause)
def click_inventar():
    pause = random.randint(1, 3)
    pyautogui.keyDown('alt')
    pyautogui.press('c')
    time.sleep(2)
    pyautogui.keyUp('alt')
    time.sleep(pause)
def click_store():
    pause = random.randint(1, 3)
    pyautogui.keyDown('alt')
    pyautogui.press('g')
    time.sleep(1)
    pyautogui.keyUp('alt')
    time.sleep(pause)

def take_ore():
    click_inventar()
    ore_x, ore_y = find_store_ore()
    if ore_x == 'Отсек для руды не был найден':
        print('Отсек для руды не был найден')
        exit()
    click_store()
    ore_x += 160
    ore_y += 25

    for i in range(random.randint(2,4)):
        take_ore_click(ore_x, ore_y)
        click_inventar()
        time.sleep(random.randint(1,3))
        click_inventar()

    click_store()
    click_inventar()
def take_ore_click(ore_x, ore_y):

    pyautogui.moveTo(ore_x, ore_y)
    time.sleep(0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(ore_x, ore_y + 250)
    time.sleep(0.5)
    pyautogui.mouseUp()

def check_inventar():
    pyautogui.moveTo(670, 385)
    click_inventar()
    finder_x, finder_y = find_inventar_finder()
    _bool = find_inventar_mass(finder_x, finder_y)
    click_inventar()

    if _bool == 'True':
        return 'True'
    else:
        return 'False'

def find_store_ore():
    # Загружаем образец
    template = cv2.imread('img/store_ore.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 600}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем строку поиска в инвентаре.[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Рабочее окно найдено! x: {x} | y: {y}')
            _bool = True
            return x, y
    return 'Отсек для руды не был найден', 0
def find_inventar_mass(finder_x, finder_y):
    global max
    x = random.randint(finder_x - 180, finder_x)
    y = random.randint(finder_y + 8, finder_y + 20)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(1)
    base_screen = ImageGrab.grab(bbox=(finder_x - 141, finder_y - 20, finder_x - 31, finder_y - 4))
    base_screen.save('img/scr.png')
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img_inventar = Image.open("scr.png")
    text = pytesseract.image_to_string(img_inventar)
    print(f'1   {text}')
    text = text.replace('e', '')
    text = text.replace('t', '')
    text = text.replace(' ', '')
    text = text.replace('m', '')
    text = text.replace('(', '')
    text = text.replace('£', '')
    text = text.replace('M', '')
    text = text.replace('|', '')
    text = text.replace('w', '')
    text = text.replace('?', '')
    text = text.replace('*', '')
    text = text.replace('‘', '')
    text = text.replace(',', '.')
    text = text.replace('S', '5')
    text = text.replace('B', '5')
    print(f'2    {text}')
    txt = text.split('/')
    print(f'1now: {txt[0]} | max: {txt[1]}')

    now_arr = txt[0].split('.')
    max_arr = txt[1].split('.')

    print(f'2now: {now_arr[0]} | max: {max_arr[0]}')

    if now_arr[0] == '':
        print('if')
        now_arr[0] = 0

    now = now_arr[0]

    now = int(now)
    max_s = int(max_arr[0])
    print(f'3now: {now} | max: {max_s}')

    now = now // 1000
    max_s = max_s // 1000
    print(f'4now: {now} | max: {max_s}')

    if now == 5:
        return 'True'
    else: 'False'

def find_inventar_finder():
    # Загружаем образец
    template = cv2.imread('img/inventar_finder.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 600}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем строку поиска в инвентаре.[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Строка поиска найдена! x: {x} | y: {y}')
            _bool = True
            return x, y
def find_dock_button():
    # Загружаем образец
    template = cv2.imread('img/dock_but.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 600}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем кнопку "выйти из дока".[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Рабочее окно найдено! x: {x} | y: {y}')
            _bool = True
            return _bool
def find_dock_btn():
    # Загружаем образец
    template = cv2.imread('img/dock_btn.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 600}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем кнопку "войти в док".[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Рабочее окно найдено! x: {x} | y: {y}')
            _bool = True
            return _bool
    return 'Не найдена кнопка "Док".'
def find_icon_belt():
    # Загружаем образец
    base_screen = ImageGrab.grab(bbox=(0, 0, 1400, 800))
    base_screen.save('img/scr.png')
    template = cv2.imread('img/icon_belt.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем иконку астероидного поля.[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.5)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return 'Астероидное поле не найдено.', 0
def find_veldspar_ore():
    # Загружаем образец
    template = cv2.imread('img/veldspar_ore.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем иконку астероида veldspar.[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return 'Астероид с рудой veldspar не найден.', 0
def find_window_mine():
    # Загружаем образец
    template = cv2.imread('img/window_mine.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Вкладка добычи найдена. [{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return 'Не найдена вкладка "Добыча".', 0
def find_window_station():
    # Загружаем образец
    template = cv2.imread('img/window_station.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем вкладку станции. [{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return 'Не найдена вкладка "Станции".', 0
def find_icon_station():
    # Загружаем образец
    template = cv2.imread('img/icon_station.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Вкладка навигации найдена. [{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return 'Не найдена вкладка "Навигация".', 0
def find_window_type():
    # Загружаем образец
    template = cv2.imread('img/window_type.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем вкладку "тип".[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return 'Вкладка тип не найдена', 0
def find_btn_drons():
    # Загружаем образец
    template = cv2.imread('img/btn_drons.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем окно дронов.[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return 'Кнопка дронов не найдена', 0
def find_btn_warp():
    # Загружаем образец
    template = cv2.imread('img/btn_warp.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем кнопку варп.[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return "Кнопка варпа не найдена", 0
def find_btn_go():
    # Загружаем образец
    template = cv2.imread('img/btn_go.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем кнопку сблизиться.[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return "Кнопка сблизиться не найдена", 0
def find_btn_target():
    # Загружаем образец
    template = cv2.imread('img/btn_target.png', 0)
    bounding_box = {'top': 0, 'left': 0, 'width': 1400, 'height': 800}
    sct = mss()
    for i in range(11):
        # Захват картинки
        sct_img = sct.grab(bounding_box)
        img = np.array(sct_img)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        print(f'Ищем кнопку выбора цели.[{i}/10]')

        # Ищем объект на экране
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        x, y = 0, 0
        # Берем последнее совпадение и записываем координаты
        for pt in zip(*loc[::-1]):
            x = pt[0]
            y = pt[1]

        if(x != 0 and y != 0):
            x -= 7
            y -= 4
            print(f'Найдено! x: {x} | y: {y}')
            _bool = True
            return x, y

    return "Кнопка выбрать цель не найдена", 0

