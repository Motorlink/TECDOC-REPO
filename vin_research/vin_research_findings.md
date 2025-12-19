# VIN-zu-Artikel Deep Research - Findings

## 🔍 XSD Schema Analyse - Gefundene Funktionen

### VIN-bezogene Funktionen:

1. **`getVehiclesByVIN`** - VIN → Fahrzeuge
2. **`getOEArticlesByVIN`** - VIN → OE-Artikel! ⭐

### Fahrzeug-ID Funktionen:

3. **`getVehicleIdsByMark`** - Nach Marke
4. **`getVehicleIdsByVendorId2`** - Nach Vendor ID
5. **`getVehicleIdsByKeyNumberPlates3`** - Nach Kennzeichen (HSN/TSN)
6. **`getVehicleByIds3`** - Fahrzeug-Details nach ID
7. **`getVehicleByIds4`** - Fahrzeug-Details nach ID (v4)
8. **`getVehiclesByKeyNumberPlates`** - Fahrzeuge nach Kennzeichen
9. **`getVehicleIdsByCriteria`** - Fahrzeuge nach Kriterien

---

## ⭐ WICHTIGE ENTDECKUNG: `getOEArticlesByVIN`

```xml
<xs:complexType name="oEArticlesByVINRequest">
    <xs:element name="vin" type="xs:string"/>
    ...
</xs:complexType>
```

**Dokumentation:**
- Valid Values for `getOEArticlesByVIN`: mfrName, articleNumber, genericArticleName
- Sortierung: mfrName, articleNumber, genericArticleName

**Das bedeutet:**
- ✅ Direkte VIN → Artikel Zuordnung möglich!
- ✅ Liefert OE-Artikel basierend auf VIN

---

## 📋 Linkage-System

### linkageTargetType Werte:

- **'P'**: Passenger Car/LCV (ohne Motorrad)
- **'V'**: Passenger Car
- **'L'**: LCV (Light Commercial Vehicle)
- **'B'**: Motorcycle
- **'O'**: Commercial Vehicle
- **'C'**: Commercial Vehicle
- **'T'**: Tractor
- **'M'**: Engine
- **'A'**: Axle
- **'K'**: CV Body Type
- **'U'**: Universal

### Linkage-Parameter:

- `linkageTargetId` - ID des Linkage-Ziels
- `linkageTargetType` - Typ des Linkage-Ziels
- `linkageTargetCountry` - Land-spezifische Linkages
- `includeLinkages` - Linkage-Details einschließen

---

## 🎯 Nächste Schritte:

1. Test `getOEArticlesByVIN` - Funktioniert diese Funktion?
2. Test `getVehicleIdsByKeyNumberPlates3` - HSN/TSN → Fahrzeug
3. Analyse der Response-Struktur
4. Mapping OE-Artikel → MANN-FILTER Artikel

---

**Status:** In Progress  
**Datum:** 19. Dezember 2024


---

## 🧪 Test-Ergebnisse (19. Dezember 2024)

### Test 1: `getOEArticlesByVIN`
- **Status:** ❌ **NICHT freigeschaltet**
- **Fehler:** `Access not allowed` (Status 401)
- **Bedeutung:** Funktion existiert, aber Lizenz erlaubt keinen Zugriff

### Test 2: `getVehiclesByVIN`
- **Status:** ❌ **NICHT freigeschaltet**
- **Fehler:** `Access not allowed` (Status 401)
- **Bedeutung:** Funktion existiert, aber Lizenz erlaubt keinen Zugriff

### Test 3: `getLinkedArticles`
- **Status:** ❌ **NICHT freigeschaltet**
- **Fehler:** `Access not allowed` (Status 401)
- **Bedeutung:** Funktion existiert, aber Lizenz erlaubt keinen Zugriff

---

## 📊 Zusammenfassung

### ❌ Alle VIN-bezogenen Funktionen sind NICHT freigeschaltet:

| Funktion | XSD | API-Test | Lizenz |
|----------|-----|----------|--------|
| `getOEArticlesByVIN` | ✅ Vorhanden | ❌ 401 | ❌ Nicht freigeschaltet |
| `getVehiclesByVIN` | ✅ Vorhanden | ❌ 401 | ❌ Nicht freigeschaltet |
| `getLinkedArticles` | ✅ Vorhanden | ❌ 401 | ❌ Nicht freigeschaltet |

**Fazit:**
- Die Funktionen sind **technisch verfügbar** (im XSD Schema definiert)
- Die Funktionen sind **NICHT in der Lizenz** (Provider ID 23862) enthalten
- **Direkter VIN → Artikel Workflow ist NICHT möglich** mit aktueller Lizenz

---

## 💡 OpenAI Analyse-Ergebnis

**Workflow (theoretisch):**
1. `getVehiclesByVIN` → Fahrzeugdaten
2. `getOEArticlesByVIN` → OE-Artikel + Aftermarket-Filter
3. `aftermarketDataSupplierIds=4` → Nur MANN-FILTER

**Aber:** Alle 3 Funktionen sind nicht freigeschaltet!

---

## 🎯 Alternative Lösungen

Da die direkte VIN-Zuordnung nicht verfügbar ist, bleiben nur **Workarounds**:

### Option A: Externe VIN-Decoder + OE-Index
1. Externe VIN-Decoder API → Fahrzeugdaten
2. OE-Nummern-Datenbank → OE-Nummern für Fahrzeug
3. TecDoc OE-Index → MANN-FILTER Artikel

### Option B: HSN/TSN (Kennzeichen-Nummern)
- `getVehicleIdsByKeyNumberPlates3` - Eventuell verfügbar?
- Test erforderlich

### Option C: TecDoc Reference Data
- Vollständige Katalog-Datenbank
- Separate Lizenz erforderlich
- Kosten: ~€5.000-€20.000/Jahr

---

**Status:** VIN-Funktionen nicht verfügbar  
**Empfehlung:** Hybrid-Lösung (externe VIN-API + TecDoc OE-Index)
