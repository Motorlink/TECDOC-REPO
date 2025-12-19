# TecDoc API - ALLE 68 Funktionen

**Vollständige Übersicht aller verfügbaren Funktionen**  
**Quelle:** TecdocToCatDLB.xsd Schema  
**Datum:** 19. Dezember 2024

---

## 📊 Übersicht

**Gesamt:** 68 Funktionen  
**Freigeschaltet (Provider 23862):** 10 Funktionen (14.7%)  
**Nicht freigeschaltet:** 58 Funktionen (85.3%)

---

## ✅ Freigeschaltete Funktionen (8)

### 1. Basis-Daten

| Funktion | Zweck | Status |
|----------|-------|--------|
| `getCountries` | Länder-Liste | ✅ Funktioniert |
| `getLanguages` | Sprachen-Liste | ⚠️ Nicht getestet |
| `getVersion` | API-Version | ❌ Nicht freigeschaltet |
| `getPegasusVersionInfo` | Pegasus-Version | ✅ Funktioniert |
| `getPegasusVersionInfo2` | Pegasus-Version (erweitert) | ✅ Funktioniert |

### 2. Hersteller & Marken

| Funktion | Zweck | Status |
|----------|-------|--------|
| `getManufacturers` | Autohersteller (434) | ✅ Funktioniert |
| `getAmBrands` | Aftermarket-Marken (197) | ✅ Funktioniert (als getBrands) |

### 3. Artikel

| Funktion | Zweck | Status |
|----------|-------|--------|
| `getArticles` | Artikel-Liste mit allen Feldern | ✅ Funktioniert |
| `getGenericArticles` | Generische Artikel (11.002) | ✅ Funktioniert |
| `getArticleDirectSearchAllNumbersWithState` | Artikelsuche | ✅ Funktioniert |

### 4. Fahrzeuge

| Funktion | Zweck | Status |
|----------|-------|--------|
| `getModelSeries` | Modellreihen | ✅ Funktioniert (leer) |

---

## ❌ NICHT Freigeschaltete Funktionen (60)

### Kategorie 1: Fahrzeug-Identifikation (11 Funktionen)

**VIN-basiert:**
- `getVehiclesByVIN` - VIN → Fahrzeug
- `getVehiclesByVINDataSource` - VIN → Fahrzeug (mit Datenquelle)
- `getOEArticlesByVIN` - VIN → OE-Artikel + Aftermarket

**kTyp-basiert:**
- `getVehicleIdsByKTypeNumber` - kTyp → Fahrzeug-ID
- `getVehicleByIds3` - Fahrzeug-IDs → Fahrzeugdaten
- `getVehicleByIds4` - Fahrzeug-IDs → Fahrzeugdaten (erweitert)

**HSN/TSN (Kennzeichen):**
- `getVehiclesByKeyNumberPlates` - HSN/TSN → Fahrzeug
- `getVehicleIdsByKeyNumberPlates3` - HSN/TSN → Fahrzeug-IDs

**Motorcode:**
- `getVehicleIdsByMotor2` - Motorcode → Fahrzeug-IDs
- `getMotorsByCarTypeManuIdTerm2` - Fahrzeugtyp → Motorcodes

**Sonstige:**
- `getVehicleIdsByCriteria` - Kriterien → Fahrzeug-IDs
- `getVehicleIdsByMark` - Marke → Fahrzeug-IDs
- `getVehicleIdsByVendorId2` - Vendor-ID → Fahrzeug-IDs

---

### Kategorie 2: Fahrzeug-Artikel-Zuordnung (8 Funktionen)

**Linkage (Zuordnung):**
- `getLinkedArticles` - Fahrzeug → Artikel
- `getArticleLinkedAllLinkingTarget3` - Artikel → Fahrzeuge
- `getArticleLinkedAllLinkingTarget4` - Artikel → Fahrzeuge (erweitert)
- `getArticleLinkedAllLinkingTargetManufacturer` - Artikel → Fahrzeuge (Hersteller)
- `getArticleLinkedAllLinkingTargetManufacturer2` - Artikel → Fahrzeuge (Hersteller erweitert)
- `getArticleLinkedAllLinkingTargetsByIds3` - Artikel-IDs → Fahrzeuge

