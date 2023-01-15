from enum import Enum

__all__ = ['review', 'gmarket', 'naver', 'coupang']


class Mall(Enum):
    """
    Mall class for mall types
    """
    GMARKET = 1
    ELEVENST = 2
