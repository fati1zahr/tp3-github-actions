from unittest.mock import patch

import pytest 
from app.surveillance import surveiller 

def test_surveillance_taux_eleve():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.15)
        assert resultat == "alerte"
        notifier.assert_called_once_with("Taux eleve")

def test_surveillance_taux_normal():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.05)
        assert resultat == "ok"
        notifier.assert_not_called()

def test_surveillance_taux_exact():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.10)
        assert resultat == "ok"
        notifier.assert_not_called()

def test_serveillance_erreur_service_notification():
    with patch("app.surveillance.envoyer_notification") as notifier:
        notifier.side_effect = RuntimeError("Service indisponible")

        with pytest.raises(RuntimeError, match="Service indisponible"):
            surveiller(0.20)