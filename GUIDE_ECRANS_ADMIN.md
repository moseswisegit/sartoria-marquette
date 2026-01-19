# 🔧 Guide des Écrans - Profil Administrateur

**Version :** 1.0  
**Date :** 2025-01-XX  
**Profil :** Administrateur (Gestion plateforme)

---

## 📋 Vue d'Ensemble

Le profil Administrateur permet de :
- Superviser toute la plateforme
- Gérer les utilisateurs (clients, tailleurs, revendeurs)
- Modérer les contenus et produits
- Gérer les litiges et médiations
- Configurer les paramètres système
- Analyser les performances globales

**Total d'écrans :** 16 écrans

---

## 🗂️ Organisation des Écrans

### 1. AUTHENTIFICATION (1 écran)

#### A07 - Écran de Connexion
**Description :** Authentification administrateur avec accès sécurisé  
**Fichier :** `écran_de_connexion/code.html`  
**Fonctionnalités :**
- Connexion par email/mot de passe
- Authentification à deux facteurs (2FA) obligatoire
- Session sécurisée avec expiration automatique
- Logs d'accès

**Navigation :**
- → F01 (Dashboard Statistiques) après connexion réussie

---

### 2. DASHBOARD & STATISTIQUES (1 écran)

#### F01 - Dashboard Statistiques
**Description :** Vue d'ensemble globale de la plateforme  
**Fichier :** `dashboard_statistiques/code.html`  
**Fonctionnalités :**
- **KPIs globaux :**
  - Utilisateurs actifs (clients, tailleurs, revendeurs)
  - Commandes du jour/semaine/mois
  - Revenus totaux
  - Taux de croissance
- **Graphiques :**
  - Évolution des utilisateurs
  - Répartition par profil
  - Revenus par période
  - Top villes/regions
- **Alertes :**
  - Litiges en attente
  - KYC à valider
  - Produits à modérer
  - Transactions suspectes
- **Actions rapides :**
  - Accès aux sections principales

**Navigation :**
- → F02 (Gestion Utilisateurs)
- → F12 (Gestion Revendeurs)
- → F03 (Gestion Litiges)
- → F05 (Gestion Abonnements)

---

### 3. GESTION UTILISATEURS (1 écran)

#### F02 - Gestion des Utilisateurs
**Description :** Liste et gestion de tous les utilisateurs de la plateforme  
**Fichier :** `gestion_des_utilisateurs/code.html`  
**Fonctionnalités :**
- **Liste des utilisateurs :**
  - Clients
  - Tailleurs
  - Revendeurs
  - Filtres par type, statut, KYC, date
- **Statistiques :**
  - Total utilisateurs
  - Par type
  - Par statut KYC
- **Recherche :**
  - Par nom, email, téléphone
- **Actions :**
  - Voir profil détaillé
  - Activer/Désactiver compte
  - Valider/Rejeter KYC
  - Modifier informations
  - Supprimer compte (avec confirmation)

**Navigation :**
- ← Retour (F01)
- → A09 (Validation KYC Tailleur) pour un tailleur
- → F13 (Validation KYC Revendeur) pour un revendeur

---

### 4. GESTION REVENDEURS (5 écrans)

#### F12 - Gestion des Revendeurs
**Description :** Liste et gestion de tous les revendeurs  
**Fichier :** `f12_-_gestion_des_revendeurs/code.html`  
**Fonctionnalités :**
- **Statistiques :**
  - Total revendeurs
  - Actifs, En attente, Rejetés
- **Liste des revendeurs :**
  - Nom boutique, revendeur, localisation
  - Statut (Actif, En attente, Suspendu)
  - Statut KYC (Validé, En cours, Rejeté)
  - Nombre de produits, ventes
- **Filtres :**
  - Par statut
  - Par KYC
  - Par date
- **Recherche :**
  - Par nom boutique, revendeur
- **Actions :**
  - Voir détails
  - Valider/Rejeter KYC
  - Activer/Suspendre boutique
  - Voir produits

**Navigation :**
- ← Retour (F01)
- → F13 (Validation KYC Revendeur)
- → F14 (Modération Produits)

---

#### F13 - Validation KYC Revendeur
**Description :** Validation détaillée du KYC d'un revendeur  
**Fichier :** `f13_-_validation_kyc_revendeur/code.html`  
**Fonctionnalités :**
- **Onglets :**
  - En attente
  - Validés
  - Rejetés
- **Dossier revendeur :**
  - Informations personnelles
  - Type de boutique (Individuel/Entreprise)
  - Documents justificatifs :
    - RCCM (si entreprise)
    - CNI/Pièce identité
    - Justificatif de domicile
  - Validation IA des documents
