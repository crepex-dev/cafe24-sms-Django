from django.test import TestCase

import cafe24_sms


class SendFunctionsTestCase(TestCase):

    max_length_sms = '동' * 45
    max_length_lms = '기' * 1000
    max_length_title = '야' * 25
    test_receiver = '010-0000-0000'

    def test_max_length_sms_send_success(self):
        result_code, remaining_count = cafe24_sms.send_message(
            self.max_length_sms,
            self.test_receiver,
        )
        assert result_code == 'Test Success!'

    def test_max_length_lms_and_with_max_length_title_send_success(self):
        result_code, remaining_count = cafe24_sms.send_message(
            self.max_length_lms,
            self.test_receiver,
            title=self.max_length_title
        )
        assert result_code == 'Test Success!'

    def test_over_length_lms_send_failure(self):
        with self.assertRaisesMessage(
                cafe24_sms.exceptions.ReceivedErrorResponse,
                str(cafe24_sms.get_result_message('0004', True))
        ):
            result_code, remaining_count = cafe24_sms.send_message(
                self.max_length_lms + '더',
                self.test_receiver,
            )
            assert result_code == '0004'
