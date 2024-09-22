import sys

def error_msg_details(error, error_details: sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno
    error_message=f"Error occured in python script name [{file_name}] line number [{line_no}] error message [{str(error)}]"
    return error_message

class CustomExceptions(Exception):
    def __init__(self, error_message, error_message_details: sys):
        super().__init__(error_message)
        self.error_message=error_msg_details(error_message,error_details=error_message_details)

    def __str__(self):
        return self.error_message


