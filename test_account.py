from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('Justin')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'Justin'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(5) == True
        assert self.p1.get_balance() == 5

        assert self.p1.deposit(5.5) == True
        assert self.p1.get_balance() == approx(10.5, abs=0.001)

        assert self.p1.deposit(0) == False
        assert self.p1.get_balance() == approx(10.5, abs=0.001)

        assert self.p1.deposit(-2) == False
        assert self.p1.get_balance() == approx(10.5, abs=0.001)

        assert self.p1.deposit(-2.5) == False
        assert self.p1.get_balance() == approx(10.5, abs=0.001)


    def test_withdraw(self):
        assert self.p1.deposit(10) == True
        assert self.p1.withdraw(1) == True
        assert self.p1.get_balance() == 9

        assert self.p1.withdraw(1.5) == True
        assert self.p1.get_balance() == approx(7.5, abs=0.001)

        assert self.p1.withdraw(20) == False
        assert self.p1.get_balance() == approx(7.5, abs=0.001)

        assert self.p1.withdraw(20.5) == False
        assert self.p1.get_balance() == approx(7.5, abs=0.001)

        assert self.p1.withdraw(0) == False
        assert self.p1.get_balance() == approx(7.5, abs=0.001)

        assert self.p1.withdraw(-2) == False
        assert self.p1.get_balance() == approx(7.5, abs=0.001)

        assert self.p1.withdraw(-2.5) == False
        assert self.p1.get_balance() == approx(7.5, abs=0.001)
