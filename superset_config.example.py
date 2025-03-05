import os
from flask_appbuilder.security.manager import AUTH_DB

# Data directory config
DATA_DIR = os.path.join(os.path.expanduser("~"), "superset")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Database connection
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123456@localhost:5432/superset"

# Redis configuration
CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 86400,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": "localhost",
    "CACHE_REDIS_PORT": 6379,
    "CACHE_REDIS_DB": 1,
}

# Feature flags
FEATURE_FLAGS = {
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
}

# Security & Authentication
SECRET_KEY = os.urandom(32)
AUTH_TYPE = AUTH_DB
AUTH_USER_REGISTRATION = False
AUTH_USER_REGISTRATION_ROLE = "Admin"

# Webserver settings
SUPERSET_WEBSERVER_PORT = 8088
WEBSERVER_THREADS = 8
WEBSERVER_TIMEOUT = 60

# Additional settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = True
WTF_CSRF_EXEMPT_LIST = []
ENABLE_PROXY_FIX = False
PREVENT_UNSAFE_DB_CONNECTIONS = True

# Paths
ROW_LIMIT = 50000
SUPERSET_WORKERS = 4
