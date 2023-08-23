# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libnrm(AutotoolsPackage):
    """Libnrm, the application instrumentation library for the Node
    Resource Manager(NRM)."""

    homepage = "https://nrm.readthedocs.io/en/latest/"
    git = "https://github.com/anlsys/libnrm.git"
    version("master", branch="master", get_full_repo=True)

    maintainers = ["perarnau"]
    tags = ["e4s"]

    variant("geopm", default=False, description="Support for GeoPM.")
    variant("openmp", default=True, description="Support for OMPT.")

    with when("@master"):
        depends_on("m4", type="build")
        depends_on("autoconf", type="build")
        depends_on("automake", type="build")
        depends_on("libtool", type="build")
        depends_on("pkgconfig", type="build")
        depends_on("libzmq")
        depends_on("czmq")
        depends_on("protobuf-c")
        depends_on("hwloc")
        depends_on("jansson")
        depends_on("check")
        depends_on("bats")
        depends_on("papi+powercap")
        depends_on("geopm", when="+geopm")

    def configure_args(self):
        config_args = []
        config_args.extend(self.with_or_without("geopm"))
        config_args.extend(self.enable_or_disable("openmp"))
        return config_args
