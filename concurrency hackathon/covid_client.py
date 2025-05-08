import requests

def fetch_covid_data(country: str) -> dict:
    try:
        url = f"https://disease.sh/v3/covid-19/countries/{country}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "country": data["country"],
            "cases": data["cases"],
            "deaths": data["deaths"],
            "population": data["population"],
            "updated": data["updated"]
        }
    except Exception as e:
        return {"country": country, "error": str(e)}