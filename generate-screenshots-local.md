# 📸 Génération des Captures d'Écran (Local)

GitHub Pages ne peut pas exécuter Puppeteer car c'est un hébergement statique. Vous devez générer les captures **localement** avant de publier.

## 🚀 Méthode 1 : Script Automatique (Local)

### Installation (une seule fois)

```bash
cd "/Users/mac/DOSSIER_MOSES/MOSESWISE/STYLISTE APP/Marquette"
npm install puppeteer
```

### Génération

```bash
npm run screenshots
```

Les captures seront générées dans chaque dossier.

### Push vers GitHub

```bash
git add .
git commit -m "Add screenshots"
git push origin master
```

## 🖼️ Méthode 2 : Capture Manuelle (Recommandé)

### Étapes

1. **Ouvrir chaque fichier HTML** dans votre navigateur :
   - `stitch_onboarding_ia_mesures 3/mot_de_passe_oublié/code.html`
   - `stitch_onboarding_ia_mesures 3/recherche_avancée_marketplace/code.html`
   - etc.

2. **Faire une capture d'écran** :
   - **Mac** : Cmd + Shift + 4, puis sélectionner la zone
   - **Windows** : Win + Shift + S
   - Ou utiliser un outil de capture

3. **Enregistrer** comme `screen.png` dans le dossier correspondant

### Liste des captures à générer

- ✅ `mot_de_passe_oublié/screen.png`
- ✅ `recherche_avancée_marketplace/screen.png`
- ✅ `prise_de_mesures_-_résumé_ia/screen.png`
- ✅ `création_de_commande/screen.png`
- ✅ `centre_de_notifications/screen.png`
- ✅ `notation_&_avis_tailleur/screen.png`
- ✅ `sélecteur_de_textures_hd/screen.png`
- ✅ `détails_profil_tailleur/screen.png`
- ✅ `portfolio_tailleur/screen.png`
- ✅ `gestion_stock_tissus_détaillée/screen.png`
- ✅ `détails_&_médiation_litige/screen.png`

## 🛠️ Méthode 3 : Extension Navigateur

### Chrome/Edge : GoFullPage

1. Installer l'extension [GoFullPage](https://chrome.google.com/webstore/detail/gofullpage-full-page-scre/fdpohaocaechififmbbbbbknoalclacl)
2. Ouvrir chaque `code.html`
3. Cliquer sur l'extension pour capturer
4. Télécharger et renommer en `screen.png`

### Firefox : FireShot

1. Installer [FireShot](https://addons.mozilla.org/firefox/addon/fireshot/)
2. Ouvrir chaque `code.html`
3. Capturer la page
4. Enregistrer comme `screen.png`

## 📐 Format Recommandé

- **Taille** : 390 x 844 pixels (format mobile)
- **Format** : PNG
- **Qualité** : Haute résolution (2x pour Retina)

## ⚡ Astuce Rapide

Vous pouvez ouvrir tous les fichiers HTML en une fois :

```bash
# Sur Mac
open "stitch_onboarding_ia_mesures 3"/*/code.html
```

Puis faire les captures une par une.
