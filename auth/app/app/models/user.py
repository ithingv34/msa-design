# This could be a SQLAlchemy model,
# an ElasticSearch document, a MongoDB document, etc
class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
