import traceback # for getting the traceback of the error
import sys

class CustomException(Exception):# we inherit from the Exception class because we not only want custom error but also want to use the built-in error handling mechanism

    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)#inhnerit the __init__ method of the parent class if the error is proesent in predifined errors of python,otherwise we will use our custom error
        self.error_message = self.get_detailed_error_message(error_message,error_detail)

    @staticmethod#we do not need to create custom class again and again,by this @staticmethod our method become independent of the class and can be called without creating an object of the class
    def get_detailed_error_message(error_message , error_detail:sys):

        _, _, exc_tb = traceback.sys.exc_info()# exc_info() method returns a tuple of three values that give information about the exception that is currently being handled but we need only the traceback object which is the third value in the tuple
                                               # traceback object contains information about the error like the file in which the error occured, the line number at which the error occured etc.
        file_name = exc_tb.tb_frame.f_code.co_filename # get the file name in which the error occured
        line_number = exc_tb.tb_lineno # get the line number at which the error occured

        return f"Error in {file_name} , line {line_number} : {error_message}"
    
    def __str__(self): #magic method to return the error message 
        return self.error_message


# /Users/vidhan_mac/Downloads/hotelreservation-1-0855df03b5af.json
