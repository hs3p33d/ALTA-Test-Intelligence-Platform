from pathlib import Path


MASTER_DATA_FOLDER = Path(
    "master_data"
)


def load_master_data():

    context = ""

    for file in MASTER_DATA_FOLDER.glob("*.md"):

        content = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        context += f"""

========================
FILE: {file.name}
========================

{content}

"""

    return context


if __name__ == "__main__":

    data = load_master_data()

    print(data[:3000])