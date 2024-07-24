from datetime import datetime


def generate_email_time_stamp():
    time_stamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    return f"aziguy{time_stamp}@gmail.com"