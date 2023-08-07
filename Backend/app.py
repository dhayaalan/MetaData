from flask import Flask, request, jsonify
from flask_cors import CORS
from pytube import YouTube

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    video_link = data.get('videoUrl')
    print(video_link)
    
    try:
        yt = YouTube(video_link)
        stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream
        video_title = yt.title
        filename = f"videos/{video_title}.mp4"
        
        stream.download(output_path = ".",filename=filename)
        return "Downloaded successfully"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
