import pytest
from app.reservation import Stock, Reservation

@pytest.fixture
def stock():
    return Stock(5)

def test_reservation_confirmee(stock):
    reservation = Reservation(stock)
    statut = reservation.reserver(2)
    assert statut == "confirmee"
    assert stock.quantite == 3

def test_reservation_refusee(stock):
    reservation = Reservation(stock)
    statut = reservation.reserver(6)
    assert statut == "refusee"
    assert stock.quantite == 5

def test_reservation_stock_epuise(stock):
    reservation = Reservation(stock)
    statut = reservation.reserver(5)
    assert statut == "confirmee"
    assert stock.quantite == 0