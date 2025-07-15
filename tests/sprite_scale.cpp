#include "asset_config.h"
#include <SFML/Graphics.hpp>
#include <iostream>

int main() {
    // Use sf::Image to avoid opening a window while still retrieving the
    // dimensions of the sprite sheet.
    sf::Image image;
    if (!image.loadFromFile(ASSET_PATH)) {
        std::cerr << "Failed to load zombie sprite\n";
        return 1;
    }
    const float target_size = 64.0f;
    sf::Vector2u tex_size = image.getSize();
    float scale_x = target_size / tex_size.x;
    float scale_y = target_size / tex_size.y;

    // After scaling, the sprite should be exactly 64x64 pixels.
    if (static_cast<int>(tex_size.x * scale_x) != 64 ||
        static_cast<int>(tex_size.y * scale_y) != 64) {
        std::cerr << "Incorrect sprite size\n";
        return 1;
    }
    return 0;
}
