import sys
from typing import Tuple

def get_error_details(error_details: sys) -> Tuple[str, int]:
    _, _, exc_tb = error_details.exc_info()

    filename = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno

    return filename, lineno


class SensorException(Exception):
    def __init__(self, error, error_details: sys) -> None:
        super().__init__(error)

        self.filename, self.lineno = get_error_details(error_details)
        self.error_message = f"Error occurred in the File: [{self.filename}] Line: [{self.lineno}] Error Details: [{error}]"
        

    def __str__(self) -> str:
        return self.error_message