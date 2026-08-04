"""
LinkedIn Profile Updater - Playwright Visible Browser
=====================================================
Mở trình duyệt Chrome THỰC trên màn hình của anh Duy,
tự động điền thông tin Headline, About, Experience lên LinkedIn.

Cách dùng: Double-click file "dong_bo_linkedin.bat" trên Desktop hoặc File Explorer.
"""
import os
import sys
import time
from pathlib import Path

# Setup path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from playwright.sync_api import sync_playwright
from core.cv_parser import CVParser

def main():
    parser = CVParser()
    profile = parser.get_candidate_profile()

    headline = profile["headline"]
    about = profile["summary"]

    # Persistent browser data so login is remembered
    user_data = str(Path(__file__).resolve().parent / "browser_session" / "chrome_data")
    os.makedirs(user_data, exist_ok=True)

    print("=" * 65)
    print("  DONG BO HO SO LINKEDIN - NGUYEN VAN DUY")
    print("=" * 65)
    print()
    print("Dang mo trinh duyet Chrome...")
    print()

    with sync_playwright() as pw:
        browser = pw.chromium.launch_persistent_context(
            user_data_dir=user_data,
            headless=False,
            slow_mo=800,
            viewport={"width": 1280, "height": 900},
            args=[
                "--start-maximized",
                "--disable-blink-features=AutomationControlled",
            ],
        )

        page = browser.pages[0] if browser.pages else browser.new_page()

        # Step 1: Go to LinkedIn
        print("[1/4] Dang truy cap LinkedIn...")
        page.goto("https://www.linkedin.com/feed/", wait_until="domcontentloaded", timeout=30000)
        time.sleep(3)

        # Check if needs login
        current_url = page.url
        if "login" in current_url or "authwall" in current_url or "checkpoint" in current_url:
            print()
            print("=" * 65)
            print("  ANH DUY VUI LONG DANG NHAP LINKEDIN TREN CUA SO CHROME")
            print("  (Nhap email + mat khau + OTP neu co)")
            print("  He thong se doi toi da 120 giay...")
            print("=" * 65)
            print()

            # Wait for user to login (max 120 seconds)
            for i in range(120):
                url = page.url
                if "feed" in url or "/in/" in url or "mynetwork" in url:
                    print(">> Da dang nhap thanh cong!")
                    break
                time.sleep(1)
                if i % 10 == 0 and i > 0:
                    print(f"   ...dang doi ({i}s)...")
            else:
                print("Het thoi gian doi. Vui long chay lai.")
                browser.close()
                return

        time.sleep(2)

        # Step 2: Go to own profile
        print("[2/4] Dang mo trang Profile ca nhan...")
        page.goto("https://www.linkedin.com/in/me/", wait_until="domcontentloaded", timeout=20000)
        time.sleep(4)

        # Step 3: Try to click Edit Intro button
        print("[3/4] Dang tim nut chinh sua ho so...")
        
        edit_clicked = False
        # LinkedIn edit intro button selectors (may vary)
        edit_selectors = [
            'button[aria-label="Edit intro"]',
            'button.pv-top-card--edit',
            '.pv-top-card .artdeco-button--muted',
            'button:has-text("Edit")',
            '[data-control-name="edit_profile"]',
        ]
        
        for sel in edit_selectors:
            try:
                btn = page.locator(sel).first
                if btn.is_visible(timeout=2000):
                    btn.click()
                    edit_clicked = True
                    print(">> Da bam nut Edit Intro!")
                    time.sleep(3)
                    break
            except Exception:
                continue

        if edit_clicked:
            # Try to fill Headline
            try:
                headline_input = page.locator('input[id*="headline"], input[name*="headline"], .pv-edit-text-detail input').first
                if headline_input.is_visible(timeout=3000):
                    headline_input.fill("")
                    headline_input.fill(headline)
                    print(f">> Da dien Headline: {headline[:60]}...")
                    time.sleep(1)
            except Exception as e:
                print(f"   (Khong tu dong dien duoc Headline: {e})")

            # Try to save
            try:
                save_btn = page.locator('button:has-text("Save"), button[aria-label="Save"]').first
                if save_btn.is_visible(timeout=2000):
                    save_btn.click()
                    print(">> Da bam Save!")
                    time.sleep(3)
            except Exception:
                pass

        # Step 4: Show info for manual paste if automation didn't work
        print()
        print("=" * 65)
        print("  THONG TIN HO SO DA CHUAN BI SAN (COPY-PASTE NEU CAN)")
        print("=" * 65)
        print()
        print(">>> HEADLINE (Tieu de):")
        print(headline)
        print()
        print(">>> ABOUT (Gioi thieu ban than):")
        print(about)
        print()
        print(">>> KINH NGHIEM CHINH:")
        for exp in profile["experiences"][:3]:
            print(f"  - {exp['title']}")
            print(f"    {exp['company']} ({exp['period']})")
            for ach in exp["achievements"][:2]:
                print(f"    * {ach}")
            print()
        print("=" * 65)
        print()
        print("Trinh duyet se giu mo. Anh co the chinh sua truc tiep tren LinkedIn.")
        print("Khi xong, dong cua so trinh duyet hoac bam Ctrl+C tai day.")
        print()

        # Keep browser open until user closes it
        try:
            page.wait_for_event("close", timeout=600000)  # 10 minutes
        except Exception:
            pass

        browser.close()

    print("Da dong trinh duyet. Hoan tat!")

if __name__ == "__main__":
    main()
