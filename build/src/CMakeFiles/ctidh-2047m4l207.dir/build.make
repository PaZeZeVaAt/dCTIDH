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
include src/CMakeFiles/ctidh-2047m4l207.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/CMakeFiles/ctidh-2047m4l207.dir/compiler_depend.make

# Include the progress variables for this target.
include src/CMakeFiles/ctidh-2047m4l207.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/ctidh-2047m4l207.dir/flags.make

src/CMakeFiles/ctidh-2047m4l207.dir/codegen:
.PHONY : src/CMakeFiles/ctidh-2047m4l207.dir/codegen

src/CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.o: src/CMakeFiles/ctidh-2047m4l207.dir/flags.make
src/CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.o: /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/CTIDH/ctidh_api.c
src/CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.o: src/CMakeFiles/ctidh-2047m4l207.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object src/CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.o"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT src/CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.o -MF CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.o.d -o CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.o -c /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/CTIDH/ctidh_api.c

src/CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing C source to CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.i"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/CTIDH/ctidh_api.c > CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.i

src/CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling C source to assembly CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.s"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/CTIDH/ctidh_api.c -o CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.s

ctidh-2047m4l207: src/CMakeFiles/ctidh-2047m4l207.dir/CTIDH/ctidh_api.c.o
ctidh-2047m4l207: src/CMakeFiles/ctidh-2047m4l207.dir/build.make
.PHONY : ctidh-2047m4l207

# Rule to build all files generated by this target.
src/CMakeFiles/ctidh-2047m4l207.dir/build: ctidh-2047m4l207
.PHONY : src/CMakeFiles/ctidh-2047m4l207.dir/build

src/CMakeFiles/ctidh-2047m4l207.dir/clean:
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && $(CMAKE_COMMAND) -P CMakeFiles/ctidh-2047m4l207.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/ctidh-2047m4l207.dir/clean

src/CMakeFiles/ctidh-2047m4l207.dir/depend:
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src/CMakeFiles/ctidh-2047m4l207.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : src/CMakeFiles/ctidh-2047m4l207.dir/depend

