# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyNrm(PythonPackage):
    """Python interface to the Argo Node Resource Manager,
    an infrastructure to allow applications to manage node resources
    on the fly."""

    homepage = "https://nrm.readthedocs.io"

    url = 'https://github.com/anlsys/nrm-python/archive/refs/tags/v0.7.0.tar.gz'
    maintainers = ['perarnau']

    version('0.7.0', sha256='474f656f5696a6d6f5680d8e2f8470612aa181b9496058fa9d3e092b0a3adc50')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('nrm-core@0.7.0')
    depends_on('py-msgpack', type=('build', 'run'))
    depends_on('py-warlock@1.3.3', type=('build', 'run'))
    depends_on('py-pyzmq', type=('build', 'run'))
    depends_on('py-tornado@5.1.1', type=('build', 'run'))
    depends_on('py-jsonschema@3.2.0', type=('build', 'run'))

    def setup_run_environment(self, env):
        env.prepend_path('LD_LIBRARY_PATH', self.spec['nrm-core'].prefix.lib)
