from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)
@app.route("/")
def home():    
    return render_template("index.html")

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_input = request.args.get('msg')
    #Cridem al subprocess (model amb el input)
    result = subprocess.run(['python', 'model/SapaGPT/gpt2.py', user_input], capture_output=True, text=True)
    #CompletedProcess(args=['python', 'model/picoGPT/gpt2.py', 'hello bot how are you'], returncode=0, stdout=', a former member of the National Assembly, said he was "very disappointed" by the decision.\n', stderr='0.01s - Debugger warning: It seems that frozen modules are being used, which may\n0.00s - make the debugger miss breakpoints. Please pass -Xfrozen_modules=off\n0.00s - to python to disable frozen modules.\n0.00s - Note: Debugging will proceed. Set PYDEVD_DISABLE_FILE_VALIDATION=1 to disable this validation.\n')
    response = result.stdout.strip()
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)