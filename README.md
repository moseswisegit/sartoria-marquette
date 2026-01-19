# 🎨 Sartoria - Galerie des Maquettes

Plateforme de visualisation des maquettes de l'application Sartoria.

## 📋 Structure

- `index.html` - Page principale de la galerie
- `stitch_onboarding_ia_mesures 3/` - Dossier contenant toutes les maquettes

## 🚀 Accès au site

Le site est hébergé sur GitHub Pages : [https://moseswisegit.github.io/sartoria-marquette/](https://moseswisegit.github.io/sartoria-marquette/)

## 📱 Fonctionnalités

- **Galerie** : Visualisation de toutes les maquettes organisées par profil (Client, Tailleur, Admin)
- **Mode Prototype** : Navigation séquentielle entre les écrans
- **Recherche** : Filtrage par nom ou profil
- **Aperçu** : Visualisation des fichiers HTML directement dans la page

## 👥 Profils

- **Client** : 24 écrans
- **Tailleur** : 12 écrans  
- **Administrateur** : 10 écrans

**Total : 44 écrans**

## 🔧 Configuration GitHub Pages

1. Allez dans **Settings** > **Pages**
2. Source : **Deploy from a branch**
3. Branch : **master** (ou **main**)
4. Folder : **/ (root)**
5. Cliquez sur **Save**

## ⚠️ Dépannage

Si vous voyez une erreur 404 :
- Vérifiez que `index.html` est bien à la racine du dépôt
- Attendez 1-2 minutes après l'activation de GitHub Pages
- Vérifiez que tous les fichiers sont bien commités et pushés
- Videz le cache de votre navigateur (Ctrl+F5 ou Cmd+Shift+R)

## 📸 Génération des Captures d'Écran

⚠️ **Important** : Les captures doivent être générées **localement** avant de publier sur GitHub. GitHub Pages ne peut pas exécuter de scripts Node.js.

### 🎯 Méthode Recommandée : Assistant Navigateur

1. **Ouvrir l'assistant** :
   ```bash
   open generate-screenshots-browser.html
   # Ou double-cliquez sur le fichier
   ```

2. **Suivre les instructions** :
   - Cliquez sur "Ouvrir" pour chaque maquette
   - Faites la capture d'écran
   - Enregistrez comme `screen.png`
   - Marquez comme "fait" dans l'assistant

### Méthode Alternative : Script Shell

```bash
# Ouvrir tous les fichiers HTML en une fois
./open-all-html.sh

# Puis faire les captures manuellement
# Mac: Cmd + Shift + 4
# Windows: Win + Shift + S
```

### Méthode Automatique (Si Puppeteer installé)

```bash
# 1. Installer Puppeteer (une seule fois)
npm install puppeteer

# 2. Générer toutes les captures
npm run screenshots

# 3. Commit et push
git add .
git commit -m "Add screenshots"
git push origin master
```

📖 Voir `generate-screenshots-local.md` pour plus de détails.

## 📝 Notes

- Les fichiers `screen.png` vides afficheront un placeholder "Image non disponible"
- Format recommandé : 390 x 844 pixels (format mobile)
