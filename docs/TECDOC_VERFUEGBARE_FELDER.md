# TecDoc API - Verfügbare Felder (Provider ID 23862)

**Stand:** 19. Dezember 2025  
**Basierend auf:** Deep Research mit OpenAI & XSD Schema-Analyse

---

## ✅ VERFÜGBARE FELDER (27)

Diese Felder kann ich **erfolgreich abrufen** und sie enthalten **Daten**:

### 1. Basis-Informationen (5 Felder)

| Feld | Beschreibung | Beispiel |
|------|--------------|----------|
| **articleNumber** | TecDoc-interne Artikelnummer | `1180461S01` |
| **dataSupplierId** | DataSupplier-ID | `4` |
| **mfrId** | Hersteller-ID | `504` |
| **mfrName** | Hersteller-Name | `MANN-FILTER` |
| **ean (gtins)** | EAN-Nummer / GTIN | `4011558054885` |

---

### 2. Produkt-Klassifizierung (6 Felder)

| Feld | Beschreibung | Beispiel |
|------|--------------|----------|
| **genericArticleId** | Generischer Artikel ID | `8` |
| **genericArticleDescription** | Produkttyp / Kategorie | `Luftfilter` |
| **assemblyGroupNodeId** | Montagegruppe ID | `67` |
| **assemblyGroupName** | Montagegruppe Name | `Luftversorgung` |
| **legacyArticleId** | Legacy Artikel-ID | `283611344` |
| **linkageTargetTypes** | Zuordnungstypen | `V, O, M` (Vehicle, CV, Motor) |

---

### 3. OE-Nummern (1 Feld, mehrere Werte)

| Feld | Beschreibung | Beispiel |
|------|--------------|----------|
| **oemNumbers** | Original Equipment Nummern | `000 094 69 04 (MERCEDES-BENZ)`<br>`A 000 094 69 04 (MERCEDES-BENZ)` |

**Struktur:** Jede OE-Nummer enthält:
- `articleNumber` - OE-Nummer
- `mfrId` - Fahrzeughersteller-ID
- `mfrName` - Fahrzeughersteller-Name

---

### 4. Technische Attribute (1 Feld, mehrere Werte)

| Feld | Beschreibung | Beispiel |
|------|--------------|----------|
| **articleCriteria** | Technische Daten & Eigenschaften | `Filterausführung: Filtereinsatz`<br>`Innendurchmesser: 222 mm`<br>`Außendurchmesser: 125 mm`<br>`Höhe: 164 mm` |

**Struktur:** Jedes Kriterium enthält:
- `criteriaId` - Kriterium-ID
- `criteriaDescription` - Beschreibung
- `criteriaType` - Typ (K=Key, N=Numeric)
- `rawValue` - Rohdaten
- `formattedValue` - Formatierter Wert
- `criteriaUnitDescription` - Einheit (z.B. mm)
- `immediateDisplay` - Sofort anzeigen
- `isMandatory` - Pflichtfeld
- `isInterval` - Ist Intervall

---

### 5. Artikel-Status & Metadaten (14 Felder)

| Feld | Beschreibung | Beispiel |
|------|--------------|----------|
| **articleStatusId** | Status-ID | `1` |
| **articleStatusDescription** | Status-Beschreibung | `Normal` |
| **articleStatusValidFromDate** | Gültig ab Datum | `20141110` |
| **quantityPerPackage** | Menge pro Paket | `1` |
| **quantityPerPartPerPackage** | Menge pro Teil pro Paket | `1` |
| **isSelfServicePacking** | Selbstbedienungsverpackung | `false` |
| **hasMandatoryMaterialCertification** | Materialzertifikat erforderlich | `false` |
| **isRemanufacturedPart** | Wiederaufbereitetes Teil | `false` |
| **isAccessory** | Zubehör | `false` |
| **batchSize1** | Losgröße 1 | `0` |
| **batchSize2** | Losgröße 2 | `0` |
| **hasPartsListParent** | Hat Teileliste | `false` |
| **hasAccessoryListParent** | Hat Zubehörliste | `false` |
| **totalLinkages** | Anzahl Fahrzeugzuordnungen | `0` |

---

## ❌ NICHT VERFÜGBARE FELDER (10)

Diese Felder sind **im XSD Schema definiert**, aber für Provider ID 23862 **NICHT freigeschaltet**:

### 1. Beschreibungen & Texte

| Feld | Beschreibung | Status |
|------|--------------|--------|
| **articleText** | Artikelbeschreibungen | ❌ Leer |
| **tradeNumbers** | Handelsnummern | ❌ Leer |

---

### 2. Medien & Dokumente

| Feld | Beschreibung | Status |
|------|--------------|--------|
| **images** | Artikelbilder (URLs) | ❌ Leer |
| **pdfs** | PDF-Dokumente (URLs) | ❌ Leer |

---

### 3. Preise

