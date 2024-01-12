from exchange.settings import env

EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT', default=587)
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=True)
EMAIL_CONFIRMATION_EXPIRE_DAYS = env('EMAIL_CONFIRMATION_EXPIRE_DAYS', default=1)
EMAIL_CONFIRMATION_COOLDOWN = env('EMAIL_CONFIRMATION_COOLDOWN', default=180)
