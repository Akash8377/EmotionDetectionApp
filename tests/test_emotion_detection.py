import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_valid_input(self):
        result = emotion_detector("I am very happy today")
        self.assertIn("joy", result)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_empty_input(self):
        result = emotion_detector("")
        self.assertEqual(result["status"], 400)

    def test_none_input(self):
        result = emotion_detector(None)
        self.assertEqual(result["status"], 400)

if __name__ == "__main__":
    unittest.main()
