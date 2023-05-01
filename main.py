
import turtle
import pandas

t = turtle.Turtle()
t.penup()
t.hideturtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)                     #creating a shape to add new image
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        data = pandas.DataFrame(missing_states)
        data.to_csv("States_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        row = data[data["state"] == answer_state]
        t.goto(int(row.x), int(row.y))
        t.write(answer_state)






# def get_mouse_click_coor(x, y):             #get the coordinates wherever you click
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()                          #alternative to exitonclick(), keeps screen open even when the code has finish running.
