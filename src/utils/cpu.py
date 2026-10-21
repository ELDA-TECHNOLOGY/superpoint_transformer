import os


__all__ = ['available_cpu_count', 'set_available_cpu_count']

_OVERRIDE = None


def set_available_cpu_count(n):
    """Pin the thread count parallel sections use; None restores autodetection."""
    global _OVERRIDE
    _OVERRIDE = None if n is None else max(1, int(n))


def available_cpu_count():
    """Number of CPUs available to this process, or the pinned override."""
    if _OVERRIDE is not None:
        return _OVERRIDE
    try:
        return len(os.sched_getaffinity(0))
    except AttributeError:
        pass
    count = os.cpu_count()
    return count if count else 1
