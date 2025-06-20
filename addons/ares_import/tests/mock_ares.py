from flask import Flask, jsonify, request

app = Flask(__name__)

# Example mocked response for ICO 06635482
mock_companies = {
    "06635482": {
        "ico": "06635482",
        "obchodniJmeno": "Profisolv s.r.o.",
        "sidlo": {
            "stat": "CZ",
            "nazevObce": "Dolni Bojanovice",
            "ulice": "U Hriste",
            "cisloDomovni": "647",
            "psc": "69617"
        },
        "pravniForma": "121",
        "datumVzniku": "2017-11-28"
    },
    "12345678": {
        "ico": "12345678",
        "obchodniJmeno": "Alfatech Solutions a.s.",
        "sidlo": {
            "stat": "CZ",
            "nazevObce": "Brno",
            "ulice": "Technologická",
            "cisloDomovni": "12",
            "psc": "61200"
        },
        "pravniForma": "121",
        "datumVzniku": "2001-06-15"
    },
    "87654321": {
        "ico": "87654321",
        "obchodniJmeno": "GreenFarm Agro s.r.o.",
        "sidlo": {
            "stat": "CZ",
            "nazevObce": "Olomouc",
            "ulice": "Polní",
            "cisloDomovni": "204",
            "psc": "77900"
        },
        "pravniForma": "121",
        "datumVzniku": "2012-09-10"
    },
    "11223344": {
        "ico": "11223344",
        "obchodniJmeno": "CzechDesign Studio s.r.o.",
        "sidlo": {
            "stat": "CZ",
            "nazevObce": "Praha",
            "ulice": "Dlouhá",
            "cisloDomovni": "88",
            "psc": "11000"
        },
        "pravniForma": "121",
        "datumVzniku": "2018-02-01"
    },
    "55667788": {
        "ico": "55667788",
        "obchodniJmeno": "Medisoft Systems a.s.",
        "sidlo": {
            "stat": "CZ",
            "nazevObce": "Plzeň",
            "ulice": "Zdravotní",
            "cisloDomovni": "301",
            "psc": "32300"
        },
        "pravniForma": "121",
        "datumVzniku": "2009-05-25"
    },
    "99887766": {
        "ico": "99887766",
        "obchodniJmeno": "Energetika Zlín s.r.o.",
        "sidlo": {
            "stat": "CZ",
            "nazevObce": "Zlín",
            "ulice": "Elektrárenská",
            "cisloDomovni": "7",
            "psc": "76001"
        },
        "pravniForma": "121",
        "datumVzniku": "2015-08-19"
    }
}

@app.route("/ares/api/ekonomicke-subjekty/<ico>", methods=["GET"])
def get_company(ico):
    company_data = mock_companies.get(ico)
    if company_data:
        return jsonify({"ekonomickySubjekt":company_data}), 200
    else:
        return jsonify({"error": "Company not found"}), 404   

if __name__ == "__main__":
    app.run(debug=True, port=5000)