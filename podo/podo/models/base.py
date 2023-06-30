from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from ..logger import get_logger

logger = get_logger()
Base = declarative_base()
engine = create_engine("sqlite:///mydb.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(bind=engine)