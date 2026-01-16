#!/bin/bash

# Script pour ouvrir tous les fichiers HTML dans le navigateur
# Utile pour faire les captures d'écran manuellement

BASE_DIR="stitch_onboarding_ia_mesures 2"

echo "🌐 Ouverture de tous les fichiers HTML dans le navigateur..."
echo ""

count=0

for dir in "$BASE_DIR"/*/; do
    if [ -d "$dir" ]; then
        code_html="$dir/code.html"
        
        if [ -f "$code_html" ]; then
            count=$((count + 1))
            echo "  [$count] Ouverture: $(basename "$dir")"
            
            # Ouvrir dans le navigateur par défaut
            if [[ "$OSTYPE" == "darwin"* ]]; then
                # macOS
                open "$code_html"
            elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
                # Linux
                xdg-open "$code_html"
            elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
                # Windows
                start "$code_html"
            fi
            
            # Attendre un peu entre chaque ouverture pour éviter de surcharger
            sleep 0.5
        fi
    fi
done

echo ""
echo "✅ $count fichier(s) ouvert(s)"
echo ""
echo "💡 Faites maintenant vos captures d'écran :"
echo "   - Mac: Cmd + Shift + 4"
echo "   - Windows: Win + Shift + S"
echo "   - Enregistrez comme 'screen.png' dans chaque dossier"
