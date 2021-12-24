class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log','a+') as arq:
            arq.write(msg)
            arq.write('\n')


    def log_info(self, msg):
        self.write(f'INFO: {msg}')


    def log_error(self, msg):
        self.write(f'ERRO: {msg}')

