converter_data = dict(idr=9000, jpy=300, cad=400)

command = ""
while command != "quit":
    command, currency, value = input(">").split()

    if command.upper() == "KURS":
        for dict_key, dict_value in converter_data.items():
            if dict_key == currency.lower():
                converter_data[dict_key] = value

            elif dict_key != currency.lower():
                pass
            else:
                converter_data[currency] = value

    elif command.upper() == "CONV":
        for dict_key, dict_value in converter_data.items():
            if dict_key == currency.lower():
                print(f"USD {value / dict_value}")

            elif currency.lower() not in converter_data:
                converter_data[currency.lower()] = value
                print("data telah ditambahkan")
                break
