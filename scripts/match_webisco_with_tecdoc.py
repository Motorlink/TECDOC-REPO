#!/usr/bin/env python3
"""
Match Webisco CSV with TecDoc Data
Create enriched export with all available fields
"""

import csv
import json
from datetime import datetime

def normalize_article_number(number):
    """Normalize article number for matching"""
    if not number:
        return ''
    # Remove spaces, convert to uppercase
    return number.replace(' ', '').replace('-', '').upper()

def create_index(tecdoc_articles):
    """Create lookup index for TecDoc articles"""
    
    print("Creating article index...")
    
    index = {
        'by_article_number': {},
        'by_ean': {},
        'by_normalized_number': {}
    }
    
    for article in tecdoc_articles:
        # Index by article number
        article_num = article.get('articleNumber', '')
        if article_num:
            index['by_article_number'][article_num] = article
            # Also by normalized
            normalized = normalize_article_number(article_num)
            if normalized:
                index['by_normalized_number'][normalized] = article
        
        # Index by EAN
        ean = article.get('ean', '')
        if ean:
            index['by_ean'][ean] = article
    
    print(f"  Indexed by article number: {len(index['by_article_number'])}")
    print(f"  Indexed by EAN: {len(index['by_ean'])}")
    print(f"  Indexed by normalized number: {len(index['by_normalized_number'])}")
    
    return index

def find_article(csv_article_number, csv_ean, index):
    """Find matching TecDoc article"""
    
    # Try exact match by article number
    if csv_article_number and csv_article_number in index['by_article_number']:
        return index['by_article_number'][csv_article_number]
    
    # Try normalized match
    normalized = normalize_article_number(csv_article_number)
    if normalized and normalized in index['by_normalized_number']:
        return index['by_normalized_number'][normalized]
    
    # Try EAN match
    if csv_ean and csv_ean in index['by_ean']:
        return index['by_ean'][csv_ean]
    
    return None

def format_oe_numbers(oe_list):
    """Format OE numbers for CSV"""
    if not oe_list:
        return ''
    return ' | '.join([f"{oe['number']} ({oe['manufacturer']})" for oe in oe_list])

def format_criteria(criteria_list):
    """Format article criteria for CSV"""
    if not criteria_list:
        return ''
    result = []
    for crit in criteria_list:
        if crit.get('unit'):
            result.append(f"{crit['description']}: {crit['value']} {crit['unit']}")
        else:
            result.append(f"{crit['description']}: {crit['value']}")
    return ' | '.join(result)

def enrich_csv(csv_file, tecdoc_json, output_file):
    """Enrich Webisco CSV with TecDoc data"""
    
    print("\n" + "="*80)
    print("WEBISCO CSV ENRICHMENT WITH TECDOC DATA")
    print("="*80 + "\n")
    
    # Load TecDoc data
    print(f"Loading TecDoc data from: {tecdoc_json}")
    with open(tecdoc_json, 'r', encoding='utf-8') as f:
        tecdoc_articles = json.load(f)
    print(f"  Loaded {len(tecdoc_articles)} TecDoc articles\n")
    
    # Create index
    index = create_index(tecdoc_articles)
    print()
    
    # Read Webisco CSV
    print(f"Reading Webisco CSV: {csv_file}")
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader)
        rows = list(reader)
    print(f"  Found {len(rows)} rows\n")
    
    # Prepare output header
    output_header = header + [
        'TD_ArticleNumber',
        'TD_EAN',
        'TD_MfrId',
        'TD_MfrName',
        'TD_GenericArticleId',
        'TD_GenericArticleDescription',
        'TD_AssemblyGroupName',
        'TD_OEMNumbers',
        'TD_ArticleCriteria',
        'TD_ArticleStatus',
        'TD_QuantityPerPackage',
        'TD_TotalLinkages',
        'TD_ImageCount',
        'TD_Bild_1_URL',
        'TD_Bild_2_URL',
        'TD_Bild_3_URL',
        'TD_Bild_4_URL',
        'TD_Bild_5_URL',
        'TD_Bild_6_URL',
        'TD_Bild_7_URL',
        'TD_Bild_8_URL',
        'TD_Bild_9_URL',
        'TD_Bild_10_URL'
    ]
    
    # Process rows
    enriched_rows = []
    matched = 0
    not_matched = 0
    
    print("Matching articles...")
    for idx, row in enumerate(rows, 1):
        # Skip empty rows
        if not row or all(not cell.strip() for cell in row):
            continue
        
        # Get article number (column 3, index 2) and EAN (column 6, index 5)
        csv_article_number = row[2].strip() if len(row) > 2 else ''
        csv_ean = row[5].strip() if len(row) > 5 else ''
        
        if not csv_article_number:
            enriched_rows.append(row + [''] * 23)
            continue
        
        # Find matching TecDoc article
        td_article = find_article(csv_article_number, csv_ean, index)
        
        if td_article:
            # Get image URLs
            images = td_article.get('images', [])
            image_urls = []
            for img in images[:10]:  # Max 10 images
                # Prefer 400px version
                url = img.get('url400') or img.get('url200') or img.get('url800') or ''
                if url:
                    image_urls.append(url)
            
            # Pad with empty strings
            while len(image_urls) < 10:
                image_urls.append('')
            
            # Add TecDoc data
            enriched_row = row + [
                td_article.get('articleNumber', ''),
                td_article.get('ean', ''),
                td_article.get('mfrId', ''),
                td_article.get('mfrName', ''),
                td_article.get('genericArticleId', ''),
                td_article.get('genericArticleDescription', ''),
                td_article.get('assemblyGroupName', ''),
                format_oe_numbers(td_article.get('oemNumbers', [])),
                format_criteria(td_article.get('articleCriteria', [])),
                td_article.get('articleStatus', ''),
                td_article.get('quantityPerPackage', ''),
                td_article.get('totalLinkages', ''),
                str(len(images))
            ] + image_urls
            
            enriched_rows.append(enriched_row)
            matched += 1
            
            if idx % 100 == 0:
                print(f"  Processed {idx}/{len(rows)} rows (Matched: {matched}, Not matched: {not_matched})")
        else:
            # No match found
            enriched_rows.append(row + [''] * 23)
            not_matched += 1
    
    # Write output
    print(f"\nWriting enriched CSV: {output_file}")
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(output_header)
        writer.writerows(enriched_rows)
    
    print(f"\n{'='*80}")
    print("ENRICHMENT COMPLETE")
    print("="*80)
    print(f"Total rows processed: {len(rows)}")
    print(f"Matched with TecDoc: {matched} ({matched/len(rows)*100:.1f}%)")
    print(f"Not matched:         {not_matched} ({not_matched/len(rows)*100:.1f}%)")
    print(f"Output file:         {output_file}")
    print("="*80)

if __name__ == "__main__":
    csv_file = "/home/ubuntu/upload/Webisco_Export_GeppSellSoft_2025-12-19_MANN&HUMMEL.csv"
    tecdoc_json = "/home/ubuntu/mann_filter_all_articles_20251219_043704.json"
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"/home/ubuntu/Webisco_FINAL_Enriched_{timestamp}.csv"
    
    enrich_csv(csv_file, tecdoc_json, output_file)
