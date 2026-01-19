# 📱 Guide des Écrans - Profil Client

**Version :** 1.0  
**Date :** 2025-01-XX  
**Profil :** Client (Utilisateur final)

---

## 📋 Vue d'Ensemble

Le profil Client permet aux utilisateurs finaux de :
- Découvrir des tailleurs et leurs services
- Commander des vêtements sur mesure avec prise de mesures IA
- Acheter des produits finis auprès des revendeurs
- Suivre leurs commandes en temps réel
- Gérer leur profil et leurs mesures

**Total d'écrans :** 32 écrans

---

## 🗂️ Organisation des Écrans

### 1. AUTHENTIFICATION & ONBOARDING (8 écrans)

#### A01 - Splash Screen
**Description :** Écran de chargement initial avec le logo Sartoria  
**Fichier :** `splash_screen/code.html`  
**Fonctionnalités :**
- Affichage du logo et animation de chargement
- Transition automatique vers l'onboarding après 2-3 secondes
- Vérification de l'état de connexion

**Navigation :**
- → A02 (Onboarding IA Mesures) si première utilisation
- → A07 (Connexion) si utilisateur déjà connecté

---

#### A02 - Onboarding IA Mesures
**Description :** Présentation de la fonctionnalité Smart-Fit AI pour la prise de mesures automatique  
**Fichier :** `onboarding_-_ia_mesures/code.html`  
**Fonctionnalités :**
- Explication de la technologie IA de prise de mesures
- Avantages : précision, rapidité, pas besoin de rendez-vous physique
- Bouton "Suivant" pour continuer

**Navigation :**
- ← Retour (A01)
- → A03 (Onboarding Essayage 3D)

---

#### A03 - Onboarding Essayage Virtuel 3D
**Description :** Présentation de l'essayage virtuel 3D  
**Fichier :** `onboarding_-_essayage_virtuel_3d/code.html`  
**Fonctionnalités :**
- Explication de l'essayage virtuel avant confection
- Visualisation 360° du vêtement
- Application de textures réelles

**Navigation :**
- ← Retour (A02)
- → A04 (Onboarding Marketplace)

---

#### A04 - Onboarding Marketplace
**Description :** Présentation de la marketplace pour découvrir des tailleurs  
**Fichier :** `onboarding_-_marketplace/code.html`  
**Fonctionnalités :**
- Découverte de tailleurs près de chez soi
- Recherche par spécialité, ville, prix
- Système de notation et avis

**Navigation :**
- ← Retour (A03)
- → A05 (Onboarding Revendeur)

---

#### A05 - Onboarding Revendeur
**Description :** Présentation des boutiques revendeurs et produits finis  
**Fichier :** `onboarding_-_revendeur/code.html`  
**Fonctionnalités :**
- Découverte des produits finis disponibles
- Achat direct sans prise de mesures
- Livraison rapide

**Navigation :**
- ← Retour (A04)
- → A06 (Inscription Client)

---

#### A06 - Écran d'Inscription Client
**Description :** Formulaire d'inscription pour les clients  
**Fichier :** `écran_d'inscription_client/code.html`  
**Champs requis :**
- Nom complet
- Email
- Téléphone (optionnel)
- Pays
- Mot de passe
- Confirmation mot de passe

**Navigation :**
- ← Retour (A05)
- → A07 (Connexion) après inscription réussie
- → Lien vers A07 (Connexion) si déjà inscrit

---

#### A07 - Écran de Connexion
**Description :** Authentification de l'utilisateur  
**Fichier :** `écran_de_connexion/code.html`  
**Fonctionnalités :**
- Connexion par email/mot de passe
- Option "Se souvenir de moi"
- Lien vers A08 (Mot de passe oublié)
- Lien vers A06 (Inscription)

**Navigation :**
- ← Retour (A01)
- → A08 (Mot de passe oublié)
- → B01 (Accueil Marketplace) après connexion réussie

---

#### A08 - Mot de Passe Oublié
**Description :** Récupération du mot de passe  
**Fichier :** `mot_de_passe_oublié/code.html`  
**Fonctionnalités :**
- Saisie de l'email
- Envoi d'un lien de réinitialisation
- Confirmation d'envoi

**Navigation :**
- ← Retour (A07)
- → A07 (Connexion) après réinitialisation

---

### 2. MARKETPLACE & DÉCOUVERTE (2 écrans)

#### B01 - Accueil / Marketplace
**Description :** Page d'accueil principale avec découverte des tailleurs  
**Fichier :** `accueil_/_marketplace/code.html`  
**Fonctionnalités :**
- Barre de recherche (tailleur, tissu, type de vêtement)
- Filtres : Ville, Spécialité, Prix, Note
- Catégories : Femme, Homme, Mariage, Tissus
- Section "Tailleurs recommandés" avec cartes profil
- Section "Tendances actuelles" avec produits

