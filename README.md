# python_gui_apps
GUI apps made with Python

## Dependancies
You'll need to install Kivy first. The following should do it (on Linux Mint or Ubuntu, anyway). 
If you have any issues, go to [Kivy's site](https://kivy.org/doc/stable/gettingstarted/installation.html) 
for more help with installation

```bash
python3 -m pip install --upgrade pip setuptools virtualenv
pip3 install --upgrade pip
cd ~  # or wherever you want to install the virtual environment
python3 -m virtualenv kivy_venv
source kivy_venv/bin/activate
python3 -m pip install "kivy[base]" kivy_examples
```

