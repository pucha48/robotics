from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Specify the directory where uploaded images will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file is uploaded in the request
        if 'image' not in request.files:
            return redirect(request.url)
        
        image_file = request.files['image']
        
        # If no file is selected, redirect back to the form
        if image_file.filename == '':
            return redirect(request.url)
        
        if image_file:
            # Save the uploaded image to the specified folder
            filename = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(filename)
            return redirect(url_for('display', filename=image_file.filename))
    
    return render_template('index.html')

@app.route('/display/<filename>')
def display(filename):
    # Construct the path to the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    return render_template('display.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
