class Config:
    #definir 'cadena de conexion'(connectionString)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/project'
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SECRET_KEY = 'PGLO_MANITO'
