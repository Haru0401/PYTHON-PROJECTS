import turtle

def draw_smile(emo):
    emo.penup()
    emo.goto(-60, -20)
    emo.setheading(-60)
    emo.pendown()
    emo.width(5)
    emo.circle(60, 120)

def draw_angry(emo):
    # Draw frown
    emo.penup()
    emo.goto(0, 25)
    emo.pendown()
    emo.circle(-100, 80)

    emo.penup()
    emo.setheading(180)
    emo.goto(0, 25)
    emo.pendown()
    emo.circle(100, 80)

def draw_love(emo):
    emo.penup()
    emo.goto(0, -50)
    emo.pendown()
    emo.color('red')
    emo.begin_fill()
    emo.fillcolor('red')
    emo.left(140)
    emo.forward(180)
    emo.circle(-90, 200)
    emo.setheading(60)
    emo.circle(-90, 200)
    emo.forward(180)
    emo.end_fill()

def draw_emoji(face_color, expression):
    emo = turtle.Turtle()
    emo.speed(2)

    # Draw the face
    emo.penup()
    emo.goto(0, -100)
    emo.pendown()
    emo.begin_fill()
    emo.fillcolor(face_color)
    emo.circle(100)
    emo.end_fill()

    # Draw the eyes
    for i in range(-35, 70, 70):
        emo.penup()
        emo.goto(i, 35)
        emo.pendown()
        emo.begin_fill()
        emo.circle(10)
        emo.end_fill()

    # Draw the mouth or expression based on input
    if expression == "smile":
        draw_smile(emo)
    elif expression == "angry":
        draw_angry(emo)
    elif expression == "love":
        draw_love(emo)

def main():
    face_color = input("Enter the face color (e.g., yellow, red, pink): ").strip().lower()
    expression = input("Enter the facial expression (smile, angry, love): ").strip().lower()
    
    if face_color not in ['yellow', 'red', 'pink']:
        print("Invalid color! Using default color: yellow")
        face_color = 'yellow'
    
    if expression not in ['smile', 'angry', 'love']:
        print("Invalid expression! Using default expression: smile")
        expression = 'smile'
    
    turtle.clearscreen()  # Clear the screen for each new emoji
    draw_emoji(face_color, expression)
    turtle.done()

main()
