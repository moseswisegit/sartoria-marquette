# 🛒 Guide des Écrans - Profil Revendeur

**Version :** 1.0  
**Date :** 2025-01-XX  
**Profil :** Revendeur (Marchand / Vendeur de produits finis)

---

## 📋 Vue d'Ensemble

Le profil Revendeur permet aux commerçants de :
- Créer et gérer leur boutique en ligne
- Ajouter et gérer leurs produits
- Suivre leurs ventes et revenus
- Gérer les commandes clients
- Optimiser leur performance commerciale

**Total d'écrans :** 18 écrans

---

## 🗂️ Organisation des Écrans

### 1. AUTHENTIFICATION & ONBOARDING (3 écrans)

#### A05 - Onboarding Revendeur
**Description :** Présentation des fonctionnalités pour revendeurs  
**Fichier :** `onboarding_-_revendeur/code.html`  
**Fonctionnalités :**
- Explication du système de boutique
- Avantages : visibilité, gestion simplifiée, paiements sécurisés
- Commission plateforme
- Bouton "Commencer"

**Navigation :**
- → A06c (Inscription Revendeur)

---

#### A06c - Écran d'Inscription Revendeur
**Description :** Formulaire d'inscription pour revendeurs  
**Fichier :** `écran_d'inscription_revendeur/code.html`  
**Champs requis :**
- Nom complet
- Email
- Téléphone (obligatoire)
- Pays
- Mot de passe
- Confirmation mot de passe
- Note informative sur la configuration de la boutique

**Navigation :**
- → R01 (Inscription & Choix Type Revendeur) après inscription

---

#### R01 - Inscription & Choix Type Revendeur
**Description :** Choix du type de revendeur (individuel ou entreprise)  
**Fichier :** `r01_-_inscription_&_choix_type_revendeur/code.html`  
**Fonctionnalités :**
- Sélection : Individuel ou Entreprise
- Champs supplémentaires selon le type :
  - **Individuel :** CNI, adresse personnelle
  - **Entreprise :** RCCM, raison sociale, adresse siège
- Upload de documents justificatifs
- Validation et soumission

**Navigation :**
- ← Retour (A06c)
- → R02 (Dashboard Revendeur) après validation

---

### 2. DASHBOARD & VUE D'ENSEMBLE (1 écran)

#### R02 - Dashboard Revendeur Vue d'Ensemble
**Description :** Tableau de bord principal avec statistiques de vente  
**Fichier :** `r02_-_dashboard_revendeur_vue_d'ensemble/code.html`  
**Fonctionnalités :**
- **KPIs principaux :**
  - Ventes du jour/semaine/mois
  - Revenus totaux
  - Commandes en attente
  - Taux de conversion
- **Graphiques :**
  - Évolution des ventes
  - Produits les plus vendus
  - Revenus par période
- **Alertes :**
  - Stock faible
  - Nouvelles commandes
  - Retours clients
- **Actions rapides :**
  - Ajouter un produit
  - Voir les commandes
  - Gérer le stock

**Navigation :**
- → R03 (Personnalisation Boutique)
- → R04 (Gestion Catalogue)
- → R07 (Liste Commandes)
- → R08 (Revenus & Paiements)

---

### 3. GESTION BOUTIQUE (1 écran)

#### R03 - Personnalisation de la Boutique
**Description :** Configuration et personnalisation de la boutique  
**Fichier :** `r03_-_personnalisation_de_la_boutique/code.html`  
**Fonctionnalités :**
- **Informations boutique :**
  - Nom de la boutique
  - Logo (upload)
  - Bannière (upload)
  - Description
  - Catégories principales
- **Paramètres :**
  - Adresse de livraison
  - Coordonnées
  - Horaires
  - Politique de retour
- **Aperçu public :** Visualisation de la boutique côté client
- Sauvegarde et publication

**Navigation :**
- ← Retour (R02)
- → R11 (Aperçu Public Boutique) pour prévisualiser

---

