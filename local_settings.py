
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "af73fcdd-5289-421c-ab14-a3d769355bcc727df19b-c476-4f1e-ad3b-faa3e1459b499961f23e-3810-4e27-87f0-30c34aa6ecc3"
NEVERCACHE_KEY = "347503e6-86d3-4a7a-81e6-d782817841eee7c2e445-11ab-475b-8094-4dad2841f0daf1f28a9c-f93b-45a5-b09b-0ccb2c5f2147"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": "blog",
        # Not used with sqlite3.
        "USER": "blog",
        # Not used with sqlite3.
        "PASSWORD": "blog",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "3306",
    }
}
