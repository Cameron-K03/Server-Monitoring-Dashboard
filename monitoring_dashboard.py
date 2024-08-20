# Install Flask and psutil if you don't have.
# pip install Flask psutil

from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    data = {
        'cpu_usage': cpu_usage,
        'memory_total': memory_info.total / (1024 ** 3),  # Convert to GB
        'memory_used': memory_info.used / (1024 ** 3),  # Convert to GB
        'memory_free': memory_info.free / (1024 ** 3),  # Convert to GB
        'disk_total': disk_info.total / (1024 ** 3),  # Convert to GB
        'disk_used': disk_info.used / (1024 ** 3),  # Convert to GB
        'disk_free': disk_info.free / (1024 ** 3)  # Convert to GB
    }

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
