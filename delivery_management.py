print("🚚 Delivery Management System")

deliveries = []

while True:
    print("\n1. Add Delivery")
    print("2. View Deliveries")
    print("3. Search Delivery")
    print("4. Update Delivery Status")
    print("5. Delete Delivery")
    print("6. Count Deliveries")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Delivery
    if choice == "1":
        delivery_id = input("Enter delivery ID: ")
        customer = input("Enter customer name: ")
        item = input("Enter item name: ")
        address = input("Enter delivery address: ")

        delivery = {
            "id": delivery_id,
            "customer": customer,
            "item": item,
            "address": address,
            "status": "Pending"
        }

        deliveries.append(delivery)

        print("✅ Delivery added successfully!")

    # View Deliveries
    elif choice == "2":
        if len(deliveries) == 0:
            print("❌ No deliveries found.")
        else:
            print("\n📋 Delivery Details")
            print("--------------------------")

            for delivery in deliveries:
                print("Delivery ID:", delivery["id"])
                print("Customer:", delivery["customer"])
                print("Item:", delivery["item"])
                print("Address:", delivery["address"])
                print("Status:", delivery["status"])
                print("--------------------------")

    # Search Delivery
    elif choice == "3":
        search_id = input("Enter delivery ID to search: ")

        found = False

        for delivery in deliveries:
            if delivery["id"] == search_id:
                print("\n✅ Delivery Found")
                print("Delivery ID:", delivery["id"])
                print("Customer:", delivery["customer"])
                print("Item:", delivery["item"])
                print("Address:", delivery["address"])
                print("Status:", delivery["status"])
                found = True

        if not found:
            print("❌ Delivery not found.")

    # Update Status
    elif choice == "4":
        update_id = input("Enter delivery ID: ")

        found = False

        for delivery in deliveries:
            if delivery["id"] == update_id:
                print("\n1. Pending")
                print("2. Packed")
                print("3. Out for Delivery")
                print("4. Delivered")

                status_choice = input("Choose new status: ")

                if status_choice == "1":
                    delivery["status"] = "Pending"
                elif status_choice == "2":
                    delivery["status"] = "Packed"
                elif status_choice == "3":
                    delivery["status"] = "Out for Delivery"
                elif status_choice == "4":
                    delivery["status"] = "Delivered"
                else:
                    print("❌ Invalid status!")
                    break

                print("✅ Delivery status updated!")
                found = True
                break

        if not found:
            print("❌ Delivery not found.")

    # Delete Delivery
    elif choice == "5":
        delete_id = input("Enter delivery ID to delete: ")

        found = False

        for delivery in deliveries:
            if delivery["id"] == delete_id:
                deliveries.remove(delivery)
                print("✅ Delivery deleted successfully!")
                found = True
                break

        if not found:
            print("❌ Delivery not found.")

    # Count Deliveries
    elif choice == "6":
        print("🚚 Total Deliveries:", len(deliveries))

    # Exit
    elif choice == "7":
        print("Thank you for using Delivery Management System! 🚚")
        break

    else:
        print("❌ Invalid choice!")
