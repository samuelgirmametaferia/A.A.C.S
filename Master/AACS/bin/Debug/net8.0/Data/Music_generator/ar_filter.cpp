#include <GL/glut.h>
#include <opencv2/opencv.hpp>

// ... (OpenGL and OpenCV setup)

void display() {
  // ... (Render scene with 3D models)
}

int main(int argc, char** argv) {
  glutInit(&argc, argv);
  // ... (Initialize OpenGL and OpenCV)
  glutDisplayFunc(display);
  glutMainLoop();
  return 0;
}