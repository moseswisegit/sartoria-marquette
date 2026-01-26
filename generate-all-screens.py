#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de génération automatique des écrans manquants pour CouturioShop
"""

import os
import json
from pathlib import Path

# Configuration
BASE_DIR = Path("stitch_onboarding_ia_mesures 3")
PRIMARY_COLOR = "#1A73B5"

# Template HTML de base
HTML_TEMPLATE = """<!DOCTYPE html>
<html class="light" lang="fr">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>{title} - CouturioShop</title>
    <link href="https://fonts.googleapis.com" rel="preconnect" />
    <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect" />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <script>
        tailwind.config = {{
            darkMode: "class",
            theme: {{
                extend: {{
                    colors: {{
                        "primary": "{primary_color}",
                        "background-light": "#f6f6f8",
                    }},
                    fontFamily: {{
                        "display": ["Inter", "sans-serif"]
                    }},
                }},
            }},
        }}
    </script>
    <style>
        body {{
            min-height: max(884px, 100dvh);
        }}
    </style>
</head>
<body class="bg-background-light font-display text-gray-900">
    <div class="relative flex h-auto min-h-screen w-full flex-col overflow-x-hidden max-w-md mx-auto bg-white shadow-xl pb-32">
        <!-- Header -->
        <div class="sticky top-0 z-50 flex items-center bg-white/90 backdrop-blur-md p-4 pb-2 justify-between border-b border-gray-100">
            <button class="flex items-center justify-center rounded-full w-10 h-10 hover:bg-gray-100 transition-colors">
                <span class="material-symbols-outlined text-gray-700">arrow_back</span>
            </button>
            <h2 class="text-gray-900 text-lg font-bold leading-tight">{header_title}</h2>
            <div class="w-10"></div>
        </div>

        <!-- Contenu -->
        <div class="flex flex-col px-4 pt-6 pb-4 gap-6">
            {content}
        </div>
    </div>
