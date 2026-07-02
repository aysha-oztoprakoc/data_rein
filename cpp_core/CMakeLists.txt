cmake_minimum_required(VERSION 3.20)
project(data_rein_cpp_core VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# PON Compliance: Strict warnings
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror -Wpedantic")

# Find Paho MQTT (DYSKORDIA integration)
find_package(PahoMqttCpp REQUIRED)

add_executable(pon_engine src/main.cpp)
target_link_libraries(pon_engine PahoMqttCpp::paho-mqttpp3 PahoMqttC::paho-mqtt3as)
