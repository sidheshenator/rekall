# Rekall Memory Forensics
#
# Copyright 2014 Google Inc. All Rights Reserved.
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
#

"""
Windows entity collectors - common code.
"""
__author__ = "Adam Sindelar <adamsh@google.com>"

from rekall.entities import collector


class WindowsEntityCollector(collector.EntityCollector):
    """Base class for all Windows collectors."""

    __abstract = True

    @classmethod
    def is_active(cls, session):
        return (super(WindowsEntityCollector, cls).is_active(session) and
                session.profile.metadata("os") == "windows")
