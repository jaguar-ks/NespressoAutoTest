# Nespresso Auto Test
UI automation test project for Nespresso website flows using Playwright + Pytest (Python), organized with the Page Object Model pattern.

## Technologies Used
| Technology | Usage |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | Core programming language |
| ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white) | Test framework |
| ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white) | Browser automation |
| ![PyPI](https://img.shields.io/badge/pytest--playwright-3775A9?logo=pypi&logoColor=white) | Pytest + Playwright integration |
| ![PyPI](https://img.shields.io/badge/pytest--xdist-3775A9?logo=pypi&logoColor=white) | Parallel test execution |
| ![PyPI](https://img.shields.io/badge/pytest--html-3775A9?logo=pypi&logoColor=white) | HTML test reporting |
| ![PyPI](https://img.shields.io/badge/playwright--stealth-3775A9?logo=pypi&logoColor=white) | Stealth browser behavior helpers |
| ![dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?logo=dotenv&logoColor=black) | Load environment variables from `.env` |

## Dependencies
Main Python dependencies are listed in `req.txt` (for example: `playwright`, `pytest`, `pytest-playwright`, `pytest-xdist`, `pytest-html`, `playwright-stealth`, `requests`).

System/runtime requirements:
- Python 3.10+ (recommended)
- `pip`
- Playwright browser binaries (`python -m playwright install`)

## Usage
### 1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r req.txt
pip install python-dotenv
python -m playwright install
```

### 3) Configure test credentials
Create a `.env` file in the repository root:
```env
INVALID_EMAIL=your_invalid_email
INVALID_PASS=your_invalid_password
VALID_EMAIL=your_valid_email
VALID_PASS=your_valid_password
```

### 4) Run the automated tests
```bash
pytest
```

Based on `pytest.ini`, tests run:
- Headed mode
- On both Chromium and Firefox
- In parallel (`-n auto`)
- With tracing/screenshots/video on failure
- With HTML report output to `report.html`

### 5) Open the report
After execution, open `report.html` in your browser.

## Automated Tests
Current automated coverage:

1. Login scenarios (`tests/test_sign_in.py`)
- Invalid credentials: verifies the login error message is displayed.
- Valid credentials: verifies successful login by checking the account label (`My Account`).

2. Navigation scenario (`tests/test_navigating_to_coffee_mugs.py`)
- Opens the homepage.
- Navigates through Accessories to Travel Coffee Mugs.
- Verifies page title starts with `Travel Mugs`.

## Project Structure Tree

- NespressoAutoTest/
-  ├── [`conftest.py`](conftest.py)
-  ├── [`pytest.ini`](pytest.ini)
-  ├── [`req.txt`](req.txt)
-  ├── `pages/`
-  │   ├── [`pages/__init__.py`](pages/__init__.py)
-  │   ├── [`pages/home_page.py`](pages/home_page.py)
-  │   └── [`pages/login_page.py`](pages/login_page.py)
-  ├── `tests/`
-  │   ├── [`tests/__init__.py`](tests/__init__.py)
-  │   ├── [`tests/test_navigating_to_coffee_mugs.py`](tests/test_navigating_to_coffee_mugs.py)
-  │   └── [`tests/test_sign_in.py`](tests/test_sign_in.py)
-  ├── [`.env`](.env) *(local credentials, gitignored)*
-  └── [`report.html`](report.html) *(generated test report)*