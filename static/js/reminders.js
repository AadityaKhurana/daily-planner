function check(){
    const water_checkbox = document.getElementById('water').checked
    const meditate_checkbox = document.getElementById('meditation').checked
    const exercise_checkbox = document.getElementById('exercise').checked
    const rest_checkbox = document.getElementById('rest').checked
    const entertain_checkbox = document.getElementById('entertain').checked

    const water_input = document.getElementById('water_input')
    const meditate_input = document.getElementById('meditation_input')
    const exercise_input = document.getElementById('exercise_input')
    const rest_input = document.getElementById('rest_input')
    const entertain_input = document.getElementById('entertain_input')
    
    water_input.value = water_checkbox
    meditate_input.value = meditate_checkbox
    exercise_input.value = exercise_checkbox
    rest_input.value = rest_checkbox
    entertain_input.value = entertain_checkbox
}