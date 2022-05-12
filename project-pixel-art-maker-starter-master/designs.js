const
/* Getting the grid from the HTML. */ 
grid = document.getElementById('pixelCanvas'),

/* Selecting the form element from the HTML. */
form = document.querySelector('#sizePicker'),

/* Getting the submit button from the HTML. */
buildGrid = document.getElementById('submitButton');

/* Select color input*/
colorPicker = document.getElementById('colorPicker');
/* Select size input*/
height = document.getElementById('inputHeight');
/* Getting the width of the grid. */
width = document.getElementById('inputWidth');

/* When size is submitted by the user, call makeGrid()*/
document.addEventListener('DOMContentLoaded', function (event) {
})

/* This is a function that is creating the grid. */
function makeGrid() {
    let numberOfRows = height.value,
        numberOfColumns = width.value;

    /* This is a for loop that is creating the grid. */
    for (gridHeight = 0; gridHeight < numberOfRows; gridHeight++) {
        let row = grid.appendChild(document.createElement('tr'));
        for (gridWidth = 0; gridWidth < numberOfColumns; gridWidth++) {
            let cell = row.appendChild(document.createElement('td'));
            cell.addEventListener('click', function (e) {
                let colorSelected = colorPicker.value;
                if (this.style.backgroundColor != colorSelected) {
                    this.style.backgroundColor = colorSelected;
                } else {
                    this.style.backgroundColor = '';
                }
            });
        }
    }
};


/* This is an event listener that is listening for a click on the submit button. When the submit button
is clicked, the event is prevented from happening, the grid is cleared, and a new grid is created. */
buildGrid.addEventListener('click', function (event) {
    event.preventDefault();
    clearGrid();
    makeGrid();
    let reset = document.createElement('input');
    let form = document.getElementById('sizePicker');
    reset.type = 'reset';
    if (form.length < 2) {
        form.appendChild(reset);
    }
});

/**
 * It removes all the child nodes of the grid element
 */
function clearGrid() {
    while (grid.hasChildNodes()) {
        grid.removeChild(grid.firstChild);
    }
};

/* This is an event listener that is listening for a reset on the form. When the form is reset, the
grid is cleared and the reset button is removed. */
form.addEventListener('reset', function (e) {
    if ('isValid') {
        clearGrid();
        form.lastChild.remove();
    }
});
console.log(height, width)

