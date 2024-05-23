from write import generate_invoice
from datetime import datetime

def rent_land(land_data, customer_name, bill=[]):
    """
    Rent a land based on provided information.

    Args:
        land_data (dict): Dictionary containing land information.
        customer_name (str): Name of the customer renting the land.
        bill (list, optional): List to store billing information. Defaults to [].

    Returns:
        tuple: A tuple containing a boolean indicating success or failure, and an invoice if successful.

    """
    try:
        kitta_number = input("Enter Kitta Number of land to rent: ")
        rent_duration = int(input("Enter rent duration (in months): "))
        land_info = land_data[kitta_number]
        if land_info['status'].lower() == 'available':
            area = int(land_info['area'])
            price = int(land_info['price'])
            total_amount = price * rent_duration
            land_info['status'] = 'Not Available'
            land_info['rent_duration'] = rent_duration
            land_info['total_amount'] = total_amount
            land_info['last_customer'] = customer_name
            land_info['rent_start_date'] = datetime.now()

            d = ['rent', dict(land_info), customer_name, kitta_number, rent_duration, price, total_amount]
            bill.append(d)
            
            while True:
                rent_again = input("Do you want to rent another land? Yes or No: ").lower()
                if rent_again == 'yes':
                    continue_rent = rent_land(land_data, customer_name, bill=bill)
                    if not continue_rent[0]:
                        return continue_rent
                elif rent_again == 'no':
                    break
                else:
                    print("Choose a valid option")
            invoice = generate_invoice('rent', land_info, customer_name, rent_duration, total_amount, kitta_number, bill=bill)
            return True, invoice
        else:
            return False, "Land is not available for rent."
    except KeyError:
        return False, "Invalid Kitta Number."
    except ValueError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def return_land(land_data, customer_name, kitta_number, late_percent=10):
    """
    Return a rented land based on provided information.

    Args:
        land_data (dict): Dictionary containing land information.
        customer_name (str): Name of the customer returning the land.
        kitta_number (str): Kitta Number of the land to be returned.
        late_percent (int, optional): Late fee percentage. Defaults to 10.

    Returns:
        tuple: A tuple containing a boolean indicating success or failure, and an invoice if successful.

    """
    try:
        land_info = land_data[kitta_number]
        if land_info['status'].lower() == 'not available':
            land_info['status'] = 'Available'
            rent_start_date = datetime.strptime(input("Enter the booked rent start date (YYYY-MM-DD): "), '%Y-%m-%d')
            rent_end_date = datetime.strptime(input("Enter the actual rent end date (YYYY-MM-DD): "), '%Y-%m-%d')
            days_rented = (rent_end_date - rent_start_date).days
            total_amount = land_info['price'] * days_rented

            if days_rented > 365:
                late_fee_amount = (late_percent / 100) * ((days_rented) / 30) * total_amount
                total_amount += late_fee_amount
                land_info['late_fee'] = late_fee_amount

            invoice = generate_invoice('return', land_info, customer_name, kitta_number, total_amount=total_amount)
            return True, invoice
        else:
            return False, "Land is not rented or already returned."
    except KeyError:
        return False, "Invalid Kitta Number."
    except ValueError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)
