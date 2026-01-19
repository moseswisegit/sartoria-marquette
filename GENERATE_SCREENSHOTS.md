# 📸 Guide de Génération des Captures d'Écran

Ce guide explique comment générer automatiquement les captures d'écran des maquettes HTML.

## 🚀 Installation

### Option 1 : Avec npm (recommandé)

```bash
# Installer les dépendances
npm install

# Ou directement Puppeteer
npm install puppeteer
```

### Option 2 : Avec yarn

```bash
yarn install
# ou
yarn add puppeteer
```

## 📋 Utilisation

### Générer toutes les captures manquantes

```bash
node generate-screenshots.js
```

Ou avec npm :

```bash
npm run screenshots
```

## 🔧 Fonctionnement

Le script :
1. ✅ Scanne le dossier `stitch_onboarding_ia_mesures 3/`
2. ✅ Trouve tous les dossiers contenant un fichier `code.html`
3. ✅ Vérifie si `screen.png` existe et n'est pas vide
4. ✅ Génère automatiquement les captures manquantes
5. ✅ Utilise un format mobile (390x844px) pour les captures

## 📐 Format des Captures

- **Taille** : 390 x 844 pixels (format iPhone)
- **Résolution** : 2x (deviceScaleFactor)
- **Format** : PNG
- **Zone** : Zone visible uniquement (pas de scroll)

## ⚙️ Configuration

Vous pouvez modifier les paramètres dans `generate-screenshots.js` :

```javascript
await page.setViewport({
    width: 390,      // Largeur
    height: 844,     // Hauteur
    deviceScaleFactor: 2  // Résolution
});
```

## 🐛 Dépannage

### Erreur : "Puppeteer n'est pas installé"

```bash
npm install puppeteer
```

### Erreur : "Cannot find module"

Assurez-vous d'être dans le bon répertoire :
```bash
cd "/Users/mac/DOSSIER_MOSES/MOSESWISE/STYLISTE APP/Marquette"
```

### Les captures sont vides

- Vérifiez que les fichiers HTML se chargent correctement dans un navigateur
- Augmentez le timeout dans le script si nécessaire
- Vérifiez que Chrome/Chromium peut être lancé sur votre système

## 📝 Notes

- Le script ne génère que les captures manquantes ou vides
- Les captures existantes ne sont pas écrasées
- Le processus peut prendre quelques minutes selon le nombre d'écrans

## 🔄 Alternative Manuelle

Si le script automatique ne fonctionne pas, vous pouvez :

1. Ouvrir chaque `code.html` dans un navigateur
2. Faire une capture d'écran (Cmd+Shift+4 sur Mac, ou outil de capture)
3. Enregistrer comme `screen.png` dans le dossier correspondant
