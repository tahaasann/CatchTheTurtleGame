import turtle
import math
from random import randint
import time

# Ekran oluşturmak için
turtle_screen = turtle.Screen()
turtle_screen.title("Python Catch The Turtle")
turtle_screen.bgcolor("#935FA7")
turtle_screen.setup(width=1000,height=1000)

# Scoreboard için de bir turtle tanımlıyoruz.
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.speed(0)
scoreboard.goto(0,360)

point = 0 # Scoreboard'ın default olarak 0'dan başlaması gerekiyor.

# Timer
time_counter = turtle.Turtle()
time_counter.hideturtle()
time_counter.penup()
time_counter.speed(0)
time_counter.goto(0,270)

sure = 60 # 60 saniye

# Kaplumbağamızı tanımlıyoruz
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("light green")
turtle_instance.penup()
turtle_instance.speed(1)
turtle_instance.shapesize(1.25)

# Kaplumbağa random yer değiştirme
def turtle_moving():
    turtle_instance.hideturtle()
    turtle_instance.setposition(randint(-250, 0), randint(0, 250))
    turtle_instance.showturtle()

# Scoreboard'u her puan alındığından güncellenmesi için gereken fonksiyon
def update_scoreboard():
    global point
    scoreboard.clear()
    scoreboard.write(f"Your point: {point}", align="center", font=("Courier", 24, "bold"))

# Time counter'ı yazdıran fonksiyon
def update_time_counter():
    time_counter.clear()
    time_counter.write(f"Time left: {sure}", align="center", font=("Courier", 24, "bold"))

# Timer'ı her saniye 1 azaltan fonksiyon
def countdown_timer():
    global sure
    if sure > 0: # Süre 0'dan büyükse
        sure -= 1 # Süreyi 1 azalt
        update_time_counter() # Sayacı ekranda güncelle
        turtle_moving()  # Kaplumbağa random bir yere ışınla
        turtle_screen.ontimer(countdown_timer, 1000) # 1 saniye (1000 milisaniye) sonra countdown_timer() fonksiyonunu tekrar çağır

    else:
        time_counter.clear() # Sayacı temizle
        time_counter.write("Süre Doldu! Oyun Bitti", align="center", font=("Courier", 24, "bold")) # Oyun bitti mesajı yazdır
        turtle_instance.hideturtle() # Oyun bitince kaplumbağayı gizle

# Puan arttığında point değişkenine 1 puan eklenir ve update_scoreboard() fonksiyonu çağrılır.
def up_points(x, y): # x ve y tıklama koordinatları(kullanılmasa bile gerekli)
    global point

    turtle_position = turtle_instance.position() # Kaplumbağanın pozisyonu tuple olarak alınır (x, y)
    turtle_radius = 25 # Kaplumbağanın yarı çapı

    # Ekranda tıklanılan yerin koordinatı ile kaplumbağının merkezi arasındaki mesafe
    mesafe = math.sqrt(math.pow(x - turtle_position[0], 2) + math.pow(y - turtle_position[1],2))

    """
    print(turtle_position)
    print(x, y)
    print(f"mesafe {mesafe}")
    """

    if mesafe <= turtle_radius:
        point += 1
        update_scoreboard()
        print("Clicked to Turtle")
        turtle_instance.hideturtle() # Tıklanınca kaplumbağayı sakla
    else:
        print("Not Clicked to Turtle")



turtle.listen()

update_scoreboard() # Başlangıç scoreboard'u yazdırır
update_time_counter() # Başlangıçta zaman sayacını ekrana yazdırır
countdown_timer() # Geri sayımı başlatır

turtle_screen.onscreenclick(up_points) # tıklandığı yerin koordinat bilgisini alır


turtle.mainloop()
#turtle.exitonclick()