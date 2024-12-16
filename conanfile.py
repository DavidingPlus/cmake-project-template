from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMakeToolchain


class ExampleRecipe(ConanFile):
    name = "cmake-project"
    description = "C/C++ 项目的 CMake 模板。"
    languages = "C++"
    author = "DavidingPlus"
    homepage = "https://github.com/DavidingPlus/cmake-project-template"

    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    def requirements(self):
        self.requires("gtest/1.12.1")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.presets_prefix = "cmake-project"
        tc.generate()
