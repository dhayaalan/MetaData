from flask import request, Flask, jsonify
from flask_cors import CORS
import youtube_dl
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def download():
    data = request.get_json()
    video_url = data.get('videoUrl')

    try:
        ydl_opts = {
            'format': 'best',  # Get the best quality format available
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video_info = ydl.extract_info(video_url, download=False)

        metadata = {
            'title': video_info['title'],
            'author': video_info['uploader'],
            'duration': video_info['duration'],
            'views': video_info.get('view_count', 0),
            'likes': video_info.get('like_count', 0),
            'dislikes': video_info.get('dislike_count', 0),
            'description': video_info['description'],
            'thumbnails': video_info['thumbnail'],
            'streams': [{
                'resolution': stream['format'],
                'extension': stream['ext'],
                'url': stream['url']
            } for stream in video_info['formats'] if 'format' in stream]
        }

        # Convert the metadata to a JSON response
        return jsonify(metadata)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
