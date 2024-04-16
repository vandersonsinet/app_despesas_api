from datetime import datetime
import sqlite3

print("Conectando...")
db_path = "database/"
conn = sqlite3.connect('database//db.sqlite3')
sql = 'INSERT INTO tipo_despesa (descricao, data_insercao) VALUES (?,?)'
dados = [
      ('Conta de Luz', datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
      ('Alimentação', datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
      ('Aluguel', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),   
      ('Gastos Extras', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),   
]
print("Carga efetuada...")
conn.executemany(sql, dados)
conn.commit()
conn.close()