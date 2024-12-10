#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
#include <queue>

using namespace cv;
using namespace std;

struct Node {
  int x, y;
  double cost;
  Node* parent;
};

vector<vector<int>> createGrid(Mat image) {
  // ... Implement grid creation logic ...
}

vector<Node*> findPath(vector<vector<int>> grid, Point start, Point end) {
  priority_queue<Node*, vector<Node*>, greater<Node*>> openList;
  vector<vector<bool>> closedList(grid.size(), vector<bool>(grid[0].size(), false));

  Node* startNode = new Node{start.x, start.y, 0, nullptr};
  openList.push(startNode);

  while (!openList.empty()) {
    Node* current = openList.top();
    openList.pop();

    if (current->x == end.x && current->y == end.y) {
      vector<Node*> path;
      Node* node = current;
      while (node != nullptr) {
        path.push_back(node);
        node = node->parent;
      }
      reverse(path.begin(), path.end());
      return path;
    }

    closedList[current->y][current->x] = true;

    // ... Implement neighbor exploration and pathfinding logic ...
  }

  return {};
}

int main() {
  Mat image = imread("indoor_map.jpg");
  vector<vector<int>> grid = createGrid(image);

  Point start = {10, 10};
  Point end = {50, 50};

  vector<Node*> path = findPath(grid, start, end);

  // ... Process and visualize the path ...

  return 0;
}