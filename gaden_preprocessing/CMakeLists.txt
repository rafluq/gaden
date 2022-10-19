cmake_minimum_required(VERSION 2.8.3)
project(gaden_preprocessing)

set(CMAKE_CXX_FLAGS "-std=c++11 -fopenmp ${CMAKE_CXX_FLAGS}")

# set(CMAKE_BUILD_TYPE Debug) 
# set(CMAKE_CXX_FLAGS_RELEASE "-O3 -Wall -fPIC")
# set(CMAKE_CXX_FLAGS_DEBUG "-O0 -g")

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

find_package(Eigen3 REQUIRED)

catkin_package(
    DEPENDS roscpp std_msgs EIGEN3
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${EIGEN_INCLUDE_DIRS}
)

add_executable(preprocessing src/preprocessing.cpp)
add_dependencies(preprocessing ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(preprocessing
   ${catkin_LIBRARIES}
)
