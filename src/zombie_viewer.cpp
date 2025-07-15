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
    // Scale the sprite so that it fits within a 64x64 pixel box
    const float target_size = 64.0f;
    sf::Vector2u tex_size = texture.getSize();
    sprite.setScale(target_size / tex_size.x, target_size / tex_size.y);

    // Center the sprite in the window
    sprite.setPosition(
        (window.getSize().x - target_size) / 2.0f,
        (window.getSize().y - target_size) / 2.0f);

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
