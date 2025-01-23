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
include src/CMakeFiles/karatsuba_fp_sqr.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include src/CMakeFiles/karatsuba_fp_sqr.dir/compiler_depend.make

# Include the progress variables for this target.
include src/CMakeFiles/karatsuba_fp_sqr.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/karatsuba_fp_sqr.dir/flags.make

src/CMakeFiles/karatsuba_fp_sqr.dir/codegen:
.PHONY : src/CMakeFiles/karatsuba_fp_sqr.dir/codegen

src/CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.o: src/CMakeFiles/karatsuba_fp_sqr.dir/flags.make
src/CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.o: /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/common/fp/karatsuba/sqr.s
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building ASM object src/CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.o"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && /usr/bin/cc $(ASM_DEFINES) $(ASM_INCLUDES) $(ASM_FLAGS) -o CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.o -c /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/common/fp/karatsuba/sqr.s

src/CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing ASM source to CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.i"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && /usr/bin/cc $(ASM_DEFINES) $(ASM_INCLUDES) $(ASM_FLAGS) -E /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/common/fp/karatsuba/sqr.s > CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.i

src/CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling ASM source to assembly CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.s"
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && /usr/bin/cc $(ASM_DEFINES) $(ASM_INCLUDES) $(ASM_FLAGS) -S /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src/common/fp/karatsuba/sqr.s -o CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.s

karatsuba_fp_sqr: src/CMakeFiles/karatsuba_fp_sqr.dir/common/fp/karatsuba/sqr.s.o
karatsuba_fp_sqr: src/CMakeFiles/karatsuba_fp_sqr.dir/build.make
.PHONY : karatsuba_fp_sqr

# Rule to build all files generated by this target.
src/CMakeFiles/karatsuba_fp_sqr.dir/build: karatsuba_fp_sqr
.PHONY : src/CMakeFiles/karatsuba_fp_sqr.dir/build

src/CMakeFiles/karatsuba_fp_sqr.dir/clean:
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src && $(CMAKE_COMMAND) -P CMakeFiles/karatsuba_fp_sqr.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/karatsuba_fp_sqr.dir/clean

src/CMakeFiles/karatsuba_fp_sqr.dir/depend:
	cd /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/src /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src /home/krijn/Documents/Mathematics/Research/dachshund-wombat/code/build/src/CMakeFiles/karatsuba_fp_sqr.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : src/CMakeFiles/karatsuba_fp_sqr.dir/depend

