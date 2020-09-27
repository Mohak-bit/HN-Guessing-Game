let actualRank

let getNewRound = async() => {
    $('#next').hide()
    $('#resultWrapper').hide()
    $('#retry').hide()
    $('#moreLess').hide()
    let res = await fetch('https://hn-guessing-game.herokuapp.com/api/fetchRandom')
    let data = await res.json()
    actualRank = data.rank
    $('#title').text(data.title)
    $('#time').text(data.time)
    $('#questionWrapper').show()
}

let lives = 0 

$('#submit').click(() => {
    let input = $('#rank').val()
    console.log(input == actualRank)
    if (input == actualRank) {
        $('#result').text('You are right!')
        $('#moreLess').hide()
        $('#questionWrapper').hide()
        $('#resultWrapper').show()
        $('#next').text('Play Again').show()
    }

    else if (input == '') {
        $('#result').text('Please enter a rank')
        $('#resultWrapper').show()
    }

    else {
        lives++
        $('#livesLeft').text(`Lives Left:  ${10 - lives}`)
        $('#result').text('You are wrong! Try again')
        if (input > actualRank){
            $('#resultWrapper').show()
            $('#moreLess').show()
            $('#moreLess').text('HINT: Correct rank is between 1 to rank entered')
        }

        if (input < actualRank){
            $('#resultWrapper').show()
            $('#moreLess').show()
            $('#moreLess').text('HINT: Correct rank is between rank entered to 30')
        }

        $('#resultWrapper').show()
        $('#next').text('Next').show()
        if (lives == 10){
            $('#moreLess').hide()
            $('#result').text('you lost')
            $('#resultWrapper').show()
            $('#questionWrapper').hide()
            $('#next').text('play again')

        }
    }
})

$('#next').click(() => {
    if (lives==10){
        lives = 0 
        $('#moreLess').hide()
        $('#livesLeft').text('Lives Left : 10')
        $('#next').text('next')
    }
    getNewRound()
})   

getNewRound()

// time, user input, correct or not, css
// https://api.jquery.com/
// higher or lower than the guess