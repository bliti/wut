try:
    from development_settings import DEBUG
except ImportError:
    DEBUG = False