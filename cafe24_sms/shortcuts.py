from .data import SMSRequestData
from .request import Request


def send_message(message, receiver,
                 sender=None, title=None, rpt_num=None, rpt_time=None):
    """Shortcut API for :class:`cafe24_sms.data.SMSRequestData`, :class:`cafe24_sms.request.Request`.\n
    Send SMS or LMS message request use with :func:`requests.post`.\n
    For detail, see also the Cafe24 site: `<https://www.cafe24.com/?controller=myservice_hosting_sms_example>`_.\n

    :param str message: A message data.
    :param str or list receiver: A telephone number separated by '-'.
    :param str sender: If none, use in settings sender. just same as receiver. (Optional)
    :param str title: A message title. if not none, use in LMS Type. (Optional)
    :param int rpt_num: A repeat number 1 to 10. (Optional)
    :param int rpt_time: A repeat time gap. It must be set at least 15 minutes. (Optional)

    :return: str result_code(Received result code), int remaining_count(Received remaining sms count)

    :raises: :class:`cafe24_sms.exceptions.RequestNotReachable`.
    :raises: :class:`cafe24_sms.exceptions.SMSModuleException`.
    :raises: :class:`cafe24_sms.exceptions.ReceivedErrorResponse`.
    """
    data = SMSRequestData(message, receiver, sender, title,
                          rpt_num=rpt_num, rpt_time=rpt_time)
    request = Request(request_data=data)
    return request.send_message()


def reserve_message(message, receiver, reservation_time,
                    sender=None, title=None, rpt_num=None, rpt_time=None):
    """Shortcut API for :class:`cafe24_sms.data.SMSRequestData`, :class:`cafe24_sms.request.Request`.\n
    Send SMS or LMS message request use with :class:`requests` package.\n
    For detail, see also the Cafe24 site: `<https://www.cafe24.com/?controller=myservice_hosting_sms_example>`_.\n

    :param str message: A message data.
    :param str or list receiver: A telephone number separated by '-'.
    :param str sender: If none, use in settings sender. just same as receiver. (Optional)
    :param str title: A message title. if not none, use in LMS Type. (Optional)
    :param datetime reservation_time: Datetime to reservation. (Optional)
    :param int rpt_num: A repeat number 1 to 10. (Optional)
    :param int rpt_time: A repeat time gap. It must be set at least 15 minutes. (Optional)

    :return: str result_code(Received result code), int remaining_count(Received remaining sms count)

    :raises: :class:`cafe24_sms.exceptions.RequestNotReachable`.
    :raises: :class:`cafe24_sms.exceptions.SMSModuleException`.
    :raises: :class:`cafe24_sms.exceptions.ReceivedErrorResponse`.
    """
    data = SMSRequestData(message, receiver, sender, title,
                          reservation_time=reservation_time, rpt_num=rpt_num, rpt_time=rpt_time)
    request = Request(request_data=data)
    return request.send_message()
