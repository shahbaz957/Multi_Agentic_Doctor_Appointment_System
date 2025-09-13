import re
from pydantic import BaseModel , Field , field_validator

class DateTimeModel(BaseModel) : # this is not OOP like class
    date : str = Field(description="Properly Formated Date and Time" ,  pattern=r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$')
    @field_validator("date")
    def check_date_time(cls , v):
        if not re.match(r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$' , v):
            raise ValueError("The Date and Time Should in Proper Format 'DD-MM-YYYY HH:MM'")
        return v
    
class DateModel(BaseModel) :
    date : str = Field(description="Properly formated Date" , pattern=r'^\d{2}-\d{2}-\d{4}$')
    @field_validator("date")
    def check_date(cls , v) : 
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', v) :
            raise ValueError("The Date should be in proper Format 'DD-MM-YYYY'")
        return v
    
class IdentificationNumberModel(BaseModel) :
    id : int = Field(description="Identification Number (7 or 8 digits long)")
    @field_validator("id")
    def check_format_id(cls , v):
        if not re.match(r'^\d{7,8}$', str(v)):
            raise ValueError("The ID Number should be in 7 to 8 Digit")
        return v