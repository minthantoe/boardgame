var board = null
var game = new Draughts()

function getCurrent(){
  var temp = game.fen()
  alert(temp)
}

function saveGame(){
  var temp = game.fen()
  document.getElementById('match').value = temp
}

function onDragStart(source, piece, position, orientation) {
    // do not pick up pieces if the game is over
    if (game.gameOver()) return false

    // only pick up pieces for White
    if (piece.search(/^b/) !== -1) return false
}

function greySquare(square) {
    var $square = $('#board .square-' + square)

    var background = whiteSquareGrey
    if ($square.hasClass('black-3c85d')) {
        background = blackSquareGrey
    }

    $square.css('background', background)
}


function makeRandomMove() {
    var possibleMoves = game.moves()

    // game over
    if (possibleMoves.length === 0) return

    var randomIdx = Math.floor(Math.random() * possibleMoves.length)
    game.move(possibleMoves[randomIdx])
}

var whiteSquareGrey = '#a9a9a9'
var blackSquareGrey = '#696969'

function removeGreySquares() {
    $('#board .square-55d63').css('background', '')
}

function onDrop(source, target) {
    removeGreySquares()
    // see if the move is legal
    var move = game.move({
        from: source,
        to: target,
    })

    // illegal move
    if (move === null) return 'snapback'

    // make random legal move for black
    window.setTimeout(makeRandomMove, 250)
}

function onMouseoverSquare(square, piece) {
    // get list of possible moves for this square
    var moves = game.getLegalMoves(square)

    // exit if there are no moves available for this square
    if (moves.length === 0) return

    // highlight the square they moused over
    greySquare(square)
    console.log(moves)

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

const config = {
    draggable: true,
    position: 'start',
    onDragStart: onDragStart,
    onDrop: onDrop,
    onSnapEnd: onSnapEnd,
    onMouseoutSquare: onMouseoutSquare,
    onMouseoverSquare: onMouseoverSquare,
    pieceTheme: 'unicode'
}
board = DraughtsBoard('board', config)
