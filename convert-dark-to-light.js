#!/usr/bin/env node
/**
 * Script pour convertir tous les écrans avec fond noir en fond blanc
 */
const fs = require('fs');
const path = require('path');

const BASE_DIR = path.join(__dirname, 'stitch_onboarding_ia_mesures 3');

// Fonction pour traiter un fichier
function processFile(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        const originalContent = content;
        
        // Remplacements des classes dark:
        const replacements = [
            // Backgrounds
            [/dark:bg-background-dark/g, 'bg-white'],
            [/dark:bg-\[#1e293b\]/g, 'bg-white'],
            [/dark:bg-\[#131022\]/g, 'bg-white'],
            [/dark:bg-\[#0f172a\]/g, 'bg-white'],
            [/dark:bg-gray-900/g, 'bg-white'],
            [/dark:bg-gray-800/g, 'bg-gray-50'],
            [/dark:bg-gray-700/g, 'bg-gray-100'],
            [/dark:bg-slate-800/g, 'bg-gray-50'],
            [/dark:bg-slate-900/g, 'bg-white'],
            
            // Text colors
            [/dark:text-white/g, 'text-gray-900'],
            [/dark:text-slate-400/g, 'text-gray-600'],
            [/dark:text-gray-400/g, 'text-gray-600'],
            [/dark:text-gray-300/g, 'text-gray-700'],
            [/dark:text-gray-500/g, 'text-gray-700'],
            
            // Borders
            [/dark:border-gray-700/g, 'border-gray-300'],
            [/dark:border-gray-800/g, 'border-gray-200'],
            
            // Hover states
            [/dark:hover:bg-gray-800/g, 'hover:bg-gray-100'],
            [/dark:hover:bg-gray-700/g, 'hover:bg-gray-200'],
            [/dark:hover:text-gray-300/g, 'hover:text-gray-700'],
            [/dark:hover:text-primary/g, 'hover:text-primary'],
            
            // Rings
            [/dark:ring-white\/5/g, 'ring-gray-200/10'],
            [/dark:ring-white\/10/g, 'ring-gray-200/20'],
            
            // Shadows
            [/dark:shadow-\[0_8px_30px_rgb\(0,0,0,0\.3\)\]/g, 'shadow-lg'],
            
            // Opacity backgrounds
            [/dark:bg-primary\/10/g, 'bg-primary/5'],
            [/dark:bg-primary\/20/g, 'bg-primary/10'],
            
            // Focus ring offset
            [/dark:focus:ring-offset-gray-900/g, 'focus:ring-offset-white'],
        ];
        
        // Appliquer tous les remplacements
        replacements.forEach(([pattern, replacement]) => {
            content = content.replace(pattern, replacement);
        });
        
        // Supprimer les classes dark: restantes (en gardant l'espace avant)
        content = content.replace(/\s+dark:[^\s"']+/g, '');
        
        // Remplacer class="dark" par class="light" dans les balises html
        content = content.replace(/<html\s+class="dark"/g, '<html class="light"');
        content = content.replace(/<html\s+class='dark'/g, "<html class='light'");
        
        // Nettoyer les espaces multiples
        content = content.replace(/\s{2,}/g, ' ');
        content = content.replace(/\s+class="/g, ' class="');
        content = content.replace(/\s+class='/g, " class='");
        
        // Écrire seulement si le contenu a changé
        if (content !== originalContent) {
            fs.writeFileSync(filePath, content, 'utf8');
            return true;
        }
        return false;
    } catch (error) {
        console.error(`Erreur lors du traitement de ${filePath}:`, error.message);
        return false;
    }
}

// Fonction récursive pour trouver tous les fichiers code.html
function findHtmlFiles(dir) {
    const files = [];
    try {
        const entries = fs.readdirSync(dir, { withFileTypes: true });
        for (const entry of entries) {
            const fullPath = path.join(dir, entry.name);
            if (entry.isDirectory()) {
                files.push(...findHtmlFiles(fullPath));
            } else if (entry.isFile() && entry.name === 'code.html') {
                files.push(fullPath);
            }
        }
    } catch (error) {
        console.error(`Erreur lors de la lecture de ${dir}:`, error.message);
    }
    return files;
}

// Fonction principale
function main() {
    if (!fs.existsSync(BASE_DIR)) {
        console.error(`Erreur: Le dossier ${BASE_DIR} n'existe pas`);
        process.exit(1);
    }
    
    const htmlFiles = findHtmlFiles(BASE_DIR);
    console.log(`Trouvé ${htmlFiles.length} fichiers HTML à traiter...\n`);
    
    let modified = 0;
    for (const filePath of htmlFiles) {
        if (processFile(filePath)) {
            modified++;
            const relativePath = path.relative(BASE_DIR, filePath);
            console.log(`✓ Modifié: ${relativePath}`);
        }
    }
    
    console.log(`\n✅ Traitement terminé: ${modified} fichiers modifiés sur ${htmlFiles.length}`);
}

main();
