from create_engine import engine
from create_base import Base
from databases_model import *

if __name__ == '__main__':
    Base.metadata.create_all(engine)
