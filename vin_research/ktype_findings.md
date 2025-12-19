# kTyp und Vehicle Search - Findings

## 🔑 Wichtigste Erkenntnisse

### kTyp (carId) ist der Schlüssel!

**kTyp = TecDoc Vehicle Type ID**

- Eindeutige Fahrzeug-Identifikation in TecDoc
- Format: Integer (z.B. 27563)
- Wird verwendet für: Fahrzeugsuche, Artikel-Zuordnung

---

## 📊 TecAlliance API Dokumentation

### Vehicle Search Endpoint (China API)

**URL:** `https://onedb.tecalliance.cn/api/vehicles`

**Parameter:**
- `country` - Land (z.B. "CN", "DE")
- `lang` - Sprache (z.B. "EN", "DE")
- `carId` - **kTyp Nummer** (z.B. 27563)

**Response enthält:**
- carId (kTyp)
- manuId, manuName (Hersteller)
- modId, modelName (Modell)
- engineCode (Motorcode!)
- yearOfConstrFrom/To (Baujahr)
- powerKwTo, powerHpTo (Leistung)
- cylinderCapacityCcm (Hubraum)
- fuelType (Kraftstoff)
- impulsionType (Antrieb)

---

## 🎯 Workflow-Möglichkeiten

### Option 1: VIN → kTyp (extern) → TecDoc

```
1. VIN → Externe VIN-Decoder API → Fahrzeugdaten
2. Fahrzeugdaten → kTyp ermitteln (extern)
3. kTyp → TecDoc API → Artikel
```

### Option 2: HSN/TSN → kTyp → TecDoc

```
1. HSN/TSN (Kennzeichen) → TecDoc API
2. TecDoc API → kTyp
3. kTyp → Artikel-Zuordnung
```

**Funktion:** `getVehicleIdsByKeyNumberPlates3`
- HSN = Hersteller-Schlüsselnummer
- TSN = Typ-Schlüsselnummer
- Aus deutschem Fahrzeugschein (Feld 2.1 und 2.2)

### Option 3: Motorcode → kTyp → TecDoc

```
1. Motorcode (z.B. "CDNC") → TecDoc API
2. TecDoc API → kTyp
3. kTyp → Artikel-Zuordnung
```

**Funktion:** `getVehicleIdsByMotor2`

---

## 🔍 Recherche-Ergebnisse

### TecDoc VIN Decoder (kommerziell)

**Quelle:** https://www.autobiz.ie/home/unlock-parts-information-with-the-tecdoc-vin-decoder

- TecDoc bietet eigenen VIN Decoder
- Liefert: kTyp + Fahrzeugdaten
- Wahrscheinlich kostenpflichtig

### TecDoc Catalogue Vehicle Identification

**Quelle:** https://shop.tecalliance.net/

- Add-On für TecDoc Catalogue
- Kennzeichen → Fahrzeug-Identifikation
- "One-Click" Fahrzeugsuche

### Externe APIs

**RapidAPI - VIN Decoder mit TecDoc:**
- https://rapidapi.com/autowaysnet/api/vin-decoder-support-tecdoc-catalog
- VIN → kTyp
- Kommerziell

**Global Vehicle List API:**
- https://rapidapi.com/fhdenniswittmann/api/global-vehicle-list-k-type-hsn-tsn-data-api-for-car-pats
- HSN/TSN → kTyp
- 250.000+ Fahrzeuge

---

## 🧪 Nächste Tests

### Test 1: HSN/TSN → kTyp

**Funktion:** `getVehicleIdsByKeyNumberPlates3`

**Parameter:**
```xml
<keyNumberPlate>
    <hsn>0588</hsn>
    <tsn>AHC</tsn>
</keyNumberPlate>
```

**Erwartung:** kTyp für deutsches Fahrzeug

### Test 2: Motorcode → kTyp

**Funktion:** `getVehicleIdsByMotor2`

**Parameter:**
```xml
<engineCode>CDNC</engineCode>
```

**Erwartung:** Liste von kTyps mit diesem Motor

### Test 3: kTyp → Artikel

**Funktion:** `getLinkedArticles` oder `getArticles`

**Parameter:**
```xml
<linkageTargetId>{kTyp}</linkageTargetId>
<linkageTargetType>P</linkageTargetType>
```

**Erwartung:** Artikel für dieses Fahrzeug

---

## 💡 Erkenntnisse

1. **kTyp ist zentral** - Alle Fahrzeug-Artikel-Zuordnungen basieren auf kTyp
2. **VIN → kTyp fehlt** - Direkte VIN-Dekodierung nicht in Lizenz
3. **HSN/TSN könnte funktionieren** - Deutsche Kennzeichen-Nummern
4. **Motorcode könnte funktionieren** - Alternative Identifikation
5. **Externe APIs verfügbar** - VIN → kTyp über RapidAPI

---

**Status:** Research in Progress  
**Nächster Schritt:** Test HSN/TSN und Motorcode Funktionen
