from .settings import module_settings
from .utils import get_local_datetime


class SMSRequestData:
    """SMSRequest data class.\n
    Instance use for Request class. :class:`cafe24_sms.request.Request`\n
    if message byte len <= 90 then SMS, len <= 2000 then LMS. (default charset 'euc-kr')
    With korean words, about 45 character SMS, more then LMS (max 1000 character).\n
    For detail, see also the Cafe24 site: `<https://www.cafe24.com/?controller=myservice_hosting_sms_example>`_.\n
    :param str message: A message data.
    :param str or list receiver: A telephone number separated by '-'.
    :param str sender: If none, use in settings sender. just same as receiver. (Optional)
    :param str title: A message title. if not none, use in LMS Type. (Optional)
    :param datetime reservation_time: Datetime to reservation. (Optional)
    :param int rpt_num: A repeat number 1 to 10. (Optional)
    :param int rpt_time: A repeat time gap. It must be set at least 15 minutes. (Optional)
    """

    def __init__(self, message, receiver, sender=None, title=None,
                 reservation_time=None, rpt_num=None, rpt_time=None, **kwargs):
        self.message = message.encode(module_settings.CHARSET)
        self.receiver = receiver
        self.title = title
        self.rpt_num = rpt_num
        self.rpt_time = rpt_time
        self.reservation_time = reservation_time

        if kwargs:
            raise TypeError(
                u"__init__ got unexpected keyword argument {}".format(
                    ', '.join(kwargs.keys())))

        default_sender = module_settings.SENDER.split('-')
        split_numbers = sender.split('-') if sender else default_sender
        base_data = {
            'user_id': module_settings.USER_ID,
            'secure': module_settings.SECURE_KEY,
            'sphone1': split_numbers[0],
            'sphone2': split_numbers[1],
        }

        if split_numbers.__len__() > 2:
            base_data.update({'sphone3': split_numbers[2]})

        if module_settings.TEST_MODE:
            base_data.update({'testflag': 'Y'})

        self.base_data = base_data

    @property
    def content(self):
        if type(self.receiver) == list:
            self.receiver = ','.join(self.receiver)

        self.base_data.update({
            'rphone': self.receiver,
            'msg': self.message,
        })

        if self.message.__len__() > 90:
            self.base_data.update({'smsType': 'L'})

            if self.title:
                # In docs, key is title. but real key is subject :(
                self.base_data.update({'subject': self.title})

        if self.rpt_num and self.rpt_time:
            self.base_data.update({
                'repeatFlag': 'Y',
                'repeatNum': self.rpt_num,
                'repeatTime': self.rpt_time,
            })

        if self.reservation_time:
            reservation_time = get_local_datetime(self.reservation_time)
            self.base_data.update({
                'rdate': reservation_time.strftime('%Y%m%d'),
                'rtime': reservation_time.strftime('%H%M%S'),
            })

        return self.base_data
