#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  This file is part of doflicky
#
#  Copyright © 2017 Ikey Doherty <ikey@solus-project.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#

from doflicky.detection import DriverBundlePCI


class DriverBundleNvidiaBase(DriverBundlePCI):
    """ Ease of implementation, base class for nvidia drivers """

    def __init__(self, modaliasesPath):
        DriverBundlePCI.__init__(self, modaliasesPath)

    def get_icon(self):
        return "video-display"

    def has_emul32(self):
        return True

    def get_base(self):
        return "nvidia-gpu"

    def triggers_emul32(self):
        """ For GPU drivers we'll suggest 32-bit when we find related pkgs """
        return ["wine-32bit", "steam", "mesalib-32bit"]


class DriverBundleNvidia(DriverBundleNvidiaBase):
    """ Main NVIDIA driver (nvidia-glx-driver) """

    def __init__(self):
        DriverBundleNvidiaBase.__init__(self, "nvidia-glx-driver.modaliases")

    def get_name(self):
        return "NVIDIA Graphics Driver (main series)"

    def get_priority(self):
        return 3

    def get_packages(self, context, emul32=False):
        basePackages = ["nvidia-glx-driver-common"]
        if emul32:
            basePackages.append("nvidia-glx-driver-32bit")
        if context.get_active_kernel_series() == "current":
            basePackages.append("nvidia-glx-driver-current")
        else:
            basePackages.append("nvidia-glx-driver")
        return basePackages
