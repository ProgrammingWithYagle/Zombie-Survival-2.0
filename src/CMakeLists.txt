find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)

add_executable(ZombieSurvival
    main.cpp
    zombie_viewer.cpp
)

target_include_directories(ZombieSurvival PUBLIC ${PROJECT_SOURCE_DIR}/include)

target_link_libraries(ZombieSurvival PRIVATE sfml-graphics sfml-window sfml-system)
