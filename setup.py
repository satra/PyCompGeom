#!/usr/bin/env python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""compgeom:  a package for computational geometry on meshes
"""

import sys


def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration(None, parent_package, top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)
    # The quiet=True option will silence all of the name setting warnings:
    # Robert Kern recommends setting quiet=True on the numpy list, stating
    # these messages are probably only used in debugging numpy distutils.

    config.get_version('comgeom/version.py') # sets config.version
    config.add_subpackage('comgeom', 'compgeom')

    return config

################################################################################

desc = """A Python library focused on computational geometry on meshes
"""

def main(**extra_args):
    from numpy.distutils.core import setup

    install_requires=['numpy >=1.1',
              'scipy >=0.7',
              'matplotlib >=1.0.0',
              'networkx >=1.0',
              'cython >=0.13']

    setup( name = 'PyCompGeom',
           description = 'Computational Geometry in Python',
           author = 'Satrajit Ghosh',
           author_email = 'satra@mit.edu',
           #url = 'http://nipy.org/nipype',
           long_description = desc,
           configuration = configuration,
           install_requires=install_requires,
           **extra_args)


if __name__ == "__main__":
    main()