**Assigned Articles:**
- `getAssignedArticlesByIds4` - Fahrzeug-IDs → Zugeordnete Artikel
- `getAssignedArticlesByIds6` - Fahrzeug-IDs → Zugeordnete Artikel (erweitert)
- `getAssignedArticlesByIds7` - Fahrzeug-IDs → Zugeordnete Artikel (erweitert 2)

---

### Kategorie 3: Artikel-Details (10 Funktionen)

**Direkte Artikel-Abfrage:**
- `getDirectArticlesByIds4` - Artikel-IDs → Artikel-Details
- `getDirectArticlesByIds6` - Artikel-IDs → Artikel-Details (erweitert)
- `getDirectArticlesByIds7` - Artikel-IDs → Artikel-Details (erweitert 2)

**Artikel-Beziehungen:**
- `getArticleAccessoryList4` - Artikel → Zubehör-Liste
- `getArticlePartList` - Artikel → Teile-Liste

**Artikel-Suche:**
- `getArticleIdsWithState` - Artikel-IDs mit Status
- `getNewArticleIds` - Neue Artikel-IDs
- `getNewArticleBrands` - Neue Artikel-Marken
- `getNewArticleManufacturers` - Neue Artikel-Hersteller

**Autocomplete:**
- `getAutoCompleteSuggestions` - Autocomplete-Vorschläge

---

### Kategorie 4: Generische Artikel (2 Funktionen)

- `getGenericArticlesByManufacturer6` - Generische Artikel nach Hersteller
- `getGenericArticlesByManufacturer7` - Generische Artikel nach Hersteller (erweitert)

---

### Kategorie 5: Achsen (Axle) (6 Funktionen)

**Achsen-Daten:**
- `getAxleByIds2` - Achsen-IDs → Achsen-Daten
- `getAxleByIds3` - Achsen-IDs → Achsen-Daten (erweitert)
- `getAxleBrakeSizes` - Achsen-Bremsgrößen
- `getAxleKeyNumbers` - Achsen-Schlüsselnummern

**Achsen-Suche:**
- `getAxleIdByKeyNumber` - Schlüsselnummer → Achsen-ID
- `getAxleIdByTypeManCriteria3` - Typ/Hersteller/Kriterien → Achsen-ID

---

### Kategorie 6: Motoren (Motor) (3 Funktionen)

- `getMotorByIds2` - Motor-IDs → Motor-Daten
- `getMotorByIds3` - Motor-IDs → Motor-Daten (erweitert)
- `getMotorIdsByManuIdCriteria2` - Hersteller/Kriterien → Motor-IDs

---

### Kategorie 7: Marken & Hersteller (5 Funktionen)

**Marken:**
- `getAmBrandAddress` - Marken-Adresse
- `getLinkedBrands` - Verknüpfte Marken
- `getMarkById` - Marken-ID → Marke

**Hersteller:**
- `getManufacturers2` - Hersteller (erweitert)
- `getModelSeries2` - Modellreihen (erweitert)

---

### Kategorie 8: Hierarchie & Navigation (4 Funktionen)

**Child Nodes:**
- `getChildNodesAllLinkingTarget2` - Kind-Knoten (alle Linkage-Ziele)
- `getChildNodesPattern` - Kind-Knoten (Pattern)
- `getChildNodesPattern2` - Kind-Knoten (Pattern erweitert)

**Shortcuts:**
- `getShortCuts2` - Shortcuts

---

### Kategorie 9: Kriterien & Attribute (3 Funktionen)

