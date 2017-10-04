from scipy.constants import proton_mass, electron_mass, electron_volt, speed_of_light

def kg2ev(mass_in_kg):
    return mass_in_kg * speed_of_light**2/electron_volt


mass = {
    'proton': kg2ev(proton_mass),
    'electron': kg2ev(electron_mass),
    'positron': kg2ev(electron_mass),
}


def beam_rigidity(species, kinetic_energy):
    rest_mass = mass[species.lower()]
    kinetic_energy *= 1e6 # MeV --> eV

    total_energy = rest_mass + kinetic_energy
    momentum = (total_energy**2 - rest_mass**2)**0.5

    return momentum / speed_of_light


if __name__ == '__main__':
    print(beam_rigidity('proton', 10.0))
    print(beam_rigidity('electron', 10.0))
    print(beam_rigidity('positron', 10.0))
