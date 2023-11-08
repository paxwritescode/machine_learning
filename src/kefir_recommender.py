from pathlib import Path


def kefir_ocr(input_filename: Path) -> str:
    return ""  # TODO implement


def kefir_nlp(kefir_data: str) -> str:
    return ""  # TODO implement


def main():
    recognized_text = kefir_ocr(Path("./input_examples/example1.jpeg"))
    recommendations = kefir_nlp(recognized_text)
    print(recommendations)  # TODO save to file


if __name__ == "__main__":
    main()
