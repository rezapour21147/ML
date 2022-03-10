import jdatetime

def Calender_Converter(date:str , date_given:str , date_wanted:str) -> str:
    """
    for date_given and date_wanted you can only enter 'j' or 'm'
    any date that you want to give must be like the example:
    year-month-day
    with no space
    """
    intdate= [int(i) for i in date.split('-')]
    if date_given == date_wanted :
        return date
    elif date_wanted == 'm':
        return jdatetime.date(intdate[0] , intdate[1] , intdate[2]).togregorian()
    elif date_wanted == 'j':
        return jdatetime.date.fromgregorian(year = intdate[0] , month = intdate[1] , day = intdate[2])


