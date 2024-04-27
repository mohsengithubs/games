from tkinter import *
import random

GAME_WIDTH = 800
GAME_HEIGHT = 800
SPACE_SIZE = 20
SPEED = 60
BODY_PARTS = 3
SNAKE_COLOR = "#264857"
FOOD_COLOR = "#123456"
BG_COLOR = "#567890"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            squares = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake"
            )
            self.squares.append(squares)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food"
        )


def next_turn(snake, food):
    global score
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE

    snake.coordinates.insert(0, [x, y])

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake"
    )

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="score: {}".format(score))
        canvas.delete("food")

        food = Food()
    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_colisions(snake):
        game_over()
    else:
        root.after(SPEED, next_turn, snake, food)


def change_direction(new_directions):
    global direction

    if direction == "right":
        if direction != "left":
            direction = new_directions

    if direction == "left":
        if direction != "right":
            direction = new_directions

    if direction == "up":
        if direction != "down":
            direction = new_directions

    if direction == "down":
        if direction != "up":
            direction = new_directions



def check_colisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body_parts in snake.coordinates[1:]:
        if x == body_parts[0] and y == body_parts[1]:
            return True
    return False



def game_over():
    canvas.delete(all)
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font=("consolas", 70),
        text=("GAME OVER"),
        fill="red",
    )


root = Tk()
root.title("snake game")

score = 0

direction = "down"

label = Label(root, text="score: {}".format(score), font=("Arial", 40),bg=BG_COLOR)
label.pack()

canvas = Canvas(root, bg=BG_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()
root.configure(bg=BG_COLOR)
root.update()

root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (root_width / 2))
y = int((screen_height / 2) - (root_height / 2))


root.geometry(f"{root_width}x{root_height}+{x}+{y}")

root.bind("<Right>", lambda event: change_direction("right"))
root.bind("<Left>", lambda event: change_direction("left"))
root.bind("<Up>", lambda event: change_direction("up"))
root.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)
root.mainloop()