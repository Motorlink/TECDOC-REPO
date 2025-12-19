#!/usr/bin/env python3
"""
Download ALL MANN-FILTER Articles from TecDoc API
Complete data including images, OE numbers, technical attributes
"""

import requests
import xml.etree.ElementTree as ET
import json
from datetime import datetime
import time

API_KEY = "2BeBXg6Nymr1VB3KjYRu69F4S9UGm24q5WUitw1bZKDBnePtCFtC"
PROVIDER_ID = "23862"
ENDPOINT = "https://webservice.tecalliance.services/pegasus-3-0/services/TecdocToCatDLB.soapEndpoint"

def get_articles_page(page, per_page=100):
    """Get one page of MANN-FILTER articles"""
    
    soap_body = f"""<getArticles xmlns="http://server.cat.tecdoc.net">
    <provider>{PROVIDER_ID}</provider>
    <country>de</country>
    <lang>de</lang>
    <articleCountry>de</articleCountry>
    <dataSupplierIds>4</dataSupplierIds>
    <perPage>{per_page}</perPage>
    <page>{page}</page>
    
    <!-- ALL INCLUDE PARAMETERS -->
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

def get_text(element, tag_name):
    """Helper to get text from XML element"""
    if element is None:
        return ''
    
    elem = element.find(tag_name)
    if elem is not None and elem.text:
        return elem.text
    
    for child in element:
        if child.tag.endswith(f'}}{tag_name}') or child.tag == tag_name:
            return child.text if child.text else ''
    
    return ''

def parse_articles(xml_text):
    """Parse articles from XML response"""
    
    root = ET.fromstring(xml_text)
    
    articles = []
    article_elements = []
    
    for elem in root.iter():
        if elem.tag.endswith('}articles') or elem.tag == 'articles':
            article_elements.append(elem)
    
    for article_elem in article_elements:
        article = {}
        
        # Basic fields
        article['articleNumber'] = get_text(article_elem, 'articleNumber')
        article['dataSupplierId'] = get_text(article_elem, 'dataSupplierId')
        article['mfrId'] = get_text(article_elem, 'mfrId')
        article['mfrName'] = get_text(article_elem, 'mfrName')
        article['ean'] = get_text(article_elem, 'gtins')
        
        # Generic Article
        gen_art = article_elem.find('genericArticles')
        if gen_art is not None:
            article['genericArticleId'] = get_text(gen_art, 'genericArticleId')
            article['genericArticleDescription'] = get_text(gen_art, 'genericArticleDescription')
            article['assemblyGroupName'] = get_text(gen_art, 'assemblyGroupName')
            article['assemblyGroupNodeId'] = get_text(gen_art, 'assemblyGroupNodeId')
            article['legacyArticleId'] = get_text(gen_art, 'legacyArticleId')
        else:
            article['genericArticleId'] = ''
            article['genericArticleDescription'] = ''
            article['assemblyGroupName'] = ''
            article['assemblyGroupNodeId'] = ''
            article['legacyArticleId'] = ''
        
        # OEM Numbers
        oem_numbers = []
        for oem in article_elem.findall('oemNumbers'):
            oem_num = get_text(oem, 'articleNumber')
            oem_mfr = get_text(oem, 'mfrName')
            if oem_num and oem_mfr:
                oem_numbers.append({'number': oem_num, 'manufacturer': oem_mfr})
        article['oemNumbers'] = oem_numbers
        
        # Article Criteria
        criteria = []
        for crit in article_elem.findall('articleCriteria'):
            crit_desc = get_text(crit, 'criteriaDescription')
            crit_val = get_text(crit, 'formattedValue')
            crit_unit = get_text(crit, 'criteriaUnitDescription')
            if crit_desc and crit_val:
                criteria.append({
                    'description': crit_desc,
                    'value': crit_val,
                    'unit': crit_unit
                })
        article['articleCriteria'] = criteria
        
        # Misc Data
        misc = article_elem.find('misc')
        if misc is not None:
            article['articleStatus'] = get_text(misc, 'articleStatusDescription')
            article['articleStatusValidFrom'] = get_text(misc, 'articleStatusValidFromDate')
            article['quantityPerPackage'] = get_text(misc, 'quantityPerPackage')
            article['isRemanufactured'] = get_text(misc, 'isRemanufacturedPart')
            article['isAccessory'] = get_text(misc, 'isAccessory')
        else:
            article['articleStatus'] = ''
            article['articleStatusValidFrom'] = ''
            article['quantityPerPackage'] = ''
            article['isRemanufactured'] = ''
            article['isAccessory'] = ''
        
        article['totalLinkages'] = get_text(article_elem, 'totalLinkages')
        
        # Images
        images = []
        for img in article_elem.findall('images'):
            image_data = {
                'url50': get_text(img, 'imageURL50'),
                'url100': get_text(img, 'imageURL100'),
                'url200': get_text(img, 'imageURL200'),
                'url400': get_text(img, 'imageURL400'),
                'url800': get_text(img, 'imageURL800'),
                'url1600': get_text(img, 'imageURL1600'),
                'url3200': get_text(img, 'imageURL3200'),
                'fileName': get_text(img, 'fileName'),
                'typeDescription': get_text(img, 'typeDescription'),
                'headerDescription': get_text(img, 'headerDescription'),
            }
            images.append(image_data)
        article['images'] = images
        
        articles.append(article)
    
    return articles

def download_all_articles():
    """Download all MANN-FILTER articles"""
    
    print("\n" + "="*80)
    print("DOWNLOADING ALL MANN-FILTER ARTICLES FROM TECDOC")
    print("="*80 + "\n")
    
    all_articles = []
    page = 1
    per_page = 100
    total_articles = None
    
    while True:
        print(f"Fetching page {page}...", end=" ", flush=True)
        
        try:
            xml_response = get_articles_page(page, per_page)
            
            # Parse metadata
            root = ET.fromstring(xml_response)
            if total_articles is None:
                for elem in root.iter():
                    if 'totalMatchingArticles' in elem.tag and elem.text:
                        total_articles = int(elem.text)
                        max_pages = (total_articles + per_page - 1) // per_page
                        print(f"\nTotal articles: {total_articles}")
                        print(f"Pages to fetch: {max_pages}\n")
                        break
            
            # Parse articles
            articles = parse_articles(xml_response)
            
            if not articles:
                print("No more articles")
                break
            
            all_articles.extend(articles)
            print(f"✅ Got {len(articles)} articles (Total: {len(all_articles)})")
            
            # Check if we got all
            if total_articles and len(all_articles) >= total_articles:
                break
            
            page += 1
            time.sleep(0.2)  # Small delay to avoid rate limiting
            
        except Exception as e:
            print(f"❌ Error: {e}")
            break
    
    print(f"\n{'='*80}")
    print(f"DOWNLOAD COMPLETE")
    print(f"{'='*80}")
    print(f"Total articles downloaded: {len(all_articles)}")
    
    # Save to JSON
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"/home/ubuntu/mann_filter_all_articles_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_articles, f, indent=2, ensure_ascii=False)
    
    print(f"Saved to: {filename}")
    print(f"{'='*80}\n")
    
    return all_articles, filename

if __name__ == "__main__":
    articles, filename = download_all_articles()
    
    # Print statistics
    print("STATISTICS:")
    print(f"  Total articles: {len(articles)}")
    print(f"  Articles with EAN: {sum(1 for a in articles if a.get('ean'))}")
    print(f"  Articles with images: {sum(1 for a in articles if a.get('images'))}")
    print(f"  Articles with OE numbers: {sum(1 for a in articles if a.get('oemNumbers'))}")
    print(f"  Articles with criteria: {sum(1 for a in articles if a.get('articleCriteria'))}")