**Navigation :**
- → B03 (Détails Profil Tailleur) en cliquant sur un tailleur
- → B12 (Liste Boutiques Revendeurs) via menu
- → B09 (Catalogue Produits Revendeurs) via menu

---

#### B03 - Détails Profil Tailleur
**Description :** Fiche détaillée d'un tailleur avec portfolio et informations  
**Fichier :** `détails_profil_tailleur/code.html`  
**Fonctionnalités :**
- Photo de profil et bannière
- Nom, spécialités, localisation
- Note et avis clients
- Portfolio des réalisations
- Tarifs moyens
- Délais de réalisation
- Bouton "Commander" pour créer une commande

**Navigation :**
- ← Retour (B01)
- → B04 (Commande Sur Mesure Tailleur) via bouton "Commander"

---

### 3. COMMANDE TAILLEUR (Sur Mesure avec Mesures IA) (7 écrans)

#### B04 - Commande Sur Mesure Tailleur
**Description :** Formulaire de création d'une commande auprès d'un tailleur  
**Fichier :** `création_de_commande/code.html`  
**Fonctionnalités :**
- Sélection du tailleur (pré-rempli depuis B03)
- Choix du type de vêtement (Boubou, Robe, Ensemble, Chemise)
- Sélection du tissu (Wax, Bazin, Soie, etc.)
- Choix des mesures (Standard S/M/L/XL ou Sur mesure)
- Date limite souhaitée
- Instructions spéciales
- Estimation du prix total

**Navigation :**
- ← Retour (B03)
- → C01 (Instructions Prise Mesures IA) si "Sur mesure" sélectionné
- → D01 (Suivi Timeline Commande) après validation

---

#### C01 - Instructions Prise Mesures IA
**Description :** Guide pour prendre les photos nécessaires à la détection IA  
**Fichier :** `prise_de_mesures_-_instructions/code.html`  
**Fonctionnalités :**
- Instructions détaillées pour chaque pose (face, profil, dos)
- Exemple d'objet de référence (carte bancaire)
- Conseils pour un bon éclairage
- Bouton "Commencer" pour lancer la capture

**Navigation :**
- ← Retour (B04)
- → C02 (Capture Photos Mesures IA)

---

#### C02 - Capture Photos Mesures IA
**Description :** Interface de capture des photos pour la détection IA  
**Fichier :** `prise_de_mesures_-_upload_photo/code.html`  
**Fonctionnalités :**
- Capture ou upload de 3 photos (face, profil, dos)
- Prévisualisation des photos
- Validation de la qualité
- Retour si photo non conforme

**Navigation :**
- ← Retour (C01)
- → C03 (Résumé Mesures IA Détectées) après validation

---

#### C03 - Résumé Mesures IA Détectées
**Description :** Affichage des mesures détectées par l'IA avec possibilité de correction  
**Fichier :** `prise_de_mesures_-_résumé_ia/code.html`  
**Fonctionnalités :**
- Liste des 30+ mesures détectées (tour de poitrine, taille, hanches, etc.)
- Valeurs en centimètres
- Possibilité de modifier manuellement chaque mesure
- Validation de la cohérence des mesures
- Bouton "Valider" pour continuer

**Navigation :**
- ← Retour (C02)
- → C04 (Essayage Virtuel 3D Commande)

---

#### C04 - Essayage Virtuel 3D Commande
**Description :** Visualisation 3D du vêtement sur un avatar personnalisé  
**Fichier :** `essayage_virtuel_3d_immersif/code.html`  
**Fonctionnalités :**
- Avatar 3D généré à partir des mesures
- Rotation 360° du modèle
- Zoom et détail
- Application du type de vêtement sélectionné
- Bouton "Choisir le tissu" pour continuer

**Navigation :**
- ← Retour (C03)
- → C05 (Sélection Textures Tissus)

---

#### C05 - Sélection Textures Tissus
**Description :** Choix de la texture et du motif du tissu  
**Fichier :** `sélecteur_de_textures_hd/code.html`  
**Fonctionnalités :**
- Bibliothèque de textures (Wax, Bazin, Damassé, etc.)
- Application en temps réel sur l'avatar 3D
- Prévisualisation haute résolution
- Comparaison de plusieurs textures

**Navigation :**
- ← Retour (C04)
- → C06 (Conseils Style Personnalisés)

---

#### C06 - Conseils Style Personnalisés
**Description :** Recommandations de style basées sur l'analyse morphologique  
**Fichier :** `analyse_&_conseils_morpho-style/code.html`  
**Fonctionnalités :**
- Type de morphologie détecté (Rectangle, Triangle, Sablier, etc.)
- Conseils de coupe adaptés
- Recommandations de longueurs et ampleurs
- Alertes si mesure inhabituelle
- Validation finale de la commande

