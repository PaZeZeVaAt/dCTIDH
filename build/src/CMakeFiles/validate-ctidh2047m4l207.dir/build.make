# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.31

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/krijn/.local/lib/python3.10/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /home/krijn/.local/lib/python3.10/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build

# Include any dependencies generated for this target.
include src/CMakeFiles/validate-ctidh2047m4l207.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/CMakeFiles/validate-ctidh2047m4l207.dir/compiler_depend.make

# Include the progress variables for this target.
include src/CMakeFiles/validate-ctidh2047m4l207.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/validate-ctidh2047m4l207.dir/flags.make

src/CMakeFiles/validate-ctidh2047m4l207.dir/codegen:
.PHONY : src/CMakeFiles/validate-ctidh2047m4l207.dir/codegen

src/CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.o: src/CMakeFiles/validate-ctidh2047m4l207.dir/flags.make
src/CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.o: /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/common/validate.c
src/CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.o: src/CMakeFiles/validate-ctidh2047m4l207.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object src/CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.o"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT src/CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.o -MF CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.o.d -o CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.o -c /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/common/validate.c

src/CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.i"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/common/validate.c > CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.i

src/CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.s"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/common/validate.c -o CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.s

# Object files for target validate-ctidh2047m4l207
validate__ctidh2047m4l207_OBJECTS = \
"CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.o"

# External object files for target validate-ctidh2047m4l207
validate__ctidh2047m4l207_EXTERNAL_OBJECTS =

src/libvalidate-ctidh2047m4l207.a: src/CMakeFiles/validate-ctidh2047m4l207.dir/common/validate.c.o
src/libvalidate-ctidh2047m4l207.a: src/CMakeFiles/validate-ctidh2047m4l207.dir/build.make
src/libvalidate-ctidh2047m4l207.a: src/CMakeFiles/validate-ctidh2047m4l207.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C static library libvalidate-ctidh2047m4l207.a"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && $(CMAKE_COMMAND) -P CMakeFiles/validate-ctidh2047m4l207.dir/cmake_clean_target.cmake
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/validate-ctidh2047m4l207.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/validate-ctidh2047m4l207.dir/build: src/libvalidate-ctidh2047m4l207.a
.PHONY : src/CMakeFiles/validate-ctidh2047m4l207.dir/build

src/CMakeFiles/validate-ctidh2047m4l207.dir/clean:
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && $(CMAKE_COMMAND) -P CMakeFiles/validate-ctidh2047m4l207.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/validate-ctidh2047m4l207.dir/clean

src/CMakeFiles/validate-ctidh2047m4l207.dir/depend:
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src/CMakeFiles/validate-ctidh2047m4l207.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : src/CMakeFiles/validate-ctidh2047m4l207.dir/depend

