#include "zombie_viewer.h"
#include <SFML/Graphics.hpp>

// Opens an SFML window and displays the provided sprite until the window is closed.
void run_zombie_viewer(const std::string& sprite_path) {
    sf::RenderWindow window(sf::VideoMode(512, 512), "Zombie Sprite Viewer");
    sf::Texture texture;
    if (!texture.loadFromFile(sprite_path)) {
        // Failed to load the texture; exit early
        return;
    }
    sf::Sprite sprite(texture);

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }
        window.clear(sf::Color::Black);
        window.draw(sprite);
        window.display();
    }
}
