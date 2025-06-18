import requests

def fetch_company_from_ares(ico):
    url = f"https://ares.gov.cz/ekonomicke-subjekty?ico={ico}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Ensure it's JSON
        content_type = response.headers.get('Content-Type', '')
        if 'application/json' not in content_type:
            return None  # Not valid JSON response

        payload = response.json()
    except Exception as e:
        return None

    results = payload.get("ekonomickeSubjekty", [])
    if not results:
        return None

    company = results[0]
    name = company.get("obchodniJmeno")
    address = company.get("sidlo", {})
    street = address.get("textovaAdresa", "")
    zip_code = str(address.get("psc") or "")
    city = address.get("nazevObce") or ""

    return {
        "name": name,
        "street": street,
        "city": city,
        "zip": zip_code,
        "vat": company.get("dic", ""),
    }
