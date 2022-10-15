import pymongo

class PymongoConnection:
    def __init__(self) -> None:
        pass

    def my_client(self):
        """Create the mongodb connection."""
        return pymongo.MongoClient("mongodb://localhost:27017/")

    def create_db(self):
        """Create the first_database database if it does not exist."""
        return self.my_client()["first_database"]
    
    def check_database_names(self):
        """Return a list of the name of databases."""
        return self.my_client().list_database_names()

    def create_collection(self):
        """Create the `first_collection`"""
        return self.create_db()["first_collection"]

    def check_collections(self):
        """Return a list of the existing collections."""
        return self.create_db().list_collection_names()

    def insert_document(self, first_name, last_name, email):
        """Insert the post dict in the create collection on `self.create_collection()`"""
        post = {"first_name": first_name, "last_name": last_name, "email": email}
        return self.create_collection().insert_one(post)
    
    def find_documents(self):
        """Return every document in the collection."""
        return self.create_collection().find()

    def list_documents(self):
        """Return a list of all documents found in self.find_documents()"""
        list_of_documents = [doc for doc in self.find_documents()]
        return list_of_documents