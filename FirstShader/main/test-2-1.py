from core.base import Base

class Test(Base):

    def __init__(self):
        super().__init__()

    def initialize(self):
        print("Initializing Program")
    
    def update(self):
        pass

test= Test()

test.run()