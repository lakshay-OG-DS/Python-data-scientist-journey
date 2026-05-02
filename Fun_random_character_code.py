import random

list_e = ["dragon","knight","king","assassian","ninja"]

entity = (random.choice(list_e))

list_s = ["god","human","barbarian","dbz warrior","admiral","infinity"]

strength = (random.choice(list_s))

list_sp = ["normal_human_speed", "athlete_level_speed",   "peak_human_speed" , "enhanced_human_speed",  "superhuman_speed","hypersonic_speed",
    "light_speed",
    "faster_than_light",
    "god_speed",
    "teleportation",
    "instant_transmission",
    "time_manipulation_speed",
    "quantum_phase_shift",
    "dimensional_travel",
    "infinite_speed"]
   
speed = (random.choice(list_sp))

weakness_types = [
    "normal_human_fatigue",
    "low_stamina_limit",
    "energy_drain",
    "muscle_exhaustion",
    "mental_fatigue",
    "cooldown_requirement",
    "power_instability",
    "overheating",
    "time_limit_usage",
    "recoil_damage",
    "dependency_on_energy_source",
    "environmental_weakness",
    "speed_strain",
    "dimensional_instability",
    "complete_exhaustion"
]

weakness = (random.choice(weakness_types))

stamina_types = [
    "low_stamina",
    "average_human_stamina",
    "trained_athlete_stamina",
    "enhanced_stamina",
    "high_endurance",
    "superhuman_stamina",
    "regenerative_stamina",
    "limitless_stamina",
    "energy_absorption",
    "adaptive_stamina",
    "infinite_stamina",
    "divine_stamina",
    "self_sustaining_energy",
    "time_independent_stamina",
    "cosmic_level_endurance"
]

stamina = (random.choice(stamina_types))
print(f'''you are a {entity} with strength {strength}
 and speed {speed} with {stamina}
 but your weakness is {weakness} ''')

