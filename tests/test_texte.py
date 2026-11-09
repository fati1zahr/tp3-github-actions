import pytest
from app.texte import nettoyer_texte

@pytest.mark.parametrize("entree, attendu", [
    (" BONJOUR monde ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),              
    ("   ", ""),             
    ("PYTHON", "python")     
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu

def test_nettoyer_texte_type_invalide():
    with pytest.raises(TypeError):
        nettoyer_texte(123)
    
    with pytest.raises(TypeError):
        nettoyer_texte(None)

def test_nettoyer_texte_deja_propre_idempotence():
    texte_initial = "nlp et intelligence artificielle"
    premier_nettoyage = nettoyer_texte(texte_initial)
    second_nettoyage = nettoyer_texte(premier_nettoyage)
    
    assert premier_nettoyage == second_nettoyage