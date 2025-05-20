import requests
import json
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Pega chave e endpoint da API
subscription_key = os.getenv("AZURE_LANGUAGE_KEY")
endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")

# Configura cabeçalhos
headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": subscription_key
}

# Monta o corpo da requisição
data = {
    "kind": "SentimentAnalysis",
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "text": """
Hotel Stay Review:

I stayed at the Ocean Breeze Hotel for three nights during a business trip. The location was perfect — right by the beach and close to great restaurants. I absolutely loved the view from my room; waking up to the sound of the ocean was incredible.

However, the check-in process was quite slow, and the receptionist didn’t seem very welcoming. My room was clean, but the air conditioning was very noisy, which made it hard to sleep the first night. I asked for assistance, and while the staff eventually fixed it, it took almost a full day.

The breakfast buffet was decent, with fresh fruit and hot dishes, but the coffee tasted burnt. I also appreciated the free Wi-Fi, which was fast and reliable throughout my stay.

Overall, the experience had both good and bad moments. I’d consider staying here again, but there’s definitely room for improvement in customer service and maintenance.
""",
                "language": "en"
            }
        ]
    },
    "parameters": {
        "opinionMining": True
    }
}

# Faz a chamada à API
response = requests.post(endpoint, headers=headers, data=json.dumps(data))

# Exibe o resultado formatado
print("Status code:", response.status_code)
print(json.dumps(response.json(), indent=2))
