from django.utils import timezone

import pytz

from .settings import module_settings


def get_local_datetime(datetime):
    tz_name = module_settings.TIMEZONE or timezone.get_current_timezone_name()
    tz = pytz.timezone(tz_name)
    return datetime.astimezone(tz)
