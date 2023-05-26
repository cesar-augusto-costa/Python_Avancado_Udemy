# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    # method
    def set_user(self, user):
        self.user = user
    
    # method
    def set_password(self, password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def soma(x, y):
        return x + y
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)

# method
c1 = Connection()
c1.set_user('luiz')
c1.set_password('1234')
print(c1.user, c1.password)

# @classmethod
c2 = Connection.create_with_auth('luiz', '1234')
print(c2.user, c2.password)

# @staticmethod
print(Connection.soma(2, 3))
Connection.log('essa é a mensagem')
