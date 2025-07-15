# Zombie-Survival-2.0
A zombie survival game that is a revamp of my unfinished Scratch project.

Everyone is welcome to contribute to this project.

Here is the general premise of the project:

- **Art:** 2D Pixel
- **Code:** Can be written manually or with AI assistance
- **Language:** Mainly C++
- **Library:** SFML
- **Preferrable IDE** Visual Studio

## Prerequisites

Before building, make sure you have the following installed:

- A C++17 compatible compiler
- CMake 3.10 or newer
- [SFML](https://www.sfml-dev.org/) 2.5 or newer

## Building

```bash
mkdir build
cd build
cmake ..
cmake --build .
```

## Testing

After the project is built, the automated tests can be executed with CTest:

```bash
ctest --test-dir build
```

## Running

After building, the executable will be placed inside the `build` directory. Run it from the **project root** so the assets folder can be located:

```bash
./ZombieSurvival
```
This will launch a window displaying the sample zombie sprite scaled to 64x64 pixels and centered in the window.

## Coding Conventions

Please see [AGENTS.md](AGENTS.md) for coding conventions and contribution guidelines.

This repository follows the standard C++ layout with source files in `src/` and header files in `include/`.

For sprite size and spritesheet layout recommendations, see [docs/asset_guidelines.md](docs/assets/asset_guidelines.md).

## Branch Protection

This repository includes a branch protection ruleset located at
`.github/rulesets/main-branch-protection.yml`. The ruleset enforces pull
requests and requires the CI workflow to pass before changes can be merged into
the `main` branch.

To enable these rules in your fork, import the YAML file into the **Rulesets**
section of your repository settings on GitHub.
