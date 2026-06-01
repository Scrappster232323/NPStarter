# 🏴‍☠️ NET PIRATES – Central Command Terminal

> A customizable startup launcher that replaces your cluttered autostart with clean, powerful presets.

A lightweight but powerful open-source tool designed to streamline your workflow.
Instead of launching multiple apps on startup, this terminal acts as your **central command hub**.

---

## ⚡ Quick Start

1. Run `Setup.bat`
2. Edit `config.json`
3. Add your apps and presets
4. Launch `NPStarter.bat`

Done.

---

## ⚙️ Concept

Keep your system clean and efficient:

* Remove unnecessary apps from autostart
* Add this tool instead
* Launch everything through **custom presets**

At startup, the terminal opens and lets you choose exactly what you need.

### Example Presets

* 💻 **Development** → Browser, Discord, VS Code
* 🎮 **Gaming** → Steam, Discord, Spotify
* 🔍 **Research / OSINT** → Browser, VM, analysis tools

Fully customizable — your workflow, your rules.

---

## 🚀 Features

* **Preset-based App Launching**
  Start multiple applications instantly with one selection

* **Startup Optimization**
  Replace messy autostart setups with a single clean entry

* **Immersive Terminal UI**
  Fullscreen ASCII interface with animations

* **Multilingual Support**
  Switch between English and German via config

* **Modular Foundation**
  Built as a base for a future automation & productivity assistant

---

## 🔧 Configuration (`config.json`)

Setup is simple and flexible.

### 1. Define your apps

Under `"apps"`:

```json
"apps": {
    "VSC": "C:\\Path\\To\\VSCode.exe",
    "Discord": "C:\\Path\\To\\Discord.exe",
    "Steam": "C:\\Path\\To\\Steam.exe"
}
```

* Left side = **ID (name you choose)**
* Right side = **path to the .exe**

👉 You can add **unlimited apps**

---

### 2. Create presets

Under `"presets"`:

```json
"presets": {
    "1": {
        "name": "Development",
        "apps": ["VSC", "Discord"]
    },
    "2": {
        "name": "Gaming",
        "apps": ["Steam", "Discord"]
    }
}
```

* `"apps"` uses the IDs from above
* `"name"` is what shows in the menu

👉 You can:

* Rename presets
* Add unlimited presets
* Combine apps however you want

---

### 💡 Notes

* If something doesn’t start → check the path
* IDs must match exactly

---

## 🛠 Installation & Setup

### Requirements

All dependencies are installed automatically via:

```
Setup.bat
```

---

### Enable Autostart (Windows)

1. Press `Win + R`
2. Type:

   ```
   shell:startup
   ```
3. Create a shortcut to `NPStarter.bat`
4. Set it to **Run Maximized**

---

## 🔮 Future Plans

* 📂 Batch file converter (e.g. MP4 → MP3)
* 🔴 Close all apps from a preset
* 🧠 Smart assistant features
* 🛠️ Tools for developers, researchers, and gamers

Goal: a **compact but powerful digital assistant**.

---

## 🏴‍☠️ Philosophy

Built under the **Net Pirates** banner.

* Purpose over ego
* Tools that empower — not harm
* Support over exploitation

The full **Honor Code** is available inside the application.

---

## 🆘 Support

Having issues?

👉 Discord: **Taxy2507**

---

## ⚠️ Disclaimer

This tool is intended for **productivity and workflow optimization only**.
Any misuse is not supported.

---

## 🏁 Final Words

**"Real Action. Online and Off."**

Welcome aboard.
