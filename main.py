#!/usr/bin/env python3
# ===========================================================
# Mini version de test du CLI NTL-SysToolbox
# Sans dépendance externe
# ===========================================================

import os
from datetime import datetime

# -----------------------------------------------------------
# Fonctions utilitaires
# -----------------------------------------------------------

def clear_screen():
    """Nettoie l’écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Affiche le titre du programme."""
    print("=" * 60)
    print("        🧰  NTL-SysToolbox — CLI de test")
    print("=" * 60)
    print(f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def press_enter():
    """Attend que l’utilisateur appuie sur Entrée."""
    input("\nAppuie sur Entrée pour continuer...")

# -----------------------------------------------------------
# Simulations des modules
# -----------------------------------------------------------

def module_diagnostic():
    clear_screen()
    print_header()
    print("🔍 Module Diagnostic (simulation)")
    print("→ Vérification de l’AD, DNS, et du serveur MySQL...")
    print("✅ Tous les services sont opérationnels.")
    press_enter()

def module_sauvegarde():
    clear_screen()
    print_header()
    print("💾 Module Sauvegarde WMS (simulation)")
    print("→ Sauvegarde complète de la base de données WMS...")
    print("✅ Sauvegarde réalisée avec succès (fichier simulé).")
    press_enter()

def module_audit():
    clear_screen()
    print_header()
    print("🧾 Module Audit d’obsolescence (simulation)")
    print("→ Scan du réseau 192.168.10.0/24 en cours...")
    print("✅ 12 hôtes détectés — 2 systèmes obsolètes trouvés.")
    press_enter()

# -----------------------------------------------------------
# Menu principal
# -----------------------------------------------------------

def main_menu():
    while True:
        clear_screen()
        print_header()
        print("🔹 MENU PRINCIPAL 🔹\n")
        print("1️⃣  Module Diagnostic")
        print("2️⃣  Module Sauvegarde WMS")
        print("3️⃣  Module Audit d’obsolescence")
        print("0️⃣  Quitter\n")

        choix = input("Sélectionnez une option : ").strip()

        if choix == "1":
            module_diagnostic()
        elif choix == "2":
            module_sauvegarde()
        elif choix == "3":
            module_audit()
        elif choix == "0":
            print("\n👋 Merci d’avoir utilisé NTL-SysToolbox (test). À bientôt !")
            break
        else:
            print("❌ Choix invalide.")
            press_enter()

# -----------------------------------------------------------
# Point d’entrée
# -----------------------------------------------------------

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nArrêt du programme par l’utilisateur. 👋")
