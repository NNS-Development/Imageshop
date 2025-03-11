from typing import Any, List
from setuptools import setup, Extension # type: ignore
from Cython.Build import cythonize # type: ignore
from Cython.Compiler import Options # type: ignore

CFLAGS = [
    "-Oz", 
    "-flto=4", 
    "-fno-ident", 
    "-fmerge-all-constants",
    "-fno-unwind-tables",
    "-fno-asynchronous-unwind-tables",
    "-march=native"
]

LDFLAGS = [
    "-Wl,--gc-sections",
    "-Wl,--build-id=none",
    "-Wl,-z,norelro",
    "-Wl,--hash-style=sysv",
    "-Wl,--no-rosegment",
    "-nostdlib"
]

MACROS = [
    ('PY_SSIZE_T_CLEAN', "1"),
    ('CYTHON_USE_PYLONG_INTERNALS', "0"),
    ('CYTHON_FAST_THREAD_STATE', "0"),
    ('CYTHON_NO_PYINIT_EXPORT', "1"),
    ('CYTHON_USE_EXC_INFO_STACK', "0")
]

COMPILERDIRECTIVES={
    'language_level': "3",
    'boundscheck': False,
    'wraparound': False,
    'initializedcheck': False,
    'nonecheck': False,
    'cdivision': True,
    'optimize.unpack_method_calls': True,
    'optimize.inline_defnode_calls': True,
    'optimize.use_switch': True,
    'c_api_binop_methods': False
}


Options.docstrings = False
Options.embed_pos_in_docstring = False

extensions: List[Any] = []

setup(
    name="imageshop",
    version="0.0.1",
    ext_modules=cythonize(
        extensions,
        compiler_directives=COMPILERDIRECTIVES,
        exclude=[
            "**/__init__.py",
            "**/tests/*",
            "setup.py"
        ],
        build_dir="build/cython",
        nthreads=4
    ),
    entry_points={"console_scripts": ["meow=main:main"]},
    zip_safe=False
)