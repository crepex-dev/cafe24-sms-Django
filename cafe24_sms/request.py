import functools

from django.utils.translation import ugettext_lazy as _

import requests

from . import exceptions
from .result_codes import get_result_message
from .settings import module_settings


class RequestBase:
    SMS_SEND_URL = 'https://sslsms.cafe24.com/sms_sender.php'
    SEND_RESULT_URL = 'http://smsapi.cafe24.com/sms_list.php'
    SUCCESS_CODE = 'Test Success!' if module_settings.TEST_MODE else 'success'
    RESERVATION_CODE = 'reserved'

    def __init__(self, request_data, **kwargs):
        self.request_data = request_data

        if kwargs:
            raise TypeError(
                u"__init__ got unexpected keyword argument {}".format(
                    ', '.join(kwargs.keys())))

    def __repr__(self):
        return f'<Request: {self.request_data}>'

    @property
    def data(self):
        return self.request_data.content


class SMSRequest:
    def sms_request(self, url, timeout=None):
        requests_post = requests.post
        char_set = module_settings.CHARSET

        if timeout is not None:
            requests_post = functools.partial(requests_post, timeout=timeout)

        try:
            response = requests_post(url, data=self.data)
            result_code, remaining_count = response.content.decode(char_set).split(',')
        except requests.exceptions.RequestException:
            raise exceptions.RequestNotReachable()
        except UnicodeDecodeError:
            raise exceptions.SMSModuleException(
                message=_('Response decode error with %s' % char_set)
            )

        if result_code not in [self.SUCCESS_CODE, self.RESERVATION_CODE] or response.status_code != 200:
            error_message = get_result_message(result_code, self.request_data.is_lms)
            raise exceptions.ReceivedErrorResponse(
                code=result_code,
                message=error_message
            )

        return result_code, remaining_count


class Request(RequestBase, SMSRequest):
    """SMS request class. SMSData instance required.\n
    Init with :class:`cafe24_sms.data.SMSData` instance and use `sms_request` method to try sms message request
    and get result_code/remaining sms count tuple or exception.\n
    For detail, see also the Cafe24 site: `<https://www.cafe24.com/?controller=myservice_hosting_sms_example>`_.\n
    """
    timeout = module_settings.REQUEST_TIMEOUT

    def send_message(self):
        return self.sms_request(self.SMS_SEND_URL, self.timeout)
