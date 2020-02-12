"""This program deepfries every image in the default resource pack."""


from PIL import Image, ImageEnhance
import os


default_settings = """# Name of the pack (folder) you're using as input.
input_pack = 'Default'

# Should the input pack be overwritten (True) or a new folder made (False)?
overwrite_input = False

# Name of the pack (folder) to create. Ignored if overwrite_input = True
output_pack = 'Deepfried'"""

with open('settings.txt', 'r') as data:
    try:
        settings = data.read()
        exec(settings)
    except Exception:
        with open('settings.txt', 'w') as data:
            data.write(default_settings)
        with open('settings.txt', 'r') as data:
            settings = data.read()
            exec(settings)

if ('input_pack' in globals() and 'overwrite' in globals() and
        'output_pack' in globals()):
    pass
else:
    with open('settings.txt', 'w') as data:
        data.write(default_settings)
    with open('settings.txt', 'r') as data:
        settings = data.read()
        exec(settings)


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
           'models/armor/',
           'painting/',
           'particle/']

print("Working...")
if not os.path.isdir(out_dir + textures):
    os.mkdir(out_dir + textures)
for subdir in subdirs:
    for file in os.listdir(in_dir + textures + subdir):
        try:
            img = Image.open(in_dir + textures + subdir + file)
            img = img.convert("RGBA")
            enh = ImageEnhance.Color(img)
            enh.enhance(255).save(out_dir + textures + subdir + file)
        except IOError:
            pass
print("Done!")
