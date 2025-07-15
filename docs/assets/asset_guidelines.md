# Asset Guidelines

This document outlines best practices for preparing sprites and tiles for Zombie-Survival-2.0.

## Resolution
**NOTE**: The Pixels here are actual pixels (the number of pixels actually being represented on a displaying monitor)
- All images have a resolution of 1024 * 1024 pixels (physical pixels), unless stated otherwise

## Sprite Tile Size

**NOTE**: The Pixels here are logical pixels (or art pixels), in which the pixels here representing a unit within the drawing (not the actual number of pixels being displayed on a monitor)
- Use **64×64 pixel** (logical or art pixels) tiles for most sprites.
- Spread Sheet Size: **512 * 512 pixels** (logical or art pixels)
- Keep every frame or object within a 64×64 pixel box.

## Spritesheet Layout

- Arrange sprites in a grid of uniform rows and columns.
- Reserve a small amount of empty space (1–2 pixels) between tiles to prevent bleeding when rendering.
- Keep consistent padding around the edges of the spritesheet as well.

Following these guidelines makes it easier to load graphics consistently and keeps animation frames aligned.
