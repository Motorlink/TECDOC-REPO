# VIN zu MANN-FILTER Artikel - Komplette Lösung

**Deep Research Ergebnis**  
**Datum:** 19. Dezember 2024  
**Provider ID:** 23862

---

## 🎯 Ziel

**Workflow:** Fahrgestellnummer (VIN) → Fahrzeug → OE-Nummern → MANN-FILTER Artikel

---

## ❌ Ergebnis: NICHT direkt möglich mit aktueller Lizenz

### Getestete Funktionen (alle Status 401 - Access not allowed):

| Funktion | Zweck | Status |
|----------|-------|--------|
| `getVehiclesByVIN` | VIN → Fahrzeug | ❌ Nicht freigeschaltet |
| `getOEArticlesByVIN` | VIN → OE-Artikel | ❌ Nicht freigeschaltet |
| `getLinkedArticles` | Fahrzeug → Artikel | ❌ Nicht freigeschaltet |
| `getVehicleIdsByKeyNumberPlates3` | HSN/TSN → kTyp | ❌ Nicht freigeschaltet |
| `getVehicleIdsByMotor2` | Motorcode → kTyp | ❌ Nicht freigeschaltet |
| `getVehicleIdsByKTypeNumber` | kTyp → Fahrzeug | ❌ Nicht freigeschaltet |

**Fazit:** Alle Fahrzeug-bezogenen Funktionen sind in der aktuellen Lizenz **NICHT enthalten**.

---

## ✅ Verfügbare Alternative: Hybrid-Lösung

Da die TecDoc API keine Fahrzeugzuordnungen unterstützt, ist eine **Hybrid-Lösung** erforderlich:

### Architektur:

```
┌─────────────┐
│     VIN     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────┐
│  Externe VIN-Decoder API    │
│  (NHTSA, CarMD, RapidAPI)   │
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│    Fahrzeugdaten            │
│  - Hersteller               │
│  - Modell                   │
│  - Baujahr                  │
│  - Motor                    │
│  - kTyp (optional)          │
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│  OE-Nummern Datenbank       │
│  (Fahrzeug → OE-Nummern)    │
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│  TecDoc OE-Nummern Index    │
│  (6.470 MANN-FILTER Artikel)│
└──────┬──────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│  MANN-FILTER Artikel        │
│  mit allen TecDoc-Daten     │
└─────────────────────────────┘
```

---

## 🔧 Implementierung

### Phase 1: OE-Nummern Index erstellen

**Bereits vorhanden!** Wir haben alle 6.470 MANN-FILTER Artikel mit OE-Nummern.

```python
# Datei: mann_filter_all_articles.json
{
    "articles": [
        {
            "articleNumber": "HU 7029 z",
            "ean": "4011558291402",
            "oemNumbers": [
                {"number": "000 094 69 04", "mfrName": "MERCEDES-BENZ"},
                {"number": "A 000 094 69 04", "mfrName": "MERCEDES-BENZ"}
            ],
            ...
        }
    ]
}

# Index erstellen:
oe_index = {}
for article in articles:
    for oe in article["oemNumbers"]:
        oe_number = oe["number"].replace(" ", "").replace("-", "")
        if oe_number not in oe_index:
            oe_index[oe_number] = []
        oe_index[oe_number].append(article)
```

---

### Phase 2: Externe VIN-Decoder API

#### Option A: NHTSA API (USA, kostenlos)

```python
import requests

def decode_vin_nhtsa(vin):
    """Decode VIN using NHTSA API (USA only)"""
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json"
    response = requests.get(url)
    data = response.json()
    
    vehicle = {}
    for item in data["Results"]:
        if item["Value"]:
            vehicle[item["Variable"]] = item["Value"]
    
    return vehicle

# Beispiel:
vin = "1HGBH41JXMN109186"
vehicle = decode_vin_nhtsa(vin)
print(vehicle["Make"])  # Honda
print(vehicle["Model"])  # Accord
print(vehicle["ModelYear"])  # 1991
```

**Vorteil:** Kostenlos  
**Nachteil:** Nur USA-Fahrzeuge, keine OE-Nummern

---

#### Option B: RapidAPI - VIN Decoder mit TecDoc

