from distutils.core import setup, Extension


m = Extension('tinyobjloader',
              sources = ['utils/main.cpp', 'utils/tiny_obj_loader.cc'])


setup (name = 'tinyobjloader',
       version = '0.1',
       description = 'Python module for tinyobjloader',
       ext_modules = [m])


