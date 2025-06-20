import requests
import logging

_logger = logging.getLogger(__name__)

def fetch_company_from_ares(ico):
    #url = f"https://wwwinfo.mfcr.cz/ares/api/ekonomicke-subjekty/{ico}"
    #url = f"http://localhost:5000/ares/api/ekonomicke-subjekty/{ico}"
    url = f"http://host.docker.internal:5000/ares/api/ekonomicke-subjekty/{ico}"


    headers = {
        "Accept": "application/json",
        "User-Agent": "Odoo ARES Plugin - under development (Contact: petr.pribil@profisolv.cz / 776554003)"  
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        _logger.warning(f"when getting to fetch_company_fom_ares, ARES returned following response: {response}")


        # ✅ Confirm JSON response
        if "application/json" not in response.headers.get("Content-Type", ""):
            _logger.warning("ARES did not return JSON")
            _logger.warning("ARES body: %s", response.text[:500])
            return None

        payload = response.json()
        _logger.warning(f"ARES returned following data: {payload}")

    except Exception as e:
        print("ARES fetch error:", str(e))
        return None

    _logger.warning(f"DID IT GET HERE?:  {response.json()}")

    data = payload.get("ekonomickySubjekt")
    if not data:
        return None

    address = data.get("sidlo", {})
    cislo = address.get("cisloDomovni", "")
    ulice = address.get("ulice", "")
    vat = data.get("ico", "").strip().replace("CZ", "").replace(" ", "")
    _logger.warning(f"VAT: {vat}")
    return {
        "name": data.get("obchodniJmeno"),
        "street": f"{ulice} {cislo}".strip(),
        "city": address.get("nazevObce", ""),
        "zip": str(address.get("psc", "")),
        "vat": data.get("ico", ""),
    }
