import turtle
import pandas
FONT = ("Courier", 7, "normal")

# To Get the Co ordinate of x and y on mouse click.
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
screen = turtle.Screen()
screen.title("U.S.State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data[data.state == "Alaska"])
user_score = 0
total_score = len(data.state.to_list())
states_location = {}
all_state = data.state.to_list()
for states in data.state:
    file = data[data.state == states]
    x = int(file.x)
    y = int(file.y)
    # print(x, y)
    states_location[states] = (x, y)

#print(states_location)

guessed_state = []

while len(guessed_state) < 50:
    # print(len(guessed_state))
    answer_state = screen.textinput(title=f"Guess the state. {user_score}/{total_score}", prompt="What's the another st"
                                                                                                 "ate's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_state = [n for n in all_state if n not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn")
        break
    if answer_state in states_location:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
            user_score += 1
            tim.goto(states_location[answer_state])
            tim.write(answer_state, font=FONT)



