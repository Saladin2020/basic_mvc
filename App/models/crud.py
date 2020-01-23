from App.lib.database import Database

class CRUD:
    def __init__(self):
        self.db = Database()

    def create(self):
        self.db.command("SELECT * FROM oapp WHERE vstdate=CURDATE()")
        return self.db.getResult()

    def read(self, tbl, data):
        pass

    def update(self, tbl, data):
        pass

    def delete(self, tbl, data):
        pass
