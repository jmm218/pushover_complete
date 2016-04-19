"""A Python 3 package for interacting with *all* aspects of the Pushover API"""

from .error import PushoverCompleteError, BadAPIRequestError
from .pushover_api import PushoverAPI

__all__ = [
    'PushoverCompleteError', 'BadAPIRequestError',
    'PushoverAPI'
]

__version__ = '0.0.1'

__title__ = 'pushover_complete'
__description__ = ''
__url__ = ''


__author__ = 'Scott Colby'
__email__ = 'scolby33@gmail.com'


__license__ = 'MIT License'
__copyright__ = 'Copyright (c) 2016 Scott Colby'
