# ✂️ Guide des Écrans - Profil Tailleur

**Version :** 1.0  
**Date :** 2025-01-XX  
**Profil :** Tailleur (Artisan couturier)

---

## 📋 Vue d'Ensemble

Le profil Tailleur permet aux artisans couturiers de :
- Gérer leur activité professionnelle (commandes, clients, stock)
- Utiliser un CRM pour sauvegarder les mesures clients
- Suivre leurs performances business (KPIs, revenus)
- Gérer leurs abonnements et paiements
- Organiser leur calendrier de rendez-vous

**Total d'écrans :** 11 écrans

---

## 🗂️ Organisation des Écrans

### 1. AUTHENTIFICATION & ONBOARDING (2 écrans)

#### A06b - Écran d'Inscription Tailleur
**Description :** Formulaire d'inscription spécifique pour les tailleurs  
**Fichier :** `écran_d'inscription_tailleur/code.html`  
**Champs requis :**
- Nom complet
- Email
- Téléphone (obligatoire)
- Pays
- Nom de l'atelier (obligatoire)
- Adresse de l'atelier (obligatoire)
- Spécialités (checkboxes : Costume, Robe, Tenue traditionnelle, etc.)
- Mot de passe
- Confirmation mot de passe

**Navigation :**
- → A07 (Connexion) après inscription réussie

---

#### A07 - Écran de Connexion
**Description :** Authentification du tailleur  
**Fichier :** `écran_de_connexion/code.html`  
**Fonctionnalités :**
- Connexion par email/mot de passe
- Option "Se souvenir de moi"
- Lien vers mot de passe oublié
- Lien vers inscription

**Navigation :**
- → E01 (Dashboard Business) après connexion réussie
- ⚠️ Si KYC non validé, le tailleur sera redirigé vers un message d'attente (la validation KYC est gérée par l'admin via F03)

---

### 2. ABONNEMENTS & PAIEMENTS (3 écrans)

#### E06 - Forfaits d'Abonnement Tailleurs
**Description :** Choix et comparaison des forfaits d'abonnement  
**Fichier :** `forfaits_d'abonnement_tailleurs/code.html`  
**Forfaits disponibles :**
- **Basic** : Fonctionnalités essentielles
- **Pro** : Fonctionnalités avancées + analytics
- **Premium** : Toutes les fonctionnalités + support prioritaire

**Fonctionnalités :**
- Comparaison des forfaits
- Prix mensuel/annuel
- Liste des fonctionnalités incluses
- Période d'essai gratuite (si applicable)
- Bouton "Choisir ce forfait"