| Feld | Beschreibung | Status |
|------|--------------|--------|
| **prices** | Preise | ❌ Leer |

---

### 4. Fahrzeugzuordnungen (Details)

| Feld | Beschreibung | Status |
|------|--------------|--------|
| **linkages** | Fahrzeugzuordnungen (Details) | ❌ Leer |

**Hinweis:** `totalLinkages` zeigt die **Anzahl** der Zuordnungen, aber die **Details** sind nicht verfügbar.

---

### 5. Ersatzteile & Vergleiche

| Feld | Beschreibung | Status |
|------|--------------|--------|
| **replacesArticles** | Ersetzt diese Artikel | ❌ Leer |
| **replacedByArticles** | Wird ersetzt durch | ❌ Leer |
| **comparableNumbers** | Vergleichbare Nummern | ❌ Leer |

---

### 6. Links

| Feld | Beschreibung | Status |
|------|--------------|--------|
| **links** | Externe Links | ❌ Leer |

---

## 📊 Statistik

| Kategorie | Anzahl | Prozent |
|-----------|--------|---------|
| **Verfügbare Felder** | 27 | 73% |
| **Nicht verfügbare Felder** | 10 | 27% |
| **Gesamt** | 37 | 100% |

---

## 🔧 Wie rufe ich die Felder ab?

### WICHTIG: Include-Parameter verwenden!

Ohne die `include*` Parameter liefert die API nur **4 Basis-Felder**!

```xml
<getArticles xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
    <articleCountry>de</articleCountry>
    <dataSupplierIds>4</dataSupplierIds>
    <perPage>10</perPage>
    <page>1</page>
    
    <!-- WICHTIG: Diese Parameter aktivieren die zusätzlichen Felder! -->
    <includeAll>true</includeAll>
    <includeMisc>true</includeMisc>
    <includeGenericArticles>true</includeGenericArticles>
    <includeGTINs>true</includeGTINs>
    <includeOEMNumbers>true</includeOEMNumbers>
    <includeArticleCriteria>true</includeArticleCriteria>
    <includeLinkages>true</includeLinkages>
    
    <!-- Optional (funktionieren nicht mit aktueller Lizenz) -->
    <includeArticleText>true</includeArticleText>
    <includeImages>true</includeImages>
    <includePrices>true</includePrices>
    <includePDFs>true</includePDFs>
    <includeTradeNumbers>true</includeTradeNumbers>
    <includeReplacesArticles>true</includeReplacesArticles>
    <includeReplacedByArticles>true</includeReplacedByArticles>
    <includeComparableNumbers>true</includeComparableNumbers>
    <includeLinks>true</includeLinks>
</getArticles>
```

---

## 💡 Wichtige Erkenntnisse

### 1. **Include-Parameter sind essentiell**
Ohne `include*` Parameter → nur 4 Felder  
Mit `include*` Parametern → 27 Felder (**+575%**)

### 2. **Verschachtelte Daten**
Viele Felder enthalten **mehrere Werte**:
- `oemNumbers` - Mehrere OE-Nummern pro Artikel
- `articleCriteria` - Mehrere technische Attribute
- `linkageTargetTypes` - Mehrere Zuordnungstypen

### 3. **Lizenz-Limitierungen**
Die fehlenden Felder sind **technisch verfügbar** (im XSD Schema definiert), aber für die aktuelle Lizenz **nicht freigeschaltet**.

### 4. **totalLinkages vs. linkages**
- `totalLinkages` = **Anzahl** der Fahrzeugzuordnungen (verfügbar ✅)
- `linkages` = **Details** der Zuordnungen (nicht verfügbar ❌)

---

## 🎯 Empfehlungen

### Für die aktuelle Lizenz:

**Nutze diese verfügbaren Felder optimal:**

1. **EAN** - Für Produktidentifikation
2. **OE-Nummern** - Für Kreuzreferenzen zu Fahrzeugherstellern
3. **Technische Attribute** - Für Produktspezifikationen
4. **Generische Artikel** - Für Kategorisierung
5. **Artikel-Status** - Für Verfügbarkeit

### Für fehlende Daten:

**Workarounds:**
- **Bilder** → Verwende externe Bild-Datenbanken (z.B. DataSupplier-eigene)
- **Preise** → Verwende eigene Preisdatenbank
- **Beschreibungen** → Verwende generische Artikel-Beschreibungen
- **Fahrzeugzuordnungen** → Upgrade erforderlich

---

## 📖 Weitere Informationen

Siehe auch:
- **TECDOC_DEEP_RESEARCH_REPORT.md** - Vollständiger Research-Report
- **TecdocToCatDLB.xsd** - Vollständiges XSD Schema
- **openai_xsd_analysis.md** - OpenAI Schema-Analyse

---

**Erstellt am:** 19. Dezember 2025  
**Provider ID:** 23862  
**API Version:** Pegasus 3.0