- **Actions :**
  - Valider le KYC
  - Rejeter avec raison
  - Demander documents supplémentaires

**Navigation :**
- ← Retour (F12)
- → F12 (Gestion Revendeurs) après validation

---

#### F14 - Modération Produits Revendeurs
**Description :** Modération des produits soumis par les revendeurs  
**Fichier :** `f14_-_modération_produits_revendeurs/code.html`  
**Fonctionnalités :**
- **Statistiques :**
  - En attente
  - Signalés
  - Validés
- **Onglets :**
  - En attente
  - Signalés
  - Validés
- **Liste des produits :**
  - Image, nom, boutique, prix
  - Statut
  - Raison du signalement (si applicable)
- **Actions :**
  - Valider le produit
  - Rejeter avec raison
  - Bloquer (contenu non conforme)
  - Voir détails complets

**Navigation :**
- ← Retour (F12)
- → F12 (Gestion Revendeurs)

---

#### F15 - Gestion Commissions Revendeurs
**Description :** Suivi et gestion des commissions des revendeurs  
**Fichier :** `f15_-_gestion_commissions_revendeurs/code.html`  
**Fonctionnalités :**
- **Vue d'ensemble :**
  - Total commissions collectées
  - Taux moyen de commission
- **Règles de commission :**
  - Revendeur Basic : 10%
  - Revendeur Pro : 8%
  - Revendeur Premium : 5%
- **Liste des revendeurs :**
  - Nom boutique
  - Type d'abonnement
  - Chiffre d'affaires
  - Commission générée
- **Filtres :**
  - Par période
  - Par revendeur
  - Par type d'abonnement
- **Actions :**
  - Voir détails
  - Modifier les règles (si nécessaire)
  - Exporter les données

**Navigation :**
- ← Retour (F01)
- → F12 (Gestion Revendeurs)

---

#### F16 - Validation Demandes Retrait
**Description :** Validation des demandes de retrait des revendeurs  
**Fichier :** `f16_-_validation_demandes_retrait/code.html`  
**Fonctionnalités :**
- **Statistiques :**
  - En attente
  - Validées
  - Total montant
- **Onglets :**
  - En attente
  - Validées
  - Rejetées
- **Liste des demandes :**
  - Revendeur, boutique
  - Montant demandé
  - Méthode (MTN, Moov, Virement)
  - Numéro de compte
  - Date de demande
- **Actions :**
  - Valider la demande
  - Rejeter avec raison
  - Voir historique des retraits
  - Exporter les données

**Navigation :**
- ← Retour (F01)
- → F12 (Gestion Revendeurs)

---

### 5. GESTION LITIGES & MODÉRATION (2 écrans)

#### F03 - Gestion des Litiges Admin
**Description :** Liste et gestion de tous les litiges  
**Fichier :** `gestion_des_litiges_admin/code.html`  
**Fonctionnalités :**
- **Liste des litiges :**
  - Numéro, date, type
  - Parties concernées (client, tailleur/revendeur)
  - Statut (En attente, En cours, Résolu, Fermé)
  - Priorité (Urgent, Normal, Faible)
- **Filtres :**
  - Par statut
  - Par type
  - Par priorité
  - Par date
- **Recherche :**
  - Par numéro, nom, email
- **Actions :**
  - Voir détails
  - Assigner un médiateur
  - Résoudre le litige

**Navigation :**
- ← Retour (F01)
- → F04 (Détails & Médiation Litige)

---

#### F04 - Détails & Médiation Litige
**Description :** Détails complets d'un litige et processus de médiation  
**Fichier :** `détails_&_médiation_litige/code.html`  
**Fonctionnalités :**
- **Informations litige :**
  - Numéro, date, statut
  - Type (Commande, Produit, Paiement, etc.)
  - Parties concernées avec coordonnées
  - Description détaillée
  - Pièces jointes (photos, documents)
- **Historique :**
  - Chronologie des événements
  - Messages échangés
  - Actions prises
- **Médiation :**
  - Zone de communication avec les parties
  - Propositions de résolution
  - Décision finale
  - Remboursement si applicable
- **Actions :**
  - Contacter les parties
  - Proposer une solution
  - Clôturer le litige
  - Escalader si nécessaire

**Navigation :**
- ← Retour (F03)
- → D02 (Messagerie) pour contacter les parties

---

### 6. GESTION FINANCIÈRE (1 écran)

