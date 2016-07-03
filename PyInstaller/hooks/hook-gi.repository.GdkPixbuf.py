#-----------------------------------------------------------------------------
# Copyright (c) 2005-2016, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
"""
Import hook for PyGObject's "gi.repository.GdkPixbuf" package.
"""

import glob
import os
import subprocess

from PyInstaller.config import CONF
from PyInstaller.compat import (
    exec_command_stdout, is_darwin, is_win, is_linux, open_file, which)
from PyInstaller.utils.hooks import (
    collect_glib_translations, get_gi_typelibs, get_gi_libdir, logger)

binaries, datas, hiddenimports = get_gi_typelibs('GdkPixbuf', '2.0')
datas += collect_glib_translations('gdk-pixbuf')

libdir = get_gi_libdir('GdkPixbuf', '2.0')

cachefile = os.path.join(
            libdir, 'lib', 'gdk-pixbuf-2.0', '2.10.0', 'loaders.cache')

# Bundle this loader cache with this frozen application.
datas.append((cachefile, 'lib/gdk-pixbuf-2.0/2.10.0'))
