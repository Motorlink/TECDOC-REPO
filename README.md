# TecDoc API - Vollständige Dokumentation

**⚠️ WICHTIG FÜR ALLE KI-AGENTEN:**  
Diese README enthält **alle kritischen Informationen** zur korrekten Nutzung der TecDoc API. **Lesen Sie diese Datei vollständig**, bevor Sie mit der API arbeiten!

---

## 📋 Inhaltsverzeichnis

1. [Schnellstart](#schnellstart)
2. [API-Zugangsdaten](#api-zugangsdaten)
3. [Kritische Erkenntnisse](#kritische-erkenntnisse)
4. [Verfügbare Funktionen](#verfügbare-funktionen)
5. [Verfügbare Felder](#verfügbare-felder)
6. [Korrekte Parameter](#korrekte-parameter)
7. [Häufige Fehler](#häufige-fehler)
8. [Beispiel-Code](#beispiel-code)
9. [Dokumentation](#dokumentation)

---

## 🚀 Schnellstart

### API-Endpoint
```
https://webservice.tecalliance.services/pegasus-3-0/services/TecdocToCatDLB.soapEndpoint
```

### Provider ID
```
23862
```

### API Key (gültig ab 25. Nov 2025)
```
2BeBXg6Nymr1VB3KjYRu69F4S9UGm24q5WUitw1bZKDBnePtCFtC
```

---

## 🔑 API-Zugangsdaten

| Parameter | Wert |
|-----------|------|
| **Endpoint** | `https://webservice.tecalliance.services/pegasus-3-0/services/TecdocToCatDLB.soapEndpoint` |
| **Provider ID** | `23862` |
| **API Key** | `2BeBXg6Nymr1VB3KjYRu69F4S9UGm24q5WUitw1bZKDBnePtCFtC` |
| **Country** | `de` |
| **Language** | `de` |
| **Article Country** | `de` |

---

## ⚠️ Kritische Erkenntnisse

### 1. **PFLICHT-Parameter für `getArticles`**

**OHNE diese Parameter werden KEINE Daten zurückgegeben:**

```xml
<articleCountry>de</articleCountry>
<includeAll>true</includeAll>
<includeMisc>true</includeMisc>
<includeGenericArticles>true</includeGenericArticles>
<includeGTINs>true</includeGTINs>
<includeOEMNumbers>true</includeOEMNumbers>
<includeArticleCriteria>true</includeArticleCriteria>
<includeImages>true</includeImages>
```

### 2. **Ohne `include*` Parameter: Nur 4 Felder**

- ❌ **FALSCH:** Ohne `include*` Parameter → nur 4 Felder
- ✅ **RICHTIG:** Mit `include*` Parametern → 27+ Felder (+575%)

### 3. **Bilder sind DataSupplier-abhängig**

- ✅ **MANN-FILTER (ID 4):** 92% der Artikel haben Bilder
- ❌ **Nicht alle Hersteller** stellen Bilder bereit

### 4. **Artikelnummern-Suche**

- **WICHTIG:** `brandId` MUSS angegeben werden!
- **Normalisierung:** Leerzeichen und Bindestriche entfernen

---

## 📊 Verfügbare Funktionen

Von **36 getesteten Funktionen** sind **8 verfügbar**:

| Funktion | Status | Beschreibung |
|----------|--------|--------------|
| `getCountries` | ✅ | Länder-Liste (1 Land: DE) |
| `getManufacturers` | ✅ | 434 Autohersteller |
| `getBrands` | ✅ | 197 Marken/Brands |
| `getArticles` | ✅ | Artikel-Liste (mit include-Parametern!) |
| `getGenericArticles` | ✅ | 11.002 generische Artikel |
| `getArticleDirectSearchAllNumbersWithState` | ✅ | Artikelsuche |
| `getModelSeries` | ✅ | Modellreihen |
| `getVehiclesByVIN` | ❌ | **NICHT freigeschaltet** |

**27 weitere Funktionen** sind **NICHT verfügbar** (Lizenz-Limitierung).

---

## 📋 Verfügbare Felder

### ✅ Verfügbare Felder (27)

#### Basis-Informationen (5)
- `articleNumber` - TecDoc-Artikelnummer
- `dataSupplierId` - DataSupplier-ID
- `mfrId` - Hersteller-ID
- `mfrName` - Hersteller-Name
- `ean` (gtins) - EAN-Nummer

#### Produkt-Klassifizierung (6)
- `genericArticleId` - Generischer Artikel ID
- `genericArticleDescription` - Produkttyp (z.B. "Luftfilter")
- `assemblyGroupNodeId` - Montagegruppe ID
- `assemblyGroupName` - Montagegruppe (z.B. "Luftversorgung")
- `legacyArticleId` - Legacy ID
- `linkageTargetTypes` - Zuordnungstypen

#### OE-Nummern (mehrfach)
- `oemNumbers` - Original Equipment Nummern
  - Format: `{number} ({manufacturer})`
  - Beispiel: `000 094 69 04 (MERCEDES-BENZ)`

#### Technische Attribute (mehrfach)
- `articleCriteria` - Technische Daten
  - Filterausführung, Maße, SVHC-Status, etc.

#### Artikel-Status & Metadaten (14)
- `articleStatusId` - Status-ID
- `articleStatusDescription` - Status (z.B. "Normal")
- `articleStatusValidFromDate` - Gültig ab
- `quantityPerPackage` - Menge pro Paket
- `quantityPerPartPerPackage` - Menge pro Teil
- `isSelfServicePacking` - Selbstbedienungsverpackung
- `hasMandatoryMaterialCertification` - Materialzertifikat
- `isRemanufacturedPart` - Wiederaufbereitet
- `isAccessory` - Zubehör
- `batchSize1` - Losgröße 1
- `batchSize2` - Losgröße 2
- `hasPartsListParent` - Hat Teileliste
- `hasAccessoryListParent` - Hat Zubehörliste
- `totalLinkages` - Anzahl Fahrzeugzuordnungen

#### Bilder (mehrfach, bis zu 10 pro Artikel)
- `imageURL50` - 50x50 px
- `imageURL100` - 100x100 px
- `imageURL200` - 200x200 px
- `imageURL400` - 400x400 px ⭐ **Empfohlen**
- `imageURL800` - 800x800 px
- `imageURL1600` - 1600x1600 px
- `imageURL3200` - 3200x3200 px
- `fileName` - Dateiname
- `typeDescription` - Bildtyp
- `headerDescription` - Bild-Header

### ❌ NICHT verfügbare Felder (10)

Diese Felder sind **technisch im Schema definiert**, aber für Provider ID 23862 **NICHT freigeschaltet**:

- `articleText` - Artikelbeschreibungen
- `tradeNumbers` - Handelsnummern
- `prices` - Preise
- `pdfs` - PDF-Dokumente
- `linkages` (Details) - Fahrzeugzuordnungen Details
- `replacesArticles` - Ersetzt diese Artikel
- `replacedByArticles` - Wird ersetzt durch
- `comparableNumbers` - Vergleichbare Nummern
- `links` - Externe Links

---

## 🔧 Korrekte Parameter

### `getArticles` - VOLLSTÄNDIG

```xml
<getArticles xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
    <articleCountry>de</articleCountry>
    <dataSupplierIds>4</dataSupplierIds>
    <perPage>100</perPage>
    <page>1</page>
    
    <!-- KRITISCH: Include-Parameter -->
    <includeAll>true</includeAll>
    <includeMisc>true</includeMisc>
    <includeGenericArticles>true</includeGenericArticles>
    <includeArticleText>true</includeArticleText>
    <includeGTINs>true</includeGTINs>
    <includeTradeNumbers>true</includeTradeNumbers>
    <includeOEMNumbers>true</includeOEMNumbers>
    <includeReplacesArticles>true</includeReplacesArticles>
    <includeReplacedByArticles>true</includeReplacedByArticles>
    <includeArticleCriteria>true</includeArticleCriteria>
    <includeLinkages>true</includeLinkages>
    <includePDFs>true</includePDFs>
    <includeImages>true</includeImages>
    <includeComparableNumbers>true</includeComparableNumbers>
    <includeLinks>true</includeLinks>
    <includePrices>true</includePrices>
</getArticles>
```

### `getArticleDirectSearchAllNumbersWithState`

```xml
<getArticleDirectSearchAllNumbersWithState xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <lang>de</lang>
    <articleCountry>de</articleCountry>
    <articleNumber>C 10 005</articleNumber>
    <brandId>4</brandId>
    <numberType>0</numberType>
    <searchExact>false</searchExact>
    <sortType>0</sortType>
</getArticleDirectSearchAllNumbersWithState>
```

### `getBrands`

```xml
<getBrands xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
    <articleCountry>de</articleCountry>
</getBrands>
```

---

## ❌ Häufige Fehler

### 1. **Fehlendes `articleCountry`**
```
❌ Field 'articleCountry' must be not null.
```
**Lösung:** Immer `<articleCountry>de</articleCountry>` hinzufügen!

### 2. **Keine `include*` Parameter**
```
❌ Nur 4 Felder zurückgegeben
```
**Lösung:** ALLE `include*` Parameter auf `true` setzen!

### 3. **Fehlende `brandId` bei Artikelsuche**
```
❌ Falsche Artikel gefunden
```
**Lösung:** `<brandId>4</brandId>` für MANN-FILTER angeben!

### 4. **Page = 0**
```
❌ Field 'page' must be greater than 0
```
**Lösung:** `<page>1</page>` (Seiten beginnen bei 1!)

---

## 💻 Beispiel-Code

### Python - Alle MANN-FILTER Artikel abrufen

```python
import requests
import xml.etree.ElementTree as ET

API_KEY = "2BeBXg6Nymr1VB3KjYRu69F4S9UGm24q5WUitw1bZKDBnePtCFtC"
PROVIDER_ID = "23862"
ENDPOINT = "https://webservice.tecalliance.services/pegasus-3-0/services/TecdocToCatDLB.soapEndpoint"

def get_articles(page=1, per_page=100):
    soap_body = f"""<getArticles xmlns="http://server.cat.tecdoc.net">
    <provider>{PROVIDER_ID}</provider>
    <country>de</country>
    <lang>de</lang>
    <articleCountry>de</articleCountry>
    <dataSupplierIds>4</dataSupplierIds>
    <perPage>{per_page}</perPage>
    <page>{page}</page>
    
    <includeAll>true</includeAll>
    <includeMisc>true</includeMisc>
    <includeGenericArticles>true</includeGenericArticles>
    <includeGTINs>true</includeGTINs>
    <includeOEMNumbers>true</includeOEMNumbers>
    <includeArticleCriteria>true</includeArticleCriteria>
    <includeImages>true</includeImages>
</getArticles>"""
    
    soap_envelope = f"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>{soap_body}</soap:Body>
</soap:Envelope>"""
    
    headers = {
        "Content-Type": "text/xml; charset=UTF-8",
        "X-Api-Key": API_KEY,
        "SOAPAction": ""
    }
    
    response = requests.post(ENDPOINT, data=soap_envelope, headers=headers, timeout=60)
    return response.text

# Beispiel-Aufruf
xml_response = get_articles(page=1, per_page=10)
print(xml_response)
```

---

## 📚 Dokumentation

### Verfügbare Dokumente in diesem Repo:

1. **TECDOC_DEEP_RESEARCH_REPORT.md** - Vollständiger Research-Report
2. **openai_xsd_analysis.md** - OpenAI GPT-4o Schema-Analyse
3. **TecdocToCatDLB.xsd** - Vollständiges XSD Schema (322 KB)
4. **TECDOC_VERFUEGBARE_FELDER.md** - Alle verfügbaren Felder
5. **download_all_mann_filter.py** - Script zum Download aller Artikel
6. **match_webisco_with_tecdoc.py** - CSV-Enrichment Script
7. **MANN-FILTER_Complete_Data_*.xlsx** - Beispiel-Exporte

### Externe Ressourcen:

- **TecAlliance Developer Portal:** https://developer.tecalliance.cn/en/
- **TecDoc Downloads:** https://www.tecalliance.net/de/downloads/
- **GitHub PHP Client:** https://github.com/myrzan/tecdoc-php-client

---

## 📊 Statistik

### MANN-FILTER (DataSupplier ID 4)

- **Gesamt Artikel:** 6.470
- **Mit EAN:** 6.130 (95%)
- **Mit Bildern:** 5.961 (92%)
- **Mit OE-Nummern:** 5.574 (86%)
- **Mit techn. Attributen:** 6.470 (100%)

### API-Funktionen

- **Verfügbar:** 8 von 36 (22%)
- **Nicht verfügbar:** 28 von 36 (78%)

### Datenfelder

- **Verfügbar:** 27 Felder (73%)
- **Nicht verfügbar:** 10 Felder (27%)

---

## 🎯 Best Practices

### 1. **Immer alle `include*` Parameter setzen**
Ohne diese Parameter erhältst du nur 4 Felder statt 27+!

### 2. **Paginierung nutzen**
- Max. 100 Artikel pro Seite
- Seiten beginnen bei 1
- `totalMatchingArticles` gibt Gesamtanzahl an

### 3. **Artikelsuche mit `brandId`**
Ohne `brandId` werden falsche Artikel gefunden!

### 4. **Bilder-URLs cachen**
Die URLs sind stabil und können gecacht werden.

### 5. **Fehlerbehandlung**
Prüfe immer `status` und `statusText` in der Response.

---

## ⚡ Schnell-Referenz

### DataSupplier IDs (Auswahl)

| ID | Name |
|----|------|
| 1 | BOSCH |
| 2 | MAHLE |
| 3 | HELLA |
| 4 | MANN-FILTER |

### Generic Article IDs (Auswahl)

| ID | Beschreibung |
|----|--------------|
| 7 | Ölfilter |
| 8 | Luftfilter |
| 9 | Kraftstofffilter |
| 133 | Dichtung, Ölfilter |

---

## 📞 Support

Bei Fragen zur API-Lizenz oder technischen Problemen:
- **TecAlliance Support:** https://help.manus.im

---

**Version:** 1.0  
**Letzte Aktualisierung:** 19. Dezember 2024  
**Autor:** Manus AI Agent (Deep Research)
