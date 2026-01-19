# 📝 Instructions pour le Commit

## Commandes à exécuter

Copiez et collez ces commandes dans votre terminal :

```bash
cd "/Users/mac/DOSSIER_MOSES/MOSESWISE/STYLISTE APP/Marquette"

# Ajouter tous les fichiers modifiés
git add -A

# Vérifier le statut
git status

# Créer le commit
git commit -m "feat: Ajout guides développeurs et réorganisation écrans

- Ajout de 4 guides téléchargeables (Client, Tailleur, Revendeur, Admin)
- Réorganisation des écrans client avec distinction claire entre commande Tailleur et achat Revendeur
- Ajout de 5 nouveaux écrans admin pour gestion revendeurs (F12-F16)
- Ajout de 4 nouveaux écrans client pour produits revendeurs (B09-B12)
- Modification des titres d'écrans pour plus de clarté
- Mise à jour de index.html avec section de téléchargement des guides
- Tous les écrans convertis en fond blanc"

# Pousser les changements (optionnel)
git push
```

## Fichiers modifiés/ajoutés

- ✅ `GUIDE_ECRANS_CLIENT.md` (nouveau)
- ✅ `GUIDE_ECRANS_TAILLEUR.md` (nouveau)
- ✅ `GUIDE_ECRANS_REVENDEUR.md` (nouveau)
- ✅ `GUIDE_ECRANS_ADMIN.md` (nouveau)
- ✅ `index.html` (modifié)
- ✅ Nouveaux écrans admin (F12-F16)
- ✅ Nouveaux écrans client (B09-B12)
- ✅ Tous les écrans HTML convertis en fond blanc

## Alternative : Utiliser le script

Vous pouvez aussi exécuter le script créé :

```bash
chmod +x commit-changes.sh
./commit-changes.sh
```
