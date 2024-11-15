from payload_standardizer.standardizer import PayloadStandardizer
from payload_standardizer.config import AGENT_LANGUAGES
from payload_standardizer.constants import AGENT_PAYLOADS
from auth.huggingface_auth import authenticate_with_huggingface


def main():
    # Authenticate with Hugging Face
    authenticate_with_huggingface()

    # Process each agent's payload
    for agent, payload in AGENT_PAYLOADS.items():
        source_lang = AGENT_LANGUAGES[agent]
        standardizer = PayloadStandardizer(source_lang=source_lang)
        standardized_payload = standardizer.standardize_payload(payload)
        print(f"Standardized Payload ({agent}): {standardized_payload}")


if __name__ == "__main__":
    main()
