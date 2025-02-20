from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Shreyas N"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    ist_time = datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
