# Breeze Dark Cursor

Dark version of the default KDE Breeze cursor.

## I. Installation

Just copy the folder Breeze_Dark into your local icon folder:

### With Dolphin:

1. Right click on the downloaded `tar.gz` file. `Extract` -> `Extract archive here`.
2. Copy the extracted directory `Breeze_Dark`
3. Go to `~/.local/share/icons`. (`~` is the same as `/home/your_username/`)
4. Paste the folder.

### B. From the command line:

```command
$ tar xzf Breeze_dark_v1.0.tar.gz
$ cp -r Breeze_Dark ~/.local/share/icons/
```
## II. Set the theme

Then simply select the theme in the `Cursors` sections of the System settings:

1. Go to `System settings` -> `Appearance` -> `Cursors`. Select **Breeze Dark**.
2. Restart the system

## Build

Building the Bridge Icon set from the Inkscape SVG:

1. Ensure you have inkscape and xcursorgen installed.
2. Run build.sh in a terminal. The script may take several minutes.
3. Copy the folder created by the script (should match the name of the theme)
   to your cursors folder.

No trimming will have been done to the cursors, and X11 *may* give you
split-second glitches when switching cursors making them appear to 'jump'
for an instant. To remedy this, you will need to open any auto-generated in
gimp and re-export when with the “trim whitespace” option checked. I do not
beleive it impacts all versions of X, or Wayland.

You will need the “X11 Mouse Cursor (XMC)” plugin for GIMP installed to trim
the cursors if you choose to do so.

---

**This is just a simple modification of the original theme from grey to black color.
All credits to the original creators.**
