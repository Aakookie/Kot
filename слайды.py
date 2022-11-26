from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import os 
li = ["Федор Тютчев \nSILENTIUM! ",
"Молчи, скрывайся и таи \nИ чувства и мечты свои —",
"Пускай в душевной глубине \nВстают и заходят оне",
"Безмолвно, как звезды в ночи, \nЛюбуйся ими — и молчи.",
"Как сердцу высказать себя? \nДругому как понять тебя?",
"Поймет ли он, чем ты живешь? \nМысль изреченная есть ложь.",
"Взрывая, возмутишь ключи, — \nПитайся ими — и молчи.",
"Лишь жить в себе самом умей — \nЕсть целый мир в душе твоей",
"Таинственно-волшебных дум; \nИх оглушит наружный шум,",
"Дневные разгонят лучи, — \nВнимай их пенью — и молчи!.."]
def create_image(l):
    n = 0
    for i in l:
        n += 1 
        stop = i.find("\n")
        l1 = stop - 1
        x = (800 - l1*26)/2

        im = Image.new('RGB', (800,600), color=('#ADD8E6'))
        font = ImageFont.truetype('C:/Users/student/Documents/122А/Kукина/MTCORSVA.TTF', size = 60)

        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (x,230),
            i,
            font = font,
            fill = ("#000080")
        )
  
        im.save(f'C:/Users/student/Documents/122А/Kукина/slaydy/s{n}9.jpg')

#create_image(li)
directory = 'C:/Users/student/Documents/122А/Kукина/slaydy'
files = os.listdir(directory)
images = list(filter(lambda x: x.endswith('.jpg'), files))
clips = [ImageClip(m).set_duration(2) for m in images]
print(images)
input()
final_clip = concatenate_videoclips(clips, method = 'compose')
final_clip.write_videofile('test.mp4', fps = 24)