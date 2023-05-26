from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        super().__init__()
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é R$ {self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(Saque Negado: {valor})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, conta: int,
        saldo: float = 0, limite: float = 0
    ) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(Saque Negado: {valor})')
        return self.saldo


if __name__ == '__main__':
    conta_poupanca_1 = ContaPoupanca(111, 222)
    conta_poupanca_1.sacar(1)
    conta_poupanca_1.depositar(1)
    conta_poupanca_1.sacar(1)
    conta_poupanca_1.sacar(1)
    conta_poupanca_1.sacar(1)
    print('######')
    conta_corrente_1 = ContaCorrente(111, 222, 0, 100)
    conta_corrente_1.sacar(1)
    conta_corrente_1.depositar(1)
    conta_corrente_1.sacar(1)
    conta_corrente_1.sacar(1)
    conta_corrente_1.sacar(98)
    conta_corrente_1.sacar(1)
