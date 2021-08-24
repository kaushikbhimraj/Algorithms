"""
Design a Snake game that is played on a device with screen size = width x height. Play the game 
online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length 
and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the 
first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied 
by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears 
at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)
"""
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width - 1
        self.height = height - 1
        self.food = food
        self.snake = [[0,0]]
        self.body = set()
        self.body.add((0,0))
        self.score = 0

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        head_row, head_col = self.snake[0]
        
        if direction == "U":
            if head_row - 1 < 0:
                return -1
            if self.food and [head_row - 1, head_col] == self.food[0]:
                return self.growSnake()
            else:
                return self.moveSnake(head_row - 1, head_col)
            
        if direction == "D":
            if head_row + 1 > self.height:
                return -1
            if self.food and [head_row + 1, head_col] == self.food[0]:
                return self.growSnake()
            else:
                return self.moveSnake(head_row + 1, head_col)
        
        if direction == "L":
            if head_col - 1 < 0:
                return -1
            if self.food and [head_row, head_col - 1] == self.food[0]:
                return self.growSnake()
            else:
                return self.moveSnake(head_row, head_col - 1)
        
        if direction == "R":
            if head_col + 1 > self.width:
                return -1
            if self.food and [head_row, head_col + 1] == self.food[0]:
                return self.growSnake()
            else:
                return self.moveSnake(head_row, head_col + 1)
                
    # Since food will never on snakes body, no need to check the new head's location. 
    def growSnake(self):
        temp = self.food.pop(0)
        self.snake = [temp] + self.snake
        self.body.add((temp[0], temp[1]))
        return len(self.snake) - 1
    
    # Before adding a new head remove the tail and check if new head is colliding 
    # with the snake's body.
    def moveSnake(self, row, col):
        temp = self.snake.pop() 
        self.body.remove((temp[0], temp[1]))
        
        if (row, col) in self.body:
            return -1
        self.snake = [[row, col]] + self.snake
        self.body.add((row, col))
        return len(self.snake) - 1
        
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)