**Navigation :**
- ← Retour (C05)
- → D01 (Suivi Timeline Commande) après validation

---

### 4. ACHAT PRODUITS REVENDEURS (E-commerce) (4 écrans)

#### B12 - Découvrir Boutiques Revendeurs
**Description :** Liste des boutiques revendeurs disponibles  
**Fichier :** `b12_-_liste_boutiques_revendeurs/code.html`  
**Fonctionnalités :**
- Recherche de boutiques
- Filtres : Vérifiées, Nouvelles, Top ventes
- Cartes boutique avec logo, nom, localisation
- Note et nombre de produits/ventes
- Badge "Vérifiée" pour boutiques certifiées

**Navigation :**
- ← Retour (B01)
- → R11 (Aperçu Public Boutique) en cliquant sur une boutique
- → B09 (Catalogue Produits Revendeurs) via menu

---

#### B09 - Catalogue Produits Revendeurs
**Description :** Liste des produits disponibles auprès des revendeurs  
**Fichier :** `b09_-_catalogue_produits_revendeurs/code.html`  
**Fonctionnalités :**
- Recherche de produits
- Filtres par catégorie (Tissus, Prêt-à-porter, Accessoires, Chaussures)
- Grille de produits avec image, nom, boutique, prix, note
- Badges : Nouveau, Promo, Stock
- Favoris

**Navigation :**
- ← Retour (B01 ou B12)
- → B10 (Fiche Produit Revendeur) en cliquant sur un produit

---

#### B10 - Fiche Produit Revendeur
**Description :** Détails complets d'un produit revendeur  
**Fichier :** `b10_-_détails_produit_revendeur/code.html`  
**Fonctionnalités :**
- Galerie d'images du produit
- Nom, description, prix
- Informations revendeur (boutique, localisation)
- Sélection variantes (couleur, taille)
- Indicateur de stock
- Note et avis clients
- Boutons "Ajouter au panier" et "Acheter maintenant"

**Navigation :**
- ← Retour (B09)
- → B11 (Panier & Achat Produit Revendeur) via boutons d'action

---

#### B11 - Panier & Achat Produit Revendeur
**Description :** Panier d'achat et finalisation de commande pour produits revendeurs  
**Fichier :** `b11_-_panier_&_commande_produit_revendeur/code.html`  
**Fonctionnalités :**
- Liste des produits dans le panier
- Modification des quantités
- Suppression de produits
- Adresse de livraison (modifiable)
- Récapitulatif : sous-total, livraison, total
- Bouton "Passer la commande"

**Navigation :**
- ← Retour (B10 ou B09)
- → D01 (Suivi Timeline Commande) après validation

---

### 5. SUIVI & COMMUNICATION (3 écrans)

#### D01 - Suivi Timeline Commande
**Description :** Suivi visuel de l'avancement d'une commande  
**Fichier :** `suivi_de_commande_-_timeline/code.html`  
**Fonctionnalités :**
- Timeline interactive avec 7 étapes :
  1. Commande
  2. Mesures
  3. Coupe
  4. Couture
  5. Essayage
  6. Retouches
  7. Livraison
- Photos à chaque étape clé
- Estimation du temps restant
- Statut actuel mis en évidence
- Bouton "Contacter" pour messagerie

**Navigation :**
- ← Retour (B01 ou menu)
- → D02 (Messagerie - Chat) via bouton "Contacter"

---

#### D02 - Messagerie - Chat
**Description :** Chat en temps réel avec le tailleur ou revendeur  
**Fichier :** `messagerie_-_chat/code.html`  
**Fonctionnalités :**
- Liste des conversations
- Chat temps réel avec historique
- Envoi de photos/vidéos
- Messages vocaux
- Accusés de lecture
- Partage de localisation

**Navigation :**
- ← Retour (D01 ou menu)
- → D01 (Suivi Timeline Commande) depuis une conversation

---

#### D03 - Calendrier des Rendez-vous
**Description :** Gestion des rendez-vous pour essayages  
**Fichier :** `calendrier_des_rendez-vous/code.html`  
**Fonctionnalités :**
- Vue calendrier mensuelle
- Liste des rendez-vous à venir
- Détails : date, heure, tailleur, type (essayage, retouches)
- Rappels automatiques
- Possibilité de modifier/annuler

**Navigation :**
- ← Retour (Menu)
- → D01 (Suivi Timeline Commande) depuis un RDV

---

### 6. PROFIL & GESTION (4 écrans)

#### B05 - Profil Client - Infos
**Description :** Informations personnelles du client  
**Fichier :** `profil_client_-_infos/code.html`  
**Fonctionnalités :**
- Nom, email, téléphone
- Photo de profil (modifiable)
- Adresse de livraison par défaut
- Préférences de notification
- Modification des informations

