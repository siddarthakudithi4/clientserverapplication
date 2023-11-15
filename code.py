import requests
import tkinter as tk
from tkinter import font, Text, messagebox, ttk
import webbrowser

# Function to make the HTTP request and display the response code and message
def get_response_message():
    # Show a progress bar while the request is being made.
    progress_label.config(text="Loading...")
    progress_bar.start()

    url = entry.get()
    response = requests.get(url)
    response_code = response.status_code

    if response_code == 200:
        message = "The server accepted your request."
        message_color = "green"
    else:
        message = "The server denied your request."
        message_color = "red"

    response_label.config(text=f"Response Code: {response_code}\n{message}", font=("Helvetica", 14), fg=message_color)

    # Stop the progress bar.
    progress_bar.stop()
    progress_label.config(text="")

# Function to clear the input field and response label
def clear_fields():
    entry.delete(0, tk.END)
    response_label.config(text="")
    
    

# Function to view the response content in a separate window
def view_response_content():
    url = entry.get()
    response = requests.get(url)
    response_text = response.text

    content_window = tk.Toplevel(app)
    content_window.title("Response Content")
    content_text = Text(content_window)
    content_text.pack()
    content_text.insert(tk.END, response_text)

# Function to open the URL in the default web browser
def open_in_browser():
    url = entry.get()
    webbrowser.open(url)

# Function for notification using messagebox
def notify_user(message):
    messagebox.showinfo("Notification", message)

# Create the main application window
app = tk.Tk()
app.title("Web Page Viewer")

# Configure the window size
app.geometry("500x400")

# Create a custom font for labels
custom_font = font.nametofont("TkDefaultFont")
custom_font.configure(size=12)

# Create an entry widget to enter the URL
label = tk.Label(app, text="Enter URL:", font=custom_font)
label.pack(pady=10)

entry = tk.Entry(app, font=custom_font)
entry.pack(pady=5)

# Create a button to make the request and display the response message
check_button = tk.Button(app, text="Check Website Access", command=get_response_message, font=custom_font, bg="blue", fg="white")
check_button.pack(pady=10)

# Create a button to clear the input field and response label
clear_button = tk.Button(app, text="Clear", command=clear_fields, font=custom_font, bg="gray", fg="white")
clear_button.pack()

# Create a button to view the response content
view_content_button = tk.Button(app, text="View Response Content", command=view_response_content, font=custom_font, bg="green", fg="white")
view_content_button.pack()

# Create a button to open the URL in the browser
open_browser_button = tk.Button(app, text="Open in Browser", command=open_in_browser, font=custom_font, bg="orange", fg="white")
open_browser_button.pack()

# Create a label to display the response message
response_label = tk.Label(app, text="", font=("Helvetica", 16))
response_label.pack()

# Create a progress bar widget
progress_bar = ttk.Progressbar(app, mode="indeterminate")
progress_label = tk.Label(app, text="", font=("Helvetica", 14))

# Place the progress bar and label in the layout
progress_label.pack()
progress_bar.pack()

# Create a Canvas for the background
background_canvas = tk.Canvas(app, width=500, height=400)
background_canvas.pack()

# Add names to the background with specific colors
names = [("Siddartha", "lightgray"), ("Dimpul", "lightgray"), ("Akshitha", "lightgray"), ("OS PROJECT", "#f5bf42")]

# Position for the first name
y_position = 100

for name, color in names:
    background_canvas.create_text(250, y_position, text=name, font=("Helvetica", 20), fill=color)
    y_position += 40  # Adjust this value for the desired gap

app.mainloop()