### 4. GESTION PRODUITS (4 écrans)

#### R04 - Gestion du Catalogue Produits
**Description :** Liste et gestion de tous les produits  
**Fichier :** `r04_-_gestion_du_catalogue_produits/code.html`  
**Fonctionnalités :**
- **Liste des produits :**
  - Image, nom, prix, stock
  - Statut (Disponible, Rupture, En attente validation)
  - Performance (ventes, vues)
- **Filtres :**
  - Par catégorie
  - Par statut
  - Par performance
- **Actions :**
  - Ajouter un produit
  - Modifier un produit
  - Dupliquer
  - Mettre en pause
  - Supprimer

**Navigation :**
- ← Retour (R02)
- → R05 (Formulaire Ajout Produit 1)

---

#### R05 - Formulaire Ajout Produit 1
**Description :** Première étape du formulaire d'ajout de produit  
**Fichier :** `r05_-_formulaire_ajout_produit_1/code.html`  
**Champs :**
- Nom du produit
- Catégorie
- Description
- Prix
- Photos (multiple)
- Tags

**Navigation :**
- ← Retour (R04)
- → R05 (Formulaire Ajout Produit 2)

---

#### R05 - Formulaire Ajout Produit 2
**Description :** Deuxième étape avec variantes et stock  
**Fichier :** `r05_-_formulaire_ajout_produit_2/code.html`  
**Fonctionnalités :**
- **Variantes :**
  - Tailles (S, M, L, XL, etc.)
  - Couleurs
  - Autres attributs
- **Stock :**
  - Quantité par variante
  - Gestion automatique
- **Paramètres :**
  - Statut (Disponible, Rupture)
  - Visibilité
  - SEO (mots-clés)
- Validation et publication

**Navigation :**
- ← Retour (R05 Formulaire 1)
- → R04 (Gestion Catalogue) après validation

---

#### R13 - Statistiques Détaillées Produit
**Description :** Analytics détaillées pour un produit spécifique  
**Fichier :** `r13_-_statistiques_détaillées_produit/code.html`  
**Fonctionnalités :**
- Vues et impressions
- Taux de conversion
- Ventes par période
- Revenus générés
- Graphiques de performance
- Comparaison avec autres produits

**Navigation :**
- ← Retour (R04)
- → R04 (Gestion Catalogue)

---

### 5. GESTION STOCK (1 écran)

#### R06 - Inventaire & Gestion Stock
**Description :** Gestion complète de l'inventaire  
**Fichier :** `r06_-_inventaire_&_gestion_stock/code.html`  
**Fonctionnalités :**
- **Liste des produits avec stock :**
  - Quantité disponible
  - Seuil d'alerte
  - Statut (En stock, Faible, Rupture)
- **Alertes :**
  - Stock faible (badge visuel)
  - Stock épuisé
- **Actions :**
  - Ajouter/Retirer du stock
  - Ajustement manuel
  - Historique des mouvements
  - Export Excel
- **Filtres :**
  - Par statut de stock
  - Par catégorie

**Navigation :**
- ← Retour (R02)
- → R04 (Gestion Catalogue) pour modifier un produit

---

### 6. GESTION COMMANDES (2 écrans)

#### R07 - Liste des Commandes Client
**Description :** Liste de toutes les commandes reçues  
**Fichier :** `r07_-_liste_des_commandes_client/code.html`  
**Fonctionnalités :**
- **Liste des commandes :**
  - Numéro, date, client
  - Produits commandés
  - Montant total
  - Statut (En attente, Confirmée, Expédiée, Livrée, Annulée)
- **Filtres :**
  - Par statut
  - Par date
  - Par montant
- **Actions rapides :**
  - Voir détails
  - Confirmer commande
  - Préparer expédition
  - Marquer comme livrée

**Navigation :**
- ← Retour (R02)
- → R09 (Détails Commande & Expédition)

---

