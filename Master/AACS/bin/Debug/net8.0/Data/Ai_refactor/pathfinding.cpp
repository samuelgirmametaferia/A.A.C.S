#include <iostream>
#include <vector>
#include <queue>

struct Node {
  int x, y;
  int gCost, hCost;
  Node* parent;
};

int calculateHeuristic(Node* node, Node* target) {
  return abs(node->x - target->x) + abs(node->y - target->y);
}

std::vector<Node*> findPath(std::vector<std::vector<int>>& grid, Node* start, Node* target) {
  std::priority_queue<Node*, std::vector<Node*>, std::function<bool(Node*, Node*)>> openList(
      [](Node* a, Node* b) { return a->gCost + a->hCost > b->gCost + b->hCost; });
  std::vector<std::vector<bool>> visited(grid.size(), std::vector<bool>(grid[0].size(), false));

  start->gCost = 0;
  start->hCost = calculateHeuristic(start, target);
  openList.push(start);

  while (!openList.empty()) {
    Node* current = openList.top();
    openList.pop();

    if (current == target) {
      std::vector<Node*> path;
      while (current != nullptr) {
        path.push_back(current);
        current = current->parent;
      }
      std::reverse(path.begin(), path.end());
      return path;
    }

    visited[current->x][current->y] = true;

    for (int dx = -1; dx <= 1; dx++) {
      for (int dy = -1; dy <= 1; dy++) {
        if (dx == 0 && dy == 0) continue;
        int nx = current->x + dx;
        int ny = current->y + dy;
        if (nx < 0 || nx >= grid.size() || ny < 0 || ny >= grid[0].size() || grid[nx][ny] == 1 || visited[nx][ny]) continue;

        Node* neighbor = new Node{nx, ny, 0, 0};
        neighbor->parent = current;
        neighbor->gCost = current->gCost + 1;
        neighbor->hCost = calculateHeuristic(neighbor, target);
        openList.push(neighbor);
      }
    }
  }

  return {};
}

int main() {
  std::vector<std::vector<int>> grid = {
    {0, 0, 0, 0, 0},
    {0, 1, 0, 1, 0},
    {0, 0, 0, 0, 0},
    {0, 1, 1, 1, 0},
    {0, 0, 0, 0, 0}
  };

  Node* start = new Node{0, 0, 0, 0};
  Node* target = new Node{4, 4, 0, 0};

  std::vector<Node*> path = findPath(grid, start, target);

  for (Node* node : path) {
    std::cout << "(" << node->x << ", " << node->y << ")" << std::endl;
  }

  return 0;
}