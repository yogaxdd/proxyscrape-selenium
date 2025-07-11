import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time

# Load Random User-Agent dari ua.txt
with open("ua.txt", "r") as f:
    user_agents = [line.strip() for line in f if line.strip()]
UA = random.choice(user_agents)

# Generate strong password
def generate_password(length=10):
    chars = string.ascii_letters + string.digits
    while True:
        pw = ''.join(random.choices(chars, k=length))
        if any(c.isupper() for c in pw) and any(c.isdigit() for c in pw):
            return pw

PASSWORD = generate_password()

# Input email manual
EMAIL = input("Masukkan email yang ingin digunakan: ")
print(f"🔐 Password akan digunakan: {PASSWORD}")

# Setup browser
options = uc.ChromeOptions()
options.add_argument(f"user-agent={UA}")
options.add_argument("--start-maximized")
options.add_argument("--incognito")
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# 1. Buka halaman trial
driver.get("https://proxyscrape.com/premium-free-trial")
time.sleep(4)

# 2. Klik tombol Start Free Trial
try:
    start_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[contains(@href,"sign-up")]')
    ))
    start_btn.click()
except:
    print("⚠️ Gagal klik Start Free Trial")
    driver.quit()
    exit()

# 3. Isi Form Pendaftaran
time.sleep(5)
driver.find_element(By.XPATH, '//input[@placeholder="youremail@example.com"]').send_keys(EMAIL)
driver.find_element(By.ID, 'auth-login-v2-password').send_keys(PASSWORD)
driver.find_element(By.XPATH, '//input[@placeholder="MyPassword123" and @id!="auth-login-v2-password"]').send_keys(PASSWORD)

# Centang agreement
agree = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
driver.execute_script("arguments[0].click();", agree)

# Tunggu captcha manual
input("🧠 Silakan selesaikan CAPTCHA 'I am human', lalu tekan Enter...")

# Klik Sign Up
print("📌 Mencoba klik tombol Sign Up...")
sign_up_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Sign Up")]')))
sign_up_btn.click()
time.sleep(6)

# Langsung ke halaman login
print("🔁 Menuju halaman login...")
driver.get("https://dashboard.proxyscrape.com/v2/login")
time.sleep(4)

# Login pakai email & password
try:
    driver.find_element(By.XPATH, '//input[@placeholder="youremail@example.com"]').send_keys(EMAIL)
    driver.find_element(By.ID, 'auth-login-v2-password').send_keys(PASSWORD)
    input("🧠 Silakan selesaikan CAPTCHA 'I am human' saat login, lalu tekan Enter...")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Sign in")]'))).click()
    time.sleep(5)
except:
    print("❌ Gagal login. Email/password mungkin salah.")
    driver.quit()
    exit()

# OTP manual input
otp = input("📩 Masukkan kode verifikasi dari email: ")
driver.find_element(By.XPATH, '//input[@placeholder="Email verification code"]').send_keys(otp)

# Klik tombol Verify Email
try:
    verify_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Verify email")]')))
    verify_btn.click()
    time.sleep(4)
except:
    print("❌ Tombol 'Verify email' tidak ditemukan.")

# Selesai
print("\n🎉 Akun berhasil dibuat dan diverifikasi!")
print(f"📧 Email: {EMAIL}")
print(f"🔐 Password: {PASSWORD}")

# Simpan ke done.txt
with open("done.txt", "a") as done_file:
    done_file.write(f"{EMAIL}|{PASSWORD}\n")
