import platform

from django.db import models


class Subsonic(models.Model):
    """
    Django model describing every tunable setting for subsonic
    """

    enable = models.BooleanField(default=False)
    subsonic_max_memory = models.IntegerField(
        verbose_name="Max Memory (MB)",
        default=100,
        )
    subsonic_ssl = models.BooleanField(
        verbose_name="Enable SSL",
        default=False,
        )
    subsonic_ssl_keystore = models.CharField(
         verbose_name="SSL Keystore",
         max_length=500,
         blank=True
         )
    subsonic_ssl_password = models.CharField(
         verbose_name="SSL Keystore Password",
         max_length=120,
         blank=True,
         )
    subsonic_port = models.IntegerField(
        verbose_name="WebUI Port",
        default=4040,
        )
    subsonic_context_path = models.CharField(
        verbose_name="Context Path",
        max_length=120,
        default="/",
        )
