# Rekall Memory Forensics
#
# Copyright 2015 Google Inc. All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
"""Miscelaneous information gathering plugins."""

__author__ = "Michael Cohen <scudette@google.com>"


from rekall.plugins import core
from rekall.plugins.linux import common

class LinuxSetProcessContext(core.SetProcessContextMixin,
                             common.LinProcessFilter):
    """A cc plugin for windows."""


class LinVtoP(core.VtoPMixin, common.LinProcessFilter):
    """Describe virtual to physical translation on Linux platforms."""
