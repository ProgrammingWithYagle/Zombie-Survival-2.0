# Code Map (auto-generated)

**Do not edit by hand. Run `make codemap` to regenerate.**

## File tree (docs / include / src)
```
docs/
include/
src/
  UI (Interface)/
  assets/
  inspirations/
  mechanics/
  shop/
  world/
  ReadMe.md
  code_map.md
    Main Menu
    Sub Menu (Select Mode)
    asset_guidelines.md
    ideas
    General Premise
    Shop Community
    generation.md
    world_requirements.md
  README.md
  zombie_viewer.h
  CMakeLists.txt
  README.md
  main.cpp
  zombie_viewer.cpp
```

## Responsibilities

### `docs/ReadMe.md`
Here is the area where all the ideas and features for the game would be.
> `Here is the area where all the ideas and features for the game would be.`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/980151f2301bc27d46df660797d3b324db5b0493/docs/ReadMe.md#L1

### `docs/UI (Interface)/Main Menu`
Main Menu:
> `Main Menu:`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/d96ee7caa8ad4c9448323c90da7cf87d359ddfd6/docs/UI%20%28Interface%29/Main%20Menu#L1

### `docs/UI (Interface)/Sub Menu (Select Mode)`
Sub Menu (After hitting Play Button in Main Menu):
> `Sub Menu (After hitting Play Button in Main Menu):`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a4961f349603033f372c35684bda7e4322dc27d/docs/UI%20%28Interface%29/Sub%20Menu%20%28Select%20Mode%29#L1

### `docs/assets/asset_guidelines.md`
# Asset Guidelines
> `# Asset Guidelines`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/4599768db1549c182f1b998ae84fcd166dbaf507/docs/assets/asset_guidelines.md#L1

### `docs/code_map.md`
Documentation.

### `docs/inspirations/ideas`
Inspirations:
> `Inspirations:`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/a76d78e0af0a31c0d17d5982c489433b63d93794/docs/inspirations/ideas#L1

### `docs/mechanics/General Premise`
General Functionality and Purpose of Game:
> `General Functionality and Purpose of Game:`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/0b07116cc921a39d44de1175614ef9cb1505c71d/docs/mechanics/General%20Premise#L1

### `docs/shop/Shop Community`
Shop Community:
> `Shop Community:`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/10f576fb30d26541c82ef53299c18202998cd671/docs/shop/Shop%20Community#L1

### `docs/world/generation.md`
# World Generation
> `# World Generation`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/3e2c77e085e087f5a9fb79bea48184356f074129/docs/world/generation.md#L1

### `docs/world/world_requirements.md`
# World Requirements
> `# World Requirements`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/8e0ecac3dd09dcc928d44c159d3f0c166326661b/docs/world/world_requirements.md#L1

### `include/README.md`
This directory will contain the project's header files.
> `This directory will contain the project's header files.`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/fb2fdc58389ea7cc66f855dbc19834f2e410c66d/include/README.md#L1

### `include/zombie_viewer.h`
pragma once include <string>
> `#pragma once`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/f4adb5ee624ce4147977940139ef09b18128f15e/include/zombie_viewer.h#L1-L2

### `src/CMakeLists.txt`
find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)
> `find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/f4adb5ee624ce4147977940139ef09b18128f15e/src/CMakeLists.txt#L1

### `src/README.md`
This directory will contain the project's source files.
> `This directory will contain the project's source files.`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/fb2fdc58389ea7cc66f855dbc19834f2e410c66d/src/README.md#L1

### `src/main.cpp`
include "zombie_viewer.h"
> `#include "zombie_viewer.h"`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/f4adb5ee624ce4147977940139ef09b18128f15e/src/main.cpp#L1

### `src/zombie_viewer.cpp`
include "zombie_viewer.h" include <SFML/Graphics.hpp>
> `#include "zombie_viewer.h"`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/9e583a17e287537672f936ddb38caa3a65f1793f/src/zombie_viewer.cpp#L1-L2

## Cross-references (`#include "..."`)

- `src/main.cpp` ➜ `zombie_viewer.h`  
  > `#include "zombie_viewer.h"`  
  > https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/f4adb5ee624ce4147977940139ef09b18128f15e/src/main.cpp#L1
- `src/zombie_viewer.cpp` ➜ `zombie_viewer.h`  
  > `#include "zombie_viewer.h"`  
  > https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/9e583a17e287537672f936ddb38caa3a65f1793f/src/zombie_viewer.cpp#L1

## TODO / FIXME

_No TODO/FIXME found._
