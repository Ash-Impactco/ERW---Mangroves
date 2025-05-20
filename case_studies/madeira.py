# Madeira Basalt Case Study Prototype

def madeira_basalt_mass(area_km2=740, depth_m=10, density_kgm3=2900):
    volume_m3 = area_km2 * 1e6 * depth_m
    mass_kg = volume_m3 * density_kgm3
    mass_Mt = mass_kg / 1e9
    return mass_Mt

if __name__ == "__main__":
    print("Estimated Basalt Mass in Madeira (Mt):", madeira_basalt_mass()) 