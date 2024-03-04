from relogio_virtual import RelogioVirtual

class Ambiente:
   def __init__(self,start_year=2024, start_month=1, start_day=1, factor_hour_per_sec=24):
        self.relogio_virtual = RelogioVirtual(start_year, start_month, start_day, factor_hour_per_sec)
   
   def __enter__(self):
        print(f"Entrando no ambiente virtual. Data inicial: {self.relogio_virtual.get_current_time()}")
        return self  # Retorna uma instância de Ambiente para ser usada dentro do bloco 'with'

   def __exit__(self, exc_type, exc_val, exc_tb):
       pass
