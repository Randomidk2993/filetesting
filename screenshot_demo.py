import pyautogui
import requests
from io import BytesIO

print("This demo will take a screenshot and send it to a Discord channel. Continue? (y/n)")
user_input = input().lower()

if user_input != 'y':
    print("Cancelled.")
    exit()

screenshot = pyautogui.screenshot()
img_buffer = BytesIO()
screenshot.save(img_buffer, format='PNG')
img_buffer.seek(0)

print(f"Send screenshot to Discord? (y/n)")
confirm = input().lower()

if confirm == 'y':
    webhook_url = "https://discord.com/api/webhooks/1360484114582470708/QlDgmnyFP4VIpxlPXoGGpQdIzrHDe0CD0bR5zAa6HIBuflr0eV1WASOEj0dz2LUepYkh"  
    files = {'file': ('screenshot.png', img_buffer, 'image/png')}
    response = requests.post(webhook_url, files=files)
    print("Screenshot sent!" if response.status_code == 200 else "Failed to send.")
else:
    print("Cancelled upload.")