#### F05 - Gestion Abonnements & Commissions
**Description :** Gestion des abonnements tailleurs et commissions  
**Fichier :** `gestion_abonnements_&_commissions/code.html`  
**Fonctionnalités :**
- **Abonnements tailleurs :**
  - Liste des abonnements actifs
  - Forfaits (Basic, Pro, Premium)
  - Renouvellements
  - Paiements en attente
- **Commissions :**
  - Règles de commission par type
  - Historique des commissions
  - Calculs automatiques
- **Actions :**
  - Modifier les forfaits
  - Ajuster les commissions
  - Gérer les renouvellements
  - Exporter les données

**Navigation :**
- ← Retour (F01)
- → E06 (Forfaits d'Abonnement) pour voir les détails

---

### 7. GESTION STOCK (1 écran)

#### F07 - Gestion du Stock Tissus
**Description :** Vue globale du stock de tissus de tous les tailleurs  
**Fichier :** `gestion_du_stock_tissus/code.html`  
**Fonctionnalités :**
- Vue agrégée du stock
- Statistiques par type de tissu
- Alertes stock faible globales
- Export des données

**Navigation :**
- ← Retour (F01)
- → E04 (Gestion Stock Tissus Tailleur) pour un tailleur spécifique

---

### 8. CONFIGURATION & DOCUMENTATION (4 écrans)

#### F09 - Plan de Site & Architecture Flux 1
**Description :** Documentation de l'architecture et des flux de l'application  
**Fichier :** `plan_de_site_&_architecture_flux_1/code.html`  
**Fonctionnalités :**
- Vue d'ensemble de l'architecture
- Flux principaux
- Structure des profils

**Navigation :**
- ← Retour (F01)
- → F10 (Plan de Site & Architecture Flux 2)

---

#### F10 - Plan de Site & Architecture Flux 2
**Description :** Suite de la documentation des flux  
**Fichier :** `plan_de_site_&_architecture_flux_2/code.html`  
**Fonctionnalités :**
- Flux détaillés par profil
- Interactions entre modules

**Navigation :**
- ← Retour (F09)
- → F11 (Guide des Interactions)

---

#### F11 - Guide des Interactions & Navigation Flux
**Description :** Guide complet des interactions et navigation  
**Fichier :** `guide_des_interactions_&_navigation_flux/code.html`  
**Fonctionnalités :**
- Carte des interactions
- Navigation entre écrans
- Flux utilisateur complets

**Navigation :**
- ← Retour (F10)
- → F01 (Dashboard)

---

## 🔄 Flux de Navigation Principaux

### Flux 1 : Validation KYC Revendeur
```
F01 (Dashboard) 
  → F12 (Gestion Revendeurs) 
  → F13 (Validation KYC) 
  → Validation/Rejet 
  → F12 (Gestion Revendeurs)
```

### Flux 2 : Modération Produit
```
F01 (Dashboard) 
  → F14 (Modération Produits) 
  → Voir détails 
  → Valider/Bloquer 
  → F14 (Modération)
```

### Flux 3 : Gestion Litige
```
F01 (Dashboard) 
  → F03 (Gestion Litiges) 
  → F04 (Détails & Médiation) 
  → Médiation 
  → Résolution 
  → F03 (Gestion Litiges)
```

### Flux 4 : Validation Retrait
```
F01 (Dashboard) 
  → F16 (Validation Retraits) 
  → Voir détails 
  → Valider/Rejeter 
  → F16 (Validation Retraits)
```

---

## 🎯 Points Clés pour les Développeurs

1. **Sécurité :** Accès admin très sécurisé avec 2FA obligatoire

2. **KYC :** Validation manuelle requise pour tailleurs et revendeurs

3. **Modération :** Tous les produits revendeurs sont modérés avant publication

4. **Commissions :** Calcul automatique mais possibilité d'ajustement manuel

5. **Litiges :** Processus de médiation avec communication directe avec les parties

6. **Retraits :** Validation manuelle des demandes de retrait pour sécurité

7. **Audit :** Toutes les actions admin sont loggées pour traçabilité

---

## 📝 Notes Techniques

- Tous les écrans utilisent un fond blanc
- Couleur primaire : `#1A73B5`
- Framework : Tailwind CSS
- Icônes : Material Symbols Outlined
- Police : Inter (corps), Poppins (titres)
- **Sécurité :** Sessions avec expiration, logs d'audit, 2FA

---

## 🔐 Permissions Administrateur

- **Lecture seule :** Consultation de toutes les données
- **Modification :** Utilisateurs, produits, contenus
- **Validation :** KYC, produits, retraits
- **Médiation :** Litiges, résolution de conflits
- **Configuration :** Paramètres système, règles de commission

---

**Dernière mise à jour :** 2025-01-XX
