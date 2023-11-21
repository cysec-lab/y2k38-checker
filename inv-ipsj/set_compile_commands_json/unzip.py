import zipfile


def unzip(zip_path, dst_path):
    with zipfile.ZipFile(zip_path) as existing_zip:
        existing_zip.extractall(
            dst_path,
            members=existing_zip.infolist(),
        )


if __name__ == '__main__':
    unzip(
        zip_path="/home/cysec/develop/.y2k38-checker/analysis-objects/0x90__wifi-arsenal/src.zip",
        dst_path="/home/cysec/develop/.y2k38-checker/analysis-objects/0x90__wifi-arsenal/src"
    )
