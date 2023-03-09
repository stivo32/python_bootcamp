import os.path
import random
import tkinter

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

if os.path.exists('words_to_learn.csv'):
    words_df: pd.DataFrame = pd.read_csv('words_to_learn.csv')
else:
    words_df: pd.DataFrame = pd.read_csv('data/french_words.csv')
to_learn = words_df.to_dict(orient='records')


def main():
    # make simple tkinter window
    current_card = {}
    after_id = None

    def next_card():
        nonlocal current_card, after_id
        window.after_cancel(after_id)
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_title, text='French', fill="black")
        canvas.itemconfig(card_word, text=current_card['French'], fill="black")
        canvas.itemconfig(image, image=card_front_img)
        after_id = window.after(3000, func=flip_card)

    def flip_card():
        canvas.itemconfig(card_title, text='English', fill="white")
        canvas.itemconfig(card_word, text=current_card['English'], fill="white")
        canvas.itemconfig(image, image=card_back_img)

    def is_known():
        to_learn.remove(current_card)
        next_card()

    window = tkinter.Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    after_id = window.after(3000, func=flip_card)

    canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_front_img = tkinter.PhotoImage(file="images/card_front.png")
    card_back_img = tkinter.PhotoImage(file="images/card_back.png")
    image = canvas.create_image(400, 263, image=card_front_img)
    card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="white")
    card_word = canvas.create_text(400, 250, text='Word', font=("Ariel", 60, "bold"), fill="white")
    canvas.grid(column=0, row=0, columnspan=2)

    right_img = tkinter.PhotoImage(file="images/right.png")
    right_button = tkinter.Button(image=right_img, highlightthickness=0, command=is_known)
    right_button.grid(column=1, row=1)

    left_img = tkinter.PhotoImage(file="images/wrong.png")
    left_button = tkinter.Button(image=left_img, highlightthickness=0, command=next_card)
    left_button.grid(column=0, row=1)

    next_card()
    window.mainloop()

    pd.DataFrame(to_learn).to_csv('words_to_learn.csv', index=False)


if __name__ == '__main__':
    main()
