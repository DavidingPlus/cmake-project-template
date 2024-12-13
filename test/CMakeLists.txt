message ("-- Checking if GoogleTest is installed ...")

find_package (GTest REQUIRED)
if (NOT GTest_FOUND)
    message (WARNING "-- GoogleTest not installed")
    return ()

endif ()

include (GoogleTest)


aux_source_directory (${CMAKE_CURRENT_SOURCE_DIR} SRC_GTEST)
add_executable (gtest_testrun EXCLUDE_FROM_ALL ${SRC_GTEST})
target_link_libraries (gtest_testrun gtest gtest_main cmakeproject)

add_custom_target (tests)
add_dependencies (tests gtest_testrun)


message ("-- Done configuring gtest")
