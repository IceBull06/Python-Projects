from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def home():
  # append following divs to create a shape
  #   <div class="piece">&#9812;</div>
  #   <div class="piece">&#9813;</div>
  #   <div class="piece">&#9814;</div>
  #   <div class="piece">&#9815;</div>
  #   <div class="piece">&#9816;</div>
  #   <div class="piece">&#9817;</div>
  #   <div class="piece">&#9818;</div>
  #   <div class="piece">&#9819;</div>
  #   <div class="piece">&#9820;</div>
  #   <div class="piece">&#9821;</div>
  #   <div class="piece">&#9822;</div>
  #   <div class="piece">&#9823;</div>
  rows = [x for x in range(1,9)]
  cols = [x for x in range(1,9)]
  return render_template('index.html', rows=rows, cols=cols)

app.run(host='0.0.0.0', port=8080)