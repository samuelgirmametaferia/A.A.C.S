#include <iostream>
#include <vector>
#include <queue>

struct Node {
  int x, y;
  int cost;
  Node* parent;
};

int calculateHeuristic(Node* current, Node* goal) {
  return abs(current->x - goal->x) + abs(current->y - goal->y);
}

std::vector<Node*> findPath(std::vector<std::vector<int>>& map, Node* start, Node* goal) {
  std::priority_queue<Node*, std::vector<Node*>, std::function<bool(Node*, Node*)>> openList(
    [](Node* a, Node* b) { return a->cost + calculateHeuristic(a, goal) > b->cost + calculateHeuristic(b, goal); }
  );

  openList.push(start);

  while (!openList.empty()) {
    Node* current = openList.top();
    openList.pop();

    if (current->x == goal->x && current->y == goal->y) {
      std::vector<Node*> path;
      while (current != nullptr) {
        path.push_back(current);
        current = current->parent;
      }
      return path;
    }

    // Explore neighbors
  }

  return {};
}

int main() {
  // Load map data
  std::vector<std::vector<int>> map = {
    {1, 1, 1, 1, 1},
    {1, 0, 0, 0, 1},
    {1, 0, 1, 0, 1},
    {1, 0, 0, 0, 1},
    {1, 1, 1, 1, 1}
  };

  Node* start = {0, 0, 0, nullptr};
  Node* goal = {4, 4, 0, nullptr};

  std::vector<Node*> path = findPath(map, start, goal);

  // ... Use the path for navigation in Unity ...
  return 0;
}