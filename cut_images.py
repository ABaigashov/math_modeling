# In the CodeSpace
# По оси y: 30 * количество строк - должен быть размер изображения (Font Size 20)
# По оси x: 1160
# 1440 X 822 - размер скрина редактора
# 14 * количество строк - должен быть размер изображения для терминала

# Методика быстрых скринов:
#   - Сначала загружаем все файлы для занятия в CodeSpace
#   - Затем делаем скрины редактора (после чего удаляем код) и раскидываем все по папкам
#   - Далее делаем скрины терминала и очищаем его
#   - Делаем коммит
#   - Делаем скрины для заднего фона
#   - Делаем скрины python3

# Лайфхаки:
#   - Лучше поджать нижнюю строчку при выборе масштаба

from PIL import Image
import os

im = Image.open('pic.png')

folder_name = input('folder name: ')
try:
    os.mkdir(f'{folder_name}')
except:
    print('Folder exist')

line_number = int(input('lines number: '))
pictures_number = int(input('start pictures number: '))
output_name = int(input('output name (0 - redactor, 1 - terminal): '))
image_size = im.size
crop_step = image_size[1] // line_number

x0 = 0
y0 = 0
x1 = image_size[0]
y1 = crop_step

for i in range(line_number):
    im_crop = im.crop((x0, y0, x1, y1))
    if output_name == 0:
        im_crop.thumbnail((1920, 50))
        im_crop.save(f'{folder_name}/redactor pic_{i + pictures_number}.png', quality=100)
    else:
        im_crop.thumbnail((1920, 23))
        im_crop.save(f'{folder_name}/terminal pic_{i + pictures_number}.png', quality=100)
    y0 = y1
    y1 += crop_step
