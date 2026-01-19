#!/bin/bash

# Script simple pour lister les fichiers nécessitant des captures d'écran
# Usage: ./generate-screenshots-simple.sh

BASE_DIR="stitch_onboarding_ia_mesures 3"

echo "🎨 Maquettes nécessitant des captures d'écran:"
echo ""

count=0

for dir in "$BASE_DIR"/*/; do
    if [ -d "$dir" ]; then
        folder_name=$(basename "$dir")
        code_html="$dir/code.html"
        screen_png="$dir/screen.png"
        
        if [ -f "$code_html" ]; then
            # Vérifier si screen.png n'existe pas ou est vide
            if [ ! -f "$screen_png" ] || [ ! -s "$screen_png" ]; then
                count=$((count + 1))
                echo "  $count. $folder_name"
                echo "     HTML: $code_html"
                echo "     PNG:  $screen_png"
                echo ""
            fi
        fi
    fi
done

if [ $count -eq 0 ]; then
    echo "✅ Toutes les captures d'écran existent déjà !"
else
    echo "📸 Total: $count capture(s) à générer"
    echo ""
    echo "💡 Pour générer automatiquement, utilisez:"
    echo "   npm install puppeteer"
    echo "   node generate-screenshots.js"
fi
