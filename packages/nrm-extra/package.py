# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class NrmExtra(Package):
    """Node Resource Manager. Contains external sensors and actuator for NRM."""

    homepage = "https://nrm.readthedocs.io/en/latest/"
    url = "https://github.com/anlsys/nrm-extra/archive/refs/tags/v0.7.0.tar.gz"

    maintainers = ['perarnau']

    version("0.7.0", sha256="924386f15bc37daa36570dcefc74a28454750f2c27ad2055f59e7c5feda9d37c")

    depends_on('libnrm@0.7.0', type=('build'))
    depends_on('llvm-openmp@12.0.1', type=('build'))
    depends_on('mpi', type=('build'))
