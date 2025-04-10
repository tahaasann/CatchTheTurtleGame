import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch The Turtle")
FONT = ('Arial',30,'normal')
score = 0
game_over = False

turtle_list = [] # Turtle List

#score_turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()

#make turtle properties
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10,20]
grid_size = 10

# Scoreboard'un oluşturulması
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85

    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

# Turtle oluşturma fonksiyonu
def make_turtle(x, y):
    t = turtle.Turtle()

    # turtle oluşturma ve tıkladığımız yerin koordinatını tutan fonksiyon
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)
        # print(x, y)

    t.onclick(handle_click)

    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)

# Turtles oluştururken kullanılan verdiğimiz liste elemanlarına göre koordinatlar çerçevesinde turtle oluşturan fonksiyon
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

# 5 * 4 ızgara formunda turtle oluşturduğumuz için hiçbirinin görünmemesi adına gizleriz. Sonra show_turtles_randomly() fonksiyonu ile birlikte random bir tanesini seçip gösteririz.
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function -> bir fonksiyonun içerisinde kendisini çağırmak
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

# Zamanlayıcının konumu, her saniye güncellenmesi ve süre bitince Game Over! yazmasını içeren fonksiyonumuz
def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.85

    countdown_turtle.setposition(0, y-50)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)

# Tüm yazdığımız fonksiyonların derli toplu tutulduğu bir başka fonksiyon
def start_game_up():
    turtle.tracer(0) # Animasyonu kapatır
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1) # Animasyonu açar



start_game_up()
turtle.mainloop()