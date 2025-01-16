import string
import random


class Data:

    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_lowercase, k=10))
        self.content = "Some amazing data"
        self.status = "UNKNOWN"

    def set_status(self, status):
        self.status = status


class ValidatorMetadata:

    def __init__(self):
        self._validated = False
        self.metadata = None

    def read_current_metadata(self) -> None:
        # Dummy metadata - real implementation would get metadata from the data, predefined config, etc.
        metadata = ''.join(random.choices(string.ascii_letters, k=5))
        print(f"Current metadata: {metadata}")
        self.metadata = metadata

    def validate(self) -> None:
        # Dummy metadata - real implementation would read from a file, database, etc
        valid_metadata = input("Enter valid metadata: ")
        self._validated = valid_metadata == self.metadata

    def is_validated(self) -> bool:
        return self._validated


class DataProcessor:

    def process_data(self, data: Data) -> None:
        validator = ValidatorMetadata()
        validator.read_current_metadata()
        validator.validate()
        if not validator.is_validated():
            raise Exception("Data not validated")

        print(f"Processing validation of data with id {data.id}")
        data.set_status("VALID")
        # do some more work with valid data



def main() -> None:
    data = Data()
    print(f"My initial data: '{data.id}', '{data.content}', '{data.status}'")

    processor = DataProcessor()
    processor.process_data(data)

    print(f"My processed data: '{data.id}', '{data.content}', '{data.status}'")


if __name__ == '__main__':
    main()