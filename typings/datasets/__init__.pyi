from collections.abc import Callable

class Dataset:
    column_names: list[str]
    def map(
        self,
        function: Callable[[dict[str, list[str]]], dict[str, list[list[int]]]],
        *,
        batched: bool,
        remove_columns: list[str],
    ) -> Dataset: ...

class DatasetDict:
    def __getitem__(self, key: str) -> Dataset: ...

def load_dataset(path: str, *, data_files: str) -> DatasetDict: ...
