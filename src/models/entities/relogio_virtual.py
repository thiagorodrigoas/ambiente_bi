import time
from datetime import datetime, timedelta

class RelogioVirtual:
    def __init__(self, start_year=2018, start_month=1, start_day=1, factor_hour_per_sec=24):
        self.current_date = datetime(start_year, start_month, start_day)
        self.last_checked_real_time = round(time.time())
        self.factor_hour_per_sec = factor_hour_per_sec
 
    def get_current_time(self):
        """Retorna a hora atual fictícia"""
        elapsed_real_seconds = round(time.time()) - self.last_checked_real_time
        elapsed_fictitious_hours = elapsed_real_seconds / (1/self.factor_hour_per_sec) #2.5
        self.current_date += timedelta(hours=elapsed_fictitious_hours)
        self.last_checked_real_time = round(time.time())
        return self.current_date