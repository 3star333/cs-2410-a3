import matplotlib.pyplot as plt
import pandas as pd

def main():
    lap_time_plots('cars.csv')
    fastest_manufacturer_plots('cars.csv')
    name_count_plots('cars.csv')
    PS_KG_ratio_plots('cars.csv')

def lap_time_plots(file_path):
    try:
        # Read the data from CSV
        ranking_data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return
    except pd.errors.ParserError:
        print("Error: There was a parsing error.")
        return
    
    # Ensure the CSV file contains 'Rank', 'Vehicle', 'Driver', and 'Time' columns
    if not set(['Rank', 'Vehicle', 'Driver', 'Time']).issubset(ranking_data.columns):
        raise ValueError("CSV file must contain 'Rank', 'Vehicle', 'Driver', and 'Time' columns.")
    
    # Sort data by rank and select top 10
    top_cars = ranking_data.sort_values(by='Rank').head(10)

    # Extract columns for plotting
    ranks = top_cars['Rank']
    vehicles = top_cars['Vehicle']
    lap_times = top_cars['Time']

    # Create a figure and a set of subplots
    fig, g1 = plt.subplots(figsize=(10, 8))

    # Create a horizontal bar graph
    g1.barh(vehicles, lap_times, color='skyblue')
    g1.set_xticks(lap_times)  # Set x-ticks to lap times
    g1.set_xlabel('Lap Time (minutes)')
    g1.set_title('Top 10 Vehicle Lap Times at Nürburgring')

    # Show grid
    plt.grid(True, axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    # Display the plot
    plt.show()

def fastest_manufacturer_plots(file_path):
    try:
        # Read the data from CSV
        ranking_data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return
    except pd.errors.ParserError:
        print("Error: There was a parsing error.")
        return
    
    # Ensure the CSV file contains 'Vehicle', 'Driver', 'Time' columns
    if not set(['Vehicle', 'Driver', 'Time']).issubset(ranking_data.columns):
        raise ValueError("CSV file must contain 'Vehicle', 'Driver', and 'Time' columns.")
    
    # Assuming the manufacturer is the first part of the vehicle name (you may need to adjust this)
    ranking_data['Manufacturer'] = ranking_data['Vehicle'].str.split(' ').str[0]

    # Group by manufacturer and find the fastest lap time
    fastest_times = ranking_data.groupby('Manufacturer')['Time'].min().reset_index()

    # Sort by lap time
    fastest_times = fastest_times.sort_values(by='Time')

    # Extract columns for plotting
    manufacturers = fastest_times['Manufacturer']
    lap_times = fastest_times['Time']

    # Create a figure and a set of subplots
    fig, g2 = plt.subplots(figsize=(10, 8))

    # Create a scatter plot
    g2.scatter(manufacturers, lap_times, color='black', s=15)  # s is the size of the dots
    g2.set_xticklabels(manufacturers, rotation=45, ha='right')  # Rotate x-axis labels
    g2.set_ylabel('Fastest Lap Time (minutes)')
    g2.set_title('Fastest Lap Time by Vehicle Manufacturer')

    # Show grid
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    # Display the plot
    plt.show()

def name_count_plots(file_path):
    try:
        # Read the data from CSV
        ranking_data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return
    except pd.errors.ParserError:
        print("Error: There was a parsing error.")
        return
    
    # Ensure the CSV file contains 'Rank', 'Vehicle', 'Driver', and 'Time' columns
    if not set(['Rank', 'Vehicle', 'Driver', 'Time']).issubset(ranking_data.columns):
        raise ValueError("CSV file must contain 'Rank', 'Vehicle', 'Driver', and 'Time' columns.")
    
    # Makes a dictionary with the names of the drivers and respective count
    ranks = ranking_data['Driver']
    name_count = {}
    for name in ranks:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    names = list(name_count.keys())
    counts = list(name_count.values())

    plt.figure(figsize=(10, 6))
    plt.bar(names, counts, color='skyblue')

    plt.xlabel('Drivers')
    plt.ylabel('Count')
    plt.title('Driver Name Frequency')
    plt.xticks(rotation=65) 

    plt.tight_layout()
    plt.show()

def PS_KG_ratio_plots(file_path):
    try:
        # Read the data from CSV
        ranking_data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return
    except pd.errors.ParserError:
        print("Error: There was a parsing error.")
        return
    
    # Ensure the CSV file contains 'Rank', 'Vehicle', 'Driver', and 'Time' columns
    if not set(['Rank', 'Vehicle', 'Driver', 'Time', 'PS / KG']).issubset(ranking_data.columns):
        raise ValueError("CSV file must contain 'Rank', 'Vehicle', 'Driver', 'Time', and 'PS / KG' columns.")
    
    
    pskgValues = ranking_data['PS / KG']
    PS = []
    KG = []

    for value in pskgValues:
        PSnum, KGnum = value.split(' / ')
        if (PSnum.isdigit() and KGnum.isdigit()):
             PS.append(int(PSnum))
             KG.append(int(KGnum))

	
    plt.scatter(PS, KG, color='black', s=15)  # s is the size of the dots
    plt.xlabel('PS')
    plt.ylabel('KG')
    plt.title('PS KG values')
    plt.show()

# Run the main function
main()
