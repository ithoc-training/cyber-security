from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''
        <script>
            function call_backend() {
                console.log('call backend');
                fetch('http://127.0.0.1:5003/sensitive')
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Network response was not ok ' + response.statusText);
                        }
                        return response.json(); 
                    })
                    .then(data => {
                        console.log(data); 
                    })
                    .catch(error => {
                        console.error('There has been a problem with your fetch operation:', error);
                    });
            }
        </script>
        <h1>CORS</h1>
        <button onclick="call_backend()">Rufe Backend</button>
    '''


if __name__ == '__main__':
    app.run(debug=True, port=5004)
