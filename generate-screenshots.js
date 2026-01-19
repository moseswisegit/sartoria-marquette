#!/usr/bin/env node

/**
 * Script pour générer automatiquement les captures d'écran
 * des maquettes HTML
 * 
 * ⚠️ IMPORTANT : Ce script doit être exécuté LOCALEMENT avant de publier sur GitHub.
 * GitHub Pages ne peut pas exécuter Puppeteer (hébergement statique uniquement).
 * 
 * Installation des dépendances:
 * npm install puppeteer
 * 
 * Usage:
 * node generate-screenshots.js
 * 
 * Puis commit et push vers GitHub :
 * git add .
 * git commit -m "Add screenshots"
 * git push origin master
 */

const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

const BASE_DIR = path.join(__dirname, 'stitch_onboarding_ia_mesures 3');
const OUTPUT_DIR = BASE_DIR;

// Liste des écrans à capturer (dossiers avec code.html)
async function getScreensToCapture() {
    const screens = [];
    const dirs = fs.readdirSync(BASE_DIR, { withFileTypes: true });
    
    for (const dir of dirs) {
        if (dir.isDirectory()) {
            const codeHtmlPath = path.join(BASE_DIR, dir.name, 'code.html');
            const screenPngPath = path.join(BASE_DIR, dir.name, 'screen.png');
            
            if (fs.existsSync(codeHtmlPath)) {
                // Vérifier si le fichier screen.png est vide ou n'existe pas
                const needsCapture = !fs.existsSync(screenPngPath) || 
                                   fs.statSync(screenPngPath).size === 0;
                
                if (needsCapture) {
                    screens.push({
                        folder: dir.name,
                        htmlPath: codeHtmlPath,
                        outputPath: screenPngPath
                    });
                }
            }
        }
    }
    
    return screens;
}

async function captureScreenshot(browser, screen, index, total) {
    try {
        console.log(`[${index + 1}/${total}] Capture de: ${screen.folder}`);
        
        const page = await browser.newPage();
        
        // Définir la taille de la fenêtre (format mobile)
        await page.setViewport({
            width: 390,
            height: 844,
            deviceScaleFactor: 2
        });
        
        // Charger le fichier HTML
        const fileUrl = `file://${screen.htmlPath}`;
        await page.goto(fileUrl, {
            waitUntil: 'networkidle0',
            timeout: 30000
        });
        
        // Attendre un peu pour que tout soit rendu
        await page.waitForTimeout(1000);
        
        // Prendre la capture d'écran
        await page.screenshot({
            path: screen.outputPath,
            type: 'png',
            fullPage: false, // Capturer uniquement la zone visible
            clip: {
                x: 0,
                y: 0,
                width: 390,
                height: 844
            }
        });
        
        await page.close();
        console.log(`✓ Capturé: ${screen.folder}`);
        
    } catch (error) {
        console.error(`✗ Erreur pour ${screen.folder}:`, error.message);
    }
}

async function main() {
    console.log('🎨 Génération des captures d\'écran pour les maquettes Sartoria\n');
    
    // Vérifier si Puppeteer est installé
    try {
        require.resolve('puppeteer');
    } catch (e) {
        console.error('❌ Puppeteer n\'est pas installé.');
        console.log('\n📦 Installation des dépendances...');
        console.log('   Exécutez: npm install puppeteer');
        console.log('   Ou: npm install puppeteer --save-dev\n');
        process.exit(1);
    }
    
    // Obtenir la liste des écrans à capturer
    const screens = await getScreensToCapture();
    
    if (screens.length === 0) {
        console.log('✅ Toutes les captures d\'écran existent déjà !');
        return;
    }
    
    console.log(`📸 ${screens.length} capture(s) à générer\n`);
    
    // Lancer le navigateur
    console.log('🚀 Lancement du navigateur...');
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    try {
        // Capturer chaque écran
        for (let i = 0; i < screens.length; i++) {
            await captureScreenshot(browser, screens[i], i, screens.length);
        }
        
        console.log(`\n✅ ${screens.length} capture(s) générée(s) avec succès !`);
        
    } finally {
        await browser.close();
    }
}

// Exécuter le script
main().catch(error => {
    console.error('❌ Erreur fatale:', error);
    process.exit(1);
});
