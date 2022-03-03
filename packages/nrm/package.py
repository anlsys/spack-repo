# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Nrm(Package):
    """Node Resource Manager. Installs nrm-core and py-nrm.
    Builds and installs documentation, includes examples."""

    homepage = "https://nrm.readthedocs.io/en/latest/"

    url = "https://github.com/anlsys/nrm-docs/archive/refs/tags/v0.7.0.tar.gz"
    maintainers = ['perarnau']

    version("0.7.0", sha256="75333e2bcc94cc98ccc3680e056c2e188799aa0cf5d0e56550ec7a9980c13d94")

    depends_on('py-nrm@0.7.0', type=('build', 'run'))
    depends_on('nrm-core@0.7.0', type=('build', 'run'))
    depends_on('libnrm@0.7.0', type=('build', 'run'))
    depends_on('nrm-extra@0.7.0', type=('build', 'run'))

    depends_on('py-sphinx@2.4.4', type=('build'))
    depends_on('py-docutils@0.17', type=('build'))
    depends_on('py-nbsphinx', type=('build'))

    def install(self, spec, prefix):
        with working_dir('doc'):
            make('html', parallel=False)
            mkdirp(prefix.share.html)
            mkdirp(prefix.share.examples)
            install_tree('.build/html', prefix.share.html)
            install_tree('../examples', prefix.share.examples)