```python
import requests

def decode_vin_rapidapi(vin):
    """Decode VIN using RapidAPI TecDoc Decoder"""
    url = "https://vin-decoder-support-tecdoc-catalog.p.rapidapi.com/decode"
    
    headers = {
        "X-RapidAPI-Key": "YOUR_API_KEY",
        "X-RapidAPI-Host": "vin-decoder-support-tecdoc-catalog.p.rapidapi.com"
    }
    
    params = {"vin": vin}
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    return {
        "ktype": data.get("ktype"),
        "make": data.get("make"),
        "model": data.get("model"),
        "year": data.get("year")
    }

# Beispiel:
vin = "WVWZZZ1JZYW123456"
vehicle = decode_vin_rapidapi(vin)
print(vehicle["ktype"])  # 27563
```

**Vorteil:** Liefert kTyp direkt!  
**Nachteil:** Kostenpflichtig (~$0.01 pro Request)

**API:** https://rapidapi.com/autowaysnet/api/vin-decoder-support-tecdoc-catalog

---

#### Option C: CarMD API (kommerziell)

```python
import requests

def decode_vin_carmd(vin):
    """Decode VIN using CarMD API"""
    url = f"https://api.carmd.com/v3.0/decode?vin={vin}"
    
    headers = {
        "content-type": "application/json",
        "authorization": "Basic YOUR_AUTH_TOKEN",
        "partner-token": "YOUR_PARTNER_TOKEN"
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    return {
        "year": data["data"]["year"],
        "make": data["data"]["make"],
        "model": data["data"]["model"],
        "engine": data["data"]["engine"]
    }
```

**Vorteil:** Sehr detailliert, weltweite Abdeckung  
**Nachteil:** Teuer (~$0.10 pro Request)

**API:** https://www.carmd.com/

---

### Phase 3: OE-Nummern Mapping

#### Option A: Eigene Datenbank aufbauen

```sql
CREATE TABLE vehicle_oe_numbers (
    id SERIAL PRIMARY KEY,
    make VARCHAR(100),
    model VARCHAR(100),
    year_from INTEGER,
    year_to INTEGER,
    engine_code VARCHAR(50),
    part_type VARCHAR(50),  -- z.B. 'Luftfilter', 'Ölfilter'
    oe_number VARCHAR(50),
    manufacturer VARCHAR(100)
);

-- Beispiel-Daten:
INSERT INTO vehicle_oe_numbers VALUES
(1, 'Mercedes-Benz', 'C-Klasse', 2007, 2014, 'OM651', 'Luftfilter', '000 094 69 04', 'MERCEDES-BENZ'),
(2, 'Mercedes-Benz', 'E-Klasse', 2009, 2016, 'OM651', 'Luftfilter', '000 094 69 04', 'MERCEDES-BENZ');
```

**Datenquellen:**
- TecDoc Reference Data (kostenpflichtig)
- Hersteller-Kataloge
- Manuelles Mapping

---

#### Option B: Externe OE-Nummern API

**Keine kostenlose API gefunden.**

Alternativen:
- Web-Scraping von Teilekatalogen
- Partnerschaften mit Teilehändlern
- TecDoc Reference Data Lizenz

---

### Phase 4: Kompletter Workflow

```python
def vin_to_mann_filter(vin: str, part_type: str = None):
    """
    Kompletter Workflow: VIN → MANN-FILTER Artikel
    
    Args:
        vin: Fahrgestellnummer
        part_type: Optional, z.B. 'Luftfilter', 'Ölfilter'
    
    Returns:
        List of MANN-FILTER articles
    """
    
    # 1. VIN dekodieren
    vehicle = decode_vin_rapidapi(vin)  # oder andere API
    
    # 2. OE-Nummern für Fahrzeug holen
    oe_numbers = get_oe_numbers_for_vehicle(
        make=vehicle["make"],
        model=vehicle["model"],
        year=vehicle["year"],
        part_type=part_type
    )
    
    # 3. MANN-FILTER Artikel über OE-Index finden
    articles = []
    for oe_number in oe_numbers:
        normalized = oe_number.replace(" ", "").replace("-", "")
        if normalized in oe_index:
            articles.extend(oe_index[normalized])
    
    # 4. Duplikate entfernen
    unique_articles = {a["articleNumber"]: a for a in articles}.values()
    
    return list(unique_articles)


# Beispiel-Nutzung:
vin = "WVWZZZ1JZYW123456"
articles = vin_to_mann_filter(vin, part_type="Luftfilter")

for article in articles:
    print(f"{article['articleNumber']} - {article['genericArticleDescription']}")
    print(f"  EAN: {article['ean']}")
    print(f"  OE-Nummern: {', '.join([oe['number'] for oe in article['oemNumbers']])}")
```

