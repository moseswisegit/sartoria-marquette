# 🎨 Conversion des Fonds Noirs en Fonds Blancs

## 📋 Instructions

Pour convertir tous les écrans avec fond noir en fond blanc, exécutez le script bash suivant :

```bash
chmod +x convert-dark-to-light.sh
./convert-dark-to-light.sh
```

## 🔄 Remplacements Effectués

Le script remplace automatiquement :
- `dark:bg-background-dark` → `bg-white`
- `dark:bg-gray-800` → `bg-gray-50`
- `dark:text-white` → `text-gray-900`
- `dark:text-gray-400` → `text-gray-600`
- `dark:border-gray-700` → `border-gray-300`
- Et toutes les autres classes `dark:*` par leurs équivalents light

## ✅ Fichiers Déjà Modifiés

- ✅ `splash_screen/code.html`
- ✅ `écran_d'inscription_client/code.html`

## 📝 Note

Si vous préférez modifier les fichiers manuellement, vous pouvez utiliser les remplacements suivants dans votre éditeur :

1. Rechercher : `dark:bg-background-dark`
   Remplacer par : `bg-white`

2. Rechercher : `dark:text-white`
   Remplacer par : `text-gray-900`

3. Rechercher : `dark:bg-gray-800`
   Remplacer par : `bg-gray-50`

4. Rechercher : `dark:border-gray-700`
   Remplacer par : `border-gray-300`

5. Rechercher : ` dark:[^"']*` (regex)
   Remplacer par : (vide) - pour supprimer toutes les classes dark: restantes
