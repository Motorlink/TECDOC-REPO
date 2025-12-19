# TecDoc Scripts

Funktionierende Python-Scripts für die TecDoc API.

## 📋 Verfügbare Scripts

### 1. `download_all_mann_filter.py`

**Beschreibung:** Lädt ALLE MANN-FILTER Artikel von TecDoc herunter (ca. 6.470 Artikel).

**Features:**
- Automatische Paginierung
- Alle `include*` Parameter aktiviert
- JSON-Export
- Statistiken

**Verwendung:**
```bash
python3 download_all_mann_filter.py
```

**Output:**
- `mann_filter_all_articles_YYYYMMDD_HHMMSS.json`

---

### 2. `match_webisco_with_tecdoc.py`

**Beschreibung:** Matched eine CSV-Datei mit TecDoc-Daten und erstellt einen angereicherten Export.

**Features:**
- Index-basiertes Matching (schnell!)
- Mehrere Lookup-Keys (Artikelnummer, EAN, normalisiert)
- Alle verfügbaren Felder
- Bis zu 10 Bild-URLs pro Artikel

**Verwendung:**
```bash
python3 match_webisco_with_tecdoc.py
```

**Input:**
- CSV-Datei mit Artikelnummern
- JSON-Datei von `download_all_mann_filter.py`

**Output:**
- `Webisco_FINAL_Enriched_YYYYMMDD_HHMMSS.csv`

---

### 3. `create_clean_excel.py`

**Beschreibung:** Konvertiert die angereicherte CSV in eine formatierte Excel-Datei.

**Features:**
- Farbcodierte Header (Blau/Grün)
- Eingefrorene Header-Zeile
- Angepasste Spaltenbreiten
- Rahmen um alle Zellen

**Verwendung:**
```bash
python3 create_clean_excel.py
```

**Output:**
- `Webisco_FINAL_Export_YYYYMMDD_HHMMSS.xlsx`

---

## 🔧 Anpassungen

### DataSupplier ändern

In `download_all_mann_filter.py`:
```python
<dataSupplierIds>4</dataSupplierIds>  # 4 = MANN-FILTER
```

Andere IDs:
- 1 = BOSCH
- 2 = MAHLE
- 3 = HELLA

### Artikel pro Seite

```python
<perPage>100</perPage>  # Max. 100
```

### Include-Parameter

Alle Parameter in `download_all_mann_filter.py` sind bereits auf `true` gesetzt.

---

## ⚠️ Wichtige Hinweise

1. **API-Key:** Muss in den Scripts aktualisiert werden
2. **Timeout:** Bei vielen Artikeln kann der Download lange dauern
3. **Speicher:** 6.470 Artikel = ca. 50 MB JSON
4. **Rate Limiting:** 0.2s Pause zwischen Requests

---

## 📊 Performance

| Script | Dauer | Output-Größe |
|--------|-------|--------------|
| `download_all_mann_filter.py` | ~10-15 Min | 50 MB |
| `match_webisco_with_tecdoc.py` | ~30 Sek | 5 MB |
| `create_clean_excel.py` | ~10 Sek | 3 MB |
