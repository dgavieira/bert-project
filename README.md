# Payload Standardizer

The **Payload Standardizer** is a Python application designed to process and standardize JSON payloads from multiple devices communicating in different languages and formats. This application leverages **Helsinki-NLP MarianMT models** to translate non-English payloads into English and map diverse field names into a consistent schema. The result is a unified JSON format that simplifies downstream processing and analytics.

---

## **Features**
- Translates text in payloads from multiple languages (e.g., French to English) using pre-trained **MarianMT models**.
- Standardizes field names from different patterns to a consistent schema.
- Modular design for extensibility, allowing the addition of more languages or payload structures.
- Easy integration into larger data processing pipelines.

---

## **Repository Structure**

```
.
├── LICENSE
├── main.py
├── payload_standardizer
│   ├── config.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── config.cpython-311.pyc
│   │   ├── __init__.cpython-311.pyc
│   │   ├── standardizer.cpython-311.pyc
│   │   └── translator.cpython-311.pyc
│   ├── standardizer.py
│   └── translator.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_standardizer.py

3 directories, 14 files
```


### **Key Files**
- **`translator.py`**: Handles text translation from the source language to English using MarianMT models.
- **`config.py`**: Defines the key mappings to standardize field names.
- **`standardizer.py`**: Combines translation and field mapping to standardize payloads.
- **`main.py`**: Demonstrates the application of the payload standardizer on sample payloads.

---

## **Setup and Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/payload-standardizer.git
   cd payload-standardizer
    ```

2. **Install Dependencies** 
 
    Ensure you have Python 3.8 or later installed. Then, run:
    ```bash
    pip install -r requirements.txt
    ```

## **Usage**

### **Run the Application**

1. Edit `main.py` with the desired payloads and source language.
2. Run the application

    ```bash
    python main.py
    ```

### **Example Input**

Agent 5 payload:

```json
{
    "data": "Status: Online",
    "signal": "High",
    "bandwidth": "20 Mbps",
    "latency": "50 ms",
    "connection": "Wi-Fi",
    "error_rate": "0.01%",
    "data_rate": "15 Mbps"
}
```

Agent 9 payload (in French):

```json
{
    "données": "Statut: En ligne",
    "signal": "Élevé",
    "bande_passante": "20 Mbps",
    "latence": "50 ms",
    "connexion": "Wi-Fi",
    "taux_d’erreur": "0,01%",
    "débit": "15 Mbps"
}
```

### **Output**

```json
{
    "data": "Status: Online",
    "signal": "High",
    "bandwidth": "20 Mbps",
    "latency": "50 ms",
    "connection": "Wi-Fi",
    "error_rate": "0.01%",
    "data_rate": "15 Mbps"
}
```

## **Running Tests**

The repository includes unit tests for the standardizer and translator modules.

1. Run all tests:

```bash
python -m unittest discover -s tests
```

## **Extensibility**

### **Adding a New Language**

1. Update the `source_lang` in the `PayloadStandardizer` initialization to match the desired source language code (e.g., `de` for German).
2. Extend the `KEY_MAP` dictionary in `config.py` with field mappings for the new language.

## **Dependencies**

Install all dependencies via the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## **Contributing**

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed descriptions of your changes.

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

## **Acknowledgments**

This project uses the Helsinki-NLP MarianMT Models from Hugging Face's Transformers
library.