---

## 💰 Kosten-Schätzung

### Variante A: NHTSA + Eigene OE-Datenbank

| Komponente | Kosten |
|------------|--------|
| NHTSA API | Kostenlos |
| OE-Datenbank Aufbau | ~€5.000 (einmalig) |
| Wartung | ~€500/Monat |
| **Gesamt (Jahr 1)** | **~€11.000** |

**Vorteil:** Niedrige laufende Kosten  
**Nachteil:** Nur USA-Fahrzeuge, hoher initialer Aufwand

---

### Variante B: RapidAPI + Eigene OE-Datenbank

| Komponente | Kosten |
|------------|--------|
| RapidAPI VIN Decoder | ~€0.01 pro Request |
| Bei 1.000 Requests/Monat | ~€10/Monat |
| OE-Datenbank Aufbau | ~€5.000 (einmalig) |
| Wartung | ~€500/Monat |
| **Gesamt (Jahr 1)** | **~€11.120** |

**Vorteil:** Weltweite Abdeckung, liefert kTyp  
**Nachteil:** Abhängigkeit von externer API

---

### Variante C: TecDoc Reference Data (Professionell)

| Komponente | Kosten |
|------------|--------|
| TecDoc Reference Data Lizenz | ~€10.000-€20.000/Jahr |
| Infrastruktur (Server, DB) | ~€200/Monat |
| Entwicklung | ~€10.000 (einmalig) |
| **Gesamt (Jahr 1)** | **~€22.400-€32.400** |

**Vorteil:** Vollständige Daten, keine externen APIs  
**Nachteil:** Hohe Kosten

---

## 🎯 Empfehlung

### Für MVP / Proof of Concept:

**Variante B: RapidAPI + Eigene OE-Datenbank**

**Vorteile:**
- ✅ Schnelle Implementierung
- ✅ Weltweite VIN-Abdeckung
- ✅ Liefert kTyp direkt
- ✅ Niedrige initiale Kosten

**Schritte:**
1. RapidAPI Account erstellen
2. OE-Nummern Index aus TecDoc erstellen (bereits vorhanden!)
3. Kleine OE-Datenbank mit häufigsten Fahrzeugen aufbauen
4. Workflow implementieren und testen

**Zeitaufwand:** 2-3 Wochen

---

### Für Produktiv-Betrieb:

**Variante C: TecDoc Reference Data**

**Vorteile:**
- ✅ Vollständige Fahrzeugdaten
- ✅ Vollständige OE-Nummern
- ✅ Keine Abhängigkeit von externen APIs
- ✅ Professionelle Lösung

**Schritte:**
1. TecDoc Reference Data Lizenz erwerben
2. Lokale Datenbank aufsetzen (PostgreSQL)
3. Import-Scripts entwickeln
4. Regelmäßige Updates einrichten

**Zeitaufwand:** 2-3 Monate

---

## 📝 Nächste Schritte

### Sofort umsetzbar:

1. **OE-Nummern Index erstellen** (bereits vorhanden!)
2. **RapidAPI Account** erstellen und testen
3. **Proof of Concept** implementieren mit 10 Test-VINs
4. **OE-Datenbank** mit 100 häufigsten Fahrzeugen aufbauen

### Mittelfristig:

1. **OE-Datenbank** erweitern (1.000+ Fahrzeuge)
2. **Caching** implementieren für häufige Anfragen
3. **Fehlerbehandlung** verbessern
4. **Monitoring** einrichten

### Langfristig:

1. **TecDoc Reference Data** Lizenz evaluieren
2. **Migration** auf vollständige Lösung planen
3. **Skalierung** für hohe Request-Zahlen

---

## 📊 Zusammenfassung

| Aspekt | Status |
|--------|--------|
| **VIN → Fahrzeug (TecDoc)** | ❌ Nicht verfügbar |
| **VIN → Fahrzeug (extern)** | ✅ Möglich (RapidAPI) |
| **Fahrzeug → OE-Nummern** | ⚠️ Eigene Datenbank erforderlich |
| **OE-Nummern → MANN-FILTER** | ✅ Verfügbar (TecDoc Index) |
| **Kompletter Workflow** | ✅ Mit Hybrid-Lösung möglich |

---

**Erstellt:** 19. Dezember 2024  
**Autor:** Manus AI  
**Version:** 1.0
