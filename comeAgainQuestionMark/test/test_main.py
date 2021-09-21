#!/bin/python3
from zipfile import ZipFile
from urllib.request import urlretrieve
import sys
import os

sys.path.insert(0, os.path.abspath(__file__ + "/../.."))
from ComeAgainQuestionMark import transcribe


test_assets_url = "https://space.metaprovide.org/index.php/s/zLZoYFG9WEpgrEt/download"
dirname = os.getcwd()


def download_assets(url):
    zippath = os.path.join(dirname, "assets.zip")
    urlretrieve(test_assets_url, zippath)
    zipfile = ZipFile(zippath, "r")
    zipfile.extractall()
    zipfile.close()
    os.remove(zippath)


def test_mp3_to_raw_no_timestamp(test_audio, benchmark_text):
    print(test_audio)
    print(benchmark_text)


def test_mp4_to_raw_no_timestamp():
    pass


if __name__ == "__main__":
    if not os.path.exists("./ComeAgainQuestionMark - Test Assets"):
        download_assets(test_assets_url)

    test_audio = os.path.join(
        dirname, "ComeAgainQuestionMark - Test Assets/audio/test_case_1.mp3"
    )
    benchmark = os.path.join(
        dirname, "ComeAgainQuestionMark - Test Assets/transcription/test_case_1.txt"
    )
    test_mp3_to_raw_no_timestamp(test_audio, benchmark)