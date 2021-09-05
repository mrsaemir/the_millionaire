from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "the_millionaire.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import the_millionaire.users.signals  # noqa F401
        except ImportError:
            pass
