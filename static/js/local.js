// NOTE: this example uses the chess.js library:
// https://github.com/jhlywa/chess.js

var board = null
var game = new Chess()
var $status = $('#status')
var $fen = $('#fen')
var $pgn = $('#pgn')
var whiteSquareGrey = '#a9a9a9'
var blackSquareGrey = '#696969'
var gameState = 0

if (gameState == 0) {
  function removeGreySquares() {
    $('#myBoard .square-55d63').css('background', '')
  }

  function greySquare(square) {
    var $square = $('#myBoard .square-' + square)

    var background = whiteSquareGrey
    if ($square.hasClass('black-3c85d')) {
      background = blackSquareGrey
    }

    $square.css('background', background)
  }

  function onDragStart(source, piece, position, orientation) {
    // do not pick up pieces if the game is over
    if (game.game_over()) return false

    // only pick up pieces for the side to move
    if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
      (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
      return false
    }
  }

  function onDrop(source, target) {
    removeGreySquares()
    // see if the move is legal
    var move = game.move({
      from: source,
      to: target,
      promotion: 'q' // NOTE: always promote to a queen for example simplicity
    })

    // illegal move
    if (move === null) return 'snapback'

    updateStatus()
  }

  function onMouseoverSquare(square, piece) {
    // get list of possible moves for this square
    var moves = game.moves({
      square: square,
      verbose: true
    })

    // exit if there are no moves available for this square
    if (moves.length === 0) return

    // highlight the square they moused over
    greySquare(square)

    // highlight the possible squares for this piece
    for (var i = 0; i < moves.length; i++) {
      greySquare(moves[i].to)
    }
  }

  function onMouseoutSquare(square, piece) {
    removeGreySquares()
  }

  // update the board position after the piece snap
  // for castling, en passant, pawn promotion
  function onSnapEnd() {
    board.position(game.fen())
  }

  function updateStatus() {
    var status = ''

    var moveColor = 'White'
    if (game.turn() === 'b') {
      moveColor = 'Black'
    }

    // checkmate?
    if (game.in_checkmate()) {
      status = 'Game over, ' + moveColor + ' is in checkmate.'
    }

    // draw?
    else if (game.in_draw()) {
      status = 'Game over, drawn position'
    }

    // game still on
    else {
      status = moveColor + ' to move'

      // check?
      if (game.in_check()) {
        status += ', ' + moveColor + ' is in check'
      }
    }

    $status.html(status)
    $fen.html(game.fen())
    $pgn.html(game.pgn())
  }

  var config = {
    draggable: true,
    onDragStart: onDragStart,
    onDrop: onDrop,
    onMouseoutSquare: onMouseoutSquare,
    onMouseoverSquare: onMouseoverSquare,
    onSnapEnd: onSnapEnd
  }
  board = Chessboard('myBoard', config)

  updateStatus()
}

function reset() {
  var btn = document.getElementById("startBtn");
  btn.innerHTML = 'Reset';

  board.start()
  game.reset()

  if (game.turn() == 'b') {
    status = 'Black to move'
  } else {
    status = 'White to move'
  }
  $status.html(status)
  $fen.html(game.fen())
  $pgn.html(game.pgn())
}

function undo() {
  var status = ''

  game.undo()
  onSnapEnd()

  if (game.turn() == 'b') {
    status = 'Black to move'
  } else {
    status = 'White to move'
  }
  $status.html(status)
  $fen.html(game.fen())
  $pgn.html(game.pgn())
}

function saveGame(){
  var fen = document.getElementById('fen').innerHTML
  document.getElementById('match').value = fen
}
