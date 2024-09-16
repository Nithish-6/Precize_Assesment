import json
import os

candidate_data = []

def calculate_pass_fail(sat_score):
    return "Pass" if sat_score > 30 else "Fail"

def integer_check(value):
    try:
        int(value)
    except ValueError:
        print("Value for the above field should be an integer")

def insert_data():
    name = input("Enter name: ")
    if any(name == candidate.get(name) for candidate in candidate_data):
        print(f"{name} already exists in candidate_data\n")
        return
    
    address = input("Enter Address: ")
    city = input("Enter City: ")
    country = input("Enter Country: ")
    pincode = input("Enter Pincode: ")
    integer_check(pincode)
    sat_score = int(input("Enter SAT Score: "))
    integer_check(sat_score)

    candidate = {
        "Name" : name,
        "Address" : address,
        "City" : city,
        "Country" : country,
        "Pincode" : pincode,
        "SAT Score" : sat_score,
        "Status" : calculate_pass_fail(sat_score)
    }

    candidate_data.append(candidate)
    print(f"{name}'s data has been added to the database\n")

def sort_data():
    candidate_data.sort(key=lambda record: record["SAT Score"],reverse=True)

def view_all_data():
    data_check()
    if candidate_data:
        print(json.dumps(candidate_data, indent=4))

def get_rank():
    name = input("Enter the name get the candidate's rank: ")
    sort_data()
    for i, candidate in enumerate(candidate_data, 1):
        if candidate.get("Name") == name:
            print(f"{name} is ranked #{i}\n")
            return
    print(f"Candidate {name} is not found!\n")

def update_score():
    name = input("Enter Name to update SAT Score: ")
    for candidate in candidate_data:
        if candidate.get("Name") == name:
            new_score = float(input(f"Enter new SAT Score for {name}: "))
            candidate["SAT Score"] = new_score
            candidate["Status"] = calculate_pass_fail(new_score)
            print(f"SAT score for {name} updated successfully!\n")
            return
    print(f"Record for {name} not found!\n")

def delete_one_record():
    name = input("Enter the name of the candidate to delete: ")
    for candidate in candidate_data:
        if candidate.get("Name") == name:
            candidate_data.remove(candidate)
            print(f"{name}'s data has been deleted successfully\n")
            return            
    print(f"No data found under the name {name}\n")
    
def calculate_avg_sat_score():   
    data_check()
    if candidate_data:
        avg_score = sum(candidate["SAT Score"] for candidate in candidate_data) / len(candidate_data)
        print(f"The average SAT score is {avg_score:.2f}\n")

def filter_records_by_status():
    data_check()
    if candidate_data:
        status = input("Enter Pass or Fail to filter: ").capitalize()
        filtered_data = [candidate for candidate in candidate_data if candidate["Status"] == status]
        print(json.dumps(filtered_data, indent=4))

def save_data_in_json_format():
    sort_data()
    file_name = input("Enter the file name: ")
    os.makedirs("candidate_data", exist_ok=True)
    with open("candidate_data/"+file_name+".json", "w") as f:
        json.dump(candidate_data, f, indent=4)
    print(f"Data has been saved successfully as "+file_name+".json under candidate_data folder\n")

def data_check():
    if not candidate_data:
        print("Insert atleast one record by selecting option 1 in order to get the details\n")

def menu():
    while True:
        print("SAT Results")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Calculate Average SAT Score")
        print("7. Filter records by Pass/Fail Status")
        print("8. Save Data in JSON format")
        print("9. Exit\n")
        
        option = input("Welcome to SAT Score Management System, Select an option from above to proceed: ")
        if option == "1":
            insert_data()
        elif option == "2":
            view_all_data()
        elif option == "3":
            get_rank()
        elif option == "4":
            update_score()
        elif option == "5":
            delete_one_record()
        elif option == "6":
            calculate_avg_sat_score()
        elif option == "7":
            filter_records_by_status()
        elif option == "8":
            save_data_in_json_format()
        elif option == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    menu()