**Navigation :**
- ← Retour (Menu)
- → B06 (Profil Client - Mesures)

---

#### B06 - Profil Client - Mesures
**Description :** Historique et gestion des mesures  
**Fichier :** `profil_client_-_mesures/code.html`  
**Fonctionnalités :**
- Liste des mesures enregistrées (IA et manuelles)
- Historique des modifications
- Mesures par type de vêtement
- Export des mesures
- Ajout de mesures manuelles

**Navigation :**
- ← Retour (B05)
- → B07 (Profil Client - Historique Commandes)

---

#### B07 - Profil Client - Historique Commandes
**Description :** Liste de toutes les commandes passées  
**Fichier :** `profil_client_-_historique_commandes/code.html`  
**Fonctionnalités :**
- Liste des commandes (en cours, terminées, annulées)
- Filtres par statut, date, tailleur/revendeur
- Détails de chaque commande
- Photos des réalisations
- Réédition de commande
- Notation/avis après livraison

**Navigation :**
- ← Retour (B06)
- → D01 (Suivi Timeline Commande) en cliquant sur une commande
- → B08 (Profil Client - Paiements)

---

#### B08 - Profil Client - Paiements
**Description :** Historique des paiements et méthodes de paiement  
**Fichier :** `profil_client_-_paiements/code.html`  
**Fonctionnalités :**
- Historique des transactions
- Méthodes de paiement enregistrées (carte, mobile money)
- Factures téléchargeables
- Remboursements
- Ajout/modification de méthodes de paiement

**Navigation :**
- ← Retour (B07)
- → B05 (Profil Client - Infos)

---

### 7. NAVIGATION & UTILITAIRES (2 écrans)

#### N02 - Sidebar de Transition Rapide
**Description :** Menu latéral pour navigation rapide entre profils  
**Fichier :** `n02_-_sidebar_de_transition_rapide/code.html`  
**Fonctionnalités :**
- Accès rapide aux sections principales
- Changement de profil (si multi-profils)
- Raccourcis vers fonctionnalités fréquentes

**Navigation :**
- Accessible depuis n'importe quel écran
- → N01 (Sélecteur Rôle Multi-Profils) si disponible

---

#### N03 - Centre de Notifications Global
**Description :** Centre de toutes les notifications  
**Fichier :** `n03_-_centre_de_notifications_global/code.html`  
**Fonctionnalités :**
- Liste de toutes les notifications
- Filtres par type (commandes, messages, promotions)
- Marquer comme lu/non lu
- Actions rapides depuis les notifications
- Paramètres de notification

**Navigation :**
- Accessible depuis n'importe quel écran
- → D01 (Suivi Timeline Commande) depuis notification commande
- → D02 (Messagerie - Chat) depuis notification message

---

## 🔄 Flux de Navigation Principaux

### Flux 1 : Commande Sur Mesure Tailleur
```
B01 (Marketplace) 
  → B03 (Détails Tailleur) 
  → B04 (Commande Sur Mesure) 
  → C01 (Instructions Mesures) 
  → C02 (Capture Photos) 
  → C03 (Résumé Mesures) 
  → C04 (Essayage 3D) 
  → C05 (Sélection Textures) 
  → C06 (Conseils Style) 
  → D01 (Suivi Timeline)
```

### Flux 2 : Achat Produit Revendeur
```
B01 (Marketplace) 
  → B12 (Boutiques Revendeurs) 
  → B09 (Catalogue Produits) 
  → B10 (Fiche Produit) 
  → B11 (Panier) 
  → D01 (Suivi Timeline)
```

### Flux 3 : Gestion Profil
```
Menu 
  → B05 (Infos) 
  → B06 (Mesures) 
  → B07 (Historique) 
  → B08 (Paiements)
```

---

## 🎯 Points Clés pour les Développeurs

1. **Distinction importante :** Il y a deux types de commandes :
   - **Commande Tailleur** : Sur mesure avec mesures IA (B04 → C01-C06)
   - **Achat Revendeur** : Produits finis, e-commerce classique (B09-B11)

2. **Mesures IA :** Le flux C01-C03 est optionnel si l'utilisateur choisit "Standard" dans B04

3. **Essayage 3D :** Disponible uniquement pour les commandes sur mesure (flux Tailleur)

4. **Panier :** Existe uniquement pour les produits revendeurs, pas pour les commandes tailleur

5. **Suivi :** D01 gère les deux types de commandes mais avec des étapes différentes

---

## 📝 Notes Techniques

- Tous les écrans utilisent un fond blanc (pas de mode sombre)
- Couleur primaire : `#1A73B5`
- Framework : Tailwind CSS
- Icônes : Material Symbols Outlined
- Police : Inter (corps), Poppins (titres)

---

**Dernière mise à jour :** 2025-01-XX
