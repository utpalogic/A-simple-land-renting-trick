def read_land_data(filename):
    """
    Read land data from a file and parse it into a dictionary.

    Args:
        filename (str): Name of the file containing land data.

    Returns:
        dict: A dictionary containing land information parsed from the file.

    """
    land_data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                land_info = line.strip().split(', ')
                if len(land_info) == 6:
                    land_data[land_info[0]] = {
                        'city': land_info[1],
                        'direction': land_info[2],
                        'area': land_info[3],
                        'price': int(land_info[4]),  # Convert to int
                        'status': land_info[5],
                        'last_customer': None,
                        'rent_duration': None,
                        'total_amount': None,
                        'rent_start_date': None
                    }
                else:
                    print("Error: Invalid format in line '{}'. Skipping.".format(line.strip()))
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)
    except Exception as e:
        print("Error reading file: {}".format(e))
        exit(1)
    return land_data
