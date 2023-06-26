from flask import Flask , request,jsonify



app=Flask(__name__)
@app.route('/')

  

@app.route('/weather', methods=['POST'] )
def get_user():
    print(request)
    from main import get_speech
    audio_data = request.files['audio']


    result = get_speech(audio_data)

    extra=request.args.get("extra")
    if extra:
        result["extra"]=extra
    return jsonify(result),200




    
if __name__ == "__main__":
    app.run(debug=True, port=8000)