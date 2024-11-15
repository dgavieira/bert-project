import torch
from transformers import MarianMTModel, MarianTokenizer


class Translator:
    def __init__(self, source_lang: str, target_lang: str = "en"):
        """
        Initializes the translator using MarianMT with GPU support if available.
        :param source_lang: Source language code (e.g., "pt").
        :param target_lang: Target language code (default is "en").
        """
        if source_lang == "pt":
            # Use ROMANCE-en model for Portuguese translations
            self.model_name = f"Helsinki-NLP/opus-mt-ROMANCE-en"
        else:
            self.model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"

        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

        # Check for GPU availability and move the model to GPU
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def translate(self, text: str) -> str:
        """
        Translates text from the source language to the target language.
        :param text: Input text.
        :return: Translated text.
        """
        # Tokenize input text
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)

        # Move inputs to GPU if available
        inputs = {key: value.to(self.device) for key, value in inputs.items()}

        # Perform translation
        translated_tokens = self.model.generate(**inputs)

        # Decode and return the translated text
        translated_text = self.tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        return translated_text

