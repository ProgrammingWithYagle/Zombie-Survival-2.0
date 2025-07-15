#include "asset_config.h"
#include <SFML/Graphics.hpp>
#include <iostream>

#ifndef ASSET_PATH
#error "ASSET_PATH not defined"
#endif

int main() {
    const char* sprite_path = ASSET_PATH;
    sf::Image image;
    if (!image.loadFromFile(sprite_path)) {
        std::cerr << "Failed to load zombie sprite\n";
        return 1;
    }
    return 0;
}
