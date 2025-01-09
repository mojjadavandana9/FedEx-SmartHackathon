from flask import Flask, render_template, request
from models.emissions_model import EmissionModel
from models.optimization_pipeline import OptimizationPipeline

# Flask App
app = Flask(__name__)

# Initialize Pipeline and Model
pipeline = OptimizationPipeline()
emission_model = EmissionModel()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize_route():
    # Gather user inputs
    start_location = request.form["start"]
    end_location = request.form["end"]
    vehicle_type = request.form["vehicle"]
    fuel_efficiency = float(request.form["fuel_efficiency"])
    emission_factor = float(request.form["emission_factor"])

    # Run the pipeline to get optimized route
    route_data = pipeline.get_optimized_route(start_location, end_location)

    # Calculate emissions
    distance = route_data["distance_km"]
    emissions = emission_model.calculate_emissions(distance, fuel_efficiency, emission_factor)

    return render_template(
        "result.html",
        route=route_data,
        emissions=emissions,
    )

if __name__ == "__main__":
    app.run(debug=True)
