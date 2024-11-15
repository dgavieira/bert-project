from payload_standardizer.config import KEY_MAP
from payload_standardizer.translator import Translator


class PayloadStandardizer:
    def __init__(self, source_lang: str):
        """
        Initializes the PayloadStandardizer with a specific source language.
        :param source_lang: Source language code (e.g., "fr").
        """
        self.translator = Translator(source_lang=source_lang)

    def standardize_payload(self, payload: dict) -> dict:
        """
        Standardizes a payload by translating values and standardizing keys.
        :param payload: Input payload dictionary.
        :return: Standardized payload dictionary.
        """
        standardized_payload = {}

        for key, value in payload.items():
            # Map the key to its standard form
            standardized_key = KEY_MAP.get(key, key)

            # Translate value if it's a string
            if isinstance(value, str):
                translated_value = self.translator.translate(value)
            else:
                translated_value = value

            # Add to the standardized payload
            standardized_payload[standardized_key] = translated_value

        return standardized_payload