- `getCriteria2` - Kriterien
- `getCriteriaDialogAttributs` - Kriterien-Dialog-Attribute
- `getKeyValues` - Schlüssel-Werte

---

### Kategorie 10: Sonstige (8 Funktionen)

**Country Groups:**
- `getCountryGroups` - Länder-Gruppen

**Vendor:**
- `getVendorIds2` - Vendor-IDs

**Version:**
- `getPegasusVersionInfo2` - Pegasus-Version (erweitert)

---

## 📊 Statistik nach Kategorie

| Kategorie | Anzahl | Freigeschaltet | Prozent |
|-----------|--------|----------------|---------|
| **Fahrzeug-Identifikation** | 11 | 1 | 9% |
| **Fahrzeug-Artikel-Zuordnung** | 8 | 0 | 0% |
| **Artikel-Details** | 10 | 3 | 30% |
| **Generische Artikel** | 2 | 1 | 50% |
| **Achsen** | 6 | 0 | 0% |
| **Motoren** | 3 | 0 | 0% |
| **Marken & Hersteller** | 5 | 2 | 40% |
| **Hierarchie & Navigation** | 4 | 0 | 0% |
| **Kriterien & Attribute** | 3 | 0 | 0% |
| **Basis-Daten** | 4 | 1 | 25% |
| **Sonstige** | 12 | 0 | 0% |
| **GESAMT** | **68** | **10** | **14.7%** |

---

## 🎯 Was fehlt in der Lizenz?

### Kritische fehlende Funktionen:

1. **Fahrzeugzuordnungen (0% verfügbar)**
   - Keine VIN-Dekodierung
   - Keine HSN/TSN-Suche
   - Keine Motorcode-Suche
   - Keine Fahrzeug-Artikel-Zuordnung

2. **Artikel-Details (70% fehlen)**
   - Keine Zubehör-Listen
   - Keine Teile-Listen
   - Keine erweiterten Artikel-Details

3. **Achsen & Motoren (0% verfügbar)**
   - Keine Achsen-Daten
   - Keine Motor-Daten

4. **Navigation (0% verfügbar)**
   - Keine Hierarchie-Navigation
   - Keine Shortcuts

---

## 💡 Empfehlungen

### Für VIN-zu-Artikel Workflow:

**Benötigte Funktionen (alle nicht verfügbar):**
- `getVehiclesByVIN` oder `getOEArticlesByVIN`
- `getVehicleIdsByKeyNumberPlates3` (HSN/TSN)
- `getLinkedArticles` oder `getAssignedArticlesByIds*`

**Lösung:** Hybrid-Ansatz mit externen APIs

---

### Für vollständige Katalog-Funktionalität:

**Benötigte Funktionen:**
- Alle Fahrzeug-Identifikation (11)
- Alle Fahrzeug-Artikel-Zuordnung (8)
- Artikel-Details erweitert (7)

**Lösung:** TecDoc Reference Data Lizenz

---

## 📝 Nächste Schritte

### Sofort testbar:

1. `getLanguages` - Sprachen-Liste
2. `getVersion` - API-Version
3. `getPegasusVersionInfo` - Pegasus-Version
4. `getCountryGroups` - Länder-Gruppen

### Für Lizenz-Upgrade anfragen:

1. **VIN-Funktionen** (3):
   - `getVehiclesByVIN`
   - `getOEArticlesByVIN`
   - `getVehiclesByVINDataSource`

2. **HSN/TSN-Funktionen** (2):
   - `getVehicleIdsByKeyNumberPlates3`
   - `getVehiclesByKeyNumberPlates`

3. **Linkage-Funktionen** (6):
   - `getLinkedArticles`
   - `getAssignedArticlesByIds6`
   - `getArticleLinkedAllLinkingTarget4`

---

**Erstellt:** 19. Dezember 2024  
**Quelle:** TecdocToCatDLB.xsd  
**Gesamt-Funktionen:** 68  
**Freigeschaltet:** 8 (11.8%)
