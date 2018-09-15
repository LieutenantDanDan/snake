import random
import time
class Snake:


    snake = []
    board = []
    width = 0
    height = 0
    food = (None, None)

    def __init__(self, height, width):
        random.seed(555)

        self.height = height
        self.width = width

        for i in range(height):
            self.board.append([' '] * width)

        self.snake.append((random.randrange(width), random.randrange(height)))

        self.food = (random.choice([x for i, x in enumerate(range(height)) if i != self.snake[0][1]]),random.choice([x for i, x in enumerate(range(height)) if i != self.snake[0][0]]) )

        self.board[self.snake[0][1]][self.snake[0][0]] = 's'
        self.board[self.food[1]][self.food[0]] = 'f'

    def __str__(self):
        string = '-' * (self.width + 2) + '\n'
        for line in self.board:
            string += '|'
            string += ''.join(line)
            string += '|\n'

        string += '-' * (self.width + 2)

        return string

    def update_board(self):
        board = []
        for i in range(self.height):
            board.append([' '] * self.width)

        for segments in self.snake:
            board[segments[1]][segments[0]] = 's'

        board[self.food[1]][self.food[0]] = 'f'
        self.board = board

    def next_state(self, new_head):
        if self.game_over(new_head):
            print('uh oh! snake ded')
            return False

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.new_food()
        else:
            self.snake.pop()

        print(self.snake)

        self.update_board()

        return True

    def trigger_move(self, direction):
        if direction not in list(self.directions().keys()):
            print("invalid move!")
            return True

        new_head = self.move(direction)

        return self.next_state(new_head)

    def random_move(self):
        direction = random.choice(list(self.directions().keys()))
        print("randomly moving " + direction)
        new_head = self.move(direction)
        return self.next_state(new_head)


    def directions(self):
        return {
            'up': (0, -1),
            'down': (0, +1),
            'left': (-1, 0),
            'right': (1, 0),
            'w': (0, -1),
            's': (0, +1),
            'a': (-1, 0),
            'd': (1, 0)
        }

    def move(self, direction):
        head = self.snake[0]
        return (head[0] + self.directions()[direction][0], head[1] + self.directions()[direction][1])

    def game_over(self, new_head):
        if new_head in self.snake:
            return True
        if new_head[0] < 0 or new_head[1] <  0:
            return True

        if new_head[0] > self.width or new_head[1] > self.height:
            return True
        return False

    def new_food(self):
        valid = []

        for i in range(self.width):
            for j in range(self.height):
                valid.append((i, j))

        valid = set(valid)
        snake = set(self.snake)
        valid = valid - snake

        self.food = random.choice(list(valid))


    def eat_block(self):


        return


if __name__ == "__main__":
    s = Snake(10, 20)
    print(s)
    print(s.snake)

    play = True
    while play:
        direction = input()
        print("you input: " + str(direction))
        play = s.trigger_move(direction)
        print(s)
