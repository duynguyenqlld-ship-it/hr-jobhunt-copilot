import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CV_PATH = BASE_DIR / "CV_Nguyen_Van_Duy_Truong_Phong_HCNS.pdf"
DATA_DIR = BASE_DIR / "data"
BROWSER_DATA_DIR = BASE_DIR / "browser_session"

# Create directories if not exist
DATA_DIR.mkdir(exist_ok=True)
BROWSER_DATA_DIR.mkdir(exist_ok=True)

# Search filters
DEFAULT_KEYWORDS = [
    "Trưởng phòng Hành chính Nhân sự",
    "HRBP Strategic Partner",
    "HR Manager",
    "Giám đốc Nhân sự",
    "Head of HR"
]

DEFAULT_LOCATIONS = [
    "Hồ Chí Minh",
    "Thủ Đức",
    "Biên Hòa"
]

DEFAULT_MIN_MATCH_SCORE = 70
