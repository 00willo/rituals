# -*- coding: utf-8 -*-
# pylint: disable=bad-continuation
""" GitHub automation.
"""
# Copyright ⓒ  2015 Jürgen Hermann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# The full LICENSE file and source are available at
#    https://github.com/jhermann/rituals

from invoke import task

from rituals import config
from rituals.util import notify


@task(name='gh-sync-readme')
def gh_sync_readme():
    """Update GH pages from project's README."""
    cfg = config.load()
    notify.banner("Syncing GH pages with 'README.md'...")

    notify.failure("Not implemented yet!")