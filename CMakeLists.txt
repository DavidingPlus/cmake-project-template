cmake_minimum_required (VERSION 3.23)

set (CMAKE_CXX_STANDARD 11)
set (CMAKE_CXX_STANDARD_REQUIRED true)

project ("CMake Project")


# configue included headers
set (DIR_SRC_ROOT "${PROJECT_SOURCE_DIR}/src")
include_directories (${DIR_SRC_ROOT})

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
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/${CMAKE_INSTALL_BINDIR}")

# configure targets
aux_source_directory (${DIR_SRC_ROOT} PROJECT_SOURCE_FILES)
add_library (cmake-project ${PROJECT_SOURCE_FILES})

unset (CMAKE_ARCHIVE_OUTPUT_DIRECTORY)
unset (CMAKE_LIBRARY_OUTPUT_DIRECTORY)
unset (CMAKE_RUNTIME_OUTPUT_DIRECTORY)


# configure snippet
add_subdirectory ("snippet")


# configure unit test
option (WITH_GTEST "Enable unit tests by GoogleTest" OFF)

if (WITH_GTEST)
    message ("-- Unit test by GoogleTest is enabled")

else ()
    message ("-- Unit test by GoogleTest is disabled")

endif ()

if (WITH_GTEST)
    add_subdirectory (test)

endif ()
