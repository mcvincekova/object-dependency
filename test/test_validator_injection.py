import unittest
from unittest.mock import patch, MagicMock

from validator_injection import Data, ValidatorMetadata, DataProcessor


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

    @patch('builtins.input', return_value="1234567")
    def test_validate_fail(self, mocked_input):
        validator = ValidatorMetadata()
        validator.read_current_metadata()
        validator.validate()
        self.assertFalse(validator.is_validated())


class TestDataProcessor(unittest.TestCase):

    def test_init(self):
        validator = ValidatorMetadata()
        processor = DataProcessor(validator)
        self.assertEqual(processor.validator, validator)

    def test_validation_success(self):
        validator = ValidatorMetadata()
        validator.read_current_metadata()

        with patch('builtins.input', return_value=validator.metadata):
            processor = DataProcessor(validator)
            data = Data()
            processor.process_data(data)
            self.assertEqual(data.status, 'VALID')

    def test_validation_success_mock(self):
        validator = MagicMock()
        validator.is_validated.return_value = True

        processor = DataProcessor(validator)
        data = Data()
        processor.process_data(data)
        self.assertEqual(data.status, 'VALID')


    def test_validation_fail(self):
        validator = ValidatorMetadata()
        validator.read_current_metadata()

        with patch('builtins.input', return_value='123'):
            processor = DataProcessor(validator)
            data = Data()
            self.assertRaises(Exception, processor.process_data, data)


if __name__ == '__main__':
    unittest.main()
