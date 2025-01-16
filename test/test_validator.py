import unittest
from unittest.mock import patch
from validator import Data, ValidatorMetadata, DataProcessor


class TestValidatorMetadata(unittest.TestCase):

    def test_init_authorized(self):
        validator = ValidatorMetadata()
        self.assertFalse(validator.is_validated())

    def test_metadata_textual(self):
        validator = ValidatorMetadata()
        validator.read_current_metadata()
        self.assertTrue(validator.metadata.isalpha())

    def test_validate_success(self):
        validator = ValidatorMetadata()
        validator.read_current_metadata()
        with patch('builtins.input', return_value=validator.metadata):
            validator.validate()
            self.assertTrue(validator.is_validated())

    @patch('builtins.input', return_value="123456")
    def test_validate_fail(self, mocked_input):
        validator = ValidatorMetadata()
        validator.read_current_metadata()
        validator.validate()
        self.assertFalse(validator.is_validated())


class TestDataProcessor(unittest.TestCase):

    @patch('validator.ValidatorMetadata')
    def test_validation_success(self, MockValidator):
        # ???
        # Why does this still pass if I set the return value to False ?
        # ???
        MockValidator.is_validated.return_value = True

        pay_processor = DataProcessor()
        order = Data()
        pay_processor.process_data(order)

        self.assertEqual(order.status, 'VALID')

    def test_validation_fail(self):
        # ???
        pass


if __name__ == '__main__':
    unittest.main()
