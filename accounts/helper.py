from pydoc import cli
from kavenegar import *
from config.settings import Kavenegar_API, Kavenegar_Number
from zeep import Client
from random import randint
from . import models
import datetime


def send_otp(mobile, otp):
    mobile = [mobile, ]
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
            'sender': '',  # optional
            'receptor': mobile,  # multiple mobile number, split by comma
            # 'message': "کد تایید شما: {}".format(otp),
            'template': 'Qiftolly',
            'token': f'{otp}',
            'token2': '',
            'token3': '',
            'type': 'sms',  # sms vs call
        }
        print('OTP: ', otp)
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def send_otp_soap(mobile, otp):
    print('OTP: ', otp)
    client = Client('http://api.kavenegar.com/soap/v1.asmx?WSDL')
    receptor = [mobile, ]

    empty_array_placeholder = client.get_type('ns0:ArrayOfString')
    receptors = empty_array_placeholder()
    for item in receptor:
        receptors['string'].append(item)

    api_key = Kavenegar_API
    message = f'Your OTP is {otp}'
    sender = '10008663'
    status = 0
    statusMessage = ''

    result = client.service.SendSimpleByApikey(api_key, sender, message, receptors, 0, 1, status, statusMessage)

    # print(result)


def get_random_otp():
    return 1234
    # return randint(1000, 9999)


def check_otp_expiration(mobile):
    try:

        user = models.CustomUser.objects.get(phone_number=mobile)
        now = datetime.datetime.now()
        otp_time = user.otp_create_time.replace(tzinfo=None)
        time_diff = (now - otp_time)
        print('OTP Time: ', time_diff)

        if int(time_diff.total_seconds()) > 30:
            return True

    except models.CustomUser.DoesNotExist:
        return False
