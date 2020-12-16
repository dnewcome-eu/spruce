"""Converters miscellany"""

__copyright__ = "Copyright (C) 2014 Ivan D Vasin"
__docformat__ = "restructuredtext"

import builtins

from . import _core as _converters_core


@_converters_core.converter('boolean value')
def bool(value):
    return __builtin__.bool(value)
