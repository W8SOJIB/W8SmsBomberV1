# 💀 Ultimate SMS Bomber 💀

**The most powerful SMS bombing tool combining 35+ services into one ultimate weapon!**

Created by: **@@8Team/W8SOJIB**

## 🚀 Features

- **35+ SMS Services** - Combined all popular Bangladeshi SMS services
- **Termux Optimized** - Perfect for mobile hacking on Android
- **Infinite Loop Mode** - Never stops until you say so
- **Hacker Interface** - Beautiful terminal animations and colors
- **Smart Phone Formatting** - Automatically handles different number formats
- **Error Recovery** - Auto-restarts on critical errors
- **Real-time Statistics** - Track success rates and total requests
- **Signal Handling** - Proper CTRL+C and CTRL+Z support
- **Async Performance** - Lightning-fast concurrent requests
- **Anti-Detection** - Dynamic cookies and headers

## 📱 Supported Services

### BTCL Services
- MyBTCL (mybtcl.btcl.gov.bd)
- PhoneBill (phonebill.btcl.com.bd)
- BDIA (bdia.btcl.com.bd)

### E-commerce & Shopping
- Bikroy.com
- Swap.com.bd
- Apex4U

### Entertainment & Media
- BDTickets
- Bioscope Plus
- Cinematic Mobi
- Deepto Play

### Healthcare & Medicine
- Arogga
- Medeasy Health
- Osudpotro
- TheClinicall
- Care Box
- RenixCare

### Education & Learning
- Ghoori Learning
- Priyoshikkhaloy

### Telecom Services
- Grameenphone OTP
- Applink.com.bd

### Others
- Ilyn Global
- Fundesh
- Garibook
- Sheba.xyz
- And many more...

## 🛠️ Installation

### For Termux (Android)

```bash
# Update Termux packages
pkg update && pkg upgrade
pkg install git -y

# Install Python and Git
pkg install python python-pip git

# Clone the repository
git clone https://github.com/W8SOJIB/W8SmsBomberV1
cd W8SmsBomberV1

# Install dependencies
pip install -r requirements.txt

# Run the bomber
python W8SmsBomber.py
```

### For Desktop (Linux/Windows/Mac)

```bash
# Clone the repository
git clone https://github.com/W8SOJIB/W8SmsBomberV1
cd W8SmsBomberV1

# Install dependencies
pip install -r requirements.txt

# Run the bomber
python W8SmsBomber.py
```

### Minimal Installation (Essential only)

```bash
pip install aiohttp requests beautifulsoup4
python W8SmsBomber.py
```

## 🎯 Usage

1. **Run the script:**
   ```bash
   python ultimate_sms_bomber.py
   ```

2. **Enter target phone number:**
   - Supports formats: `01998745882`, `+8801998745885`, `++8801998745885`
   - Auto-formats to all required variations

3. **Watch the magic happen:**
   - 35+ services attack simultaneously
   - Real-time statistics and success rates
   - Beautiful hacker-style interface

4. **Control the attack:**
   - `CTRL+C` - Stop the bomber
   - `CTRL+Z` - Pause/Resume (Linux/Mac)

## ⚡ Performance

- **Concurrent Requests:** Up to 100+ simultaneous connections
- **Speed:** 1000+ SMS per minute (depending on network)
- **Success Rate:** 70-90% average across all services
- **Memory Usage:** ~50MB RAM
- **CPU Usage:** Low (optimized async operations)

## 🔧 Configuration

Edit the script to customize:

```python
# === CONFIGURATION ===
CONCURRENCY = 10        # Concurrent requests per service
LOOP_DELAY = 3          # Seconds between bombing cycles
MAX_RETRIES = 3         # Max retries per failed request
```

## 🛡️ Anti-Detection Features

- **Dynamic Cookies:** Fresh cookies for each request cycle
- **Random User Agents:** Mobile and desktop variations
- **Smart Delays:** Randomized timing between requests
- **Header Rotation:** Different headers per service
- **Session Management:** Proper connection pooling
- **SSL Bypass:** Handles certificate issues automatically

## 📊 Statistics Display

```
[ATTACK CYCLE #1] 02:30:15 PM
[TARGET] 01998745882
[TOTAL REQUESTS] 1,250
[SUCCESS RATE] 85.2%
[RUNTIME] 5.3 minutes
[TOTAL DAMAGE] 1,250 SMS bombs sent
```

## 🚨 Troubleshooting

### SSL Errors
```bash
pip install --upgrade certifi urllib3
```

### Async Errors
```bash
pip install --upgrade aiohttp async-timeout
```

### Encoding Errors
```bash
pip install --upgrade chardet
```

### Performance Issues (Linux/Mac)
```bash
pip install uvloop
```

### Terminal Display Issues
```bash
pip install rich colorama termcolor
```

## 📱 Termux Specific Tips

1. **Grant Storage Permission:**
   ```bash
   termux-setup-storage
   ```

2. **Keep Screen On:**
   - Enable "Keep screen on while charging" in Android settings

3. **Background Execution:**
   ```bash
   nohup python ultimate_sms_bomber.py &
   ```

4. **Check Process:**
   ```bash
   ps aux | grep python
   ```

## ⚠️ Legal Disclaimer

**FOR EDUCATIONAL PURPOSES ONLY!**

This tool is created for:
- Security research and testing
- Educational purposes
- Testing your own phone numbers
- Demonstrating SMS vulnerabilities

**DO NOT USE FOR:**
- Harassment or spam
- Illegal activities
- Attacking others without permission
- Commercial purposes

The creator is not responsible for misuse of this tool.

## 🤝 Contributing

Want to add more services or improve the code?

1. Fork the repository
2. Add your service in the `ServiceManager` class
3. Test thoroughly
4. Submit a pull request

## 📞 Support

Having issues? Need help?

- **Telegram:** @W8SOJIB
- **GitHub Issues:** Create an issue in this repository
- **Email:** Contact through GitHub profile

## 🎉 Credits

**Created by:** @W8Team/W8SOJIB

**Special Thanks:**
- All the original script creators
- The open-source community
- Termux developers
- Python async community

## 📝 Changelog

### v1.0.0 (Latest)
- Combined 35+ SMS services
- Added Termux optimization
- Implemented infinite loop mode
- Added hacker-style interface
- Real-time statistics
- Signal handling
- Error recovery
- Anti-detection features

## 🔮 Future Updates

- [ ] More SMS services
- [ ] Call bombing integration
- [ ] Web interface
- [ ] Mobile app version
- [ ] Proxy support
- [ ] Rate limiting bypass
- [ ] Advanced anti-detection

## ⭐ Star This Repository

If this tool helped you, please give it a star! ⭐

**Happy Hacking! 💀**

---

*Remember: With great power comes great responsibility. Use wisely!*
