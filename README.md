# Server Monitoring Dashboard

This is a simple server monitoring dashboard built with Python, Flask, and psutil. It displays real-time CPU usage, memory usage, and disk space on a web interface.

## Features

- **CPU Usage**: Real-time CPU usage percentage.
- **Memory Usage**: Total, used, and free memory displayed in GB.
- **Disk Space**: Total, used, and free disk space displayed in GB.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Cameron-K03/server-monitoring-dashboard.git
    ```

2. Install the required packages:

    ```bash
    pip install Flask psutil
    ```

3. Run the Flask app:

    ```bash
    python monitoring_dashboard.py
    ```

4. Open your web browser and go to `http://127.0.0.1:5000/`.

## Future Enhancements

- Add more metrics (network usage, system uptime, etc.).
- Improve the UI with a CSS framework like Bootstrap.
- Deploy on a remote server for accessible monitoring.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
