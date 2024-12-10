import SpriteKit

class GameScene: SKScene {
  // ... (Game logic and UI elements)
  
  func handleTap(atPoint point: CGPoint) {
    // ... (Handle user interaction)
  }
}

let scene = GameScene(size: CGSize(width: 320, height: 480))
view?.presentScene(scene)