# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class NrmCore(Package):
    """
    nrm-core contains the core logic for the Argo Node Resource Manager,
    a user-level daemon for application to manage and optimize their
    resource usage on the fly.
    """

    homepage = "https://nrm.readthedocs.io"

    maintainers = ['perarnau']

    # nrm-core is written in Haskell which is currently not supported in
    # spack, thus a similar approach as in the pandoc package was chosen. The
    # following installs the standalone binaries and shared libraries for nrm.

    url = "https://github.com/anlsys/nrm-core/releases/download/v0.7.0/nrm-core-v0.7.0-x86_64-linux.tar.gz"

    version('0.7.0', sha256='7cd5f592119378c65f14e581350034676e29ffbbddc952249d21c1c4dae16fa5')

    depends_on('gmp')
    depends_on('zlib')
    depends_on('libffi')
    depends_on('libzmq')
    depends_on('ncurses')
    depends_on('hwloc@2', type=('build', 'run'))

    conflicts('platform=darwin', msg='Darwin is not supported.')
    conflicts('platform=windows', msg='Windows is not supported.')

    def install(self, spec, prefix):
        install_tree('.', prefix)
