import flask
import joblib
import numpy as np
import os

app = flask.Flask(__name__)

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model.pkl')
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    print("Error: model.pkl not found.")
    model = None
except Exception as e:
    print(f"Error loading model with joblib: {e}")
    model = None

@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return flask.render_template('index.html', prediction_text="Model not loaded.")

    try:
        
        resolution = flask.request.form.get('resolution', '0x0')
        try:
            px_height, px_width = map(int, resolution.lower().split('x'))
        except ValueError:
            px_height, px_width = 0, 0

        screen_dims = flask.request.form.get('screen_dims', '0x0')
        try:
            sc_h, sc_w = map(int, screen_dims.lower().split('x'))
        except ValueError:
            sc_h, sc_w = 0, 0

        blue = 1 if 'blue' in flask.request.form else 0
        dual_sim = 1 if 'dual_sim' in flask.request.form else 0
        four_g = 1 if 'four_g' in flask.request.form else 0
        three_g = 1 if 'three_g' in flask.request.form else 0
        touch_screen = 1 if 'touch_screen' in flask.request.form else 0
        wifi = 1 if 'wifi' in flask.request.form else 0

        battery_power = int(flask.request.form.get('battery_power', 0))
        clock_speed = float(flask.request.form.get('clock_speed', 0))
        fc = int(flask.request.form.get('fc', 0))
        int_memory = int(flask.request.form.get('int_memory', 0))
        m_dep = float(flask.request.form.get('m_dep', 0))
        mobile_wt = int(flask.request.form.get('mobile_wt', 0))
        n_cores = int(flask.request.form.get('n_cores', 0))
        pc = int(flask.request.form.get('pc', 0))
        ram = int(flask.request.form.get('ram', 0)) * 1024
        talk_time = int(flask.request.form.get('talk_time', 0))

        features = [
            battery_power, blue, clock_speed, dual_sim, fc, four_g, 
            int_memory, m_dep, mobile_wt, n_cores, pc, px_height, 
            px_width, ram, sc_h, sc_w, talk_time, three_g, 
            touch_screen, wifi
        ]
        
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        
        output = prediction[0]
        
        price_map = {
            0: "Low Cost",
            1: "Medium Cost",
            2: "High Cost",
            3: "Very High Cost"
        }
        prediction_text = f"Predicted Price Range: {price_map.get(output, output)}"

        summary = {
            'battery_power': battery_power,
            'ram_gb': int(ram / 1024),
            'int_memory': int_memory,
            'clock_speed': clock_speed,
            'n_cores': n_cores,
            'resolution': f"{px_height}x{px_width}",
            'pc': pc,
            'fc': fc,
            'four_g': four_g,
            'three_g': three_g,
            'wifi': wifi,
            'blue': blue
        }

        return flask.render_template('result.html', prediction_text=prediction_text, summary=summary)

    except Exception as e:
        return flask.render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
