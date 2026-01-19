#!/bin/bash
# Script pour convertir tous les écrans avec fond noir en fond blanc

find "stitch_onboarding_ia_mesures 3" -name "code.html" -type f | while read file; do
    echo "Traitement de: $file"
    
    # Remplacer toutes les classes dark: par leurs équivalents light
    sed -i '' \
        -e 's/dark:bg-background-dark/bg-white/g' \
        -e 's/dark:bg-\[#1e293b\]/bg-white/g' \
        -e 's/dark:bg-\[#131022\]/bg-white/g' \
        -e 's/dark:bg-\[#0f172a\]/bg-white/g' \
        -e 's/dark:bg-gray-900/bg-white/g' \
        -e 's/dark:bg-gray-800/bg-gray-50/g' \
        -e 's/dark:bg-gray-700/bg-gray-100/g' \
        -e 's/dark:bg-slate-800/bg-gray-50/g' \
        -e 's/dark:bg-slate-900/bg-white/g' \
        -e 's/dark:text-white/text-gray-900/g' \
        -e 's/dark:text-slate-400/text-gray-600/g' \
        -e 's/dark:text-gray-400/text-gray-600/g' \
        -e 's/dark:text-gray-300/text-gray-700/g' \
        -e 's/dark:text-gray-500/text-gray-700/g' \
        -e 's/dark:border-gray-700/border-gray-300/g' \
        -e 's/dark:border-gray-800/border-gray-200/g' \
        -e 's/dark:hover:bg-gray-800/hover:bg-gray-100/g' \
        -e 's/dark:hover:bg-gray-700/hover:bg-gray-200/g' \
        -e 's/dark:hover:text-gray-300/hover:text-gray-700/g' \
        -e 's/dark:ring-white\/5/ring-gray-200\/10/g' \
        -e 's/dark:ring-white\/10/ring-gray-200\/20/g' \
        -e 's/dark:shadow-\[0_8px_30px_rgb(0,0,0,0\.3)\]/shadow-lg/g' \
        -e 's/dark:bg-primary\/10/bg-primary\/5/g' \
        -e 's/dark:bg-primary\/20/bg-primary\/10/g' \
        "$file"
    
    # Supprimer les classes dark: restantes (en gardant l'espace avant)
    sed -i '' 's/ dark:[^"'"'"' ]*//g' "$file"
    
    # Remplacer class="dark" par class="light" dans les balises html
    sed -i '' 's/<html class="dark"/<html class="light"/g' "$file"
    sed -i '' "s/<html class='dark'/<html class='light'/g" "$file"
    
    echo "✓ Fait: $file"
done

echo ""
echo "✅ Conversion terminée ! Tous les fonds noirs ont été remplacés par des fonds blancs."