#### R09 - Détails Commande & Expédition
**Description :** Détails complets d'une commande et gestion de l'expédition  
**Fichier :** `r09_-_détails_commande_&_expédition/code.html`  
**Fonctionnalités :**
- **Informations commande :**
  - Numéro, date, statut
  - Client (nom, adresse, téléphone)
  - Produits commandés avec quantités
  - Montant total (produits + livraison)
- **Gestion expédition :**
  - Adresse de livraison
  - Numéro de suivi
  - Transporteur
  - Date d'expédition
  - Statut de livraison
- **Actions :**
  - Confirmer la commande
  - Préparer l'expédition
  - Ajouter numéro de suivi
  - Marquer comme livrée
  - Contacter le client

**Navigation :**
- ← Retour (R07)
- → D02 (Messagerie) pour contacter le client

---

### 7. REVENUS & PAIEMENTS (2 écrans)

#### R08 - Revenus & Paiements Revendeur
**Description :** Suivi des revenus et gestion des paiements  
**Fichier :** `r08_-_revenus_&_paiements_revendeur/code.html`  
**Fonctionnalités :**
- **Vue d'ensemble :**
  - Solde disponible
  - Revenus du mois
  - Commission plateforme
  - Paiements en attente
- **Historique des transactions :**
  - Ventes
  - Commissions déduites
  - Retraits
  - Dates et montants
- **Graphiques :**
  - Évolution des revenus
  - Revenus par produit
- **Actions :**
  - Demander un retrait
  - Voir les détails d'une transaction

**Navigation :**
- ← Retour (R02)
- → R16 (Demande de Retrait)

---

#### R16 - Demande de Retrait (Payout)
**Description :** Formulaire de demande de retrait des fonds  
**Fichier :** `r16_-_demande_de_retrait_(payout)/code.html`  
**Fonctionnalités :**
- **Informations :**
  - Solde disponible
  - Montant minimum de retrait
- **Méthode de retrait :**
  - Mobile Money (MTN, Moov, Wave)
  - Virement bancaire
  - Autres méthodes locales
- **Détails :**
  - Montant à retirer
  - Numéro de compte/téléphone
  - Frais de transaction
  - Montant net
- Soumission et suivi

**Navigation :**
- ← Retour (R08)
- → R08 (Revenus & Paiements) après soumission

---

### 8. GESTION RETOURS (2 écrans)

#### R14 - Gestion des Retours Clients
**Description :** Liste des demandes de retour  
**Fichier :** `r14_-_gestion_des_retours_clients/code.html`  
**Fonctionnalités :**
- **Liste des retours :**
  - Numéro, date, client
  - Produit concerné
  - Raison du retour
  - Statut (En attente, Approuvé, Rejeté, Traité)
- **Filtres :**
  - Par statut
  - Par date
- **Actions :**
  - Voir détails
  - Approuver/Rejeter
  - Traiter le retour

**Navigation :**
- ← Retour (R02)
- → R15 (Détails du Retour & Chat SAV)

---

#### R15 - Détails du Retour & Chat SAV
**Description :** Détails d'un retour et communication avec le client  
**Fichier :** `r15_-_détails_du_retour_&_chat_sav/code.html`  
**Fonctionnalités :**
- **Informations retour :**
  - Commande originale
  - Produit retourné
  - Raison détaillée
  - Photos (si fournies)
  - Statut actuel
- **Chat SAV :**
  - Communication avec le client
  - Historique des échanges
  - Résolution du problème
- **Actions :**
  - Approuver le retour
  - Organiser la collecte
  - Remboursement
  - Échanger le produit

**Navigation :**
- ← Retour (R14)
- → D02 (Messagerie) pour le chat

---

### 9. PARAMÈTRES & OUTILS (4 écrans)

#### R10 - Paramètres & Sécurité Revendeur
**Description :** Paramètres du compte et sécurité  
**Fichier :** `r10_-_paramètres_&_sécurité_revendeur/code.html`  
**Fonctionnalités :**
- **Compte :**
  - Informations personnelles
  - Email, téléphone
  - Mot de passe
  - Authentification à deux facteurs
