from datetime import datetime

def generate_invoice(transaction_type, land_info, customer_name, rent_duration=None, total_amount=None, kitta_number=None, bill=None):
    """
    Generate an invoice based on transaction details.

    Args:
        transaction_type (str): Type of transaction ('rent' or 'return').
        land_info (dict): Dictionary containing land information.
        customer_name (str): Name of the customer involved in the transaction.
        rent_duration (int, optional): Duration of rent in months. Defaults to None.
        total_amount (int, optional): Total amount involved in the transaction. Defaults to None.
        kitta_number (str, optional): Kitta Number of the land involved in the transaction. Defaults to None.
        bill (list, optional): List containing billing information. Defaults to None.

    Returns:
        str: Invoice details as a string.
    """
    try:
        transaction_id = str(int(datetime.now().timestamp()))
        invoice_filename = "\t\t\tTECHNO PROPERTY NEPAL\n\t\tLalitpur, Nepalinvoice_{}.txt".format(transaction_id)
        invoice = "----- {} INVOICE -----\n".format(transaction_type.upper())
        invoice += "Transaction ID: {}\n".format(transaction_id)
        invoice += "Customer Name: {}\n".format(customer_name)
        invoice += "Date & Time: {}\n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        if transaction_type == 'return':
            invoice += "Transaction: Land returned\n"
            if 'late_fee' in land_info:
                invoice += "Late Fee: NPR {}\n".format(land_info['late_fee'])
            invoice += "-----------------------------\n"
        
        if transaction_type == 'rent':
            invoice += "| {:<20} | {:<15} | {:<15} | | {:<15} | {:<15} |\n".format("Description","Kitta No", "City", "Direction", "Rent Duration", "Total Amount")
            invoice += "| {:<20} | {:<15} | {:<15} | {:<15} | {:<15} | \n".format("-" * 20, "-" * 15, "-" * 15, "-" * 15, "-" * 15, "-" * 15, "-" * 15)
            for item in bill:
                invoice += "Rent for {} months       | Kitta No {}    || {}     || {}       | {}      ||  NPR {:<12} |\n".format(item[4], item[3], item[1]['city'], item[1]['direction'], item[4], item[6])
        
        elif transaction_type == 'return':
            invoice += "| {:<20} | {:<15} | {:<15} | | {:<15} | {:<15} |\n".format("Description","Kitta No", "Quantity", "Late Amount", "Total Amount")
            invoice += "| {:<20} | {:<15} | {:<15} | \n".format("-" * 20, "-" * 15, "-" * 15)
            invoice += "Land returned      |  {}   ||     {}     ||   {}  | NPR {}  |\n".format(kitta_number, 1, land_info['late_fee'], total_amount)
            invoice += "-----------------------------\n"
        
        with open(invoice_filename, 'w') as invoice_file:
            invoice_file.write(invoice)
        
        return invoice
    except Exception as e:
        print("Error generating invoice: {}".format(e))

def write_land_data(filename, land_data):
    """
    Write land data to a file.

    Args:
        filename (str): Name of the file to write the data to.
        land_data (dict): Dictionary containing land information.

    """
    try:
        with open(filename, 'w') as file:
            for kitta_number, land_info in land_data.items():
                file.write("{}, {}, {}, {}, {}, {}\n".format(kitta_number, land_info['city'], land_info['direction'], land_info['area'], land_info['price'], land_info['status']))
    except Exception as e:
        print("Error writing to file: {}".format(e))
