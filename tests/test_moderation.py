from unittest.mock import Mock
import pytest
from app.moderation import decider

# 1 et 2. Test pour le cas "spam" -> décision "bloquer" + vérification de l'appel
def test_decider_spam():
    modele = Mock()
    # Configuration du faux modèle pour qu'il retourne "spam"
    modele.predict.return_value = "spam"
    
    # Appel de la fonction
    resultat = decider(modele, "Offre miracle")
    
    # Vérifications
    assert resultat == "bloquer"
    # Vérifie que la méthode predict a bien été appelée exactement une fois avec cet argument
    modele.predict.assert_called_once_with("Offre miracle")

# 3. Second test indépendant où le modèle retourne "normal" -> décision "autoriser"
def test_decider_normal():
    modele = Mock()
    # Configuration du faux modèle pour qu'il retourne "normal"
    modele.predict.return_value = "normal"
    
    resultat = decider(modele, "Bonjour, je souhaite des informations.")
    
    assert resultat == "autoriser"
    modele.predict.assert_called_once_with("Bonjour, je souhaite des informations.")

# Bonus : Vérifier la propagation d'une erreur (modèle indisponible)
def test_decider_modele_indisponible():
    modele = Mock()
    # Configuration d'une exception levée lors de l'appel à predict
    modele.predict.side_effect = RuntimeError("Modele indisponible")
    
    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Test message")