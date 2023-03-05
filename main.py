import turtle

import pandas as pd


def main():
    states_data = pd.read_csv('50_states.csv')
    states = states_data['state'].to_list()
    states_count = len(states_data['state'])
    found_states_count = 0
    found_states = []

    screen = turtle.Screen()
    screen.title('U.S. States Game')
    image = 'blank_states_img.gif'
    screen.addshape(image)

    turtle.shape(image)

    while found_states_count < states_count:
        answer_state = screen.textinput(
            title=f'{found_states_count}/{states_count} States Correct', prompt='What\'s another state\'s name?'
        )
        if answer_state is None:
            continue
        answer_state = answer_state.title()
        if answer_state == 'Exit':
            break
        if answer_state not in states:
            continue

        index = states.index(answer_state)
        state_info = states_data.iloc[index]
        found_states_count += 1
        found_states.append(answer_state)
        x, y = state_info.x, state_info.y
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.setposition(x, y)
        t.write(answer_state, move=True, align='center', font=('Arial', 8, 'normal'))
    unfound_states = [state for state in states if state not in found_states]
    unfound_df = states_data[states_data['state'].isin(unfound_states)]
    unfound_df.to_csv('unfound_states.csv')


if __name__ == '__main__':
    main()