- **Boutique :**
  - Paramètres de visibilité
  - Notifications
  - Langue, devise
- **Sécurité :**
  - Historique de connexion
  - Appareils autorisés
  - Désactiver le compte

**Navigation :**
- ← Retour (R02 ou menu)
- → R03 (Personnalisation Boutique)

---

#### R11 - Aperçu Public Boutique
**Description :** Visualisation de la boutique côté client  
**Fichier :** `r11_-_aperçu_public_boutique/code.html`  
**Fonctionnalités :**
- Vue exacte de la boutique publique
- Navigation comme un client
- Test de l'expérience utilisateur
- Vérification des produits visibles

**Navigation :**
- ← Retour (R03)
- → R04 (Gestion Catalogue) pour modifier

---

#### R12 - Création de Coupons de Réduction
**Description :** Création et gestion de codes promo  
**Fichier :** `r12_-_création_de_coupons_de_réduction/code.html`  
**Fonctionnalités :**
- **Création coupon :**
  - Code promo
  - Type (Pourcentage, Montant fixe)
  - Valeur
  - Date de validité
  - Produits concernés
  - Limite d'utilisation
- **Gestion :**
  - Liste des coupons actifs/expirés
  - Statistiques d'utilisation
  - Désactiver/Activer

**Navigation :**
- ← Retour (R02)
- → R02 (Dashboard) après création

---

#### R17 - Programme de Parrainage (Referral)
**Description :** Gestion du programme de parrainage  
**Fichier :** `r17_-_programme_de_parrainage_(referral)/code.html`  
**Fonctionnalités :**
- Code de parrainage unique
- Statistiques :
  - Nombre de parrainés
  - Récompenses gagnées
- Partage du code
- Historique des parrainages

**Navigation :**
- ← Retour (R02)
- → R02 (Dashboard)

---

#### R18 - Rapport de Performance Mensuel PDF
**Description :** Génération et téléchargement du rapport mensuel  
**Fichier :** `r18_-_rapport_de_performance_mensuel_pdf/code.html`  
**Fonctionnalités :**
- Sélection de la période
- **Contenu du rapport :**
  - Résumé des ventes
  - Top produits
  - Revenus détaillés
  - Graphiques
  - Statistiques comparatives
- Téléchargement PDF
- Envoi par email

**Navigation :**
- ← Retour (R02)
- → R02 (Dashboard)

---

## 🔄 Flux de Navigation Principaux

### Flux 1 : Inscription et Configuration
```
A05 (Onboarding) 
  → A06c (Inscription) 
  → R01 (Choix Type) 
  → R02 (Dashboard) 
  → R03 (Personnalisation Boutique)
```

### Flux 2 : Ajout de Produit
```
R02 (Dashboard) 
  → R04 (Gestion Catalogue) 
  → R05 (Formulaire 1) 
  → R05 (Formulaire 2) 
  → R04 (Catalogue)
```

### Flux 3 : Gestion Commande
```
R02 (Dashboard) 
  → R07 (Liste Commandes) 
  → R09 (Détails Commande) 
  → Expédition 
  → R08 (Revenus)
```

---

## 🎯 Points Clés pour les Développeurs

1. **Validation produits :** Les produits sont soumis à modération admin avant publication

2. **Commission :** Un pourcentage est prélevé sur chaque vente (varie selon l'abonnement)

3. **Stock :** Gestion automatique lors des commandes, alertes si seuil atteint

4. **Paiements :** Les revenus sont disponibles après validation de la commande par le client

5. **Retours :** Gestion via R14-R15 avec possibilité de médiation admin

6. **Aperçu public :** R11 permet de voir exactement ce que voient les clients

---

## 📝 Notes Techniques

- Tous les écrans utilisent un fond blanc
- Couleur primaire : `#1A73B5`
- Framework : Tailwind CSS
- Icônes : Material Symbols Outlined
- Police : Inter (corps), Poppins (titres)

---

**Dernière mise à jour :** 2025-01-XX