</body>
</html>
"""

# Définitions des écrans à créer
SCREENS = {
    # CLIENT - Priorité HAUTE
    "b02_-_recherche_avancée_marketplace": {
        "title": "Recherche Avancée Marketplace",
        "header_title": "Recherche Avancée",
        "content": """
            <div class="space-y-4">
                <div class="relative">
                    <input type="text" placeholder="Rechercher un tailleur, tissu, type de vêtement..." 
                        class="w-full rounded-xl border border-gray-300 bg-white p-3.5 pl-12 text-base text-gray-900 focus:border-primary focus:ring-1 focus:ring-primary outline-none" />
                    <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-gray-400">search</span>
                </div>
                
                <div>
                    <h3 class="text-gray-900 font-bold mb-3">Filtres</h3>
                    <div class="space-y-3">
                        <div>
                            <label class="text-sm font-medium text-gray-700 mb-2 block">Localisation</label>
                            <input type="text" placeholder="Ville ou quartier" 
                                class="w-full rounded-xl border border-gray-300 bg-white p-3 text-base text-gray-900 focus:border-primary focus:ring-1 focus:ring-primary outline-none" />
                        </div>
                        <div>
                            <label class="text-sm font-medium text-gray-700 mb-2 block">Spécialités</label>
                            <div class="flex flex-wrap gap-2">
                                <button class="px-4 py-2 rounded-lg border border-gray-300 bg-white text-sm hover:border-primary hover:bg-primary/5">Boubou</button>
                                <button class="px-4 py-2 rounded-lg border border-gray-300 bg-white text-sm hover:border-primary hover:bg-primary/5">Robe</button>
                                <button class="px-4 py-2 rounded-lg border border-gray-300 bg-white text-sm hover:border-primary hover:bg-primary/5">Costume</button>
                            </div>
                        </div>
                        <div>
                            <label class="text-sm font-medium text-gray-700 mb-2 block">Prix</label>
                            <div class="flex items-center gap-2">
                                <input type="number" placeholder="Min" 
                                    class="w-full rounded-xl border border-gray-300 bg-white p-3 text-base text-gray-900 focus:border-primary focus:ring-1 focus:ring-primary outline-none" />
                                <span class="text-gray-500">-</span>
                                <input type="number" placeholder="Max" 
                                    class="w-full rounded-xl border border-gray-300 bg-white p-3 text-base text-gray-900 focus:border-primary focus:ring-1 focus:ring-primary outline-none" />
                            </div>
                        </div>
                        <div>
                            <label class="text-sm font-medium text-gray-700 mb-2 block">Note minimale</label>
                            <div class="flex items-center gap-2">
                                <input type="range" min="1" max="5" value="3" class="flex-1" />
                                <span class="text-sm text-gray-600">3+</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <button class="w-full flex items-center justify-center rounded-xl h-14 px-5 bg-primary text-white text-base font-bold shadow-lg shadow-primary/20 hover:bg-primary/90 transition-colors">
                    <span>Rechercher</span>
                </button>
            </div>
        """
    },
    "b25_-_notation_&_avis_tailleur": {
        "title": "Notation & Avis Tailleur",
        "header_title": "Noter le tailleur",
        "content": """
            <div class="space-y-6">
                <div class="text-center">
                    <h3 class="text-xl font-bold text-gray-900 mb-2">Comment était votre expérience ?</h3>
                    <p class="text-gray-600 text-sm">Partagez votre avis pour aider d'autres clients</p>
                </div>
                
                <div>
                    <label class="text-sm font-medium text-gray-700 mb-3 block">Note globale</label>
                    <div class="flex items-center justify-center gap-2">
                        <button class="text-4xl text-yellow-400 hover:text-yellow-500">★</button>
                        <button class="text-4xl text-yellow-400 hover:text-yellow-500">★</button>
                        <button class="text-4xl text-yellow-400 hover:text-yellow-500">★</button>
                        <button class="text-4xl text-yellow-400 hover:text-yellow-500">★</button>
                        <button class="text-4xl text-gray-300 hover:text-yellow-400">★</button>
                    </div>
                </div>
                
                <div class="space-y-4">
                    <div>
                        <label class="text-sm font-medium text-gray-700 mb-2 block">Qualité</label>
                        <div class="flex items-center gap-2">
                            <input type="range" min="1" max="5" value="4" class="flex-1" />
                            <span class="text-sm text-gray-600">4/5</span>
                        </div>
                    </div>
                    <div>
                        <label class="text-sm font-medium text-gray-700 mb-2 block">Respect des délais</label>
                        <div class="flex items-center gap-2">
                            <input type="range" min="1" max="5" value="5" class="flex-1" />
                            <span class="text-sm text-gray-600">5/5</span>
                        </div>
                    </div>
                    <div>
                        <label class="text-sm font-medium text-gray-700 mb-2 block">Communication</label>
                        <div class="flex items-center gap-2">
                            <input type="range" min="1" max="5" value="4" class="flex-1" />
                            <span class="text-sm text-gray-600">4/5</span>
                        </div>
                    </div>
                </div>
                
                <div>
                    <label class="text-sm font-medium text-gray-700 mb-2 block">Votre commentaire</label>
                    <textarea rows="4" placeholder="Décrivez votre expérience..." 
                        class="w-full rounded-xl border border-gray-300 bg-white p-3.5 text-base text-gray-900 focus:border-primary focus:ring-1 focus:ring-primary outline-none resize-none"></textarea>
                </div>
                
                <div>
                    <label class="text-sm font-medium text-gray-700 mb-2 block">Photos de la réalisation (optionnel)</label>
                    <div class="border-2 border-dashed border-gray-300 rounded-xl p-8 text-center">
                        <span class="material-symbols-outlined text-4xl text-gray-400 mb-2">add_a_photo</span>
                        <p class="text-sm text-gray-600">Ajouter des photos</p>
                    </div>
                </div>
                
                <button class="w-full flex items-center justify-center rounded-xl h-14 px-5 bg-primary text-white text-base font-bold shadow-lg shadow-primary/20 hover:bg-primary/90 transition-colors">
                    <span>Publier l'avis</span>
                </button>
            </div>
        """
    },
    "b14_-_paramètres_sécurité_confidentialité": {
        "title": "Paramètres Sécurité & Confidentialité",
        "header_title": "Sécurité & Confidentialité",
        "content": """
            <div class="space-y-6">
                <div>
                    <h3 class="text-gray-900 font-bold mb-4">Sécurité du compte</h3>
                    <div class="space-y-3">
                        <div class="flex items-center justify-between p-4 bg-gray-50 rounded-xl border border-gray-200">
                            <div>
                                <p class="font-semibold text-gray-900">Authentification à deux facteurs</p>
                                <p class="text-sm text-gray-600">Protégez votre compte avec 2FA</p>
                            </div>
                            <label class="relative inline-flex items-center cursor-pointer">
                                <input type="checkbox" class="sr-only peer" />
                                <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/20 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
                            </label>
                        </div>
                        <a href="#" class="flex items-center justify-between p-4 bg-white rounded-xl border border-gray-200 hover:border-primary transition-colors">
                            <div>
                                <p class="font-semibold text-gray-900">Changer le mot de passe</p>
                                <p class="text-sm text-gray-600">Mettre à jour votre mot de passe</p>
                            </div>
                            <span class="material-symbols-outlined text-gray-400">chevron_right</span>
                        </a>
                    </div>
                </div>
                
                <div>
                    <h3 class="text-gray-900 font-bold mb-4">Appareils connectés</h3>
                    <div class="space-y-3">
                        <div class="p-4 bg-white rounded-xl border border-gray-200">
                            <div class="flex items-center justify-between mb-2">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-primary">phone_android</span>
                                    <div>
                                        <p class="font-semibold text-gray-900">iPhone 13 Pro</p>
                                        <p class="text-xs text-gray-600">Connecté il y a 2 heures</p>
                                    </div>
                                </div>
                                <span class="text-xs text-green-600 font-medium">Actuel</span>
                            </div>
                        </div>
                        <div class="p-4 bg-white rounded-xl border border-gray-200">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-3">
                                    <span class="material-symbols-outlined text-gray-400">computer</span>
                                    <div>
                                        <p class="font-semibold text-gray-900">MacBook Pro</p>
                                        <p class="text-xs text-gray-600">Connecté il y a 5 jours</p>
                                    </div>
                                </div>
                                <button class="text-red-600 text-sm font-medium hover:underline">Déconnecter</button>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div>
                    <h3 class="text-gray-900 font-bold mb-4">Confidentialité</h3>
                    <div class="space-y-3">
                        <label class="flex items-center justify-between p-4 bg-white rounded-xl border border-gray-200 cursor-pointer">
                            <div>
                                <p class="font-semibold text-gray-900">Profil public</p>
                                <p class="text-sm text-gray-600">Rendre votre profil visible</p>
                            </div>
                            <input type="checkbox" class="h-4 w-4 text-primary border-gray-300 rounded focus:ring-primary" checked />
                        </label>
                        <label class="flex items-center justify-between p-4 bg-white rounded-xl border border-gray-200 cursor-pointer">
                            <div>
                                <p class="font-semibold text-gray-900">Partage de données</p>
                                <p class="text-sm text-gray-600">Autoriser le partage avec partenaires</p>
                            </div>
                            <input type="checkbox" class="h-4 w-4 text-primary border-gray-300 rounded focus:ring-primary" />
                        </label>
                    </div>
                </div>
                
                <div class="pt-4 border-t border-gray-200">
                    <button class="w-full flex items-center justify-center rounded-xl h-12 px-5 bg-red-50 text-red-600 text-base font-semibold border border-red-200 hover:bg-red-100 transition-colors">
                        <span>Désactiver mon compte</span>
                    </button>
                </div>
            </div>
        """
    },
    "b21_-_sélection_adresse_livraison": {
        "title": "Sélection Adresse de Livraison",
        "header_title": "Adresse de livraison",
        "content": """
            <div class="space-y-4">
                <button class="w-full flex items-center justify-center gap-2 rounded-xl h-12 px-5 bg-primary text-white text-base font-semibold hover:bg-primary/90 transition-colors">
                    <span class="material-symbols-outlined">add</span>
                    <span>Ajouter une nouvelle adresse</span>
                </button>
                
                <div class="space-y-3">
                    <label class="flex items-start gap-4 p-4 rounded-xl border-2 border-primary bg-primary/5 cursor-pointer">
                        <input type="radio" name="address" value="1" checked class="mt-1 h-5 w-5 text-primary border-gray-300 focus:ring-primary" />
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-1">
                                <p class="font-semibold text-gray-900">Domicile</p>
                                <span class="text-xs bg-primary/20 text-primary px-2 py-1 rounded">Par défaut</span>
                            </div>
                            <p class="text-sm text-gray-600">Jean Dupont</p>
                            <p class="text-sm text-gray-600">123 Rue de la République</p>
                            <p class="text-sm text-gray-600">Cotonou, Bénin</p>
                            <p class="text-sm text-gray-600 mt-1">+229 XX XX XX XX</p>
                            <div class="flex gap-2 mt-2">
                                <button class="text-xs text-primary hover:underline">Modifier</button>
                                <button class="text-xs text-red-600 hover:underline">Supprimer</button>
                            </div>
                        </div>
                    </label>
                    
                    <label class="flex items-start gap-4 p-4 rounded-xl border border-gray-200 bg-white cursor-pointer hover:border-primary/50 transition-colors">
                        <input type="radio" name="address" value="2" class="mt-1 h-5 w-5 text-primary border-gray-300 focus:ring-primary" />
                        <div class="flex-1">
                            <div class="flex items-center justify-between mb-1">
                                <p class="font-semibold text-gray-900">Travail</p>
                            </div>
                            <p class="text-sm text-gray-600">Jean Dupont</p>
                            <p class="text-sm text-gray-600">456 Avenue de la Paix</p>
                            <p class="text-sm text-gray-600">Cotonou, Bénin</p>
                            <p class="text-sm text-gray-600 mt-1">+229 XX XX XX XX</p>
                            <div class="flex gap-2 mt-2">
                                <button class="text-xs text-primary hover:underline">Modifier</button>
                                <button class="text-xs text-red-600 hover:underline">Supprimer</button>
                            </div>
                        </div>
                    </label>
                </div>
                
                <button class="w-full flex items-center justify-center rounded-xl h-14 px-5 bg-primary text-white text-base font-bold shadow-lg shadow-primary/20 hover:bg-primary/90 transition-colors mt-6">
                    <span>Confirmer l'adresse</span>
                </button>
            </div>
        """
    },
}

def create_screen(folder_name, screen_data):
    """Crée un écran HTML"""
    folder_path = BASE_DIR / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)
    
    file_path = folder_path / "code.html"
    
    html_content = HTML_TEMPLATE.format(
        title=screen_data["title"],
        header_title=screen_data["header_title"],
        content=screen_data["content"],
        primary_color=PRIMARY_COLOR
    )
    
    file_path.write_text(html_content, encoding='utf-8')
    print(f"✅ Créé: {folder_name}/code.html")

def main():
    """Fonction principale"""
    print("🚀 Génération des écrans manquants...\n")
    
    for folder_name, screen_data in SCREENS.items():
        try:
            create_screen(folder_name, screen_data)
        except Exception as e:
            print(f"❌ Erreur pour {folder_name}: {e}")
    
    print(f"\n✨ {len(SCREENS)} écrans créés avec succès!")

if __name__ == "__main__":
    main()
