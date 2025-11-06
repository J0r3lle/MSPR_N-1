#!/usr/bin/env python3
# ===========================================================
# Version batch du CLI NTL-SysToolbox
# Utilisation : python3 ntl_systoolbox.py [diagnostic|sauvegarde|audit|all]
# ===========================================================

import os
import sys
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 60)
    print("        🧰  NTL-SysToolbox — Mode batch")
    print("=" * 60)
    print(f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def module_diagnostic():
    print("🔍 Module Diagnostic (simulation)")
    print("→ Vérification de l’AD, DNS, et du serveur MySQL...")
    print("✅ Tous les services sont opérationnels.\n")

def module_sauvegarde():
    print("💾 Module Sauvegarde WMS (simulation)")
    print("→ Sauvegarde complète de la base de données WMS...")
    print("✅ Sauvegarde réalisée avec succès (fichier simulé).\n")

def module_audit():
    print("🧾 Module Audit d’obsolescence (simulation)")
    print("→ Scan du réseau 192.168.10.0/24 en cours...")
    print("✅ 12 hôtes détectés — 2 systèmes obsolètes trouvés.\n")

def run_batch(mode: str):
    clear_screen()
    print_header()

    if mode == "diagnostic":
        module_diagnostic()
    elif mode == "sauvegarde":
        module_sauvegarde()
    elif mode == "audit":
        module_audit()
    elif mode == "all":
        module_diagnostic()
        module_sauvegarde()
        module_audit()
    else:
        print("❌ Option invalide.")
        print("Utilisation : python3 ntl_systoolbox.py [diagnostic|sauvegarde|audit|all]")
        sys.exit(1)

    print("✅ Exécution terminée.\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Aucun argument fourni.")
        print("Utilisation : python3 ntl_systoolbox.py [diagnostic|sauvegarde|audit|all]")
        sys.exit(1)

    try:
        mode = sys.argv[1].lower()
        run_batch(mode)
    except KeyboardInterrupt:
        print("\n\nArrêt du programme par l’utilisateur. 👋")
