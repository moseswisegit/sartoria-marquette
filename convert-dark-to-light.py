#!/usr/bin/env python3
"""
Script pour convertir tous les écrans avec fond noir en fond blanc
"""
import os
import re
from pathlib import Path

# Dossier contenant les maquettes
BASE_DIR = Path("stitch_onboarding_ia_mesures 3")

# Remplacements à effectuer
replacements = [
    # Classes dark:bg-background-dark → bg-white ou bg-background-light
    (r'dark:bg-background-dark', 'bg-white'),
    (r'dark:bg-\[#1e293b\]', 'bg-white'),
    (r'dark:bg-\[#131022\]', 'bg-white'),
    (r'dark:bg-\[#0f172a\]', 'bg-white'),
    
    # Classes dark:bg-gray-* → bg-white ou bg-gray-50
    (r'dark:bg-gray-900', 'bg-white'),
    (r'dark:bg-gray-800', 'bg-gray-50'),
    (r'dark:bg-gray-700', 'bg-gray-100'),
    (r'dark:bg-slate-800', 'bg-gray-50'),
    (r'dark:bg-slate-900', 'bg-white'),
    
    # Classes dark:text-white → text-gray-900
    (r'dark:text-white', 'text-gray-900'),
    (r'dark:text-slate-400', 'text-gray-600'),
    (r'dark:text-gray-400', 'text-gray-600'),
    (r'dark:text-gray-300', 'text-gray-700'),
    (r'dark:text-gray-500', 'text-gray-700'),
    
    # Classes dark:border-* → border-gray-300
    (r'dark:border-gray-700', 'border-gray-300'),
    (r'dark:border-gray-800', 'border-gray-200'),
    
    # Classes dark:hover:*
    (r'dark:hover:bg-gray-800', 'hover:bg-gray-100'),
    (r'dark:hover:bg-gray-700', 'hover:bg-gray-200'),
    (r'dark:hover:text-primary', 'hover:text-primary'),
    (r'dark:hover:text-gray-300', 'hover:text-gray-700'),
    
    # Classes dark:ring-*
    (r'dark:ring-white/5', 'ring-gray-200/10'),
    (r'dark:ring-white/10', 'ring-gray-200/20'),
    
    # Classes dark:shadow-*
    (r'dark:shadow-\[0_8px_30px_rgb\(0,0,0,0\.3\)\]', 'shadow-lg'),
    (r'dark:shadow-\[.*?\]', 'shadow-lg'),
    
    # Classes dark:bg-* avec opacité
    (r'dark:bg-primary/10', 'bg-primary/5'),
    (r'dark:bg-primary/20', 'bg-primary/10'),
    
    # Supprimer les classes dark: restantes
    (r'\s+dark:[^\s]+', ''),  # Supprime les classes dark: restantes
]

def process_file(file_path):
    """Traite un fichier HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Appliquer tous les remplacements
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        # Remplacer class="dark" par class="light" dans les balises html
        content = re.sub(r'<html\s+class="dark"', '<html class="light"', content)
        content = re.sub(r'<html\s+class=\'dark\'', '<html class="light"', content)
        
        # Nettoyer les espaces multiples créés par les suppressions
        content = re.sub(r'\s{2,}', ' ', content)
        content = re.sub(r'\s+class="', ' class="', content)
        content = re.sub(r'\s+class=\'', ' class=\'', content)
        
        # Écrire seulement si le contenu a changé
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur lors du traitement de {file_path}: {e}")
        return False

def main():
    """Fonction principale"""
    if not BASE_DIR.exists():
        print(f"Erreur: Le dossier {BASE_DIR} n'existe pas")
        return
    
    html_files = list(BASE_DIR.rglob("code.html"))
    print(f"Trouvé {len(html_files)} fichiers HTML à traiter...")
    
    modified = 0
    for file_path in html_files:
        if process_file(file_path):
            modified += 1
            print(f"✓ Modifié: {file_path.relative_to(BASE_DIR.parent)}")
    
    print(f"\n✅ Traitement terminé: {modified} fichiers modifiés sur {len(html_files)}")

if __name__ == "__main__":
    main()
