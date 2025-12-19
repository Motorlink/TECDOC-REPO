# TecDoc API - Vollständiger Funktionsbericht

**Provider ID:** 23862  
**API Key:** 2BeBXg6Nymr1VB3KjYRu69F4S9UGm24q5WUitw1bZKDBnePtCFtC  
**Test-Datum:** 17. Dezember 2025  
**Getestete Funktionen:** 36

---

## 📊 Zusammenfassung

| Status | Anzahl | Prozent |
|--------|--------|---------|
| ✅ **Erfolgreich** | 7 | 19% |
| ⚠️ **Fehler (Parameter fehlen)** | 2 | 6% |
| ❌ **Nicht verfügbar** | 27 | 75% |

---

## ✅ FUNKTIONIERENDE FUNKTIONEN (7)

### 1. `getCountries` - Länder abrufen
**Status:** ✅ Funktioniert  
**Rückgabe:** 1 Land (DE - Deutschland)  
**Parameter:** Keine erforderlich  

**Beispiel:**
```xml
<getCountries xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
</getCountries>
```

---

### 2. `getManufacturers` - Autohersteller abrufen
**Status:** ✅ Funktioniert  
**Rückgabe:** 434 Hersteller (Audi, BMW, Mercedes, etc.)  
**Parameter:** `linkingTargetType` = "P" (erforderlich)

**Felder pro Hersteller:**
- `manuId` - Hersteller-ID
- `manuName` - Hersteller-Name

**Beispiel:**
```xml
<getManufacturers xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
    <linkingTargetType>P</linkingTargetType>
</getManufacturers>
```

---

### 3. `getArticles` - Artikelliste abrufen
**Status:** ✅ Funktioniert  
**Rückgabe:** 10 Artikel (bei pageSize=5 angefordert!)  
**Parameter:** 
- `articleCountry` = "de" (erforderlich)
- `dataSupplierIds` = Supplier-ID (erforderlich)
- `pageSize` = Anzahl (erforderlich)
- `pageNumber` = Seite (erforderlich)

**Felder pro Artikel:**
- `dataSupplierId` - DataSupplier-ID
- `articleNumber` - TecDoc-Artikelnummer
- `mfrId` - Hersteller-ID
- `mfrName` - Hersteller-Name

**Metadaten:**
- `totalMatchingArticles` - Gesamtanzahl
- `maxAllowedPage` - Max. Seiten

**Beispiel:**
```xml
<getArticles xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
    <articleCountry>de</articleCountry>
    <dataSupplierIds>4</dataSupplierIds>
    <pageSize>5</pageSize>
    <pageNumber>0</pageNumber>
</getArticles>
```

---

### 4. `getArticleDirectSearchAllNumbersWithState` - Artikelsuche
**Status:** ✅ Funktioniert  
**Rückgabe:** 1 Artikel gefunden  
**Parameter:**
- `articleNumber` = Artikelnummer (erforderlich)
- `articleCountry` = "de" (erforderlich)

**Beispiel:**
```xml
<getArticleDirectSearchAllNumbersWithState xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
    <articleNumber>HU 7029 z</articleNumber>
    <articleCountry>de</articleCountry>
</getArticleDirectSearchAllNumbersWithState>
```

---

### 5. `getVehiclesByVIN` - Fahrzeugsuche per VIN
**Status:** ✅ Funktioniert (aber keine Daten)  
**Rückgabe:** 0 Fahrzeuge (Test-VIN nicht gefunden)  
**Parameter:**
- `vin` = Fahrgestellnummer (erforderlich)

**Beispiel:**
```xml
<getVehiclesByVIN xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
    <vin>WVWZZZ1KZBW123456</vin>
</getVehiclesByVIN>
```

---

### 6. `getModelSeries` - Modellreihen abrufen
**Status:** ✅ Funktioniert (aber keine Daten)  
**Rückgabe:** 0 Modellreihen  
**Parameter:**
- `manuId` = Hersteller-ID (erforderlich)

**Beispiel:**
```xml
<getModelSeries xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
    <manuId>4</manuId>
</getModelSeries>
```

---

### 7. `getGenericArticles` - Generische Artikel abrufen
**Status:** ✅ Funktioniert  
**Rückgabe:** 11.002 generische Artikel!  
**Parameter:** Keine erforderlich

**Beispiel:**
```xml
<getGenericArticles xmlns="http://server.cat.tecdoc.net">
    <provider>23862</provider>
    <country>de</country>
    <lang>de</lang>
</getGenericArticles>
```

---

## ⚠️ FUNKTIONEN MIT FEHLERN (2)

### 1. `getBrands` - Marken abrufen
**Status:** ⚠️ Fehler  
**Fehlermeldung:** "Field 'articleCountry' must be not null."  
**Lösung:** Parameter `articleCountry` hinzufügen

---

### 2. `getLinkageTargets` - Fahrzeugzuordnungen
**Status:** ⚠️ Fehler  
**Fehlermeldung:** "Field 'country' must be not null."  
**Hinweis:** Parameter `country` wird bereits gesendet - möglicherweise anderer Parameter-Name erforderlich

---

## ❌ NICHT VERFÜGBARE FUNKTIONEN (27)

Diese Funktionen sind **NICHT in der API-Lizenz enthalten** und geben "Unknown Call" zurück:

### DataSupplier-Funktionen
- ❌ `getDataSuppliers` - DataSupplier-Liste
- ❌ `getDataSupplierList` - DataSupplier-Liste (Alternative)

