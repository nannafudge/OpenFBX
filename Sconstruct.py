from scons import *

target_os = "Windows"
build_dir = classes = Dir('build')
out_dir = classes = Dir('out')

if (target_os == "Windows"):
    env = Environment(LINKFLAGS='/DEF:src/ofbx.def')
else:
    env = Environment()

env.SharedLibrary('out/openfbx', ['src/ofbx.cpp', 'src/miniz.c'], variant_dir='build')

#Default()