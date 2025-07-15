enable_testing()
find_package(SFML 2.5 COMPONENTS graphics REQUIRED)

set(ASSET_PATH "${PROJECT_SOURCE_DIR}/assets/images/zombie/normal zombie/variation 1/Normal Zombie Sprite (Model).png")
configure_file(asset_config.h.in ${CMAKE_CURRENT_BINARY_DIR}/asset_config.h @ONLY)

add_executable(asset_load_test asset_load.cpp)
target_include_directories(asset_load_test PUBLIC ${PROJECT_SOURCE_DIR}/include ${CMAKE_CURRENT_BINARY_DIR})
target_link_libraries(asset_load_test PRIVATE sfml-graphics)

add_test(NAME asset_load COMMAND asset_load_test)

add_executable(sprite_scale_test sprite_scale.cpp)
target_include_directories(sprite_scale_test PUBLIC ${PROJECT_SOURCE_DIR}/include ${CMAKE_CURRENT_BINARY_DIR})
target_link_libraries(sprite_scale_test PRIVATE sfml-graphics)

add_test(NAME sprite_scale COMMAND sprite_scale_test)
