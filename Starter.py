# ============================================================
#                        ______
#                     .-"      "-.
#                    /            \
#        _          |              |          _
#       ( \         |,  .-.  .-.  ,|         / )
#        > "=._     | )(__/  \__)( |     _.=" <
#       (_/"=._"=._ |/     /\     \| _.="_.="\_)
#             "=._ (_     ^^     _)"_.="
#                 "=\__|IIIIII|__/="
#                _.="| \IIIIII/ |"=._
#       _     _.="_.="\          /"=._"=._     _
#      ( \_.="_.="     `--------`     "=._"=._/ )
#       > _.="      N E T  P I R A T E S  "=._ <
#      (_/    Real Action. Online and Off.    \_)
# ============================================================

import os
import time
import sys
import json
import subprocess
from colorama import init, Fore, Style, Back
import socket
import ctypes
import shutil
import urllib.request

init(autoreset=True)

IS_WINDOWS = os.name == 'nt'

# --- UTILITY FUNCTIONS ---

def clear():
    os.system('cls' if IS_WINDOWS else 'clear')

def typewrite(text, color="", delay=0.03):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def get_ping():
    try:
        param = '-n' if IS_WINDOWS else '-c'
        output = subprocess.check_output(
            ['ping', param, '1', '8.8.8.8'],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        if "Zeit=" in output:
            return output.split("Zeit=")[1].split("ms")[0].strip() + "ms"
        elif "time=" in output:
            return output.split("time=")[1].split("ms")[0].strip() + "ms"
        return "22ms"
    except:
        return "OFFLINE"

def repair_animation():
    clear()
    repair_tasks = [
        "Calling the Repair Crew...",
        "Patching holes in the hull...",
        "Recalibrating the compass...",
        "Securing the cargo...",
        "Polishing the Captain's desk..."
    ]
    print(f"{Fore.CYAN}--- EMERGENCY REPAIR IN PROGRESS ---")
    for task in repair_tasks:
        sys.stdout.write(f"\r{Fore.WHITE}[ ] {task}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f"\r{Fore.GREEN}[✔] {task}\n")
        sys.stdout.flush()
        time.sleep(0.2)
    print(f"\n{Fore.GREEN}REPAIR COMPLETE. WELCOME BACK, CAPTAIN.")
    time.sleep(1.5)

def load_config():
    default_config = {
        "settings": {"language": "EN"},
        "apps": {
            "App1": "C:\\Path\\To\\Your\\Program1.exe" if IS_WINDOWS else "/usr/bin/nano",
            "App2": "C:\\Path\\To\\Your\\Program2.exe" if IS_WINDOWS else "/usr/bin/top",
            "App3": "C:\\Path\\To\\Your\\Program3.exe" if IS_WINDOWS else "/usr/bin/htop",
            "App4": "C:\\Path\\To\\Your\\Program4.exe" if IS_WINDOWS else "/usr/bin/curl",
            "App5": "C:\\Path\\To\\Your\\Program5.exe" if IS_WINDOWS else "/usr/bin/wget"
        },
        "presets": {
            "1": {"name": "Preset 1", "apps": ["App1", "App2"]},
            "2": {"name": "Preset 2", "apps": ["App3", "App4"]},
            "3": {"name": "Preset 3", "apps": ["App1", "App5"]},
            "4": {"name": "Preset 4", "apps": ["App2", "App4"]}
        }
    }

    if not os.path.exists('config.json'):
        clear()
        print(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT} !!! CRITICAL ERROR: CONFIG FILE NOT FOUND !!! {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Action: Deploying emergency protocols...")
        print(f"{Fore.YELLOW}[+] Status: Created new clean config.json")
        print(f"{Fore.WHITE}" + "-" * 50)
        try:
            with open('config.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            time.sleep(3)
            return default_config
        except Exception as e:
            print(f"{Fore.RED}[!] FATAL: Could not write to disk: {e}")
            input("Press Enter to close...")
            sys.exit()

    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        clear()
        print(f"{Fore.RED}[!] CRITICAL: config.json is corrupted.")
        choice = input(f"{Fore.YELLOW}[?] Send out the Repair Crew? (Y/N): ").upper()
        if choice == 'Y':
            repair_animation()
            with open('config.json', 'w') as f:
                json.dump(default_config, f, indent=4)
            return default_config
        else:
            print(f"{Fore.RED}[!] Manual repair required. Terminating.")
            sys.exit()

# FIX: Config wird einmal geladen und gecacht, nicht bei jedem get_text()-Aufruf neu von Disk gelesen
_config_cache = None

def get_config():
    global _config_cache
    if _config_cache is None:
        _config_cache = load_config()
    return _config_cache

def get_text(key):
    config = get_config()
    lang = config.get('settings', {}).get('language', 'EN')
    strings = {
        "DE": {
            "welcome":      "Willkommen an Bord... Pirat.",
            "choice":       "Was ist der naechste Schritt?",
            "input":        "Auswahl > ",
            "exit_msg":     "Verbindung getrennt. Auf Wiedersehen.",
            "menu_pulse":   "Netzwerk-Puls (Echtzeit Ping)",
            "menu_code":    "Ehrenkodex lesen",
            "menu_dns":     "DNS & Cache leeren",
            "menu_temp":    "Temp-Dateien bereinigen",
            "menu_panic":   "Panic Button",
            "menu_killer":  "Process Killer (Gaming Mode)",
            "menu_latency": "Latenz-Checker",
            "menu_ip":      "Oeffentliche IP & VPN Check",
            "menu_ports":   "Port Listener",
            "menu_exit":    "Trennen & Verlassen"
        },
        "EN": {
            "welcome":      "Welcome aboard... Pirate.",
            "choice":       "What is the next move?",
            "input":        "Select > ",
            "exit_msg":     "Sailing alone now. Goodbye.",
            "menu_pulse":   "Network Pulse (Real-Time Ping)",
            "menu_code":    "Read Honor Code",
            "menu_exit":    "Disconnect & Exit",
            "menu_dns":     "DNS & Cache Flush",
            "menu_temp":    "Temp File Purge",
            "menu_panic":   "Panic Button",
            "menu_killer":  "Process Killer (Gaming Mode)",
            "menu_latency": "Latency Checker",
            "menu_ip":      "Public IP & VPN Check",
            "menu_ports":   "Port Listener"
        }
    }
    lang_strings = strings.get(lang, strings["EN"])
    return lang_strings.get(key, strings["EN"].get(key, f"[{key}]"))

# --- PHASE 1: LOGIN ---

def login_screen():
    clear()
    logo_block = r"""
███    ██ ███████ ████████     ██████  ██ ██████  █████  ████████ ███████ ███████
████   ██ ██         ██        ██   ██ ██ ██   ██ ██   ██    ██    ██      ██     
██ ██  ██ █████      ██        ██████  ██ ██████  ███████    ██    █████   ███████
██  ██ ██ ██         ██        ██      ██ ██   ██ ██   ██    ██    ██           ██
██   ████ ███████    ██        ██      ██ ██   ██ ██   ██    ██    ███████ ███████
"""
    try:
        columns, lines = os.get_terminal_size()
    except OSError:
        columns, lines = 120, 30

    logo_lines = logo_block.strip("\n").split("\n")
    v_padding = (lines - len(logo_lines) - 6) // 2
    if v_padding > 0:
        print("\n" * v_padding)

    for line in logo_lines:
        padding = (columns - len(line)) // 2
        print(" " * max(0, padding) + Fore.GREEN + line)
        time.sleep(0.05)

    time.sleep(0.2)
    print("\n" + Fore.WHITE + "[  NET PIRATES — REAL ACTION. ONLINE AND OFF.  ]".center(columns))
    time.sleep(0.15)
    print(f"{Fore.YELLOW}" + ">> PRESS ENTER TO LOG IN <<".center(columns))
    input()

# --- PHASE 2: LOADING ---

def dramatic_loading():
    clear()
    try:
        columns, lines = os.get_terminal_size()
    except OSError:
        columns = 120

    # FIX: skull_open hatte doppelte Zeile, Schädel-Animation war kaputt
    skull_closed = [
        r'                        ______',
        r'                     .-"      "-.',
        r'                    /            ' + '\\',
        r'        _          |              |          _',
        r'       ( \         |,  .-.  .-.  ,|         / )',
        r'        > "=._     | )(__/  \__)( |     _.=" <',
        r'      (_/"=._"=._  |/     /\     \| _.="_.="\_)',
        r'              "=._ (_     ^^     _)"_.="',
        r'                  "=\__|IIIIII|__/="',
        r'                 _.="| \IIIIII/ |"=._',
        r'       _     _.="_.="\          /"=._"=._     _',
        r'      ( \_.="_.="     `--------`     "=._"=._/ )',
        r'       > _.="      N E T  P I R A T E S  "=._ <',
        r'      (_/    Real Action. Online and Off.    \_)'
    ]

    skull_open = [
        r'                        ______',
        r'                     .-"      "-.',
        r'                    /            ' + '\\',
        r'        _          |              |          _',
        r'       ( \         |,  .-.  .-.  ,|         / )',
        r'        > "=._     | )(__/  \__)( |     _.=" <',
        r'      (_/"=._"=._  |/     /\     \| _.="_.="\_)',
        r'              "=._ (_     ^^     _)"_.="',
        r'                  "=\__|------|__/="',
        r'                 _.="| \------/ |"=._',
        r'       _     _.="_.="\          /"=._"=._     _',
        r'      ( \_.="_.="     `--------`     "=._"=._/ )',
        r'       > _.="      N E T  P I R A T E S  "=._ <',
        r'      (_/    Real Action. Online and Off.    \_)'
    ]

    ops = [
        "[I] Setting Sails", "[I] Raising Flag", "[I] Reloading Canons",
        "[I] Raising Anchor", "[I] Plotting Course", "[I] Scanning Horizons",
        "[I] Calibrating Compass", "[I] Patching Hull", "[I] Polishing Sextant",
        "[I] Gathering Crew", "[I] Distributing Grog", "[I] Sharpening Cutlasses",
        "[I] Counting Doubloons", "[I] Consulting the Stars", "[I] Braving the Storm",
        "[I] Checking the Tides", "[I] Finalizing Mission"
    ]

    skull_width = max(len(line) for line in skull_closed)
    left_offset = (columns - skull_width) // 2

    for line in skull_closed:
        sys.stdout.write(" " * max(0, left_offset) + Fore.RED + line + "\n")
        sys.stdout.flush()
        time.sleep(0.03)

    time.sleep(0.3)

    for op in ops:
        bar_len = 40
        for i in range(bar_len + 1):
            current_skull = skull_open if (i // 5) % 2 == 0 else skull_closed
            sys.stdout.write("\033[H")

            skull_width = max(len(line) for line in current_skull)
            left_offset = (columns - skull_width) // 2
            for line in current_skull:
                sys.stdout.write(" " * max(0, left_offset) + Fore.RED + line + "\n")

            percent = int((i / bar_len) * 100)
            bar = chr(9608) * i + chr(9617) * (bar_len - i)
            progress_text = f"PROGRESS: [{bar}] {percent}%"

            sys.stdout.write("\n" + op.center(columns) + "\n")
            sys.stdout.write(Fore.GREEN + progress_text.center(columns) + "\n")
            sys.stdout.flush()
            time.sleep(0.01)
        sys.stdout.write("\n\n")

    msg_1 = "[!] SHIP IS READY, CAPTAIN. DEPLOYING..."
    msg_2 = "[!] May the Tides be with you."
    print(f"{Fore.CYAN}{msg_1.center(columns)}")
    print(f"{Fore.YELLOW}{msg_2.center(columns)}")
    time.sleep(1.5)

# --- PHASE 3: PRESETS ---

def deployment_menu():
    config = get_config()
    presets = config.get('presets', {})
    first_run = True
    while True:
        clear()
        print(f"\n  {Fore.CYAN}--- DEPLOYMENT INITIALIZATION ---")
        print(f"  {Fore.WHITE}" + "-" * 33)

        for key in sorted(presets.keys()):
            if first_run:
                typewrite(f"  [{key}] {presets[key]['name']}", Fore.GREEN, delay=0.02)
                time.sleep(0.04)
            else:
                print(f"  {Fore.GREEN}[{key}]{Fore.WHITE} {presets[key]['name']}")

        if first_run:
            typewrite(f"  [0] Skip to Main Terminal", Fore.YELLOW, delay=0.02)
        else:
            print(f"  {Fore.YELLOW}[0]{Fore.WHITE} Skip to Main Terminal")

        print(f"  {Fore.WHITE}" + "-" * 33)
        first_run = False

        choice = input(f"\n  {Fore.GREEN}{get_text('input')}")

        if choice in presets:
            with open(os.devnull, 'w') as fnull:
                for app in presets[choice]['apps']:
                    path = config['apps'].get(app)
                    if path:
                        c_flags = subprocess.CREATE_NO_WINDOW if IS_WINDOWS else 0
                        subprocess.Popen(
                            path, shell=True, stdout=fnull, stderr=fnull,
                            creationflags=c_flags
                        )
            return
        elif choice == "0":
            return

# --- PHASE 4: MAIN MENU TOOLS ---

def network_pulse():
    clear()
    print(f"\n  {Fore.YELLOW}Testing connection to the backbone... (8.8.8.8)\n")
    for _ in range(5):
        result = get_ping()
        color = Fore.GREEN if result != "OFFLINE" else Fore.RED
        print(f"  {Fore.WHITE}Response from 8.8.8.8: {color}latency={result}")
        time.sleep(0.6)
    input(f"\n  {Fore.WHITE}Press Enter to return...")

def honor_code():
    clear()
    lines = [
        ("", ""),
        ("  NET PIRATES \u2014 HONOR CODE",                                                        f"{Fore.GREEN}{Style.BRIGHT}"),
        ("", ""),
        ("  We are not chaos. We are a crew.",                                                     f"{Fore.WHITE}"),
        ("  And a crew without a code is already lost.",                                            f"{Fore.WHITE}"),
        ("", ""),
        ("  I.     We stand for people \u2014 not ego.",                                            f"{Fore.GREEN}"),
        ("         No action is taken for clout, pride, or personal gain.",                         f"{Fore.WHITE}"),
        ("         If it doesn't protect or uplift, it has no place among us.",                     f"{Fore.WHITE}"),
        ("", ""),
        ("  II.    We do not become what we oppose.",                                               f"{Fore.GREEN}"),
        ("         We confront hate \u2014 we do not mirror it.",                                   f"{Fore.WHITE}"),
        ("         No dehumanization. No blind harassment. No targeting without cause.",             f"{Fore.WHITE}"),
        ("", ""),
        ("  III.   We act with purpose.",                                                           f"{Fore.GREEN}"),
        ("         Every move has intent.",                                                         f"{Fore.WHITE}"),
        ("         We do not swarm blindly, spam endlessly, or act without reason.",                f"{Fore.WHITE}"),
        ("", ""),
        ("  IV.    We protect the vulnerable.",                                                     f"{Fore.GREEN}"),
        ("         Those under attack are not alone.",                                              f"{Fore.WHITE}"),
        ("         We amplify voices \u2014 we do not drown them.",                                 f"{Fore.WHITE}"),
        ("", ""),
        ("  V.     We are accountable.",                                                            f"{Fore.GREEN}"),
        ("         No masks within the crew.",                                                      f"{Fore.WHITE}"),
        ("         If one of us crosses the line, we answer for it \u2014 together.",               f"{Fore.WHITE}"),
        ("", ""),
        ("  VI.    No captain rules us.",                                                           f"{Fore.GREEN}"),
        ("         We move as a collective.",                                                       f"{Fore.WHITE}"),
        ("         Leadership is earned through action, not claimed through power.",                 f"{Fore.WHITE}"),
        ("", ""),
        ("  VII.   We respect the line between resistance and harm.",                               f"{Fore.GREEN}"),
        ("         We disrupt injustice \u2014 not lives.",                                         f"{Fore.WHITE}"),
        ("         We do not endanger, dox, or destroy beyond what is justifiable.",                f"{Fore.WHITE}"),
        ("", ""),
        ("  VIII.  Presence over silence.",                                                         f"{Fore.GREEN}"),
        ("         Where injustice grows, we show up.",                                             f"{Fore.WHITE}"),
        ("         Online or on the streets - absence is not neutrality.",                          f"{Fore.WHITE}"),
        ("", ""),
        ("  IX.    We leave no one behind.",                                                        f"{Fore.GREEN}"),
        ("         Crew means loyalty.",                                                            f"{Fore.WHITE}"),
        ("         Internally, we support \u2014 not exploit.",                                     f"{Fore.WHITE}"),
        ("", ""),
        ("  X.     The flag means something.",                                                      f"{Fore.GREEN}"),
        ("         If you carry it, you represent all of us.",                                      f"{Fore.WHITE}"),
        ("         Act accordingly.",                                                               f"{Fore.WHITE}"),
        ("", ""),
        ("  \u2014 " * 23,                                                                          f"{Fore.YELLOW}"),
        ("  Break the code, and you sail alone.",                                                   f"{Fore.RED}{Style.BRIGHT}"),
        ("  \u2014 " * 23,                                                                          f"{Fore.YELLOW}"),
        ("", ""),
        ("                                \u2014 Net Pirates",                                      f"{Fore.GREEN}"),
        ("", ""),
    ]
    for text, color in lines:
        print(f"{color}{text}")
        time.sleep(0.04)
    input(f"  {Fore.WHITE}Press Enter to return...")

def dns_flush():
    clear()
    print(f"\n  {Fore.CYAN}--- DNS & CACHE FLUSH ---\n")

    if IS_WINDOWS:
        tasks = [
            ("Flushing DNS cache",        "ipconfig /flushdns"),
            ("Releasing IP lease",        "ipconfig /release"),
            ("Renewing IP lease",         "ipconfig /renew"),
            ("Resetting Winsock catalog", "netsh winsock reset"),
            ("Resetting TCP/IP stack",    "netsh int ip reset"),
        ]
    else:
        tasks = [
            ("Flushing DNS (systemd)",    "resolvectl flush-caches || systemd-resolve --flush-caches"),
            ("Clearing NSCD Cache",       "sudo service nscd restart || true"),
            ("Refreshing Interfaces",     "sudo ip link set dev $(ip route show | grep default | awk '{print $5}') down && sudo ip link set dev $(ip route show | grep default | awk '{print $5}') up || true")
        ]

    for label, cmd in tasks:
        sys.stdout.write(f"  {Fore.WHITE}[ ] {label}...")
        sys.stdout.flush()
        try:
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            sys.stdout.write(f"\r  {Fore.GREEN}[\u2714] {label}\n")
        except:
            sys.stdout.write(f"\r  {Fore.RED}[!] {label} - failed\n")
        sys.stdout.flush()
        time.sleep(0.4)
    print(f"\n  {Fore.GREEN}DNS & Cache flushed. Sails are clean, Captain.")
    input(f"\n  {Fore.WHITE}Press Enter to return...")

def temp_purge():
    clear()
    print(f"\n  {Fore.CYAN}--- TEMP FILE PURGE ---\n")

    if IS_WINDOWS:
        temp_dirs = [
            os.environ.get("TEMP", ""),
            os.environ.get("TMP", ""),
            os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Temp"),
            os.path.join(os.environ.get("LOCALAPPDATA", ""), "Temp"),
        ]
    else:
        temp_dirs = ["/tmp", "/var/tmp", os.path.expanduser("~/.cache")]

    total_deleted = 0
    total_failed  = 0
    total_size    = 0

    for temp_dir in temp_dirs:
        if not temp_dir or not os.path.exists(temp_dir):
            continue
        print(f"  {Fore.YELLOW}Scanning: {temp_dir}")
        try:
            entries = os.listdir(temp_dir)
        except:
            continue
        for entry in entries:
            entry_path = os.path.join(temp_dir, entry)
            try:
                if os.path.isfile(entry_path) or os.path.islink(entry_path):
                    size = os.path.getsize(entry_path)
                    os.remove(entry_path)
                    total_size += size
                    total_deleted += 1
                elif os.path.isdir(entry_path):
                    size = sum(
                        os.path.getsize(os.path.join(dp, f))
                        for dp, dn, fn in os.walk(entry_path)
                        for f in fn
                        if os.path.exists(os.path.join(dp, f))
                    )
                    shutil.rmtree(entry_path)
                    total_size += size
                    total_deleted += 1
            except:
                total_failed += 1

    size_mb = total_size / (1024 * 1024)
    print(f"\n  {Fore.GREEN}[\u2714] Deleted:  {total_deleted} items")
    print(f"  {Fore.GREEN}[\u2714] Freed:    {size_mb:.2f} MB")
    if total_failed > 0:
        print(f"  {Fore.YELLOW}[!] Skipped:  {total_failed} locked files (in use)")
    print(f"\n  {Fore.GREEN}Cargo hold cleared. Ship runs lighter now.")
    input(f"\n  {Fore.WHITE}Press Enter to return...")

def panic_button():
    clear()
    print(f"\n  {Fore.RED}{Style.BRIGHT}!!! PANIC BUTTON ACTIVATED !!!{Style.RESET_ALL}\n")
    time.sleep(0.3)

    if IS_WINDOWS:
        tasks = [
            ("Flushing DNS cache",   "ipconfig /flushdns"),
            ("Clearing temp files",  None),
            ("Wiping clipboard",     "cmd /c echo off | clip"),
        ]
    else:
        # FIX: xclip mit xsel als Fallback, damit es auf mehr Distros läuft
        tasks = [
            ("Flushing DNS cache",   "resolvectl flush-caches || systemd-resolve --flush-caches || true"),
            ("Clearing temp files",  None),
            ("Wiping clipboard",     "xclip -selection clipboard < /dev/null 2>/dev/null || xsel --clipboard --input < /dev/null 2>/dev/null || true"),
        ]

    for label, cmd in tasks:
        sys.stdout.write(f"  {Fore.WHITE}[ ] {label}...")
        sys.stdout.flush()
        try:
            if cmd:
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                temp_dirs = [os.environ.get("TEMP", "")] if IS_WINDOWS else ["/tmp"]
                for temp_dir in temp_dirs:
                    if temp_dir and os.path.exists(temp_dir):
                        for entry in os.listdir(temp_dir):
                            try:
                                p = os.path.join(temp_dir, entry)
                                if os.path.isfile(p): os.remove(p)
                                elif os.path.isdir(p): shutil.rmtree(p)
                            except: pass
            sys.stdout.write(f"\r  {Fore.GREEN}[\u2714] {label}\n")
        except:
            sys.stdout.write(f"\r  {Fore.RED}[!] {label} - failed\n")
        sys.stdout.flush()
        time.sleep(0.3)

    print(f"\n  {Fore.GREEN}All clear. Ghost mode activated.")
    print(f"  {Fore.YELLOW}Closing terminal in 3 seconds...")
    time.sleep(3)

    if IS_WINDOWS:
        subprocess.run(
            'taskkill /F /FI "WINDOWTITLE eq NET PIRATES*" /T',
            shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    sys.exit()

def process_killer():
    clear()
    print(f"\n  {Fore.CYAN}--- PROCESS KILLER (GAMING MODE) ---\n")

    if IS_WINDOWS:
        default_targets = [
            "chrome.exe", "msedge.exe", "firefox.exe", "opera.exe", "brave.exe",
            "DiscordUpdate.exe", "Update.exe",
            "OneDrive.exe", "OneDriveSetup.exe",
            "Teams.exe", "Slack.exe",
            "SearchIndexer.exe",
            "WallpaperEngine.exe", "wallpaper32.exe", "wallpaper64.exe",
        ]
    else:
        default_targets = ["chrome", "firefox", "brave", "discord", "slack", "steam"]

    config = get_config()
    extra = config.get("process_killer", {}).get("targets", [])
    targets = list(set(default_targets + extra))

    killed  = []
    skipped = []

    for proc in targets:
        if IS_WINDOWS:
            result = subprocess.run(
                f'tasklist /FI "IMAGENAME eq {proc}" /NH',
                shell=True, capture_output=True, text=True
            )
            if proc.lower() in result.stdout.lower():
                kill = subprocess.run(
                    f'taskkill /F /IM "{proc}" /T',
                    shell=True, capture_output=True, text=True
                )
                if kill.returncode == 0:
                    print(f"  {Fore.GREEN}[\u2714] Killed:   {proc}")
                    killed.append(proc)
                else:
                    print(f"  {Fore.RED}[!] Failed:   {proc}")
                    skipped.append(proc)
            else:
                print(f"  {Fore.WHITE}[-] Not running: {proc}")
        else:
            kill = subprocess.run(f'pkill -f {proc}', shell=True)
            if kill.returncode == 0:
                print(f"  {Fore.GREEN}[\u2714] Killed:   {proc}")
                killed.append(proc)
            else:
                print(f"  {Fore.WHITE}[-] Not running: {proc}")
        time.sleep(0.05)

    print(f"\n  {Fore.GREEN}Killed {len(killed)} processes. Ship is battle-ready.")
    if skipped:
        print(f"  {Fore.YELLOW}Could not kill {len(skipped)} (admin rights required?).")
    print(f"\n  {Fore.CYAN}Tip: Add custom targets under 'process_killer.targets' in config.json")
    input(f"\n  {Fore.WHITE}Press Enter to return...")

def latency_checker():
    clear()
    print(f"\n  {Fore.CYAN}--- LATENCY CHECKER ---\n")

    servers = [
        ("Valve / Steam",    "208.64.200.0"),
        ("Riot Games",       "162.249.73.1"),
        ("Blizzard",         "24.105.62.129"),
        ("GitHub",           "140.82.112.4"),
        ("AWS Frankfurt",    "52.28.0.0"),
        ("Vercel",           "76.76.21.21"),
        ("Google DNS",       "8.8.8.8"),
        ("Cloudflare DNS",   "1.1.1.1"),
    ]

    print(f"  {Fore.WHITE}{'Service':<20} {'IP':<18} {'Latency':<12} Status")
    print(f"  {Fore.WHITE}" + "-" * 60)

    for name, ip in servers:
        try:
            if IS_WINDOWS:
                # Windows: -w in Millisekunden
                cmd = ['ping', '-n', '1', '-w', '1000', ip]
            else:
                # Linux/Mac: -W in Sekunden
                cmd = ['ping', '-c', '1', '-W', '1', ip]

            output = subprocess.check_output(
                cmd, stderr=subprocess.STDOUT,
                universal_newlines=True, timeout=3
            )

            if "Zeit=" in output:
                ms = output.split("Zeit=")[1].split("ms")[0].strip()
            elif "time=" in output:
                ms = output.split("time=")[1].split("ms")[0].strip()
            else:
                ms = None

            if ms:
                # FIX: split(".") für Linux-Floats wie "12.4ms", replace("<") für Windows "<1ms"
                ms_int = int(float(ms.replace("<", "")))
                color = Fore.GREEN if ms_int < 50 else (Fore.YELLOW if ms_int < 100 else Fore.RED)
                status = "EXCELLENT" if ms_int < 50 else ("GOOD" if ms_int < 100 else "HIGH")
                print(f"  {Fore.WHITE}{name:<20} {ip:<18} {color}{ms_int}ms{'':<8}{Fore.WHITE} {status}")
            else:
                print(f"  {Fore.WHITE}{name:<20} {ip:<18} {Fore.RED}TIMEOUT     UNREACHABLE")
        except:
            print(f"  {Fore.WHITE}{name:<20} {ip:<18} {Fore.RED}OFFLINE     UNREACHABLE")
        time.sleep(0.1)

    print(f"\n  {Fore.GREEN}Horizon scanned. Navigate accordingly, Captain.")
    input(f"\n  {Fore.WHITE}Press Enter to return...")

def ip_vpn_check():
    clear()
    print(f"\n  {Fore.CYAN}--- PUBLIC IP & VPN CHECK ---\n")

    vpn_keywords = ["vpn", "proxy", "hosting", "datacenter", "cloud", "server",
                    "digitalocean", "linode", "vultr", "hetzner", "ovh", "aws",
                    "azure", "google cloud", "mullvad", "nordvpn", "expressvpn"]

    print(f"  {Fore.WHITE}[ ] Fetching public IP...")
    sys.stdout.flush()

    try:
        req = urllib.request.Request("https://ipinfo.io/json", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode())

        ip       = data.get("ip", "Unknown")
        city     = data.get("city", "Unknown")
        region   = data.get("region", "Unknown")
        country  = data.get("country", "Unknown")
        org      = data.get("org", "Unknown")
        timezone = data.get("timezone", "Unknown")

        vpn_detected = any(kw in org.lower() for kw in vpn_keywords)

        print(f"\r  {Fore.GREEN}[\u2714] Data received\n")
        print(f"  {Fore.WHITE}{'IP Address:':<18} {Fore.GREEN}{ip}")
        print(f"  {Fore.WHITE}{'Location:':<18} {Fore.WHITE}{city}, {region}, {country}")
        print(f"  {Fore.WHITE}{'Organization:':<18} {Fore.WHITE}{org}")
        print(f"  {Fore.WHITE}{'Timezone:':<18} {Fore.WHITE}{timezone}\n")

        if vpn_detected:
            print(f"  {Fore.GREEN}{Style.BRIGHT}[\u2714] VPN / Proxy DETECTED \u2014 You are masked, Pirate.")
        else:
            print(f"  {Fore.YELLOW}[!] No VPN detected \u2014 Your real IP is exposed.")
            print(f"  {Fore.WHITE}    Consider activating a VPN for sensitive operations.")

    except Exception as e:
        print(f"\r  {Fore.RED}[!] Could not reach ipinfo.io: {e}")
        print(f"  {Fore.YELLOW}    Check your internet connection.")

    input(f"\n  {Fore.WHITE}Press Enter to return...")

def port_listener():
    clear()
    print(f"\n  {Fore.CYAN}--- PORT LISTENER ---\n")
    print(f"  {Fore.WHITE}Scanning active connections...\n")

    cmd = "netstat -ano" if IS_WINDOWS else "ss -antp 2>/dev/null || netstat -antp 2>/dev/null"

    try:
        result = subprocess.check_output(cmd, shell=True, universal_newlines=True, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"  {Fore.RED}[!] Failed to run network scan: {e}")
        input(f"\n  {Fore.WHITE}Press Enter to return...")
        return

    if IS_WINDOWS:
        # Windows: strukturierte Ausgabe mit PID-Mapping
        pid_map = {}
        try:
            tasklist = subprocess.check_output(
                "tasklist /NH /FO CSV", shell=True, universal_newlines=True, stderr=subprocess.DEVNULL
            )
            for line in tasklist.strip().splitlines():
                parts = line.replace('"', '').split(',')
                if len(parts) >= 2:
                    pid_map[parts[1]] = parts[0]
        except:
            pass

        lines = result.strip().splitlines()
        listening = []
        established = []

        for line in lines[4:]:
            parts = line.split()
            if len(parts) < 5:
                continue
            proto, local, remote, state, pid = parts[0], parts[1], parts[2], parts[3], parts[4]
            proc_name = pid_map.get(pid, "Unknown")
            if state == "LISTENING":
                listening.append((proto, local, pid, proc_name))
            elif state == "ESTABLISHED":
                established.append((proto, local, remote, pid, proc_name))

        print(f"  {Fore.YELLOW}{Style.BRIGHT}LISTENING PORTS ({len(listening)} found)")
        print(f"  {Fore.WHITE}" + "-" * 60)
        print(f"  {Fore.WHITE}{'Proto':<8} {'Local Address':<28} {'PID':<8} Process")
        print(f"  {Fore.WHITE}" + "-" * 60)
        for proto, local, pid, proc in listening[:25]:
            print(f"  {Fore.GREEN}{proto:<8}{Fore.WHITE} {local:<28} {Fore.YELLOW}{pid:<8}{Fore.WHITE} {proc}")
        if len(listening) > 25:
            print(f"  {Fore.WHITE}... and {len(listening) - 25} more")

        print()
        print(f"  {Fore.YELLOW}{Style.BRIGHT}ESTABLISHED CONNECTIONS ({len(established)} found, showing top 15)")
        print(f"  {Fore.WHITE}" + "-" * 70)
        print(f"  {Fore.WHITE}{'Proto':<8} {'Local':<22} {'Remote':<22} {'PID':<8} Process")
        print(f"  {Fore.WHITE}" + "-" * 70)
        for proto, local, remote, pid, proc in established[:15]:
            print(f"  {Fore.CYAN}{proto:<8}{Fore.WHITE} {local:<22} {remote:<22} {Fore.YELLOW}{pid:<8}{Fore.WHITE} {proc}")
        if len(established) > 15:
            print(f"  {Fore.WHITE}... and {len(established) - 15} more")
    else:
        # Linux: Raw-Ausgabe
        lines = result.strip().splitlines()
        print(f"  {Fore.YELLOW}{Style.BRIGHT}ACTIVE NETWORK CONNECTIONS")
        print(f"  {Fore.WHITE}" + "-" * 70)
        for line in lines[:30]:
            print(f"  {Fore.WHITE}{line}")
        if len(lines) > 30:
            print(f"  {Fore.WHITE}... and {len(lines) - 30} more connections.")

    print(f"\n  {Fore.GREEN}Network mapped. Know your waters, Captain.")
    input(f"\n  {Fore.WHITE}Press Enter to return...")

# ── Main Menu ─────────────────────────────────────────────────
def main_menu():
    first_run = True
    while True:
        clear()

        menu_items = [
            (f"[1] {get_text('menu_pulse')}",   Fore.GREEN),
            (f"[2] {get_text('menu_code')}",    Fore.GREEN),
            (f"[3] {get_text('menu_dns')}",     Fore.GREEN),
            (f"[4] {get_text('menu_temp')}",    Fore.GREEN),
            (f"[5] {get_text('menu_killer')}",  Fore.GREEN),
            (f"[6] {get_text('menu_latency')}",  Fore.GREEN),
            (f"[7] {get_text('menu_ip')}",      Fore.GREEN),
            (f"[P] {get_text('menu_ports')}",   Fore.GREEN),
        ]

        print(f"\n  {Fore.WHITE}" + "-" * 45)
        if first_run:
            typewrite(f"  {get_text('welcome')}", Fore.GREEN, delay=0.04)
            first_run = False
        else:
            print(f"  {Fore.GREEN}{get_text('welcome')}")
        print(f"  {Fore.WHITE}" + "-" * 45)

        for item, color in menu_items:
            print(f"  {color}{item}")

        print(f"  {Fore.WHITE}" + "-" * 45)
        print(f"  {Fore.RED}[!] {get_text('menu_panic')}")
        print(f"  {Fore.RED}[0] {get_text('menu_exit')}")
        print(f"  {Fore.WHITE}" + "-" * 45)

        choice = input(f"\n  {Fore.GREEN}{get_text('input')}").strip().lower()

        if   choice == "1": network_pulse()
        elif choice == "2": honor_code()
        elif choice == "3": dns_flush()
        elif choice == "4": temp_purge()
        elif choice == "5": process_killer()
        elif choice == "6": latency_checker()
        elif choice == "7": ip_vpn_check()
        elif choice == "p": port_listener()
        elif choice == "!": panic_button()
        elif choice == "0":
            print(f"\n  {Fore.RED}{get_text('exit_msg')}")
            time.sleep(1.2)
            sys.exit()

# --- MAIN ---

if __name__ == "__main__":
    if IS_WINDOWS:
        os.system('title NET PIRATES')
        os.system("powershell -command \"$wshell = New-Object -ComObject WScript.Shell; $wshell.SendKeys('{F11}')\"")

    try:
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        login_screen()
        dramatic_loading()
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        deployment_menu()
        main_menu()
    except KeyboardInterrupt:
        sys.stdout.write("\033[?25h")
        sys.exit()
    except Exception as e:
        sys.stdout.write("\033[?25h")
        print(f"\n{Back.RED}{Fore.WHITE}{Style.BRIGHT} FATAL SYSTEM CRASH: {e} {Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to close...")
