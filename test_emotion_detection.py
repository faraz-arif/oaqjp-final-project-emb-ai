import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], 'joy')

        # Test case for anger
        result2 = emotion_detector("I am really angry about this")
        self.assertEqual(result2['dominant_emotion'], 'anger')

        # Test case for disgust
        result3 = emotion_detector("I feel disgusted just thinking about it")
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        # Test case for sadness
        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        # Test case for fear
        result5 = emotion_detector("I am scared of what will happen")
        self.assertEqual(result5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()