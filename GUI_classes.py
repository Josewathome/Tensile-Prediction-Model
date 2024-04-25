from model import TensileStrength
import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
import tkinter as tk
from tkinter import ttk
from model import TensileStrength
from torch.utils.data import Dataset, DataLoader
from torch import nn, optim

class DataCollection:
    def __init__(self, master):
        self.master = master
        master.title("TENSILE STRENGTH PREDICTION")

        self.font = ("Helvetica", 25) 
        # Define the options
        self.cement_types = ["OPC", "KP Silver", "WHITE CEMENT"]
        self.admixtures = ["Air-Entraining", "No Admixture"]

        #The concrete ratio we are predicting
        self.ratio_= ttk.Label(self.master, text="THE CONCRETE RATIO : 1:2:4")
        self.ratio_.grid(row=0, column=1, columnspan=2)


        # Create and grid the widgets
        ttk.Label(master, text="Mass of Cement (g) eg 134.7:").grid(row=1, column=0, sticky=tk.W)
        self.cement_amount = ttk.Entry(master)
        self.cement_amount.grid(row=1, column=1, sticky=tk.W)

        ttk.Label(master, text="Mass of water(g) eg 134.7:").grid(row=2, column=0, sticky=tk.W)
        self.water_mass = ttk.Entry(master)
        self.water_mass.grid(row=2, column=1, sticky=tk.W)

        ttk.Label(master, text="Type of Cement(dropdown menu):").grid(row=3, column=0, sticky=tk.W)
        self.cement = ttk.Combobox(master, values=self.cement_types, state="readonly")
        self.cement.grid(row=3, column=1, sticky=tk.W)

        ttk.Label(master, text="Average Aggregate Size (mm) eg 5 :").grid(row=4, column=0, sticky=tk.W)
        self.aggregate_size = ttk.Entry(master)
        self.aggregate_size.grid(row=4, column=1, sticky=tk.W)

        ttk.Label(master, text="Mass of Aggregate Coarse (g) eg 134.7 :").grid(row=5, column=0, sticky=tk.W)
        self.Coarse_aggregate = ttk.Entry(master)
        self.Coarse_aggregate.grid(row=5, column=1, sticky=tk.W)

        ttk.Label(master, text="Mass of Sand (g) eg 134.7:").grid(row=6, column=0, sticky=tk.W)
        self.mass_sand = ttk.Entry(master)
        self.mass_sand.grid(row=6, column=1, sticky=tk.W)

        ttk.Label(master, text="Curing Duration (days) eg 7:").grid(row=7, column=0, sticky=tk.W)
        self.curing_duration = ttk.Entry(master)
        self.curing_duration.grid(row=7, column=1, sticky=tk.W)

        ttk.Label(master, text="Admixtures(dropdown menu):").grid(row=8, column=0, sticky=tk.W)
        self.admixture = ttk.Combobox(master, values=self.admixtures, state="readonly")
        self.admixture.grid(row=8, column=1, sticky=tk.W)

        self.submit_button = ttk.Button(master, text="Submit", command=self.collect_data)
        self.submit_button.grid(row=9, column=0, columnspan=2)

        # OUR NAMES
        self.NAMES_1 = ttk.Label(self.master, text="E033-01-2336/2020 NELLY NKIROTE")
        self.NAMES_1.grid(row=11, column=1, columnspan=2)

        self.NAMES_2 = ttk.Label(self.master, text="EO33-01-1386/2020 JOSEPH. G. WATHOME")
        self.NAMES_2.grid(row=12, column=1, columnspan=2)

    def collect_data(self):
    # Collect the data
        data = {
            "Cement amount (g)": float(self.cement_amount.get()),
            "Water (g)": float(self.water_mass.get()),
            "Type of cement": self.cement.get(),
            "Aggregate(Coarse)(g)":float(self.Coarse_aggregate.get()),
            "Aggregate(SAND)(g)": float(self.mass_sand.get()),
            "Average Aggregate size (mm)": int(self.aggregate_size.get()),
            "Curing Duration (days)": int(self.curing_duration.get()),
            "Admixtures": self.admixture.get()
        }

        # Process the data
        if data['Type of cement'] == "OPC":
            data['Type of cement'] = 0
        elif data['Type of cement'] == "KP Silver":
            data['Type of cement'] = 1
        elif data['Type of cement'] == "WHITE CEMENT":
            data['Type of cement'] = 2

        if data['Admixtures'] == "Air-Entraining":
            data['Admixtures'] = 0
        elif data['Admixtures'] == "No Admixture":
            data['Admixtures'] = 1

        # Initialize a scaler
        scaler = StandardScaler()

        # Fit on the features and transform
        normalized_features = scaler.fit_transform([list(data.values())])
        
         # model path
        model = torch.load("Model\copytensile_strength_model.pth")
        # Load the state dictionary

        # Make a prediction
        with torch.no_grad():
            inputs = torch.tensor(normalized_features, dtype=torch.float)
            outputs = model.forward(inputs)
            
        # Create a label to display the predicted tensile strength
        self.prediction_label = ttk.Label(self.master, text="")
        self.prediction_label.grid(row=10, column=0, columnspan=2)

        # Update the label with the predicted tensile strength
        self.prediction_label.config(text="Predicted Tensile Strength: " + str(round(outputs.item(), 5)) +" MPa")

        # Print the data and prediction to the console (optional)
        print("Data:", data)
        print("Predicted Tensile Strength:", round(outputs.item(), 5), "MPa")

