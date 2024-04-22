from datetime import datetime

def get_days_from_today(date:str) -> int:
    try:
        date = datetime.strptime(date, '%Y-%m-%d')  
    except ValueError:
        return 0
    today = datetime.today()
    delta = today - date
    return delta.days
