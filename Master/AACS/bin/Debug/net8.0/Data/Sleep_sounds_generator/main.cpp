#include <SFML/Graphics.hpp>

int main()
{
    sf::RenderWindow window(sf::VideoMode(800, 600), "Simple Platformer");

    // ... (Add game logic, sprites, etc.)

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // ... (Update game state, handle input)

        window.clear();
        // ... (Draw game elements)
        window.display();
    }

    return 0;
}