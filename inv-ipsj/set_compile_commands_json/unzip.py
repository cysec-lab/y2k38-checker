import zipfile


def unzip(zip_path, dst_path):
    with zipfile.ZipFile(zip_path) as existing_zip:
        existing_zip.extractall(
            dst_path,
            members=existing_zip.infolist(),
        )


if __name__ == '__main__':
    zip_path = "/Users/rannosukehoshina/Develop/y2k38-checker/inv-ipsj/set_compile_commands_json/test.zip"
    dst_path = '/Users/rannosukehoshina/Develop/y2k38-checker/inv-ipsj/set_compile_commands_json/'
    unzip(zip_path, dst_path)
    print("Successefully unziped.", zip_path)
