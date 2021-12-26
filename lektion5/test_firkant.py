import pytest
from dataclasses import dataclass

# I virkeligheden har man selvfølgelig ikke klassen og testen sammen.

@dataclass
class Firkant:
    a: int
    b: int
    def areal(self)->int:
        return self.a-self.b

class TestFirkan:
    @pytest.fixture(scope="function")
    def firkant1(self):
        yield Firkant(10,5)
    
    def test_areal1(self, firkant1):
        assert firkant1.areal()==50