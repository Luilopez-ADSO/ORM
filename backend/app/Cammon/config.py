import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]


class Config:
    USER = os.getenv("DB_USER", "root")
    PASSWORD = os.getenv("DB_PASSWORD", "")
    HOST = os.getenv("DB_HOST", "localhost")
    DATABASE = os.getenv("DB_NAME", "productos")

    if os.getenv("USE_MYSQL", "0").lower() in {"1", "true", "yes"}:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
        )
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR / 'productos.db'}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False