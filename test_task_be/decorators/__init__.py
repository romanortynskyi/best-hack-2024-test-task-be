import functools
import logging
import threading
import time
from typing import Dict
from flask import jsonify, request

from modules.auth.auth_service import AuthService
from exceptions.invalid_token_exception import InvalidTokenException

LOGGER = logging.getLogger(__name__)

def authenticated(app):
    def decorator(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            auth_service = AuthService(app.config['db'])
						
            user = auth_service.get_user_by_token(request.headers.get('Authorization'))

            return f(*args, user = user, **kwargs)
              
        return decorated
    return decorator

def timed(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    start = time.time()

    try:
      return func(*args, **kwargs)
    finally:
      LOGGER.debug(f"Method {build_key(func)} took {time.time() - start}")

  return wrapper


TIMES_PER_FUNC: Dict[str, Dict[str, int]] = dict()
lock = threading.RLock()


def timed_windowed(period):
    """
    Decorator to print time elapsed in windows of the given period of time
    :param period: seconds
    """

    def decorator_timed_windowed(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                with lock:
                    times = TIMES_PER_FUNC.get(build_key(func), {"sum": 0, "count": 0, "first": start})
                time_elapsed = time.time() - start
                times["sum"] += time_elapsed
                times["count"] += 1
                if times["first"] + period < start:
                    avg = times["sum"] / times["count"]
                    LOGGER.debug(f"Method {build_key(func)} took {avg}")
                    with lock:
                        del TIMES_PER_FUNC[build_key(func)]
                else:
                    with lock:
                        TIMES_PER_FUNC[build_key(func)] = times

        return wrapper

    return decorator_timed_windowed


def build_key(func):
    return f"{func.__module__}:{func.__name__}"
