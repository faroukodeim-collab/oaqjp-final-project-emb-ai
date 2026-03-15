# import necessary packes and functions
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetecion(unittest.TestCase):
    def test_emotion_detecor(self):
        # test 1
        text_to_analyze = "I am glad this happened"
        analysis_result = emotion_detector(text_to_analyze)
        self.assertEqual(analysis_result["dominant_emotion"],"joy")
        # test 2
        text_to_analyze = "I am really mad about this"
        analysis_result = emotion_detector(text_to_analyze)
        self.assertEqual(analysis_result["dominant_emotion"],"anger")
        # test 3
        text_to_analyze = "I feel disgusted just hearing about this"
        analysis_result = emotion_detector(text_to_analyze)
        self.assertEqual(analysis_result["dominant_emotion"],"disgust")
        # test 4
        text_to_analyze = "I am so sad about this"
        analysis_result = emotion_detector(text_to_analyze)
        self.assertEqual(analysis_result["dominant_emotion"],"sadness")
        # test 5
        text_to_analyze = "I am really afraid that this will happen"
        analysis_result = emotion_detector(text_to_analyze)
        self.assertEqual(analysis_result["dominant_emotion"],"fear")

unittest.main()
