import pyautogui
import time
import requests 

def take_screenshot():
    print("\n⚠️ SCREENSHOT DEMO: This will capture your screen in 5 seconds.")
    print("Continue? (type 'y' and press Enter, or anything else to cancel)")
    user_input = input().lower()

    if user_input == 'y':
        time.sleep(5)
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        print("✅ Screenshot saved locally as 'screenshot.png'!")
        return True
    else:
        print("❌ Cancelled.")
        return False

def upload_to_discord():
    print("\nUpload this screenshot to Discord? (type 'y' to confirm)")
    if input().lower() != 'y':
        return

    WEBHOOK_URL = "https://discord.com/api/webhooks/1360484114582470708/QlDgmnyFP4VIpxlPXoGGpQdIzrHDe0CD0bR5zAa6HIBuflr0eV1WASOEj0dz2LUepYkh"  
    try:
        with open("screenshot.png", "rb") as f:
            requests.post(WEBHOOK_URL, files={"file": f})
        print("📤 Screenshot uploaded to Discord!")
    except Exception as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    if take_screenshot():
        upload_to_discord()
