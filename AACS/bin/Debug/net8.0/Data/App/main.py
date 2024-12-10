import random

class Obstacle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def collides_with(self, drone_x, drone_y):
        distance = ((drone_x - self.x)**2 + (drone_y - self.y)**2)**0.5
        return distance < self.radius

def generate_environment(width, height, num_obstacles):
    obstacles = []
    for _ in range(num_obstacles):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(5, 15)
        obstacles.append(Obstacle(x, y, radius))
    return obstacles

def a_star(grid, start, goal):
    # Implement A* pathfinding algorithm here
    pass

if __name__ == '__main__':
    width = 100
    height = 100
    num_obstacles = 10
    environment = generate_environment(width, height, num_obstacles)
    start_position = (0, 0)
    goal_position = (width - 1, height - 1)
    path = a_star(environment, start_position, goal_position)
    print(path)