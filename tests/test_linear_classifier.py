from unittest import TestCase

from ppp_questionparsing_ml_standalone import linear_classifier, config


class LinearClassifierTest(TestCase):
    def testLearnModel(self):
        trainModel = linear_classifier.Classifier(config.get_data('questions.train.npy'),
                                                             config.get_data('answers.train.npy'),
                                                             debug=False)

        trainModel.train()
        ratio_train = trainModel.train_evaluation()
        ratio_test = trainModel.test_evaluation(config.get_data('questions.test.npy'),
                                                config.get_data('answers.test.npy'))
        trainModel.save_model()

        self.assertGreater(ratio_train, 0.7)
        self.assertGreater(ratio_test, 0.5)
