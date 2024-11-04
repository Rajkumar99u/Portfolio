import gradio as gr

class Vehicle:
    def __init__(self, vin, make, model, year):
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model} (VIN: {self.vin})"

class VehicleManagementSystem:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vin, make, model, year):
        if vin in self.vehicles:
            return f"Vehicle with VIN {vin} already exists."
        else:
            vehicle = Vehicle(vin, make, model, year)
            self.vehicles[vin] = vehicle
            return f"Vehicle added: {vehicle}"

    def view_vehicles(self):
        if not self.vehicles:
            return "No vehicles available."
        else:
            return "\n".join(str(vehicle) for vehicle in self.vehicles.values())

    def delete_vehicle(self, vin):
        if vin in self.vehicles:
            deleted_vehicle = self.vehicles.pop(vin)
            return f"Vehicle deleted: {deleted_vehicle}"
        else:
            return f"Vehicle with VIN {vin} not found."

vms = VehicleManagementSystem()

# Gradio interface functions
def add_vehicle(vin, make, model, year):
    return vms.add_vehicle(vin, make, model, year)

def view_vehicles():
    return vms.view_vehicles()

def delete_vehicle(vin):
    return vms.delete_vehicle(vin)

# Gradio Interface
with gr.Blocks() as app:
    gr.Markdown("# Vehicle Management System")
    
    with gr.Tab("Add Vehicle"):
        vin_input = gr.Textbox(label="VIN")
        make_input = gr.Textbox(label="Make")
        model_input = gr.Textbox(label="Model")
        year_input = gr.Textbox(label="Year")
        add_btn = gr.Button("Add Vehicle")
        add_output = gr.Textbox(label="Output", interactive=False)

        add_btn.click(add_vehicle, inputs=[vin_input, make_input, model_input, year_input], outputs=add_output)

    with gr.Tab("View Vehicles"):
        view_output = gr.Textbox(label="Vehicles", interactive=False, lines=10)
        view_btn = gr.Button("View Vehicles")
        
        view_btn.click(view_vehicles, outputs=view_output)

    with gr.Tab("Delete Vehicle"):
        delete_vin_input = gr.Textbox(label="VIN to Delete")
        delete_btn = gr.Button("Delete Vehicle")
        delete_output = gr.Textbox(label="Output", interactive=False)

        delete_btn.click(delete_vehicle, inputs=delete_vin_input, outputs=delete_output)

# Launch the Gradio app
app.launch()
