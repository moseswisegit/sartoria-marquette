# ⚠️ Script à Exécuter Manuellement

En raison des restrictions de l'environnement, le script ne peut pas être exécuté automatiquement. 

## 📋 Instructions pour Exécuter le Script

### Option 1 : Script Node.js (Recommandé)

Ouvrez un terminal dans le dossier du projet et exécutez :

```bash
node convert-dark-to-light.js
```

### Option 2 : Script Bash

```bash
chmod +x convert-dark-to-light.sh
./convert-dark-to-light.sh
```

### Option 3 : Utiliser votre Éditeur de Code

Si vous utilisez VS Code ou un autre éditeur, vous pouvez utiliser la fonction "Rechercher et Remplacer" dans tous les fichiers :

1. **Ouvrir la recherche globale** (Cmd+Shift+F sur Mac, Ctrl+Shift+F sur Windows)
2. **Activer l'option "Utiliser l'expression régulière"**
3. **Rechercher :** ` dark:[^\s"']+`
4. **Remplacer par :** (vide)
5. **Cliquer sur "Remplacer tout"**

Puis répéter pour :
- Rechercher : `dark:bg-background-dark` → Remplacer par : `bg-white`
- Rechercher : `dark:text-white` → Remplacer par : `text-gray-900`
- Rechercher : `dark:bg-gray-800` → Remplacer par : `bg-gray-50`
- Rechercher : `dark:border-gray-700` → Remplacer par : `border-gray-300`

## ✅ Fichiers Déjà Modifiés

- ✅ `splash_screen/code.html`
- ✅ `écran_d'inscription_client/code.html`
- ✅ `écran_d'inscription_tailleur/code.html`
- ✅ `écran_d'inscription_revendeur/code.html`
- ✅ `onboarding_-_ia_mesures/code.html`

## 📊 Statut

**62 fichiers restants** à traiter sur 67 fichiers au total.
