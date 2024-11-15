import unittest
from payload_standardizer.standardizer import PayloadStandardizer

class TestPayloadStandardizer(unittest.TestCase):
    def test_standardize_payload(self):
        standardizer = PayloadStandardizer(source_lang="fr")
        input_payload = {
            "données": "Statut: En ligne",
            "signal": "Élevé"
        }
        standardized = standardizer.standardize_payload(input_payload)
        expected = {
            "data": "Status: Online",
            "signal": "High"
        }
        self.assertEqual(standardized, expected)


if __name__ == "__main__":
    unittest.main()
