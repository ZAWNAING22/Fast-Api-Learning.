from fastapi import FastAPI, HTTPException,UploadFile,File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import io

app = FastAPI()

# Load trained model and features
model =joblib.load("venv/house_modelrf.joblib")
feattures=joblib.load("venv/house_features.joblib")

# Define expected feature names (California Housing dataset)
FEATURE_NAMES = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms",
    "Population", "AveOccup", "Latitude", "Longitude"
]

# Schema for data validation
class HouseFeatures(BaseModel):
    MedInc     : float = Field(gt=0, description="Median income in the district")
    HouseAge   : float = Field(gt=0, description="Average age of houses in the district")
    AveRooms   : float = Field(gt=0, description="Average number of rooms per household")
    AveBedrms  : float = Field(gt=0, description="Average number of bedrooms per household")
    Population : float = Field(gt=0, description="Total population in the district")
    AveOccup   : float = Field(gt=0, description="Average household occupancy")
    Latitude   : float = Field(gt=32, le=42, description="Geographic latitude (California range)")
    Longitude  : float = Field(ge=-125, le=-114, description="Geographic longitude (California range)")

# Home
@app.get("/")
def home():
    return {
        "message": "California house prediction API",
        "status": "running",
        "endpoint": "send POST request to /predict"
    }

# Health
@app.get("/health")
def health():
    return {
        "status": "running",
        "model": "RandomForestRegressor",
        "features": feattures,
        "Average Error":"32,754.26"
    }

#predict route
@app.post("/predict")
def predict(house:HouseFeatures):
    try:
        input_data=pd.DataFrame([{
            "MedInc":house.MedInc, 
            "HouseAge":house.HouseAge,
            "AveRooms":house.AveRooms, 
            "AveBedrms":house.AveBedrms,
            "Population":house.Population, 
            "AveOccup":house.AveOccup, 
            "Latitude":house.Latitude, 
            "Longitude":house.Longitude  }],columns=FEATURE_NAMES) #Pandas will reorder the DataFrame columns to match the list in FEATURE_NAMES
        predicted=model.predict(input_data)[0]
        price_usd=predicted*100000

        return {
            "predicted_price":f"{price_usd:,.0f}",
            "predicted_short_price":f"{predicted:,.2f} hundred thousands",
            "fidence range":f"{price_usd-32754.26:,.0f} to {price_usd+32754.26:,.0f}"
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"prediction failed :{str(e)}"
        )
        
@app.post("/predict-file")
async def predict_file(file: UploadFile = File(...)):
    #🗽 Step 1: Validate file type
    # Only allow CSV uploads
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Upload only CSV file.")

    #🗽 Step 2: Read file contents
    # Convert uploaded bytes into a pandas DataFrame
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    #🗽 Step 3: Define required columns (the ones your model was trained on)
    required_columns = [
        "MedInc", "HouseAge", "AveRooms", "AveBedrms",
        "Population", "AveOccup", "Latitude", "Longitude"
    ]

    #🗽 Step 4: Check for missing columns
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise HTTPException(
            status_code=400,
            detail=f"Missing columns: {missing_columns}. Found: {list(df.columns)}"
        )

    #🗽 Step 5: Check for empty file
    if len(df) == 0:
        raise HTTPException(status_code=400, detail="The uploaded file has no data.")

    #🗽 Step 6: Run predictions
    try:
        predictions = model.predict(df[required_columns])

        # Add predictions to DataFrame
        df['predicted_price_usd'] = predictions * 100000  # scale if needed

        # Format predictions nicely (e.g., 123,456)
        df['predicted_price_usd'] = df['predicted_price_usd'].apply(lambda x: f"{x:,.0f}")

        #🗽 Step 7: Convert DataFrame back to CSV
        output = df.to_csv(index=False)

        #🗽 Step 8: Return downloadable CSV file
        return StreamingResponse(
            io.StringIO(output),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=predictions.csv"}
        )

    #🗽 Step 9: Handle prediction errors
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


