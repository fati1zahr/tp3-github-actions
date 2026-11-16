pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Récupération du code source depuis GitHub
                checkout scm
            }
        }
        
        stage('Configuration Environnement') {
            steps {
                // Affichage de la version de Python pour vérification
                bat 'python --version'
                
                // Installation des dépendances de test
                bat 'pip install -r requirements-dev.txt'
            }
        }

        stage('Exécution des Tests & Couverture') {
            steps {
                // Exécution des tests Pytest avec rapport de couverture et seuil minimal
                bat 'python -m pytest -v --cov=app --cov-report term-missing --cov-fail-under=80'
            }
        }
    }
}