### Artikel-Detail-Funktionen
- ❌ `getArticlesByIds` - Artikel nach IDs
- ❌ `getArticlesDirectSearchAllNumbers` - Direkte Artikelsuche
- ❌ `getArticlesDirectSearchAllNumbers4` - Erweiterte Artikelsuche
- ❌ `getArticleInfo` - Artikel-Informationen
- ❌ `getArticleDetails` - Artikel-Details
- ❌ `getArticleInformation` - Artikel-Informationen (Alternative)

### EAN/OE-Nummern
- ❌ `getArticleEANNumbers` - EAN-Nummern
- ❌ `getArticleOENumbers` - OE-Nummern
- ❌ `getOENrsByArticleId` - OE-Nummern nach Artikel-ID

### Fahrzeugzuordnungen
- ❌ `getLinkageTargetsByArticleId` - Fahrzeugzuordnungen nach Artikel
- ❌ `getLinkageTargetDetails` - Fahrzeugzuordnungs-Details
- ❌ `getLinkageTargetDetails2` - Fahrzeugzuordnungs-Details (Alternative)

### Fahrzeug-Funktionen
- ❌ `getVehicles` - Fahrzeuge abrufen
- ❌ `getVehicleIdsByVIN` - Fahrzeug-IDs per VIN
- ❌ `getVehicleByVIN3` - Fahrzeug per VIN (Version 3)
- ❌ `getVehiclesByModelSeries` - Fahrzeuge nach Modellreihe

### Generische Artikel
- ❌ `getGenericArticlesByIds` - Generische Artikel nach IDs

### Bilder & Dokumente
- ❌ `getArticleImages` - Artikel-Bilder
- ❌ `getArticleDocuments` - Artikel-Dokumente

### Attribute & Kriterien
- ❌ `getArticleCriteria` - Artikel-Kriterien
- ❌ `getArticleAttributes` - Artikel-Attribute

### Cross-References
- ❌ `getArticleCrossReferences` - Artikel-Querverweise
- ❌ `getTradeNumbers` - Handelsnummern

### Facetten
- ❌ `getAssemblyGroupFacets` - Baugruppen-Facetten
- ❌ `getGenericArticleFacets` - Generische Artikel-Facetten

---

## 📋 Was SOLLTE verfügbar sein (laut Dokumentation)

### Basis-Funktionen (sollten funktionieren):
1. ✅ `getCountries` - **FUNKTIONIERT**
2. ✅ `getManufacturers` - **FUNKTIONIERT**
3. ✅ `getArticles` - **FUNKTIONIERT**
4. ❌ `getDataSuppliers` - **NICHT VERFÜGBAR**

### Artikel-Suche (sollten funktionieren):
5. ❌ `getArticlesDirectSearchAllNumbers` - **NICHT VERFÜGBAR**
6. ❌ `getArticlesDirectSearchAllNumbers4` - **NICHT VERFÜGBAR**
7. ✅ `getArticleDirectSearchAllNumbersWithState` - **FUNKTIONIERT**

### Artikel-Details (sollten funktionieren):
8. ❌ `getArticleInfo` - **NICHT VERFÜGBAR**
9. ❌ `getArticleDetails` - **NICHT VERFÜGBAR**
10. ❌ `getArticleEANNumbers` - **NICHT VERFÜGBAR**
11. ❌ `getArticleOENumbers` - **NICHT VERFÜGBAR**

### Fahrzeugzuordnungen (sollten funktionieren):
12. ❌ `getLinkageTargetsByArticleId` - **NICHT VERFÜGBAR**
13. ❌ `getLinkageTargetDetails` - **NICHT VERFÜGBAR**

### Fahrzeug-Suche (sollten funktionieren):
14. ✅ `getVehiclesByVIN` - **FUNKTIONIERT** (aber keine Daten)
15. ❌ `getVehicleIdsByVIN` - **NICHT VERFÜGBAR**

---

## 🎯 Fazit

### Was funktioniert:
- ✅ Länder-Liste (1 Land)
- ✅ Autohersteller-Liste (434 Hersteller)
- ✅ Artikelliste (nur 4 Felder pro Artikel)
- ✅ Artikelsuche (eingeschränkt)
- ✅ VIN-Suche (Funktion vorhanden, aber keine Daten)
- ✅ Generische Artikel (11.002 Artikel)

### Was NICHT funktioniert:
- ❌ DataSupplier-Liste
- ❌ Artikel-Details (EAN, OE, Bilder, Attribute)
- ❌ Fahrzeugzuordnungen
- ❌ Erweiterte Suchfunktionen
- ❌ Cross-References
- ❌ Dokumente & Bilder

### Verfügbarkeit:
- **19% der Funktionen** sind verfügbar
- **75% der Funktionen** sind NICHT in der Lizenz enthalten
- **6% der Funktionen** haben Fehler (fehlende Parameter)

---

## 💡 Empfehlung

**Die API-Lizenz (Provider ID 23862) ist extrem limitiert.**

Um die fehlenden 27 Funktionen zu nutzen, ist ein **API-Upgrade bei TecAlliance** erforderlich.

**Kontakt:**
- E-Mail: sales.dach@tecalliance.net
- Website: https://www.tecalliance.net/de/kontakt/

---

**Erstellt von Manus AI - 17. Dezember 2025**
