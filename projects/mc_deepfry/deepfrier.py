"""This program deepfries every image in the provided resource pack."""

try:
    from PIL import Image, ImageEnhance
except ImportError:
    print("Missing required module 'Pillow'")
    print("python3.7 -m pip install Pillow")

import os

from random import choice

import time
start_time = time.time()


# ============================= Load settings.txt =============================
print("Attempting to load settings...")

# These are the default settings used by this script.
default_settings = """# Name of the pack (folder) you're using as input.
input_pack = 'Default'

# Should a new pack be created? If false, the input pack will be overwritten
new_pack = True

# Name of the pack (folder) to create. Ignored if new_pack = False
new_pack_name = 'Deepfried'

# NOTE: This text file is run as Python code by the script, so be careful with
# what you write in here. There are plenty of checks to make sure that the
# three settings listed above are correct, but there's no such thing to ensure
# you don't write additional code. Only add new code if you fully understand
# what you're doing."""

# Create empty vars to avoid linting errors & check existence
input_pack = None
new_pack = None
new_pack_name = None

# Try and read settings.txt; if an error happens, restore to default.
try:
    with open('settings.txt', 'r') as data:
        settings = data.read()
        exec(settings)
except Exception:
    print("An exception occured, so settings.txt is being reset.")
    with open('settings.txt', 'w') as data:
        data.write(default_settings)
    print("The script will now abort so you can change your settings.")
    quit()

# If no errors occur, make sure that all the required variables exist
if (input_pack is not None and new_pack is not None and
        new_pack_name is not None):
    # Ensure each variable is the correct type
    if (type(input_pack) == str and type(new_pack) == bool and
            type(new_pack_name) == str):
        pass
    else:
        print("One or more variables was the wrong type, so settings.txt is",
              "being reset.")
        with open('settings.txt', 'w') as data:
            data.write(default_settings)
        print("The script will now abort so you can change your settings.")
        quit()
else:
    print("One or more variables was missing, so settings.txt is being reset.")
    with open('settings.txt', 'w') as data:
        data.write(default_settings)
    print("The script will now abort so you can change your settings.")
    quit()

print("Settings loaded successfully!")
# =============================================================================


# ========================= Define texture locations ==========================
textures = '/assets/minecraft/textures/'
subdirs = ['block/',
           'colormap/',
           'effect/',

           'entity/',
           'entity/armorstand/',
           'entity/banner/',
           'entity/bear/',
           'entity/bed/',
           'entity/bell/',
           'entity/boat/',
           'entity/cat/',
           'entity/chest/',
           'entity/conduit/',
           'entity/cow/',
           'entity/creeper/',
           'entity/end_crystal/',
           'entity/enderdragon/',
           'entity/enderman/',
           'entity/fish/',
           'entity/fox/',
           'entity/ghast/',
           'entity/horse/',
           'entity/illager/',
           'entity/llama/',
           'entity/panda/',
           'entity/parrot/',
           'entity/pig/',
           'entity/projectiles/',
           'entity/rabbit/',
           'entity/sheep/',
           'entity/shield/',
           'entity/shulker/',
           'entity/signs/',
           'entity/skeleton/',
           'entity/slime/',
           'entity/spider/',
           'entity/turtle/',
           'entity/villager/',
           'entity/wither/',
           'entity/wolf/',
           'entity/zombie/',
           'entity/zombie_villager/',

           'environment/',

           'gui/',
           'gui/advancements/',
           'gui/container/',
           'gui/presets/',
           'gui/title/',

           'item/',
           'map/',
           'misc/',
           'mob_effect/',

           'models/',
           'models/armor/',

           'painting/',
           'particle/']
# =============================================================================


# ================== Create new resource pack if applicable ===================
if new_pack is True:
    print("Creating a new resource pack...")
    # main folder
    if not os.path.isdir(new_pack_name):
        os.mkdir(new_pack_name)
    # assets
    if not os.path.isdir(new_pack_name + "/assets/"):
        os.mkdir(new_pack_name + "/assets/")
    # minecraft
    if not os.path.isdir(new_pack_name + "/assets/minecraft/"):
        os.mkdir(new_pack_name + "/assets/minecraft/")
    # textures
    if not os.path.isdir(new_pack_name + textures):
        os.mkdir(new_pack_name + textures)
    for subdir in subdirs:
        if not os.path.isdir(new_pack_name + textures + subdir):
            os.mkdir(new_pack_name + textures + subdir)

    mcmeta = """{
   "pack":{
      "pack_format":5,
      "description":"\u00A7cD e e p f r i e d"
   }
}"""
    with open(new_pack_name + "/pack.mcmeta", 'w') as data:
        data.write(mcmeta)

    print(f"Created new pack '{new_pack_name}'")
# =============================================================================


# ========================== Do the image processing ==========================
print("Creating new textures...")

all_blocks = []

for subdir in subdirs:
    current_dir = textures + subdir
    try:
        for file in os.listdir(input_pack + current_dir):
            if subdir == "block/":
                if file.endswith('.png'):
                    all_blocks.append(file)
            try:
                img = Image.open(input_pack + current_dir + file)
                img = img.convert("RGBA")
                enh = ImageEnhance.Color(img)
                if new_pack is True:
                    enh.enhance(255).save(new_pack_name + current_dir + file)
                else:
                    enh.enhance(255).save(input_pack + current_dir + file)
            except IOError:
                pass
    except FileNotFoundError:
        print("ERROR: Either the pack specified in settings.txt doesn't",
              "exist, or some folders are missing.")
        print("Check for typo in the input_pack setting. (Case sensitive!)")
        print("The script will now abort.")
        quit()

if new_pack is True:
    pack_icon = choice(all_blocks)
    img = Image.open(new_pack_name + textures + "block/" + pack_icon)
    img.resize((128, 128), resample=0).save(new_pack_name + "/pack.png")
else:
    img = Image.open(input_pack + "/pack.png")
    img = img.convert("RGBA")
    enh = ImageEnhance.Color(img)
    enh.enhance(255).save(input_pack + "/pack.png")

end_time = time.time()
duration = end_time - start_time
duration = format(duration, ".2f")
print(f"All done! Finished in {duration} secs.")
# ==================================== END ====================================
