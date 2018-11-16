from django.test import TestCase
from django.utils import timezone

import cafe24_sms


class CheckFunctionsTestCase(TestCase):

    def test_result_check_without_secure_code_failure(self):
        with self.assertRaises(cafe24_sms.exceptions.ReceivedErrorResponse):
            cafe24_sms.result_check(timezone.datetime.now())
