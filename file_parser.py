from pathlib import Path
import sys

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEOS = []
MP4_VIDEOS = []
MOV_VIDEOS = []
MKV_VIDEOS = []
DOC_DOCS = []
DOCX_DOCS = []
TXT_DOCS = []
PDF_DOCS = []
XLSX_DOCS = []
PPTX_DOCS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
OTHER = []
ARCHIVES = []
FOLDERS = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEOS,
    'MP4': MP4_VIDEOS,
    'MOV': MOV_VIDEOS,
    'MKV': MKV_VIDEOS,
    'DOC': DOC_DOCS,
    'DOCX': DOC_DOCS,
    'TXT': TXT_DOCS,
    'PDF': PDF_DOCS,
    'XLSX': XLSX_DOCS,
    'PPTX': PPTX_DOCS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
}

EXTENSIONS = set()
UNKNOWN = set()


def get_extention(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def pars(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not on ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                pars(item)
            continue
            ext = get_extention(item.name)
            fullname = folder / item.name
            if not ext:
                OTHER.append(fullname)
            else:
                try:
                    container = REGISTER_EXTENSIONS[ext]
                    EXTENSIONS.add(ext)
                    container.append(fullname)
                except KeyError:
                    UNKNOWN.add(ext)
                    OTHER.append(fullname)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
