import Modes.convert as convert 
import Modes

_CONVERSIONS = {
    "1 = in -> cm": convert.conversion,
    "2 = cm -> in": convert.conversion,
    "3 = ft -> m": convert.conversion,
    "4 = m -> ft": convert.conversion,
    "5 = yd -> m": convert.conversion,
    "6 = m -> yd": convert.conversion,
    "7 = mi -> km": convert.conversion,
    "8 = km -> mi": convert.conversion,
    "9 = nmi -> m": convert.conversion,
    "10 = m -> nmi": convert.conversion,
    "11 = ac -> m^2": convert.conversion,
    "12 = m^2 -> ac": convert.conversion,
    "13 = gal(U.S.) -> L": convert.conversion,
    "14 = L -> gal(U.S.)": convert.conversion,
    "15 =  gal(UK) -> L": convert.conversion,
    "16 = L -> gal(UK)": convert.conversion,
    "17 = pc -> km": convert.conversion,
    "18 = km -> pc": convert.conversion,
    "19 = km/h -> m/s": convert.conversion,
    "20 = m/s -> km/h": convert.conversion,
    "21 = oz -> g": convert.conversion,
    "22 = g -> oz": convert.conversion,
    "23 = lb -> kg": convert.conversion,
    "24 = kg -> lb": convert.conversion,
    "25 = atm -> Pa": convert.conversion,
    "26 = Pa -> atm": convert.conversion,
    "27 = mmHg -> Pa": convert.conversion,
    "28 = Pa -> mmHg": convert.conversion,
    "29 = hp -> kW": convert.conversion,
    "30 = kW -> hp": convert.conversion,
    "31 = kgf/cm^2 -> Pa": convert.conversion,
    "32 = Pa -> kgf/cm^2": convert.conversion,
    "33 = kgf -> N": convert.conversion,
    "34 = N -> kgf": convert.conversion,
    "35 = lbf/in^2 -> kPa": convert.conversion,
    "36 = kPa -> lbf/in^2": convert.conversion,
    "37 = °F -> °C": convert.conversion,
    "38 = °C -> °F": convert.conversion,
    "39 = J -> cal": convert.conversion,
    "40 = cal -> J": convert.conversion,
}

def evaluate_mode(mode):
    mode = input("select mode: ").lower()
    if mode == "bases":
        form = input("Enter base(binary, octal,  hexadecimal, other): ").lower()
        if form == "binary":
            ...
        elif form == "octal":
            ...
        elif form == "hexadecimal":
            ...
        elif form == "other":
            ...
    elif mode == "central_tendency":
        return "Central Tendency mode activated. You can now calculate mean, median, and mode."
    elif mode == "statistics":
        ...
    elif mode == "complex":
        return "Complex Numbers mode activated. You can now perform operations with complex numbers."
    elif mode == "convert":
        print("Available conversions: ")
        for conversion in _CONVERSIONS:
            print(conversion)
        num = int(input("Enter the number corresponding to the conversion you want to perform: "))
        Modes.convert.conversion(num)
        
    elif mode == "equations":
        return "Equations mode activated. You can now solve equations."
    elif mode == "matrix":
        return "Matrix Operations mode activated. You can now perform matrix operations."
    elif mode == "vector":
        return "Vector Operations mode activated. You can now perform vector operations."
    else:
        raise ValueError(f"Unknown mode: '{mode}'")