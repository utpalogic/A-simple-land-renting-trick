from operations import rent_land, return_land
from read import read_land_data
from write import write_land_data

def main():
    """
    Main function to manage land rental operations.

    Reads land data from a file, displays available lands, and allows users to rent or return land.

    """
    filename = "land.txt"
    land_data = read_land_data(filename)

    while True:
        print("\nAvailable Lands:")
        for kitta_number, land_info in land_data.items():
            print("Kitta Number: {}, City/District: {}, Status: {}".format(kitta_number, land_info['city'], land_info['status']))

        print("\n1. Rent Land\n2. Return Land\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_name = input("Enter your name: ")

            success, message = rent_land(land_data, customer_name)
            if success:
                print("Land rented successfully!")
                print(message)
                write_land_data(filename, land_data)
            else:
                print("Error:", message)

        elif choice == '2':
            customer_name = input("Enter your name: ")
            kitta_number = input("Enter Kitta Number of land to return: ")

            success, message = return_land(land_data, customer_name, kitta_number)
            if success:
                print("Land returned successfully!")
                print(message)
                write_land_data(filename, land_data)
            else:
                print("Error:", message)

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
