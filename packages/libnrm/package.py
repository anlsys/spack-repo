# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libnrm(AutotoolsPackage):
    """Libnrm, the application instrumentation library for the Node
    Resource Manager(NRM)."""

    homepage = "https://nrm.readthedocs.io/en/latest/"
    url = "https://github.com/anlsys/libnrm/releases/download/v0.7.0/libnrm-0.7.0.tar.gz"
    git = "https://github.com/anlsys/libnrm.git"
    version('master', branch='master', get_full_repo=True)
    version('0.7.0', sha256='30933537e9db6c1f35a3eda421794d2a562c492b520ed20e6490571b3ce0f1d8')

    maintainers = ['perarnau']
    tags = ['e4s']

    with when("@master"):
        depends_on("m4", type="build")
        depends_on("autoconf", type="build")
        depends_on("automake", type="build")
        depends_on("libtool", type="build")
        depends_on("pkgconfig", type="build")
        depends_on("libzmq")
        depends_on("czmq")
        depends_on("protobuf-c", type="build")
        depends_on("hwloc")
        depends_on("jansson")
        depends_on("check")

    with when("@0.7.0"):
        depends_on('pkgconfig', type='build')
        depends_on('libzmq')
