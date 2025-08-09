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
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/docs/ReadMe.md#L1

### `docs/UI (Interface)/Main Menu`
Main Menu:
> `Main Menu:`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/docs/UI (Interface)/Main Menu#L1

### `docs/UI (Interface)/Sub Menu (Select Mode)`
Sub Menu (After hitting Play Button in Main Menu):
> `Sub Menu (After hitting Play Button in Main Menu):`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/docs/UI (Interface)/Sub Menu (Select Mode)#L1

### `docs/assets/asset_guidelines.md`
# Asset Guidelines
> `# Asset Guidelines`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/docs/assets/asset_guidelines.md#L1

### `docs/code_map.md`
Documentation.

### `docs/inspirations/ideas`
Inspirations:
> `Inspirations:`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/docs/inspirations/ideas#L1

### `docs/mechanics/General Premise`
General Functionality and Purpose of Game:
> `General Functionality and Purpose of Game:`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/docs/mechanics/General Premise#L1

### `docs/shop/Shop Community`
Shop Community:
> `Shop Community:`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/docs/shop/Shop Community#L1

### `docs/world/generation.md`
# World Generation
> `# World Generation`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/docs/world/generation.md#L1

### `docs/world/world_requirements.md`
# World Requirements
> `# World Requirements`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/docs/world/world_requirements.md#L1

### `include/README.md`
This directory will contain the project's header files.
> `This directory will contain the project's header files.`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/include/README.md#L1

### `include/zombie_viewer.h`
pragma once include <string>
> `#pragma once`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/include/zombie_viewer.h#L1-L2

### `src/CMakeLists.txt`
find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)
> `find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/src/CMakeLists.txt#L1

### `src/README.md`
This directory will contain the project's source files.
> `This directory will contain the project's source files.`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/src/README.md#L1

### `src/main.cpp`
include "zombie_viewer.h"
> `#include "zombie_viewer.h"`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/src/main.cpp#L1

### `src/zombie_viewer.cpp`
include "zombie_viewer.h" include <SFML/Graphics.hpp>
> `#include "zombie_viewer.h"`  
> https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/src/zombie_viewer.cpp#L1-L2

## Cross-references (`#include "..."`)

- `src/main.cpp` ➜ `zombie_viewer.h`  
  > `#include "zombie_viewer.h"`  
  > https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/src/main.cpp#L1
- `src/zombie_viewer.cpp` ➜ `zombie_viewer.h`  
  > `#include "zombie_viewer.h"`  
  > https://github.com/ProgrammingWithYagle/Zombie-Survival-2.0/blob/5a8186664cb5808d4b1b04ea62afce649192ecc7/src/zombie_viewer.cpp#L1

## TODO / FIXME

_No TODO/FIXME found._
