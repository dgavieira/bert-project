from payload_standardizer.standardizer import PayloadStandardizer


def main():
    # Initialize standardizer for French to English
    standardizer_fr = PayloadStandardizer(source_lang="fr")

    # Example payloads
    agent_5_payload = {
        "data": "Status: Online",
        "signal": "High",
        "bandwidth": "20 Mbps",
        "latency": "50 ms",
        "connection": "Wi-Fi",
        "error_rate": "0.01%",
        "data_rate": "15 Mbps"
    }

    agent_9_payload = {
        "données": "Statut: En ligne",
        "signal": "Élevé",
        "bande_passante": "20 Mbps",
        "latence": "50 ms",
        "connexion": "Wi-Fi",
        "taux_d’erreur": "0,01%",
        "débit": "15 Mbps"
    }

    # Standardize payloads
    standardized_agent_5 = standardizer_fr.standardize_payload(agent_5_payload)  # No translation needed
    standardized_agent_9 = standardizer_fr.standardize_payload(agent_9_payload)  # French to English

    print("Original Payload (Agent 5):", agent_5_payload)
    print("Original Payload (Agent 9):", agent_9_payload)

    print("Standardized Payload (Agent 5):", standardized_agent_5)
    print("Standardized Payload (Agent 9):", standardized_agent_9)


if __name__ == "__main__":
    main()
