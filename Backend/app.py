from flask import Flask, request, jsonify ,send_file
from flask_cors import CORS
from pytube import YouTube
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")  
db = client["MetaData"] 
collection = db["videos"]  

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    video_link = data.get('videoUrl')
    print(video_link)
    
    try:
        yt = YouTube(video_link)
        stream = yt.streams.get_highest_resolution()
        video_title = yt.title
        filename = f"{video_title}.mp4"
        
        # Download the video
        stream.download(output_path="videos/", filename=filename)
        
        # Save video metadata to MongoDB
        video_metadata = {
            'title': video_title,
            'url': video_link,
            'filename': filename
        }
        collection.insert_one(video_metadata)
        
        return "Downloaded and saved successfully"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/list', methods=['GET'])
def list_videos():
    try:
        video_list = list(collection.find({}, {'_id': False}))  # Retrieve all documents, excluding _id field
        return jsonify(video_list)
    except Exception as e:
        return f"Error: {str(e)}"  

@app.route('/video/<filename>', methods=['GET'])
def serve_video(filename):
    video_path = os.path.join('videos', filename)
    return send_file(video_path)

    
if __name__ == '__main__':
    app.run(debug=True)
