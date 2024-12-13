cmake_minimum_required (VERSION 3.12)

set (CMAKE_CXX_STANDARD 11)
set (CMAKE_CXX_STANDARD_REQUIRED true)

project ("CMake Project")

# configure compiler cross platform
if (CMAKE_HOST_WIN32)
    include (config-win32.cmake)

elseif (CMAKE_HOST_UNIX)
    include (config-unix.cmake)

else ()
    message (FATAL_ERROR "Unknown platform")

endif ()


# configure output dir of static and shared library
include (GNUInstallDirs)
set (CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR}")
set (CMAKE_LIBRARY_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_LIBDIR}")

# configure targets
set (DIR_SRC_ROOT "${PROJECT_SOURCE_DIR}/src")

include_directories (${DIR_SRC_ROOT})

option (BUILD_SHARED_LIBS "Build using shared libraries" ON)

aux_source_directory (${DIR_SRC_ROOT} PROJECT_SOURCE_FILES)

add_library (cmakeproject ${PROJECT_SOURCE_FILES})
