import pymysql


class Config:
    USER = "root"
    PASSWORD = ""
    HOST = "localhost"
    DATABASE = "productos"

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False