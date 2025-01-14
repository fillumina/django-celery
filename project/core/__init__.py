from .celery import app as celery_app

# __all__ allows you to specify which attributes or methods should 
# be exposed for import when using the from module import * syntax.
# Without __all__, Python defaults to importing everything that 
# doesn’t start with an underscore.
__all__ = ["celery_app",]