from unittest import TestCase

from ppp_nlp_ml_standalone import Linearclassifier, utils, config
import numpy


class LinearClassifierTest(TestCase):

    def testUtils(self):
        self.assertEquals(utils.sigmoid(0), 0.5)
        self.assertEquals(utils.softmax([1,0,0]).shape[0], 3)

    def testLinearClassifier(self):

        x = numpy.array([[1,1,1,0,0,0],
                         [1,0,1,0,0,0],
                         [1,1,1,0,0,0],
                         [0,0,1,1,1,0],
                         [0,0,1,1,0,0],
                         [0,0,1,1,1,0]])
        y = numpy.array([[1, 0],
                        [1, 0],
                        [1, 0],
                        [0, 1],
                        [0, 1],
                        [0, 1]])

        classifier = Linearclassifier.LogisticRegression(x, y, 6, 2)

        for i in range(1, 100):
            classifier.train(lr=0.01)

        value = numpy.array([[1, 1, 0, 0, 0, 0],
                             [0, 0, 0, 1, 1, 0],
                             [0, 0, 1, 1, 1, 1]])


        predicted_values = classifier.predict(value)
        sum_prob = numpy.sum(predicted_values, axis=1)

        self.assertTrue(numpy.linalg.norm(sum_prob-numpy.array([1, 1, 1])) < 0.01)

        self.assertTrue(numpy.array_equal(numpy.argmax(predicted_values, axis=1), numpy.array([0, 1, 1])))

        self.assertTrue(classifier.negative_log_likelihood() < 5)

    def testLearnModel(self):
        trainModel = Linearclassifier.TrainLinearClassifier(config.get_data('questions.train.txt'),
                                                            config.get_data('answers.train.txt'),
                                                            debug=False)

        trainModel.train(n_epochs=5500, learning_rate=0.001, l2_reg=0.001)
        ratio_train = trainModel.train_evaluation()
        ratio_test = trainModel.test_evaluation(config.get_data('questions.test.txt'),
                                   config.get_data('answers.test.txt'))
        trainModel.save_model()

        self.assertTrue(ratio_train > 0.7)
        self.assertTrue(ratio_test > 0.5)