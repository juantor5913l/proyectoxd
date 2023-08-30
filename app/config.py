class Config:
    #definir 'cadena de conexion'(connectionString)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin1234@localhost:3311/proyecto'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'PGLO_MANITO'
