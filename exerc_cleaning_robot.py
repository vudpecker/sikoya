import random

class CleaningRobot:
    def __init__(self, grid_width, grid_height):
        self.grid = [[0] * grid_width for _ in range(grid_height)]
        self.x = random.randint(0, grid_width - 1)
        self.y = random.randint(0, grid_height - 1)

    def move(self):
        # Randomly choose a direction (up, down, left, right)
        direction = random.choice(["up", "down", "left", "right"])

        # Update the robot's position based on the chosen direction
        if direction == "up" and self.y > 0:
            self.y -= 1
        elif direction == "down" and self.y < len(self.grid) - 1:
            self.y += 1
        elif direction == "left" and self.x > 0:
            self.x -= 1
        elif direction == "right" and self.x < len(self.grid[0]) - 1:
            self.x += 1

        # Clean the cell
        self.grid[self.y][self.x] = 1

    def display_grid(self):
        for row in self.grid:
            print(" ".join(["X" if cell == 1 else "_" for cell in row]))

def main():
    grid_width = 5
    grid_height = 5
    robot = CleaningRobot(grid_width, grid_height)
    
    for _ in range(20):  # Move the robot 20 times (you can adjust this)
        robot.move()

    robot.display_grid()

if __name__ == "__main__":
    main()
