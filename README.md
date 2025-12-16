# 🧰 NTL-SysToolbox

**Outil d'administration système pour NordTransit Logistics**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Academic-green.svg)]()
[![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen.svg)]()

---

## 📋 Table des Matières

1. [Vue d'ensemble](#-vue-densemble)
2. [Architecture du projet](#-architecture-du-projet)
3. [Prérequis](#-prérequis)
4. [Installation](#-installation)
5. [Configuration](#-configuration)
6. [Utilisation](#-utilisation)
7. [Modules](#-modules)
8. [Exemples](#-exemples)
9. [Dépannage](#-dépannage)
10. [Contribution](#-contribution)

---

## 🎯 Vue d'ensemble

NTL-SysToolbox est un outil CLI développé en Python qui regroupe trois modules essentiels pour l'administration système de NordTransit Logistics :

### Module 1 : 🔍 Diagnostic
- Vérification des services Active Directory et DNS
- Test de connexion à la base MySQL WMS
- Monitoring des ressources serveurs (CPU, RAM, Disque, Uptime)
- Support Windows et Linux
- Génération de rapports JSON horodatés

### Module 2 : 💾 Sauvegarde WMS
- Sauvegarde complète de la base MySQL (mysqldump)
- Export de tables spécifiques au format CSV
- Vérification d'intégrité des backups
- Gestion des versions et historiques
- Exports JSON structurés

### Module 3 : 🧾 Audit d'Obsolescence
- Scan réseau pour détecter les équipements
- Identification automatique des OS et versions
- Vérification des dates End-of-Life (EOL) via API
- Classification des systèmes (EOL, Support actif, Bientôt terminé)
- Rapport d'audit avec statistiques détaillées

---

## 📂 Architecture du Projet

```
NTL-SysToolbox/
│
├── Dev/                          # 📁 Code source principal
│   ├── main.py                   # 🚀 Point d'entrée - Menu CLI interactif
│   ├── config.py                 # ⚙️  Configuration centralisée
│   ├── utils.py                  # 🔧 Fonctions utilitaires partagées
│   ├── save.py                   # 💾 Module Sauvegarde WMS
│   ├── diag.py                   # 🔍 Module Diagnostic
│   └── audit.py                  # 🧾 Module Audit d'obsolescence
│
├── out/                          # 📤 Répertoire de sortie (auto-généré)
│   ├── backups/                  # Sauvegardes SQL/CSV
│   ├── diagnostics/              # Résultats diagnostics JSON
│   └── audits/                   # Rapports d'audit JSON
│
├── .env                          # 🔐 Configuration locale (NE PAS COMMITER)
├── .env.example                  # 📝 Template de configuration
├── .gitignore                    # 🚫 Fichiers à ignorer par Git
│
├── requirements.txt              # 📦 Dépendances Python complètes
├── requirements-minimal.txt      # 📦 Dépendances minimales
│
├── setup.sh                      # 🛠️  Script d'installation automatique
├── quick-start.sh                # ⚡ Script de démarrage rapide
├── test-all.sh                   # 🧪 Tests automatiques
├── clean-outputs.sh              # 🧹 Nettoyage des outputs
├── Makefile                      # 🔨 Commandes make pratiques
│
├── wms_test_db.sql               # 🗄️  Base de données de test
├── README.md                     # 📖 Ce fichier
└── GUIDE_COMPLET_PROJET.md       # 📚 Documentation détaillée
```

---

## 📄 Description des Fichiers

### 🐍 Fichiers Python (Dev/)

| Fichier | Lignes | Rôle | Fonctions Principales |
|---------|--------|------|----------------------|
| **main.py** | ~400 | Point d'entrée principal | `run_interactive()`, `run_batch()`, `run_all_modules()` |
| **config.py** | ~250 | Configuration centralisée | `Config.MYSQL_CONFIG`, `Config.validate_config()`, `Config.display_config()` |
| **utils.py** | ~450 | Utilitaires partagés | `save_json_output()`, `format_size()`, `print_success()`, `validate_ip()` |
| **save.py** | ~550 | Module Sauvegarde | `backup_full_sql()`, `export_table_to_csv()`, `verify_backup_integrity()` |
| **diag.py** | ~600 | Module Diagnostic | `check_ad_dns_services()`, `check_mysql_wms()`, `check_server_resources()` |
| **audit.py** | ~650 | Module Audit | `scan_network_simple()`, `check_eol_status()`, `run_full_audit()` |

#### 🚀 main.py - Point d'entrée
**Responsabilités :**
- Gestion du menu interactif CLI
- Mode batch pour automatisation
- Orchestration des 3 modules
- Gestion globale des erreurs
- Création des rapports consolidés

**Modes d'exécution :**
- Interactif : Menu avec choix utilisateur
- Batch : Ligne de commande avec arguments
- Debug : Mode verbeux pour développement

#### ⚙️ config.py - Configuration
**Responsabilités :**
- Chargement des variables d'environnement (.env)
- Paramètres MySQL, AD/DNS, réseaux
- Validation de la configuration
- Gestion des chemins (outputs)
- Affichage de la configuration

**Variables clés :**
```python
Config.MYSQL_CONFIG      # Paramètres MySQL
Config.AD_SERVERS        # Serveurs Active Directory
Config.SCAN_NETWORKS     # Réseaux à scanner
Config.OUTPUT_DIR        # Répertoire de sortie
```

#### 🔧 utils.py - Utilitaires
**Responsabilités :**
- Gestion des fichiers JSON
- Formatage (dates, tailles, pourcentages)
- Validation (IP, ports, réseaux CIDR)
- Affichage console avec icônes
- Création de résultats standardisés

**Fonctions utiles :**
```python
save_json_output(data, filepath)      # Sauvegarder JSON
format_size(bytes)                    # 1234567890 → "1.15 GB"
validate_network(cidr)                # Valider 192.168.1.0/24
print_success(message)                # ✅ Message
create_result(status, message)        # Résultat standardisé
```

#### 💾 save.py - Module Sauvegarde
**Responsabilités :**
- Connexion et test MySQL
- Sauvegarde complète (mysqldump)
- Export CSV avec filtres
- Liste des tables avec statistiques
- Vérification d'intégrité

**Classe principale :**
```python
class WMSBackup:
    test_connection()              # Tester connexion
    backup_full_sql(include_data)  # Sauvegarde SQL
    export_table_to_csv(table)     # Export CSV
    list_tables()                  # Lister tables
    verify_backup_integrity(file)  # Vérifier backup
```

#### 🔍 diag.py - Module Diagnostic
**Responsabilités :**
- Vérification services AD/DNS (ports 389, 636, 53)
- Test connexion MySQL WMS
- Ressources système Linux (via /proc)
- Ressources système Windows (via WMIC)
- Détection automatique de l'OS

**Classe principale :**
```python
class SystemDiagnostic:
    check_ad_dns_services()        # Vérifie AD/DNS
    check_mysql_wms()              # Teste MySQL
    check_server_resources(os)     # Ressources CPU/RAM/Disque
    run_full_diagnostic()          # Diagnostic complet
```

#### 🧾 audit.py - Module Audit
**Responsabilités :**
- Scan réseau avec ping
- Détection OS (via TTL)
- Résolution DNS inverse
- API endoflife.date pour dates EOL
- Génération de rapports d'audit

**Classe principale :**
```python
class NetworkAudit:
    scan_network_simple(cidr)      # Scanner réseau
    detect_os_simple(ip)           # Détecter OS
    get_eol_info(product)          # Récupérer infos EOL
    check_eol_status(os, version)  # Vérifier statut EOL
    run_full_audit(networks)       # Audit complet
```

### 🛠️ Scripts et Configuration

| Fichier | Type | Utilité |
|---------|------|---------|
| **setup.sh** | Bash | Installation automatique complète |
| **quick-start.sh** | Bash | Lancement rapide après installation |
| **test-all.sh** | Bash | Tests automatiques de tous les modules |
| **clean-outputs.sh** | Bash | Nettoyage des anciens outputs |
| **Makefile** | Make | Commandes pratiques (make help) |
| **.env.example** | Config | Template de configuration |
| **requirements.txt** | Pip | Dépendances Python |
| **wms_test_db.sql** | SQL | Base de données de test |

---

## 🔧 Prérequis

### Système
- **OS** : Linux (Ubuntu 20.04+, Debian 10+, CentOS 8+) ou Windows 10+
- **Python** : 3.8 ou supérieur
- **MySQL** : 5.7+ ou 8.0+ (serveur)
- **MySQL Client** : pour mysqldump (sauvegarde)
- **Espace disque** : 500 MB minimum
- **RAM** : 512 MB minimum
- **Connexion Internet** : Pour l'API endoflife.date (audit)

### Permissions
- Accès réseau aux serveurs AD/DNS (ports 389, 636, 53)
- Accès MySQL avec droits SELECT et LOCK TABLES
- Droits d'écriture dans le répertoire de sortie
- (Optionnel) Droits root/admin pour scan réseau avancé

---

## 📥 Installation

### Méthode 1 : Installation Automatique (Recommandée)

```bash
# 1. Cloner ou télécharger le projet
git clone <url-du-repo>
cd NTL-SysToolbox

# 2. Rendre le script exécutable
chmod +x setup.sh

# 3. Lancer l'installation
./setup.sh

# Le script va :
# - Vérifier Python 3 et MySQL
# - Créer l'environnement virtuel
# - Installer les dépendances
# - Créer le fichier .env
# - Créer les répertoires nécessaires
# - Tester la connexion MySQL (optionnel)
```

### Méthode 2 : Installation Manuelle

```bash
# 1. Créer l'environnement virtuel
python3 -m venv venv

# 2. Activer l'environnement virtuel
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Mettre à jour pip
pip install --upgrade pip

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Copier et configurer .env
cp .env.example .env
nano .env  # Éditer avec vos paramètres

# 6. Créer les répertoires de sortie
mkdir -p out/backups out/diagnostics out/audits
```

### Installation avec Make

```bash
# Installation complète
make install

# Ou configuration rapide
make setup
```

---

## ⚙️ Configuration

### Fichier .env

Le fichier `.env` contient tous les paramètres de configuration. **Ne jamais le commiter dans Git !**

```bash
# Copier le template
cp .env.example .env

# Éditer le fichier
nano .env
```

### Paramètres MySQL (Obligatoire pour le module Sauvegarde)

```bash
MYSQL_HOST=localhost           # Adresse du serveur MySQL
MYSQL_PORT=3306                # Port MySQL (défaut: 3306)
MYSQL_USER=root                # Utilisateur MySQL
MYSQL_PASSWORD=VotreMotDePasse # Mot de passe MySQL
MYSQL_DATABASE=wms_ntl         # Nom de la base de données
```

### Paramètres Diagnostic

```bash
# Serveurs Active Directory (séparés par virgules)
AD_SERVERS=192.168.10.10,192.168.10.11
AD_DOMAIN=ntl.local

# Serveurs DNS
DNS_SERVERS=192.168.10.10,192.168.10.11

# Base de données WMS
WMS_DB_HOST=192.168.10.21
WMS_DB_PORT=3306
```

### Paramètres Audit

```bash
# Réseaux à scanner (CIDR, séparés par virgules)
SCAN_NETWORKS=192.168.10.0/24,192.168.20.0/24,192.168.30.0/24

# Source de données EOL
EOL_DATA_SOURCE=https://endoflife.date/api/

# Timeout pour les scans (secondes)
SCAN_TIMEOUT=30
```

### Paramètres Généraux

```bash
# Répertoire de sortie
OUTPUT_DIR=out

# Mode debug (True/False)
DEBUG=False
```

### Vérifier la Configuration

```bash
# Via le menu principal
cd Dev
python3 main.py
# Puis choisir option 5 (Configuration)

# Ou directement
python3 Dev/config.py

# Avec Make
make config
```

---

## 🚀 Utilisation

### Démarrage Rapide

```bash
# Lancer l'application en mode interactif
cd Dev
python3 main.py

# Ou avec le script
./quick-start.sh

# Ou avec Make
make run
```

### Mode Interactif (Recommandé)

Le mode interactif affiche un menu avec toutes les options :

```
╔════════════════════════════════════════════════════════╗
║        🧰  NTL-SysToolbox - Menu Principal           ║
╚════════════════════════════════════════════════════════╝

📋 Modules disponibles:
  1. 🔍 Module Diagnostic
  2. 💾 Module Sauvegarde WMS
  3. 🧾 Module Audit d'obsolescence
  4. 🚀 Exécuter tous les modules
  5. ⚙️  Configuration et informations
  0. ❌ Quitter
```

### Mode Batch (Automatisation)

Pour intégrer dans des scripts ou cron jobs :

```bash
cd Dev

# Module Diagnostic seul
python3 main.py --mode diagnostic

# Module Sauvegarde seul
python3 main.py --mode sauvegarde

# Module Audit seul
python3 main.py --mode audit

# Tous les modules en séquence
python3 main.py --mode all

# Mode debug
python3 main.py --mode all --debug
```

### Avec Make

```bash
make diagnostic    # Module diagnostic
make backup        # Module sauvegarde
make audit         # Module audit
make all           # Tous les modules
```

### Exécution Planifiée (Cron)

```bash
# Éditer crontab
crontab -e

# Sauvegarde quotidienne à 2h du matin
0 2 * * * cd /chemin/vers/NTL-SysToolbox/Dev && /chemin/vers/venv/bin/python3 main.py --mode sauvegarde

# Diagnostic toutes les 6 heures
0 */6 * * * cd /chemin/vers/NTL-SysToolbox/Dev && /chemin/vers/venv/bin/python3 main.py --mode diagnostic

# Audit hebdomadaire le lundi à 3h
0 3 * * 1 cd /chemin/vers/NTL-SysToolbox/Dev && /chemin/vers/venv/bin/python3 main.py --mode audit
```

---

## 📦 Modules

### 🔍 Module Diagnostic

#### Fonctionnalités
- ✅ Vérification services AD/DNS (ports 389, 636, 53)
- ✅ Test connexion MySQL WMS
- ✅ Ressources Linux : CPU load, RAM, Disque, Uptime
- ✅ Ressources Windows : CPU %, RAM, Disque via WMIC
- ✅ Détection automatique de l'OS

#### Utilisation

**Mode interactif :**
```bash
cd Dev
python3 diag.py
```

**Options disponibles :**
1. Diagnostic complet
2. Vérifier AD/DNS seulement
3. Vérifier MySQL WMS seulement
4. Vérifier ressources serveur local

**Mode batch :**
```bash
python3 main.py --mode diagnostic
```

**Exemple de sortie :**
```json
{
  "timestamp": "2025-12-16T15:30:00",
  "diagnostics": [
    {
      "type": "ad_dns_services",
      "result": {
        "overall_status": "success",
        "servers": [
          {
            "server": "192.168.10.10",
            "status": "operational",
            "checks": [...]
          }
        ]
      }
    },
    {
      "type": "mysql_wms",
      "result": {
        "status": "success",
        "host": "192.168.10.21"
      }
    }
  ],
  "summary": {
    "total_checks": 3,
    "successful": 3,
    "failed": 0
  }
}
```

---

### 💾 Module Sauvegarde WMS

#### Fonctionnalités
- ✅ Sauvegarde complète SQL avec mysqldump
- ✅ Sauvegarde structure seulement (sans données)
- ✅ Export de tables en CSV
- ✅ Export avec filtres WHERE et LIMIT
- ✅ Liste des tables avec statistiques
- ✅ Vérification d'intégrité des backups

#### Utilisation

**Mode interactif :**
```bash
cd Dev
python3 save.py
```

**Options disponibles :**
1. Tester la connexion MySQL
2. Sauvegarde complète SQL (avec données)
3. Sauvegarde structure seulement
4. Exporter une table en CSV
5. Lister les tables disponibles
6. Vérifier une sauvegarde

**Mode batch :**
```bash
python3 main.py --mode sauvegarde
```

**Exemples de commandes :**
```bash
# Sauvegarde complète
make backup

# Test connexion
python3 -c "from save import WMSBackup; b = WMSBackup(); print(b.test_connection())"
```

**Exemple de sortie :**
```json
{
  "timestamp": "2025-12-16T15:45:00",
  "status": "success",
  "message": "Sauvegarde créée avec succès",
  "filepath": "out/backups/wms_backup_20251216_154500.sql",
  "size_bytes": 2564321,
  "size_mb": 2.45,
  "method": "mysqldump"
}
```

---

### 🧾 Module Audit d'Obsolescence

#### Fonctionnalités
- ✅ Scan réseau avec ping
- ✅ Détection OS simple (via TTL)
- ✅ Résolution DNS inverse
- ✅ API endoflife.date pour dates EOL
- ✅ Classification : EOL, Actif, Bientôt terminé
- ✅ Rapport d'audit avec statistiques

#### Utilisation

**Mode interactif :**
```bash
cd Dev
python3 audit.py
```

**Options disponibles :**
1. Audit complet (tous les réseaux)
2. Scanner un réseau spécifique
3. Lister les produits EOL disponibles
4. Afficher versions EOL d'un produit
5. Vérifier statut EOL d'un système

**Mode batch :**
```bash
python3 main.py --mode audit
```

**Exemple de sortie :**
```json
{
  "timestamp": "2025-12-16T16:00:00",
  "total_hosts": 12,
  "summary": {
    "eol_systems": 2,
    "ending_soon": 1,
    "active_support": 7,
    "unknown_status": 2
  },
  "hosts": [
    {
      "ip": "192.168.10.21",
      "hostname": "wms-db",
      "os": "Linux/Unix",
      "eol_info": {
        "os": "Ubuntu",
        "version": "20.04",
        "eol_date": "2025-04-01",
        "is_eol": false,
        "support_status": "active"
      }
    }
  ]
}
```

#### Produits EOL Supportés
- Ubuntu, Debian, CentOS, RHEL
- Windows, Windows Server
- macOS
- MySQL, PostgreSQL
- Et 200+ autres produits

---

## 💡 Exemples d'Utilisation

### Exemple 1 : Diagnostic Quotidien

```bash
#!/bin/bash
# Script: daily-diag.sh

cd /opt/NTL-SysToolbox/Dev
source ../venv/bin/activate

# Exécuter diagnostic
python3 main.py --mode diagnostic

# Envoyer le rapport par email
REPORT=$(ls -t ../out/diagnostics/*.json | head -1)
mail -s "Diagnostic NTL $(date +%Y-%m-%d)" admin@ntl.fr < $REPORT
```

### Exemple 2 : Sauvegarde Automatisée

```bash
#!/bin/bash
# Script: backup-and-rotate.sh

cd /opt/NTL-SysToolbox/Dev
source ../venv/bin/activate

# Sauvegarde
python3 main.py --mode sauvegarde

# Garder seulement les 7 dernières sauvegardes
cd ../out/backups
ls -t *.sql | tail -n +8 | xargs rm -f

# Copier vers stockage distant
rsync -az *.sql backup-server:/backups/ntl/
```

### Exemple 3 : Audit Mensuel

```bash
#!/bin/bash
# Script: monthly-audit.sh

cd /opt/NTL-SysToolbox/Dev
source ../venv/bin/activate

# Audit complet
python3 main.py --mode audit

# Générer rapport HTML (à implémenter)
AUDIT=$(ls -t ../out/audits/*.json | head -1)
python3 generate_report.py $AUDIT
```

---

## 🧪 Tests

### Tests Automatiques

```bash
# Tous les tests
./test-all.sh

# Ou avec Make
make test
```

### Tests Manuels

```bash
# Test configuration
python3 Dev/config.py

# Test utilitaires
python3 Dev/utils.py

# Test connexion MySQL
make db-check

# Test de chaque module
cd Dev
python3 diag.py
python3 save.py
python3 audit.py
```

### Base de Données de Test

```bash
# Créer la base
mysql -u root -p -e "CREATE DATABASE wms_ntl;"

# Importer le schéma
mysql -u root -p wms_ntl < wms_test_db.sql

# Vérifier
mysql -u root -p -e "USE wms_ntl; SHOW TABLES;"

# Avec Make
make db-create
make db-import
```

---

## 🐛 Dépannage

### Problème : "Module not found"

**Cause :** Environnement virtuel non activé ou dépendances manquantes

**Solution :**
```bash
# Vérifier l'environnement
which python3
# Doit pointer vers venv/bin/python3

# Activer l'environnement
source venv/bin/activate

# Réinstaller les dépendances
pip install -r requirements.txt
```

### Problème : "Access denied" MySQL

**Cause :** Identifiants incorrects ou permissions insuffisantes

**Solution :**
```bash
# Vérifier la connexion
mysql -h localhost -u root -p

# Vérifier les permissions
mysql -u root -p -e "SHOW GRANTS FOR 'votre_user'@'localhost';"

# Créer un utilisateur dédié
mysql -u root -p
CREATE USER 'ntl_backup'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, LOCK TABLES ON wms_ntl.* TO 'ntl_backup'@'localhost';
FLUSH PRIVILEGES;

# Mettre à jour .env
nano .env
```

### Problème : "mysqldump not found"

**Cause :** MySQL client non installé

**Solution :**
```bash
# Ubuntu/Debian
sudo apt install mysql-client

# CentOS/RHEL
sudo yum install mysql

# macOS
brew install mysql-client

# Windows : Installer MySQL Community Server
```

### Problème : "Can't connect to MySQL server"

**Cause :** Serveur MySQL arrêté ou port fermé

**Solution :**
```bash
# Vérifier le statut
sudo systemctl status mysql

# Démarrer MySQL
sudo systemctl start mysql

# Vérifier le port
sudo netstat -tlnp | grep 3306
```

### Problème : Scan réseau trop lent

**Cause :** Timeout trop élevé ou trop d'hôtes

**Solution :**
```bash
# Réduire le timeout dans .env
SCAN_TIMEOUT=1

# Ou scanner un sous-réseau plus petit
python3 audit.py
# Puis choisir option 2 et entrer : 192.168.10.0/28
```

### Problème : API EOL inaccessible

**Cause :** Pas de connexion Internet ou API down

**Solution :**
```bash
# Tester la connexion
curl https://endoflife.date/api/ubuntu.json

# Vérifier le proxy si nécessaire
export http_proxy=http://proxy:8080
export https_proxy=http://proxy:8080
```

---

## 📊 Structure des Outputs

Tous les résultats sont sauvegardés dans `out/` :

### Format JSON Standard

```json
{
  "timestamp": "2025-12-16T15:30:00",
  "status": "success|error|warning",
  "message": "Description du résultat",
  "...": "Données spécifiques au module"
}
```

### Fichiers Générés

```
out/
├── backups/
│   ├── wms_backup_20251216_154500.sql    # Sauvegarde complète
│   ├── orders_20251216_154530.csv        # Export CSV
│   └── backup_full_20251216_154500.json  # Métadonnées
│
├── diagnostics/
│   └── diagnostic_20251216_160000.json   # Résultat diagnostic
│
└── audits/
    └── audit_20251216_170000.json        # Rapport d'audit
```

---

## 🔐 Sécurité

### Bonnes Pratiques

✅ **À FAIRE :**
- Utiliser des comptes avec permissions minimales
- Ne jamais commiter le fichier `.env`
- Chiffrer les sauvegardes sensibles
- Limiter l'accès au répertoire `out/`
- Utiliser des mots de passe forts
- Nettoyer régulièrement les anciens backups
- Restreindre les accès réseau (firewall)

❌ **À ÉVITER :**
- Stocker des mots de passe en clair dans les scripts
- Exécuter avec des droits root sans raison
- Laisser des backups non protégés
- Exposer le répertoire `out/` sur le web
- Utiliser le compte root MySQL

### Permissions Recommandées

```bash
# Fichiers de configuration
chmod 600 .env

# Scripts
chmod 755 *.sh

# Répertoire outputs
chmod 750 out/
chmod 700 out/backups/

# Propriétaire dédié
chown -R ntl-admin:ntl-admin /opt/NTL-SysToolbox
```

---

## 📚 Documentation Additionnelle

- **Cahier des charges :** `Sujet_N°1.pdf`
- **Guide complet :** `GUIDE_COMPLET_PROJET.md`
- **Base de données :** `wms_test_db.sql` (commentée)
- **API EOL :** https://endoflife.date/docs/api/

---

## 🤝 Contribution

### Équipe Projet
- [Votre Nom] - [Rôle]
- [Nom] - [Rôle]
- [Nom] - [Rôle]
- [Nom] - [Rôle]

### Encadrement
- Encadrant pédagogique : [Nom]

---

## 📄 Licence

Projet académique - MSPR NTL-SysToolbox  
Tous droits réservés © 2025

---

## 📞 Support

Pour toute question ou problème :

1. Consulter la section [Dépannage](#-dépannage)
2. Vérifier la configuration : `python3 main.py` → Option 5
3. Consulter les logs : `cat out/*.json`
4. Contacter l'encadrant pédagogique

---

## 🎯 Roadmap

### Version Actuelle : 1.0.0
- ✅ Module Diagnostic fonctionnel
- ✅ Module Sa
