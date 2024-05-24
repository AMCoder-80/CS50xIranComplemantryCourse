from django.core.mail import send_mail


class EmailHandler:
    """ Dealing withi sending text and token via email """
    def __init__(self) -> None:
        pass

    def send_otp(self, email, token):
        """ Send only token to user without any special text"""
        # response = send_mail(
        #     "Authentication Token",
        #     f"Your token is: {token}",
        #     "from@example.com",
        #     ["alirezamortezaei50@gmail.com"],
        # )
        print("###############################")
        print(f"Your token is: {token}")
        print("###############################")
