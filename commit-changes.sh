#!/bin/bash

# Script de commit pour les modifications du projet CouturioShop

cd "/Users/mac/DOSSIER_MOSES/MOSESWISE/STYLISTE APP/Marquette"

echo "📦 Ajout des fichiers modifiés..."
git add -A

echo "📝 Statut des modifications..."
git status

echo ""
echo "💾 Création du commit..."
git commit -m "feat: Ajout guides développeurs et réorganisation écrans

- Ajout de 4 guides téléchargeables (Client, Tailleur, Revendeur, Admin)
- Réorganisation des écrans client avec distinction claire entre commande Tailleur et achat Revendeur
- Ajout de 5 nouveaux écrans admin pour gestion revendeurs (F12-F16)
- Ajout de 4 nouveaux écrans client pour produits revendeurs (B09-B12)
- Modification des titres d'écrans pour plus de clarté
- Mise à jour de index.html avec section de téléchargement des guides
- Tous les écrans convertis en fond blanc"

echo ""
echo "✅ Commit créé avec succès!"
echo ""
echo "Pour pousser les changements, exécutez:"
echo "  git push"
