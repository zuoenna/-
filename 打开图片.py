from PIL import Image,ImageFont,ImageDraw
img=Image.open (r"C:\Users\75445\Desktop\aa\1.png")
font=ImageFont.truetype(r"C:\WINDOWS\Fonts\SIMSUN.TTC",size=50)
draw=ImageDraw.Draw(img)
draw.text(xy=(360,420),text="我在夜曲编程学习编程",fill="white",font=font)
img.save(r"C:\Users\75445\Desktop\aa\1.png")


img.show()





