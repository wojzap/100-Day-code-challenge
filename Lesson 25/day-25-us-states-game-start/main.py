import turtle
import pandas as pd
image = "blank_states_img.gif"

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("Name the States")
screen.addshape(image)
turtle.shape(image)



states_data = pd.read_csv("50_states.csv")
states = states_data.state



turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.speed("fastest")


correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)} / 50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states.unique() and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        state = states_data[states == answer_state]
        x_cor = state.x
        y_cor = state.y
        turtle.goto(int(x_cor), int(y_cor))
        turtle.write(f"{answer_state}", move=False, align="center", font=("Arial", 10, "normal"))

list_of_states = states_data.state.tolist()
for answer in correct_answers:
    if answer in list_of_states:
        list_of_states.remove(answer)

print(list_of_states)


data = pd.DataFrame(list_of_states)
data.to_csv("States_to_learn.csv")



