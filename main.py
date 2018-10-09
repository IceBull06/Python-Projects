from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def home():
  # chess uft-16 pieces
  pieces = [
    '\u2654',
    '\u2655',
    '\u2656',
    '\u2657',
    '\u2658',
    '\u2659',
    '\u265A',
    '\u265B',
    '\u265C',
    '\u265D',
    '\u265E',
    '\u265F',
  ]
  
  # chess board tiles
  rows = [x for x in range(1,9)]
  cols = [x for x in range(1,9)]
  return render_template('index.html', rows=rows, cols=cols, pieces=pieces)

app.run(host='0.0.0.0', port=8080)