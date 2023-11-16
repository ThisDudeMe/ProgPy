import random
import pyperclip

column_data_lists = [('Place:',
  ['City',
   'Forest',
   'Beach',
   'Desert',
   'Mountains',
   'Village',
   'Island',
   'Jungle',
   'Ocean',
   'Space',
   'River',
   'Castle',
   'Farm',
   'School',
   'Museum',
   'Temple',
   'Factory',
   'Mansion',
   'Cave',
   'Park',
   'Library',
   'Restaurant',
   'Harbor',
   'Stadium',
   'Garden',
   'Hospital',
   'Office',
   'Aquarium',
   'Zoo',
   'Airport',
   'Station',
   'Market',
   'Theater',
   'University',
   'Cathedral',
   'Volcano',
   'Glacier',
   'Prairie',
   'Swamp',
   'Valley',
   'Canyon',
   'Alley',
   'Laboratory',
   'Salon',
   'Gym',
   'Bakery',
   'Plaza',
   'Vineyard',
   'Gallery',
   'Rooftop']),
 ('Style:',
  ['Vintage',
   'Modern',
   'Rustic',
   'Futuristic',
   'Minimalist',
   'Gothic',
   'Baroque',
   'Art Deco',
   'Industrial',
   'Bohemian',
   'Surrealist',
   'Abstract',
   'Pop Art',
   'Cubist',
   'Expressionist',
   'Impressionist',
   'Steampunk',
   'Retro',
   'Mediterranean',
   'Oriental',
   'Nordic',
   'Victorian',
   'Bauhaus',
   'Rococo',
   'Classical',
   'Byzantine',
   'Avant-Garde',
   'Tribal',
   'Coastal',
   'Shabby Chic',
   'Eclectic',
   'Zen',
   'Art Nouveau',
   'Contemporary',
   'High-Tech',
   'Organic',
   'Psychedelic',
   'Minimal',
   'Traditional',
   'Cyberpunk',
   'Romantic',
   'Fantasy',
   'Realist',
   'Geometric',
   'Neoclassical',
   'Graffiti',
   'Opulent',
   'Monochrome',
   'Conceptual',
   'Postmodern']),
 ('Resolution: ', ['4K']),
 ('Subject: ',
  ['Person',
   'Cat',
   'Dog',
   'Alien',
   'Fungoid',
   'Robot',
   'Bird',
   'Fish',
   'Dragon',
   'Unicorn',
   'Ghost',
   'Vampire',
   'Mermaid',
   'Zombie',
   'Dinosaur',
   'Insect',
   'Wizard',
   'Witch',
   'Fairy',
   'Monster',
   'Gnome',
   'Elf',
   'Tiger',
   'Bear',
   'Lion',
   'Elephant',
   'Horse',
   'Wolf',
   'Snake',
   'Gorilla',
   'Octopus',
   'Butterfly',
   'Angel',
   'Demon',
   'Tree Spirit',
   'Cyclops',
   'Yeti',
   'Sphinx',
   'Centaur',
   'Griffin',
   'Werewolf',
   'Phoenix',
   'Chimera',
   'Troll',
   'Kraken',
   'Gargoyle',
   'Minotaur',
   'Leprechaun',
   'Giant',
   'Nymph']),
 ('Action :',
  ['Running',
   'Jumping',
   'Swimming',
   'Dancing',
   'Reading',
   'Writing',
   'Cooking',
   'Painting',
   'Singing',
   'Playing (a musical instrument)',
   'Hiking',
   'Skiing',
   'Fishing',
   'Gardening',
   'Building',
   'Repairing',
   'Teaching',
   'Studying',
   'Photographing',
   'Drawing',
   'Driving',
   'Flying (a plane)',
   'Sailing',
   'Surfing',
   'Climbing',
   'Jogging',
   'Cycling',
   'Yoga',
   'Meditating',
   'Boxing',
   'Wrestling',
   'Shopping',
   'Baking',
   'Knitting',
   'Crafting',
   'Decorating',
   'Programming',
   'Gaming',
   'Exploring',
   'Traveling',
   'Camping',
   'Kayaking',
   'Rowing',
   'Skateboarding',
   'Snowboarding',
   'Scuba diving',
   'Horseback riding',
   'Archery',
   'Fencing',
   'Gymnastics'])]

def select_and_format_items(column_data_lists):
    selected_items = {}
    for column_name, items in column_data_lists:
        selected_item = random.choice(items)
        selected_items[column_name] = selected_item
    return selected_items

# Using the function to select items and prepare a message
selected_items = select_and_format_items(column_data_lists)
message = "Randomly selected items:\n" + "\n".join([f"{key}: {value}" for key, value in selected_items.items()])

# Copying the message to clipboard
pyperclip.copy(message)
print("Message copied to clipboard. You can now paste it.")