**Navigation :**
- ← Retour (E01 ou menu)
- → E07 (Paiement de l'Abonnement)

---

#### E07 - Paiement de l'Abonnement
**Description :** Finalisation du paiement de l'abonnement  
**Fichier :** `paiement_de_l'abonnement/code.html`  
**Fonctionnalités :**
- Récapitulatif du forfait choisi
- Méthodes de paiement :
  - Carte bancaire
  - Mobile Money (MTN, Moov, Wave)
  - Virement bancaire
- Informations de facturation
- Conditions générales
- Confirmation de paiement

**Navigation :**
- ← Retour (E06)
- → E10 (Facture de Paiement PDF) après paiement réussi
- → E01 (Dashboard Business) après activation

---

#### E10 - Facture de Paiement PDF
**Description :** Facture téléchargeable au format PDF  
**Fichier :** `facture_de_paiement_pdf/code.html`  
**Fonctionnalités :**
- Aperçu de la facture
- Informations : numéro, date, montant, forfait
- Détails de la transaction
- Bouton "Télécharger PDF"
- Envoi par email

**Navigation :**
- ← Retour (E07)
- → E01 (Dashboard Business)

---

### 3. DASHBOARD & VUE D'ENSEMBLE (1 écran)

#### E01 - Dashboard Business Tailleur
**Description :** Tableau de bord principal avec KPIs et vue d'ensemble  
**Fichier :** `dashboard_tailleur_-_business_kpis/code.html`  
**Fonctionnalités :**
- **KPIs principaux :**
  - Chiffre d'affaires mensuel
  - Nombre de commandes en cours
  - Clients actifs
  - Taux de satisfaction
- **Graphiques :**
  - Évolution des revenus
  - Commandes par statut
  - Top clients
- **Alertes :**
  - Commandes urgentes
  - Rendez-vous à venir
  - Stock faible
- **Actions rapides :**
  - Nouvelle commande
  - Ajouter client
  - Voir calendrier

**Navigation :**
- → E02 (Gestion des Commandes)
- → E03 (CRM Fiches Clients)
- → E04 (Gestion du Stock Tissus)
- → E05 (Calendrier des Rendez-vous)

---

### 4. GESTION OPÉRATIONNELLE (4 écrans)

#### E02 - Gestion des Commandes Tailleur
**Description :** Liste et gestion de toutes les commandes  
**Fichier :** `gestion_des_commandes_tailleur/code.html`  
**Fonctionnalités :**
- Liste des commandes avec filtres :
  - Statut (En attente, En cours, Terminée, Annulée)
  - Date
  - Client
  - Priorité
- **Workflow de production :**
  1. Commande reçue
  2. Mesures validées
  3. Coupe
  4. Couture
  5. Essayage
  6. Retouches
  7. Livraison
- Actions par commande :
  - Voir détails
  - Mettre à jour le statut
  - Ajouter des photos
  - Contacter le client
  - Marquer comme terminée

**Navigation :**
- ← Retour (E01)
- → D02 (Messagerie - Chat) pour contacter un client
- → D01 (Suivi Timeline Commande) pour voir les détails

---

#### E03 - CRM Fiches Clients
**Description :** Gestion complète de la base de données clients  
**Fichier :** `crm_tailleur_-_fiches_clients/code.html`  
**Fonctionnalités :**
- **Liste des clients :**
  - Recherche par nom, email, téléphone
  - Filtres : VIP, Régulier, Occasionnel
  - Tags et catégories
- **Fiche client complète :**
  - Informations personnelles
  - Photo de profil
  - Historique des commandes
  - **Mesures détaillées :**
    - Historique des modifications
    - Mesures par type de vêtement
    - Templates personnalisés
  - Préférences (couleurs, styles, tissus)
  - Notes privées
  - Photos d'inspiration
- **Actions :**
  - Ajouter un client
  - Modifier les mesures
  - Créer une nouvelle commande
  - Exporter les données

**Navigation :**
- ← Retour (E01)
- → B04 (Création de Commande) pour créer une commande
- → B06 (Profil Client - Mesures) pour voir les mesures

---

#### E04 - Gestion du Stock Tissus
**Description :** Inventaire et gestion du stock de tissus  
**Fichier :** `gestion_du_stock_tissus/code.html`  
**Fonctionnalités :**
- **Liste des tissus :**
  - Nom, type, couleur
  - Quantité en stock
  - Prix d'achat
  - Fournisseur
  - Photos
- **Alertes :**
  - Stock faible (seuil configurable)
  - Stock épuisé
- **Actions :**
  - Ajouter un tissu
  - Modifier la quantité
  - Historique des entrées/sorties
  - Marquer comme épuisé
- **Recherche et filtres :**
  - Par type (Wax, Bazin, Soie, etc.)
  - Par couleur
  - Par fournisseur

**Navigation :**
- ← Retour (E01)
- → E02 (Gestion des Commandes) pour utiliser un tissu

---

#### E05 - Calendrier des Rendez-vous
**Description :** Planning des rendez-vous avec clients  
**Fichier :** `calendrier_des_rendez-vous/code.html`  
**Fonctionnalités :**
- **Vue calendrier :**
  - Mensuelle
  - Hebdomadaire
  - Quotidienne
- **Types de rendez-vous :**
  - Prise de mesures
  - Essayage
  - Retouches
  - Livraison
- **Informations :**
  - Client concerné
  - Commande associée
  - Heure et durée
  - Notes
- **Actions :**
  - Créer un rendez-vous
  - Modifier/Annuler
  - Rappels automatiques
  - Synchronisation avec calendrier externe

**Navigation :**
- ← Retour (E01)
- → E02 (Gestion des Commandes) depuis un RDV
- → E03 (CRM Fiches Clients) depuis un RDV

---

### 5. PROFIL & PARAMÈTRES (1 écran)

#### E08 - Détails Profil Tailleur
**Description :** Gestion du profil professionnel du tailleur  
**Fichier :** `détails_profil_tailleur/code.html`  
**Fonctionnalités :**
- **Informations professionnelles :**
  - Nom de l'atelier
  - Photo de profil
  - Bannière
  - Description
  - Spécialités
  - Localisation
  - Coordonnées
- **Paramètres :**
  - Notifications
  - Confidentialité
  - Langue
  - Devise
- **Statistiques publiques :**
  - Note moyenne
  - Nombre d'avis
  - Nombre de réalisations
- **Actions :**
  - Modifier les informations
  - Changer le mot de passe
  - Gérer les abonnements
  - Désactiver le compte

**Navigation :**
- ← Retour (E01 ou menu)
- → E06 (Forfaits d'Abonnement)

---

### 6. NOTIFICATIONS & UTILITAIRES (1 écran)

#### N03 - Centre de Notifications Global
**Description :** Centre de toutes les notifications du tailleur  
**Fichier :** `n03_-_centre_de_notifications_global/code.html`  
**Fonctionnalités :**
- **Types de notifications :**
  - Nouvelles commandes
  - Messages clients
  - Rendez-vous à venir
  - Alertes stock
  - Paiements reçus
  - Mises à jour système
- **Filtres :**
  - Par type
  - Par date
  - Lu/Non lu
- **Actions :**
  - Marquer comme lu
  - Actions rapides depuis les notifications
  - Paramètres de notification

**Navigation :**
- Accessible depuis n'importe quel écran
- → E02 (Gestion des Commandes) depuis notification commande
- → D02 (Messagerie) depuis notification message

---

## 🔄 Flux de Navigation Principaux

### Flux 1 : Inscription et Validation
```
A06b (Inscription Tailleur) 
  → A07 (Connexion) 
  → [Attente validation KYC par admin - F03]
  → E06 (Forfaits Abonnement) 
  → E07 (Paiement) 
  → E01 (Dashboard)
```

### Flux 2 : Gestion Quotidienne
```
E01 (Dashboard) 
  → E02 (Gestion Commandes) 
  → E03 (CRM Clients) 
  → E04 (Stock Tissus) 
  → E05 (Calendrier RDV)
```

### Flux 3 : Nouvelle Commande
```
E01 (Dashboard) 
  → E03 (CRM Clients) 
  → Sélection Client 
  → E02 (Création Commande) 
  → E02 (Suivi Commande)
```

---

## 🎯 Points Clés pour les Développeurs

1. **KYC obligatoire :** Le tailleur doit avoir son KYC validé par l'admin (F03) avant d'accéder aux fonctionnalités complètes. Le tailleur soumet ses documents lors de l'inscription, puis attend la validation de l'admin.

2. **Abonnement requis :** Accès limité sans abonnement actif

3. **CRM central :** E03 est le cœur du système, toutes les données clients y sont centralisées

4. **Workflow commande :** E02 suit un workflow strict en 7 étapes avec photos obligatoires

5. **Stock :** E04 permet de gérer l'inventaire mais n'est pas obligatoire (certains tailleurs n'ont pas de stock)

6. **Calendrier :** E05 peut être synchronisé avec Google Calendar ou autres

---

## 📝 Notes Techniques

- Tous les écrans utilisent un fond blanc
- Couleur primaire : `#1A73B5`
- Framework : Tailwind CSS
- Icônes : Material Symbols Outlined
- Police : Inter (corps), Poppins (titres)

---

**Dernière mise à jour :** 2025-01-XX
