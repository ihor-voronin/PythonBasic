d = {
    "apple": ["malum", "pomum", "popula"],
    "fruit": ["baca", "bacca", "popum"],
    "punishment": ["malum", "multa"],
}

d2: dict = {}
for k, v in d.items():
    for el in v:
        # d2[el] = k
        if d2.get(el, None) is not None:
            d2[el] = d2[el].append(k)
        else:
            d2[el] = [k]

print(d2)
